#!/usr/bin/env bash
# ========================================================
# Solo ⚔️ - 1-Click Installer (macOS & Linux)
# ========================================================

set -e

echo -e "\033[1;33m==========================================\033[0m"
echo -e "\033[1;36m   Solo ⚔️ - Multi-AI Council & Muscle\033[0m"
echo -e "\033[1;33m==========================================\033[0m"
echo ""

# 1. Verify Python
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_CMD="python"
else
    echo -e "\033[1;31m[Error] Python not found. Please install Python 3.10+.\033[0m"
    exit 1
fi

echo -e "\033[1;32m[OK] Python detected: $($PYTHON_CMD --version)\033[0m"

# 2. Virtual Environment Setup
if [ ! -d ".venv" ]; then
    echo -e "\033[0;37m[*] Creating virtual environment (.venv)...\033[0m"
    $PYTHON_CMD -m venv .venv
fi

echo -e "\033[0;37m[*] Installing dependencies...\033[0m"
.venv/bin/python -m pip install -q -U pip
.venv/bin/python -m pip install -q -r requirements.txt
echo -e "\033[1;32m[OK] Dependencies installed.\033[0m"

# 3. Configure .env
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo -e "\033[1;32m[OK] Initialized .env template.\033[0m"
fi

# 4. Register Skills with Antigravity and .agents
AGY_SKILLS_DIR="$HOME/.gemini/config/skills"
AGENTS_SKILLS_DIR="$HOME/.agents/skills"
mkdir -p "$AGY_SKILLS_DIR"
mkdir -p "$AGENTS_SKILLS_DIR"

if [ -d "skills" ]; then
    for s in skills/*/; do
        [ -d "$s" ] || continue
        sname=$(basename "$s")
        cp -r "$s" "$AGY_SKILLS_DIR/"
        cp -r "$s" "$AGENTS_SKILLS_DIR/"
        echo -e "\033[1;32m[OK] Registered skill: $sname\033[0m"
    done
fi

echo ""
echo -e "\033[1;33m==========================================\033[0m"
echo -e "\033[1;32m  Setup Complete! ⚔️\033[0m"
echo -e "\033[1;36m  Start Antigravity and type: /solo\033[0m"
echo -e "\033[1;33m==========================================\033[0m"
