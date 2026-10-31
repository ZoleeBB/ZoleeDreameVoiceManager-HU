"""Idempotens, ellenőrzött minimális módosítások az upstream v1.4.0 fájljain.

Nem keres-vaktában: hiányzó/eltérő mintánál leáll, és nem készít hibás kódot.
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def patch(path: str, edits: list[tuple[str, str]]) -> None:
    file = ROOT / path
    source = file.read_text(encoding="utf-8-sig")
    original = source
    for before, after in edits:
        if after in source:
            continue
        n = source.count(before)
        if n != 1:
            raise RuntimeError(f"{path}: expected one occurrence, found {n}: {before[:85]!r}")
        source = source.replace(before, after)
    if source != original:
        file.write_text(source, encoding="utf-8")
        print(f"Patched: {path}")


def main() -> None:
    patch("README.md", [
        (
            "# Dreame Sprachpaket-Manager",
            "# Dreame Sprachpaket-Manager\n\n> Magyar privát változat: [README-HU.md](README-HU.md) – saját Windows build, magyar beszédhang és vicces szövegcsomag.",
        ),
    ])
    patch("main.py", [
        (
            "    try:\n        from dreamevoice.ui.app import run\n        run()",
            "    try:\n        from dreamevoice.hu_preset import install_if_missing\n"
            "        install_if_missing()\n"
            "        from dreamevoice.ui.app import run\n        run()",
        ),
    ])
    patch("dreamevoice/tts.py", [
        (
            "def pick_german_voice(preferred: str = \"\") -> Optional[Voice]:",
            "def supported_voices() -> List[Voice]:\n"
            "    \"\"\"German and Hungarian Windows TTS voices (HU extension).\"\"\"\n"
            "    voices = [v for v in list_voices()\n"
            "              if v.culture.lower().startswith((\"de\", \"hu\"))]\n"
            "    return sorted(voices, key=lambda v: (not v.is_male, v.name.lower()))\n\n\n"
            "def pick_german_voice(preferred: str = \"\") -> Optional[Voice]:",
        ),
        (
            "    chosen = pick_german_voice(voice)",
            "    # Explicitly selected Hungarian voices are allowed; unspecified voices\n"
            "    # still default to the upstream German voice for compatibility.\n"
            "    chosen = (next((v for v in supported_voices() if v.name == voice), None)\n"
            "              if voice else None) or pick_german_voice(voice)",
        ),
        (
            "        # Beide Wege benutzen SSML, damit Tempo und Tonhöhe gleich wirken.\n"
            "        if chosen.engine == ENGINE_ONECORE:",
            "        # Use the actual Windows TTS locale, never hard-code de-DE.\n"
            "        locale = chosen.culture if chosen.culture.lower().startswith((\"de\", \"hu\")) else \"de-DE\"\n"
            "        # Beide Wege benutzen SSML, damit Tempo und Tonhöhe gleich wirken.\n"
            "        if chosen.engine == ENGINE_ONECORE:",
        ),
        (
            "script = _ONECORE_SCRIPT.format(voice=_ps_quote(chosen.name),",
            "script = _ONECORE_SCRIPT.format(locale=locale, voice=_ps_quote(chosen.name),",
        ),
        (
            "script = _SAPI_SCRIPT.format(voice=_ps_quote(chosen.name),",
            "script = _SAPI_SCRIPT.format(locale=locale, voice=_ps_quote(chosen.name),",
        ),
    ])
    # Both SSML templates must use the selected voice's language.
    tts_path = ROOT / "dreamevoice/tts.py"
    tts_text = tts_path.read_text(encoding="utf-8-sig")
    if "xml:lang='de-DE'" in tts_text:
        if tts_text.count("xml:lang='de-DE'") != 2:
            raise RuntimeError("Expected exactly two hardcoded SSML language tags")
        tts_path.write_text(tts_text.replace("xml:lang='de-DE'", "xml:lang='{locale}'"), encoding="utf-8")
        print("Patched: SSML language")

    # This call occurs in 4 guard locations as well as the voice combobox.
    path = ROOT / "dreamevoice/ui/tab_store.py"
    s = path.read_text(encoding="utf-8-sig")
    if "tts.german_voices()" in s:
        s = s.replace("tts.german_voices()", "tts.supported_voices()")
        s = s.replace("Keine deutsche Stimme", "Keine kompatible Stimme")
        s = s.replace("Es ist keine deutsche Sprachausgabe installiert.",
                      "Es ist keine deutsche oder ungarische Sprachausgabe installiert.")
        path.write_text(s, encoding="utf-8")
        print("Patched: dreamevoice/ui/tab_store.py")

    # The original update mechanism fetches an EXE from the upstream project.
    # Prevent a custom -HU binary from replacing itself with upstream's EXE.
    patch("dreamevoice/aktualisierung.py", [
        (
            "    pfad = _repo_pfad(projekt_url)\n",
            "    if getattr(sys, \"frozen\", False) and Path(sys.executable).stem.endswith(\"-HU\"):\n"
            "        return None  # Release updates only through private GitHub Actions.\n"
            "    pfad = _repo_pfad(projekt_url)\n",
        ),
    ])
    print("Hungarian overlay applied successfully.")


if __name__ == "__main__":
    main()
