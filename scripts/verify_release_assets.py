"""Validate both bundled release voice archives and write checksums.

This is run BEFORE publishing any release. It does not extract or execute
archive members. User needs to upload files once to voicepacks/assets/.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "voicepacks" / "assets"
MANIFEST = ROOT / "voicepacks" / "elison-20261031.json"
MAX_MEMBER_SIZE = 2 * 1024 * 1024
MAX_TOTAL_SIZE = 100 * 1024 * 1024


def hash_file(path: Path) -> tuple[str, str]:
    sha = hashlib.sha256()
    md5 = hashlib.md5()  # nosec: robot protocol uses MD5 for file identity
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(1024 * 1024), b""):
            sha.update(part)
            md5.update(part)
    return sha.hexdigest(), md5.hexdigest()


def check_asset(path: Path, spec: dict) -> str:
    if not path.is_file():
        raise ValueError(f"HIÁNYZÓ release fájl: {path}")
    if path.stat().st_size != spec["bytes"]:
        raise ValueError(f"{path.name}: rossz fájlméret")
    sha, md5 = hash_file(path)
    if sha.lower() != spec["sha256"].lower():
        raise ValueError(f"{path.name}: SHA256 eltérés!")
    if "md5" in spec and md5.lower() != spec["md5"].lower():
        raise ValueError(f"{path.name}: MD5 eltérés!")
    print(f"OK {path.name}: {path.stat().st_size} bytes, SHA-256 {sha}")
    return sha


def check_factory_archive(path: Path, expected_count: int) -> None:
    seen = set()
    ogg = set()
    meta = set()
    total = 0
    with tarfile.open(path, "r:gz") as tar:
        for member in tar:
            if not member.isfile() or member.name.startswith("/") or ".." in Path(member.name).parts:
                raise ValueError(f"Váratlan vagy nem biztonságos tar elem: {member.name}")
            if not re.fullmatch(r"[a-zA-Z0-9_.-]+", member.name):
                raise ValueError(f"Érvénytelen archívumfájlnév: {member.name}")
            if member.name in seen:
                raise ValueError(f"Ismétlődő archívumfájl: {member.name}")
            seen.add(member.name)
            if member.size > MAX_MEMBER_SIZE or member.size < 0:
                raise ValueError(f"Váratlan méret: {member.name}")
            total += member.size
            if total > MAX_TOTAL_SIZE:
                raise ValueError("Túl nagy a kicsomagolt archívum")
            if re.fullmatch(r"[0-9]+\.ogg", member.name):
                ogg.add(member.name)
                fp = tar.extractfile(member)
                if fp is None or fp.read(4) != b"OggS":
                    raise ValueError(f"OGG sérült: {member.name}")
                while fp.read(65536):
                    pass
            else:
                meta.add(member.name)
                if not (member.name.endswith(".json") or member.name.endswith(".txt")):
                    raise ValueError(f"Váratlan metaadat: {member.name}")
    if len(ogg) != expected_count:
        raise ValueError(f"Teljes archívum: {len(ogg)} OGG, várt {expected_count}")
    expected_meta = {
        "mini_broad.json", "tts.json", "dmr_audio.json",
        "first_audio.json", "time.txt", "voice_mapping.json",
    }
    if meta != expected_meta:
        raise ValueError(f"Váratlan gyári vezérlőfájlok: {sorted(meta)}")
    print(f"OK teljes X50 csomag: {len(ogg)} OGG, {len(meta)} gyári vezérlőfájl")


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    sound = data["overlay_asset"]
    full = data["ready_x50_asset"]
    zip_path = ASSETS / sound["name"]
    full_path = ASSETS / full["name"]
    zip_sha = check_asset(zip_path, sound)
    # The existing zip validator also verifies individual OGG IDs, magic bytes
    # and ZIP CRCs (without writing out any archive member).
    from verify_prebuilt import verify
    verify(zip_path)
    full_sha = check_asset(full_path, full)
    check_factory_archive(full_path, data["original_ogg_count"])
    checksum = ASSETS / "VOICEPACK_SHA256SUMS.txt"
    checksum.write_text(
        f"{zip_sha}  {zip_path.name}\n"
        f"{full_sha}  {full_path.name}\n",
        encoding="ascii",
    )
    print(f"Release voice files: VALIDÁLVA; checksums: {checksum}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, tarfile.TarError) as exc:
        print(f"HIBA: {exc}", file=sys.stderr)
        raise SystemExit(1) from None
