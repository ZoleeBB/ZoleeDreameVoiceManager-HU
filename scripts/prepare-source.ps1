# Prepare pinned upstream source and apply the user's Hungarian overlay.
[CmdletBinding()]
param([string]$UpstreamCommit = '852f3043727fc85a3c06cb54231a00de013b1492')
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$target = Join-Path $root '_upstream-src'
if (Test-Path -LiteralPath $target) {
    throw "The output directory already exists: $target"
}

Write-Host 'Cloning upstream v1.4.0 ...'
git clone --depth 1 --branch v1.4.0 --single-branch https://github.com/Anon365-Project/dreame-sprachpaket-manager.git $target
if ($LASTEXITCODE -ne 0) { throw 'Upstream clone failed.' }

$actual = (git -C $target rev-parse HEAD).Trim().ToLowerInvariant()
if ($LASTEXITCODE -ne 0 -or $actual -ne $UpstreamCommit.ToLowerInvariant()) {
    throw "Upstream commit mismatch. Expected $UpstreamCommit, actual $actual. Overlay NOT applied."
}
Write-Host "Verified upstream commit: $actual"

$files = @(
    @{from='dreamevoice/hu_preset.py'; to='dreamevoice/hu_preset.py'},
    @{from='requirements-hu-build.txt'; to='requirements-hu-build.txt'},
    @{from='scripts/apply_overlay.py'; to='scripts/apply_overlay.py'},
    @{from='scripts/build-release.ps1'; to='scripts/build-release.ps1'},
    @{from='scripts/ci-selftest.py'; to='scripts/ci-selftest.py'},
    @{from='README.md'; to='README-HU.md'}
)
foreach ($item in $files) {
    $source = Join-Path $root $item.from
    $destination = Join-Path $target $item.to
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) {
        throw "Missing HU overlay file: $($item.from)"
    }
    New-Item -ItemType Directory -Force -Path (Split-Path $destination -Parent) | Out-Null
    Copy-Item -LiteralPath $source -Destination $destination -Force
}
Copy-Item -LiteralPath (Join-Path $root 'tests') -Destination (Join-Path $target 'tests') -Recurse -Force

Push-Location $target
try {
    python scripts/apply_overlay.py
    if ($LASTEXITCODE -ne 0) { throw 'HU overlay patch failed.' }
    python -m compileall -q main.py dreamevoice tests
    if ($LASTEXITCODE -ne 0) { throw 'Python syntax check failed.' }
}
finally { Pop-Location }

Write-Host "Prepared sources: $target"
