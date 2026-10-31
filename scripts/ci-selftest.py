"""Upstream comprehensive self-test with STRICT GitHub-runner exclusions.

Upstream v1.4.0 source does not include the six separately released audio ZIPs;
AMSI assertions are not reliable on shared Windows CI runners. We still run
EVERY upstream test and only tolerate the explicitly named missing-asset/AMSI
environment mismatches. ANY new failure fails CI.
"""
from __future__ import annotations

import os
import ast
from pathlib import Path
import re
import subprocess
import sys

EXPECTED_CI_ONLY = {
    "und jede eingebaute lässt sich auflösen",
    "Bayerisch-Aufnahmen.zip liegt bereit",
    "Bayerisch-Weiblich-Aufnahmen.zip liegt bereit",
    "Hessisch-Aufnahmen.zip liegt bereit",
    "Wienerisch-Aufnahmen.zip liegt bereit",
    "Berlinerisch-Aufnahmen.zip liegt bereit",
    "Servitor-Aufnahmen.zip liegt bereit",
    "eine Tondatei bleibt dort ohne Fund",
    "bei fremdem Virenschutz springt AMSI ein",
    "und daraus wird kein Freispruch",
    "AMSI bekommt jeden Eintrag einzeln, auch im inneren Archiv",
    "ein ganzer Ordner geht genauso",
}

# These two upstream assertions explicitly require the ORIGINAL German
# executable name. The HU fork intentionally publishes a different filename.
# Do not waive them unless the HU updater is independently verified below.
EXPECTED_HU_FILENAME_DIFFERENCES = {
    "die Summe der Programmdatei wird genommen",
    "die Programmdatei heißt weiter DreameSprachpaket.exe",
}


def verify_hu_updater() -> bool:
    """Inspect the exact patched source without importing GUI dependencies."""
    path = Path(__file__).resolve().parents[1] / "dreamevoice" / "aktualisierung.py"
    try:
        source = path.read_text(encoding="utf-8-sig")
        tree = ast.parse(source, filename=str(path))
        exe = None
        project = None
        body = None
        for node in tree.body:
            if isinstance(node, ast.Assign):
                if any(isinstance(t, ast.Name) and t.id == "EXE_NAME"
                       for t in node.targets):
                    exe = ast.literal_eval(node.value)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "pruefen":
                body = node
                positional = node.args.posonlyargs + node.args.args
                defaults = node.args.defaults
                for arg, val in zip(positional[-len(defaults):], defaults):
                    if arg.arg == "projekt_url":
                        project = ast.literal_eval(val)
        valid = (
            exe == "DreameSprachpaket-HU.exe"
            and project == "https://github.com/ZoleeBB/ZoleeDreameVoiceManager-HU"
            and body is not None
            and "Release updates only through private GitHub Actions" not in source
        )
        print(f"HU updater source: EXE={exe!r}, project={project!r}, valid={valid}", flush=True)
        return valid
    except (OSError, SyntaxError, ValueError, TypeError) as exc:
        print(f"HU updater source validation failed: {exc}", file=sys.stderr, flush=True)
        return False


def main() -> int:
    # GitHub's Windows PowerShell runner can default to cp1252.
    # Selftest contains accented German output, so force UTF-8 end-to-end.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    environment = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    result = subprocess.run(
        [sys.executable, "selftest.py"],
        check=False,
        capture_output=True,
        env=environment,
    )
    output = result.stdout.decode("utf-8", errors="replace")
    errors = result.stderr.decode("utf-8", errors="replace")
    if errors:
        print(errors, file=sys.stderr)
    # Keep the complete upstream test transcript in the Actions log.
    print(output)
    if result.returncode == 0:
        print("Upstream self-test: all checks passed.")
        return 0

    lines = output.splitlines()
    labels = []
    for line in lines:
        if "[FEHL]" in line:
            suffix = line.split("[FEHL]", 1)[1].strip()
            labels.append(suffix.split("  ->", 1)[0].strip())

    summary = re.search(
        r"Bestanden:\s*(\d+)\s+Fehlgeschlagen:\s*(\d+)",
        output,
    )
    if not summary:
        print("ERROR: missing upstream summary; cannot approve test failures.", file=sys.stderr)
        return 1
    passed, failed = (int(x) for x in summary.groups())
    updater_ok = verify_hu_updater()
    print(f"HU updater invariant verified: {updater_ok}", flush=True)
    allowed = EXPECTED_CI_ONLY.copy()
    if updater_ok:
        allowed |= EXPECTED_HU_FILENAME_DIFFERENCES
    unknown = [label for label in labels if label not in allowed]
    if unknown or len(labels) != failed or passed < 1000:
        print(
            "ERROR: unexpected upstream test failure(s): "
            + repr(unknown)
            + f"; failed={failed}, parsed={len(labels)}, passed={passed}",
            file=sys.stderr,
        )
        return 1

    print(
        f"Upstream CI result: {passed} passed; {failed} documented "
        "mismatches (unbundled archives, runner AMSI and verified HU EXE name). "
        "Any other failure is fatal."
    )
    for label in labels:
        print("  verified expected difference: " + label)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
