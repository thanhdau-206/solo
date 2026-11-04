#!/usr/bin/env bash
# ========================================================
# Solo ⚔️ - Multi-AI Tournament Runner (Bash)
# ========================================================
set -u
cd "$(dirname "$0")"
export LC_ALL=C.UTF-8 2>/dev/null || true

python3 solo.py "$@"
