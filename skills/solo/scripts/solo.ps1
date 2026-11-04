# ========================================================
# Solo ⚔️ - Multi-AI Tournament Runner (PowerShell)
# ========================================================
[CmdletBinding()]
param (
    [string]$Brief = "debate.md",
    [string]$Rules = "",
    [int]$PerAi = 2,
    [double]$Target = 8.0,
    [int]$FixMax = 2,
    [int]$LoopMax = 10,
    [int]$GenMax = 3,
    [int]$StallMax = 2
)

$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$PythonBin = "python"
if (Test-Path "$PSScriptRoot\..\..\..\.venv\Scripts\python.exe") {
    $PythonBin = "$PSScriptRoot\..\..\..\.venv\Scripts\python.exe"
}

Write-Host "⚔️ Khởi động SOLO Multi-AI Tournament..." -ForegroundColor Yellow
Write-Host "   - Đề bài: $Brief" -ForegroundColor Cyan
Write-Host "   - Điểm mục tiêu: $Target" -ForegroundColor Cyan
Write-Host "   - Đấu thủ: Claude (Anthropic), Codex (ChatGPT), Gemini/Antigravity" -ForegroundColor Cyan
Write-Host ""

$ScriptPath = Join-Path $PSScriptRoot "solo.py"
& $PythonBin $ScriptPath `
    --brief "$Brief" `
    --per-ai $PerAi `
    --target $Target `
    --fix-max $FixMax `
    --loop-max $LoopMax `
    --gen-max $GenMax `
    --stall-max $StallMax
