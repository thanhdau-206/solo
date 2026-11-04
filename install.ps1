# ========================================================
# Solo ⚔️ - 1-Click Installer (Windows PowerShell)
# ========================================================

Write-Host "==========================================" -ForegroundColor Yellow
Write-Host "   Solo ⚔️ - Multi-AI Council & Muscle" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Yellow
Write-Host ""

# 1. Verify Python
$PythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $PythonCmd) {
    $PythonCmd = Get-Command py -ErrorAction SilentlyContinue
}

if (-not $PythonCmd) {
    Write-Host "[Error] Python not found. Please install Python 3.10+ from python.org." -ForegroundColor Red
    Exit 1
}

$PyPath = $PythonCmd.Source
Write-Host "[OK] Python detected: $PyPath" -ForegroundColor Green

# 2. Virtual Environment Setup
$VenvDir = Join-Path $PSScriptRoot ".venv"
if (-not (Test-Path $VenvDir)) {
    Write-Host "[*] Creating virtual environment (.venv)..." -ForegroundColor Gray
    & $PyPath -m venv $VenvDir
}

$VenvPy = Join-Path $VenvDir "Scripts\python.exe"
$ReqFile = Join-Path $PSScriptRoot "requirements.txt"
if (Test-Path $VenvPy) {
    Write-Host "[*] Installing dependencies..." -ForegroundColor Gray
    & $VenvPy -m pip install -q -U pip
    if (Test-Path $ReqFile) {
        & $VenvPy -m pip install -q -r $ReqFile
    }
    Write-Host "[OK] Dependencies installed." -ForegroundColor Green
}

# 3. Configure .env
$EnvFile = Join-Path $PSScriptRoot ".env"
$EnvExample = Join-Path $PSScriptRoot ".env.example"
if ((-not (Test-Path $EnvFile)) -and (Test-Path $EnvExample)) {
    Copy-Item $EnvExample $EnvFile
    Write-Host "[OK] Initialized .env template." -ForegroundColor Green
}

# 4. Register Skills with Antigravity and .agents
$AgySkillsDir = Join-Path $HOME ".gemini\config\skills"
if (-not (Test-Path $AgySkillsDir)) {
    New-Item -ItemType Directory -Path $AgySkillsDir -Force | Out-Null
}

$AgentsSkillsDir = Join-Path $HOME ".agents\skills"
if (-not (Test-Path $AgentsSkillsDir)) {
    New-Item -ItemType Directory -Path $AgentsSkillsDir -Force | Out-Null
}

$SkillsSrc = Join-Path $PSScriptRoot "skills"
if (Test-Path $SkillsSrc) {
    $SkillDirs = Get-ChildItem -Path $SkillsSrc -Directory
    foreach ($sd in $SkillDirs) {
        $Dest1 = Join-Path $AgySkillsDir $sd.Name
        $Dest2 = Join-Path $AgentsSkillsDir $sd.Name
        Copy-Item -Recurse -Force $sd.FullName $Dest1
        Copy-Item -Recurse -Force $sd.FullName $Dest2
        Write-Host "[OK] Registered skill: $($sd.Name)" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Yellow
Write-Host "  Setup Complete! ⚔️" -ForegroundColor Green
Write-Host "  Start Antigravity and type: /solo" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Yellow
