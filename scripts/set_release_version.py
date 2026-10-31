"""Set the app, Windows PE metadata and release notes to VERSION-HU.

Do not edit the pinned upstream tag itself. Invoke AFTER apply_overlay.py.
Run with a GitHub-compatible semantic version: python scripts/set_release_version.py v1.5.0
Future v1.5.1 releases require changing VERSION-HU only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")


def set_version(raw: str, root: Path = ROOT) -> str:
    match = VERSION_RE.fullmatch(raw.strip())
    if not match:
        raise ValueError("Csak vMAJOR.MINOR.PATCH verzió engedélyezett, például v1.5.0")
    major, minor, patch = map(int, match.groups())
    version = f"{major}.{minor}.{patch}"
    pep = f"{version}.0"

    package_file = root / "dreamevoice" / "__init__.py"
    package = package_file.read_text(encoding="utf-8-sig")
    version_pattern = r'^__version__\s*=\s*"[^"]+"'
    if len(re.findall(version_pattern, package, re.MULTILINE)) != 1:
        raise ValueError("Nem található egyértelmű __version__ a csomagban")
    package = re.sub(version_pattern, f'__version__ = "{version}"',
                     package, count=1, flags=re.MULTILINE)
    package_file.write_text(package, encoding="utf-8")

    ver_file = root / "version_info.txt"
    ver = ver_file.read_text(encoding="utf-8-sig")
    for field in ("filevers", "prodvers"):
        pattern = rf"{field}=\(\d+,\s*\d+,\s*\d+,\s*\d+\)"
        ver, count = re.subn(pattern,
                             f"{field}=({major}, {minor}, {patch}, 0)",
                             ver, count=1)
        if count != 1:
            raise ValueError(f"Windows verziómező hiányzik: {field}")
    for field in ("FileVersion", "ProductVersion"):
        pattern = rf"(StringStruct\('{field}',\s*')[^']+('\))"
        ver, count = re.subn(pattern, lambda m: m.group(1) + pep + m.group(2),
                             ver, count=1)
        if count != 1:
            raise ValueError(f"Windows szöveges verzió hiányzik: {field}")
    ver_file.write_text(ver, encoding="utf-8")

    release = root / "RELEASE.md"
    old = release.read_text(encoding="utf-8-sig")
    if not re.search(r"(?m)^## v" + re.escape(version) + r"\b", old):
        heading = (f"## v{version} – Zolee Dreame Voice Manager HU\n\n"
                   "Magyar nyelvű felület, saját szövegcsomagok és "
                   "előre elkészített Elison-hangok importálása.\n"
                   "Ko-fi / Revolut-me támogatási gombok és "
                   "újragenerálás nélkül használható magyar felvételek.\n"
                   "Az eredeti upstream kiadások változáslistája alább olvasható.\n\n")
        release.write_text(heading + old, encoding="utf-8")
    print(f"Version updated: v{version} (APP, EXE metadata, RELEASE.md)")
    return version


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Használat: python scripts/set_release_version.py v1.5.0")
    set_version(sys.argv[1])
