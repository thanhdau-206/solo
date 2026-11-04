#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universal Inter-Agent CLI Bridge
Enables bidirectional communication between Antigravity (agy), Claude Code CLI,
and auxiliary LLM providers (OpenAI, DeepSeek, Ollama).
"""

import sys
import os
import json
import time
import shutil
import argparse
import subprocess
from pathlib import Path

# Ensure UTF-8 output across platforms
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def find_binary(binary_name: str) -> str:
    """Locate binary in system PATH or common user directories."""
    found = shutil.which(binary_name)
    if found:
        return found

    home = Path.home()
    if sys.platform == "win32":
        candidate_paths = [
            home / ".gemini" / "bin" / f"{binary_name}.exe",
            home / ".gemini" / "bin" / f"{binary_name}.cmd",
            home / ".gemini" / "bin" / binary_name,
            home / "AppData" / "Roaming" / "npm" / f"{binary_name}.cmd",
            Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / binary_name / f"{binary_name}.exe",
        ]
    else:
        candidate_paths = [
            home / ".gemini" / "bin" / binary_name,
            home / ".local" / "bin" / binary_name,
            Path("/usr/local/bin") / binary_name,
        ]

    for p in candidate_paths:
        if p.exists():
            return str(p)

    return binary_name  # fallback to name, let subprocess attempt or fail gracefully

def log_interaction(log_path: Path, sender: str, receiver: str, prompt: str, response: str, model: str = None, duration: float = 0.0):
    """Logs conversation turn to a JSON Lines file."""
    try:
        log_path.parent.mkdir(parents=True, exist_ok=True)
        entry = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "sender": sender,
            "receiver": receiver,
            "model": model,
            "duration_sec": round(duration, 2),
            "prompt": prompt,
            "response": response
        }
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as e:
        # Logging should never crash the main bridge process
        sys.stderr.write(f"[Warning] Failed to write bridge log: {e}\n")

def call_claude(prompt: str, model: str = None, effort: str = "medium", cwd: Path = Path.cwd()) -> str:
    """Invokes Claude Code CLI in non-interactive print mode."""
    claude_bin = find_binary("claude")
    cmd = [
        claude_bin,
        "-p", prompt,
        "--permission-mode", "auto",
        "--dangerously-skip-permissions"
    ]
    if model:
        cmd.extend(["--model", model])
    if effort:
        cmd.extend(["--effort", effort])

    start_time = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            shell=(sys.platform == "win32"),
            timeout=1800
        )
        duration = time.time() - start_time
        stdout = proc.stdout.strip()
        stderr = proc.stderr.strip()

        if proc.returncode != 0:
            return f"Claude CLI error (code {proc.returncode}): {stderr or stdout}"

        return stdout or stderr
    except subprocess.TimeoutExpired:
        return "Claude CLI call timed out after 1800 seconds."
    except Exception as e:
        return f"Failed to execute Claude CLI: {str(e)}"

def call_agy(prompt: str, model: str = None, effort: str = "high", cwd: Path = Path.cwd()) -> str:
    """Invokes Antigravity CLI (agy) in non-interactive print mode."""
    agy_bin = find_binary("agy")
    cmd = [
        agy_bin,
        "-p", prompt,
        "--dangerously-skip-permissions"
    ]
    if model:
        cmd.extend(["--model", model])
    if effort:
        cmd.extend(["--effort", effort])

    start_time = time.time()
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            shell=(sys.platform == "win32"),
            timeout=1800
        )
        duration = time.time() - start_time
        stdout = proc.stdout.strip()
        stderr = proc.stderr.strip()

        if proc.returncode != 0:
            return f"Antigravity CLI error (code {proc.returncode}): {stderr or stdout}"

        return stdout or stderr
    except subprocess.TimeoutExpired:
        return "Antigravity CLI call timed out after 1800 seconds."
    except Exception as e:
        return f"Failed to execute Antigravity CLI: {str(e)}"

def call_openai_api(prompt: str, model: str = "gpt-4o", api_key: str = None) -> str:
    """Calls OpenAI API directly via requests."""
    key = api_key or os.environ.get("OPENAI_API_KEY")
    if not key:
        return "Error: OPENAI_API_KEY environment variable is not set."

    try:
        import requests
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model or "gpt-4o",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        }
        res = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=120)
        res.raise_for_status()
        data = res.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"OpenAI API error: {str(e)}"

def call_codex(prompt: str, model: str = None, cwd: Path = Path.cwd()) -> str:
    """Invokes OpenAI Codex CLI in non-interactive mode."""
    codex_bin = find_binary("codex")
    out_file = cwd / "work" / ".codex_bridge_out.txt"
    try:
        out_file.parent.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass

    cmd = [
        codex_bin,
        "exec",
        "--skip-git-repo-check",
        "--ephemeral",
        "-o", str(out_file),
        "-"
    ]
    if model:
        cmd.extend(["-m", model])

    start_time = time.time()
    try:
        proc = subprocess.run(
            cmd,
            input=prompt,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            shell=(sys.platform == "win32"),
            timeout=1800
        )
        duration = time.time() - start_time
        if out_file.exists():
            res = out_file.read_text(encoding="utf-8").strip()
            if res:
                return res
        return proc.stdout.strip() or proc.stderr.strip()
    except subprocess.TimeoutExpired:
        return "Codex CLI call timed out after 1800 seconds."
    except Exception as e:
        return f"Failed to execute Codex CLI: {str(e)}"

def call_deepseek_api(prompt: str, model: str = "deepseek-reasoner", api_key: str = None) -> str:
    """Calls DeepSeek API directly via requests."""
    key = api_key or os.environ.get("DEEPSEEK_API_KEY")
    if not key:
        return "Error: DEEPSEEK_API_KEY environment variable is not set."

    try:
        import requests
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": model or "deepseek-reasoner",
            "messages": [{"role": "user", "content": prompt}]
        }
        res = requests.post("https://api.deepseek.com/chat/completions", headers=headers, json=payload, timeout=180)
        res.raise_for_status()
        data = res.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"DeepSeek API error: {str(e)}"

def main():
    parser = argparse.ArgumentParser(description="Universal Inter-Agent CLI Bridge")
    parser.add_argument("target", choices=["claude", "agy", "codex", "chatgpt", "openai", "deepseek"],
                        help="Target provider or agent to invoke")
    parser.add_argument("prompt", help="Prompt string or @filepath containing prompt")
    parser.add_argument("--model", default=None, help="Model override")
    parser.add_argument("--effort", default=None, help="Reasoning effort level")
    parser.add_argument("--workspace", default=None, help="Workspace directory")
    parser.add_argument("--log", default="logs/inter_agent_chat.jsonl", help="Log file path")

    args = parser.parse_args()

    # Resolve workspace
    cwd = Path(args.workspace).resolve() if args.workspace else Path.cwd()
    log_path = Path(args.log) if Path(args.log).is_absolute() else (cwd / args.log)

    # Read prompt from file if prefixed with '@'
    prompt_text = args.prompt
    if prompt_text.startswith("@"):
        prompt_file = Path(prompt_text[1:])
        if not prompt_file.is_absolute():
            prompt_file = cwd / prompt_file
        if prompt_file.exists():
            prompt_text = prompt_file.read_text(encoding="utf-8")
        else:
            sys.stderr.write(f"Error: Prompt file not found: {prompt_file}\n")
            sys.exit(1)

    start_time = time.time()

    # Route request
    if args.target == "claude":
        response = call_claude(prompt_text, model=args.model, effort=args.effort or "medium", cwd=cwd)
        sender, receiver = "Antigravity", "Claude"
    elif args.target == "agy":
        response = call_agy(prompt_text, model=args.model, effort=args.effort or "high", cwd=cwd)
        sender, receiver = "Claude", "Antigravity"
    elif args.target in ("codex", "chatgpt"):
        response = call_codex(prompt_text, model=args.model, cwd=cwd)
        sender, receiver = "Antigravity", "Codex (ChatGPT)"
    elif args.target == "openai":
        response = call_openai_api(prompt_text, model=args.model or "gpt-4o")
        sender, receiver = "Antigravity", "OpenAI"
    elif args.target == "deepseek":
        response = call_deepseek_api(prompt_text, model=args.model or "deepseek-reasoner")
        sender, receiver = "Antigravity", "DeepSeek"
    else:
        response = f"Unsupported target: {args.target}"
        sender, receiver = "Unknown", args.target

    duration = time.time() - start_time
    log_interaction(log_path, sender=sender, receiver=receiver, prompt=prompt_text, response=response, model=args.model, duration=duration)

    # Print pure output to stdout for caller
    print(response)

if __name__ == "__main__":
    main()
