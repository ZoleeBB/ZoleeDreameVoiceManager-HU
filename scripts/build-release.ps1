# GitHub Actions / Windows / Python 3.12. No administrator rights required.
[CmdletBinding()]
param(
    [switch]$SkipFFmpeg,
    [switch]$SkipSelfTest
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
Set-Location (Join-Path $PSScriptRoot '..')

# Immutable tagged BtbN FFmpeg build (2026-10-25 13:00), verified against
# the sha256 digest exposed by the official GitHub Release asset metadata.
# Never download mutable /latest in a reproducible/supply-chain-safe build.
$FFmpegUrl = 'https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2026-10-25-13-00/ffmpeg-N-128094-g31855b2a70-win64-gpl.zip'
$FFmpegSha256 = '94810842a634c7742936dc2690d6b4957561a38b05f00c27f045e07131924acc'
$TempFolder = if ($env:RUNNER_TEMP) { $env:RUNNER_TEMP } else { $env:TEMP }
$TempZip = Join-Path $TempFolder 'dreame-hu-ffmpeg.zip'

Write-Host 'Install build dependencies (pinned versions)...'
python -m pip install --disable-pip-version-check -r requirements-hu-build.txt
if ($LASTEXITCODE -ne 0) { throw 'pip install failed' }

if (-not $SkipSelfTest) {
    Write-Host 'Run upstream self-test...'
    python scripts/ci-selftest.py
    if ($LASTEXITCODE -ne 0) { throw 'Upstream self-test failed (unexpected errors)' }
    Write-Host 'Run HU regression checks...'
    python -m unittest discover -s tests -p 'test_hu*.py' -v
    if ($LASTEXITCODE -ne 0) { throw 'HU tests failed' }
    python -m compileall -q main.py dreamevoice
    if ($LASTEXITCODE -ne 0) { throw 'Python compilation failed' }
}

if (-not $SkipFFmpeg) {
    $Existing = Join-Path (Get-Location) 'ffmpeg.exe'
    if (-not (Test-Path $Existing)) {
        Write-Host 'Download FFmpeg from pinned and checksum-verified release...'
        Invoke-WebRequest -Uri $FFmpegUrl -OutFile $TempZip -UseBasicParsing
        $Actual = (Get-FileHash -Algorithm SHA256 -Path $TempZip).Hash.ToLowerInvariant()
        if ($Actual -ne $FFmpegSha256) {
            Remove-Item $TempZip -Force -ErrorAction SilentlyContinue
            throw "FFmpeg ZIP checksum mismatch. Expected $FFmpegSha256, got $Actual. Update hash only after review."
        }
        Add-Type -AssemblyName System.IO.Compression
        $zip = [System.IO.Compression.ZipFile]::OpenRead($TempZip)
        try {
            $entries = @($zip.Entries | Where-Object {
                [System.IO.Path]::GetFileName($_.FullName.Replace('/','\')) -eq 'ffmpeg.exe'
            })
            if ($entries.Count -ne 1) { throw 'Exactly one ffmpeg.exe required inside archive' }
            if ($entries[0].Length -gt 260MB) { throw 'ffmpeg.exe unexpectedly large' }
            $inputStream = $entries[0].Open()
            $outputStream = [System.IO.File]::Create($Existing)
            try { $inputStream.CopyTo($outputStream) }
            finally { $outputStream.Dispose(); $inputStream.Dispose() }
        }
        finally { $zip.Dispose(); Remove-Item $TempZip -Force -ErrorAction SilentlyContinue }
    } else {
        throw 'Unexpected pre-existing ffmpeg.exe: refusing unverified binary input in release build.'
    }
}

Write-Host 'Build PyInstaller EXE...'
python -m PyInstaller DreameSprachpaket.spec --noconfirm --clean
if ($LASTEXITCODE -ne 0) { throw 'PyInstaller failed' }
$exe = Join-Path (Get-Location) 'dist\DreameSprachpaket.exe'
if (-not (Test-Path $exe)) { throw 'PyInstaller EXE missing' }

if (-not $SkipFFmpeg) {
    Write-Host 'Embed the verified FFmpeg binary...'
    python embed_ffmpeg.py (Join-Path (Get-Location) 'ffmpeg.exe') $exe
    if ($LASTEXITCODE -ne 0) { throw 'Embedding FFmpeg failed' }
}
# Do not embed third-party pre-recorded German audio. HU sound files are
# synthesized locally with a selected Windows hu-HU voice, on user request.
$target = Join-Path (Get-Location) 'dist\DreameSprachpaket-HU.exe'
Move-Item -Force $exe $target
Get-FileHash $target -Algorithm SHA256 | ForEach-Object {
    $sum = $_.Hash.ToLowerInvariant()
    "$sum  DreameSprachpaket-HU.exe" | Set-Content -Encoding ascii 'dist\SHA256SUMS.txt'
}
Write-Host "Done: $target"
