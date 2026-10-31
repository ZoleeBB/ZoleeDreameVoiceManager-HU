"""Validate a published, pre-recorded Hungarian Dreame overlay ZIP.

Usage: python scripts/verify_prebuilt.py path/to/Zolee_Dreame_HU_Elison_589_OGG.zip
No TTS API, no robot, no secrets, no external dependencies.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path


def verify(path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads(
        (root / "voicepacks" / "elison-20261031.json").read_text(encoding="utf-8")
    )
    expected = manifest["overlay_asset"]
    if not path.is_file():
        raise ValueError(f"Nem található a ZIP: {path}")
    if path.stat().st_size != expected["bytes"]:
        raise ValueError("A ZIP mérete nem egyezik a manifesttel.")
    actual_hash = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            actual_hash.update(chunk)
    if actual_hash.hexdigest().lower() != expected["sha256"].lower():
        raise ValueError("SHA-256 eltérés! A letöltött archívum megváltozott.")

    found = set()
    extracted = 0
    with zipfile.ZipFile(path, "r") as archive:
        for f in archive.infolist():
            if f.is_dir():
                raise ValueError(f"Váratlan mappa az archívumban: {f.filename}")
            if not re.fullmatch(r"(0|[1-9][0-9]*)\.ogg", f.filename):
                raise ValueError(f"Váratlan fájlnév: {f.filename}")
            if f.filename in found:
                raise ValueError(f"Duplikált OGG: {f.filename}")
            if f.file_size > 2 * 1024 * 1024:
                raise ValueError(f"Túl nagy OGG hang: {f.filename}")
            extracted += f.file_size
            if extracted > 60 * 1024 * 1024:
                raise ValueError("Túl nagy a kicsomagolt tartalom.")
            with archive.open(f) as stream:
                if stream.read(4) != b"OggS":
                    raise ValueError(f"Érvénytelen OGG-formátum: {f.filename}")
                # Force ZIP CRC verification, including truncated/corrupt files.
                while stream.read(128 * 1024):
                    pass
            found.add(f.filename)
    if len(found) != manifest["generated_ogg_count"]:
        raise ValueError(f"Elvárt 589 OGG, talált {len(found)}.")
    print(f"RENDBEN: {len(found)} magyar OGG; "
          f"SHA-256: {actual_hash.hexdigest()}")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("Használat: python scripts/verify_prebuilt.py <hangcsomag.zip>")
        verify(Path(sys.argv[1]))
    except (OSError, zipfile.BadZipFile, ValueError) as exc:
        print(f"HIBA: {exc}", file=sys.stderr)
        raise SystemExit(1) from None
