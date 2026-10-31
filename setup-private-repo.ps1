# Run THIS FILE from the extracted starter ZIP on Windows (with git, gh and Python).
[CmdletBinding()]
param(
  [string]$RepoName = 'ZoleeBB/DreameVoiceManager-HU',
  [string]$Tag = 'v1.4.0-hu.1'
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$overlay = $PSScriptRoot
$folder = ($RepoName.Split('/') | Select-Object -Last 1)
$target = Join-Path (Split-Path $overlay -Parent) $folder

foreach ($command in @('git','gh','python')) {
    if (-not (Get-Command $command -ErrorAction SilentlyContinue)) {
        throw "$command is required. Install Git, GitHub CLI and Python 3.12 before running."
    }
}
if (Test-Path $target) { throw "Destination already exists: $target. Nothing changed." }
& gh auth status
if ($LASTEXITCODE -ne 0) { throw 'GitHub CLI is not authenticated. Run: gh auth login' }
& gh repo view $RepoName --json name 2>$null
if ($LASTEXITCODE -eq 0) { throw "Repository already exists: $RepoName. Refusing to overwrite it." }

Write-Host 'Clone original project, including Git history...'
& git clone https://github.com/Anon365-Project/dreame-sprachpaket-manager.git $target
if ($LASTEXITCODE -ne 0) { throw 'git clone failed' }
Push-Location $target
try {
    & git rev-parse 'v1.4.0^{commit}' 1>$null
    if ($LASTEXITCODE -ne 0) { throw 'Upstream v1.4.0 tag missing' }
    & git switch -c main v1.4.0
    if ($LASTEXITCODE -ne 0) { throw 'Unable to switch to v1.4.0' }
    & git remote rename origin upstream
    if ($LASTEXITCODE -ne 0) { throw 'Unable to configure upstream' }

    Write-Host 'Copy HU overlay files...'
    $files = Get-ChildItem -LiteralPath $overlay -File -Recurse -Force
    foreach ($file in $files) {
        $relative = $file.FullName.Substring($overlay.Length).TrimStart('\','/')
        if ($relative.StartsWith('__pycache__') -or $relative.Contains('\__pycache__\') -or $relative.EndsWith('.pyc')) { continue }
        $dest = Join-Path $target $relative
        $parent = Split-Path $dest -Parent
        New-Item -ItemType Directory -Path $parent -Force | Out-Null
        Copy-Item -LiteralPath $file.FullName -Destination $dest -Force
    }

    & python scripts/apply_overlay.py
    if ($LASTEXITCODE -ne 0) { throw 'HU patching failed; nothing pushed' }
    & python -m compileall -q main.py dreamevoice tests
    if ($LASTEXITCODE -ne 0) { throw 'Python syntax check failed; nothing pushed' }
    & git add -A
    & git -c user.name='Dreame HU Bootstrap' -c user.email='noreply@users.noreply.github.com' commit -m 'feat(hu): secure Windows CI, HU voice support and funny voice preset'
    if ($LASTEXITCODE -ne 0) { throw 'Initial commit failed' }

    Write-Host 'Create PRIVATE repository in your GitHub account...'
    & gh repo create $RepoName --private --source . --remote origin --push --description 'Private, customized Dreame Voice Manager: Hungarian voice and Windows release'
    if ($LASTEXITCODE -ne 0) { throw 'GitHub repo creation / initial push failed. Local changes remain.' }

    & git switch -c develop
    if ($LASTEXITCODE -ne 0) { throw 'Unable to create develop branch' }
    & git push -u origin develop
    if ($LASTEXITCODE -ne 0) { throw 'Could not push develop branch' }
    & git switch main
    & git tag $Tag
    if ($LASTEXITCODE -ne 0) { throw 'Unable to create release tag' }
    & git push origin $Tag
    if ($LASTEXITCODE -ne 0) { throw 'Unable to push release tag' }
    Write-Host "Repository: https://github.com/$RepoName"
    Write-Host "CI: https://github.com/$RepoName/actions"
    Write-Host "Release will be published if the Windows workflow succeeds: https://github.com/$RepoName/releases"
} finally {
    Pop-Location
}
