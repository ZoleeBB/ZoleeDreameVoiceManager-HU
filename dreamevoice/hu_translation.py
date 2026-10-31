"""Complete Hungarian voice-pack translation without overwriting user edits.

The official robot pack is the source of truth for sound IDs. Labels from
sound_catalog.json are only hints and must never be treated as transcripts
when no text is available. No ElevenLabs calls are made in this module.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set

from .sounds import SoundCatalog

MISSING = "[FORDÍTANDÓ]"
UNVERIFIED = "[HANGMINTA ELLENŐRZÉSE SZÜKSÉGES]"
PLACEHOLDERS = {
    "", "-", "?", MISSING.lower(), UNVERIFIED.lower(),
    "nincs adat", "nincs_adat", "ellenőrizendő",
    "nem ismert", "unknown", "to translate", "[fordítás]",
}

PROMPT = """\
# MAGYAR DREAME HANGCSOMAG — HIÁNYZÓ BEMONDÁSOK
#
# A cél: minden, a csatolt gyári hangcsomagban létező bemondás pontos,
# természetes magyar változata, az eredeti X50 Ultra jelentésével.
#
# FELADAT AZ AI SZÁMÁRA
# 1. Fordítsd le kizárólag a lent felsorolt hiányzó bemondásokat magyarra.
# 2. MINDEN soron tartsd meg a sorszámot és a második oszlop jelentését.
#    A szöveg kizárólag a HARMADIK oszlopba kerüljön. Ne hagyj ki sort!
# 3. A robothang stílusa szarkasztikus, morgós, vicces férfihang, de csak
#    a hétköznapi takarítási/állapotüzenetek lehetnek csipkelődők.
# 4. HIBA, KARBANTARTÁS, BIZTONSÁG, víz/elektromosság, elakadás,
#    érzékelők, gyermek/állat és garanciális figyelmeztetés esetén a
#    pontos ok és a konkrét teendő maradjon az elsődleges.
# 5. Ne változtasd meg a bemondás célját! Az indítás nem leállítás,
#    a töltés nem merülés, az alacsony vízszint nem teli tartály.
# 6. Rövid, magyarul természetesen kimondható TTS-mondatokat írj.
#    Ne írj bevezetőt, magyarázatot, új azonosítókat vagy markdown-táblát.
# 7. A második oszlopban található német (DE) és angol (EN) szöveg csak
#    orientáló CÍMKE / transzkripciós támpont, nem garantáltan pontos.
#    Ha eltérnek, biztonságos üzenetnél használj visszafogott megfogalmazást.
# 8. Ha egy sorhoz NINCS ELÉRHETŐ jelentés, NEM szabad kitalálni.
#    Hagyd a [HANGMINTA ELLENŐRZÉSE SZÜKSÉGES] jelölőt a harmadik
#    oszlopban; az eredeti hang meghallgatása után tölthető ki.
# 9. A meglévő 183+ felhasználói magyar szöveghez NE nyúlj:
#    a lista eleve kizárólag a hiányzó azonosítókat tartalmazza.
# 10. A 101 akkumulátorszázalék és 16 helyiségnév már le van fedve.
#    Az egyedi sorszámok sorrendje és száma legyen pontosan változatlan.
#
# FORMÁTUM: AZONOSÍTÓ | EREDETI JELENTÉS | MAGYAR TTS SZÖVEG
# A fájl UTF-8, pontosan ugyanebben a formátumban importálható.
# A kommenteket (#) a program figyelmen kívül hagyja.
#
# Megjegyzés: a teljes lefedettség csak a tényleges gyári hangazonosítókon
# mérhető. A címke nélküli hangokat kézzel kell meghallgatni/leírni.
"""


@dataclass
class ImportResult:
    new: Dict[int, str] = field(default_factory=dict)
    skipped_existing: List[int] = field(default_factory=list)
    skipped_unknown: List[int] = field(default_factory=list)
    skipped_placeholder: List[int] = field(default_factory=list)
    duplicate: List[int] = field(default_factory=list)


def uncovered_ids(official_ids: Iterable[int], covered_ids: Iterable[int]) -> List[int]:
    """Compare ONLY actual robot audio IDs, never highest numeric ID."""
    actual = {int(i) for i in official_ids}
    existing = {int(i) for i in covered_ids}
    return sorted(actual - existing)


def reference_for(sound_id: int, catalog: SoundCatalog) -> str:
    sound = catalog.get(sound_id)
    if sound is None or not (sound.de or sound.en):
        return "NINCS ADAT – az eredeti német hang meghallgatása szükséges"
    de = (sound.de or "").replace("|", "/").replace("\n", " ").strip()
    en = (sound.en or "").replace("|", "/").replace("\n", " ").strip()
    group = (sound.group or "").replace("|", "/")
    return f"{group}; DE: {de or '-'}; EN: {en or '-'}"


def export_prompt(official_ids: Iterable[int], existing: Dict[int, str],
                  catalog: SoundCatalog, dest: Path) -> tuple[Path, int, int]:
    """Export a complete missing-ID translation prompt; never overwrite work."""
    missing = uncovered_ids(official_ids, existing.keys())
    lines = [PROMPT.rstrip(), "",
             f"# HIÁNYZÓ BEMONDÁSOK: {len(missing)}",
             f"# MEGLÉVŐ MAGYAR SZÖVEGEK: {len(set(official_ids) & set(existing))}",
             ""]
    unknown = 0
    for sound_id in missing:
        sound = catalog.get(sound_id)
        no_label = sound is None or not (sound.de or sound.en)
        unknown += int(no_label)
        marker = UNVERIFIED if no_label else MISSING
        lines.append(f"{sound_id} | {reference_for(sound_id, catalog)} | {marker}")
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    # Fail closed if this name already exists: a previous AI-edited draft
    # must never be erased by clicking export twice.
    with dest.open("x", encoding="utf-8") as fp:
        fp.write("\n".join(lines) + "\n")
    return dest, len(missing), unknown


def parse_missing(text: str, allowed_ids: Iterable[int],
                  current: Dict[int, str]) -> ImportResult:
    """Parse only missing, actually installed IDs, without overwriting old texts.

    Repeated IDs are invalid, even if one of the rows contains placeholder
    text. Empty/unknown placeholders are never imported as spoken text.
    """
    allowed: Set[int] = {int(i) for i in allowed_ids}
    result = ImportResult()
    seen: Set[int] = set()
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        pieces = line.split("|", 2)
        if len(pieces) != 3:
            continue
        key = pieces[0].strip()
        if not key.isdecimal():
            continue
        sound_id = int(key)
        if sound_id in seen:
            result.duplicate.append(sound_id)
            continue
        seen.add(sound_id)
        if sound_id not in allowed:
            result.skipped_unknown.append(sound_id)
            continue
        if sound_id in current:
            result.skipped_existing.append(sound_id)
            continue
        hu = pieces[2].strip()
        if (not hu or hu.lower() in PLACEHOLDERS or
                "HANGMINTA ELLENŐRZÉSE SZÜKSÉGES" in hu.upper() or
                hu.upper().startswith("[FORDÍTANDÓ]")):
            result.skipped_placeholder.append(sound_id)
            continue
        if len(hu) > 600 or any(ord(ch) < 32 for ch in hu):
            raise ValueError(f"{lineno}. sor: túl hosszú vagy érvénytelen TTS-szöveg")
        result.new[sound_id] = hu

    if result.duplicate:
        raise ValueError("Ismétlődő hangazonosító(k): " +
                         ", ".join(map(str, sorted(set(result.duplicate)))))
    return result
