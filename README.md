<div align="center">

# ⚔️ Solo
### Multi-AI Planning Council & Debate Tournament Protocol (Claude + ChatGPT + Gemini) & Antigravity Muscle

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Antigravity](https://img.shields.io/badge/Muscle-Antigravity%20($0%20Tokens)-4285F4.svg)](#)
[![Multi-AI Council](https://img.shields.io/badge/Brain-Claude%20%7C%20Codex%20%7C%20Gemini-D97706.svg)](#)
[![Code Discipline](https://img.shields.io/badge/Discipline-Ponytail%20Lean-10B981.svg)](#)

*One commander. Three frontier AIs. Twelve ironclad rules. Zero social consensus.*  
**Solo orchestrates Claude Code, OpenAI Codex (ChatGPT), and Google Gemini into a high-stakes planning tournament, then deploys Antigravity to build at $0 token cost.**

</div>

---

## 💡 The Philosophy of Solo

When you rely on a single AI model to both plan and code, you inevitably get:
- **Confirmation bias & hallucinated simplicity**
- **Over-engineered architecture and boilerplate ("AI Slop")**
- **Astronomical API token expenses**

**Solo solves this completely:**
1. **You are the Commander (`## Tôi`):** Your directives and constraints have absolute priority.
2. **Multi-AI Tournament (The Brain):** Claude, Codex, and Gemini debate under **12 ironclad rules**—no polite flattery, strict `[CHẶN]` feasibility tags, blind cross-scoring, regression freezes, and automatic graveyard for failing ideas.
3. **Antigravity (The Muscle):** Once the winning blueprint is forged at `ket-qua.md`, Antigravity ingests the whole codebase and writes clean code under **Ponytail discipline** at **$0 token cost**.

---

## 🏗️ Architecture: Tournament Planning & Muscle Execution

```mermaid
sequenceDiagram
    autonumber
    actor Commander as 👑 Commander (You)
    participant Council as ⚔️ Multi-AI Council (Claude + Codex + Gemini)
    participant Muscle as 🛠️ Antigravity Muscle ($0 Token Cost)
    participant Gate as 🛡️ Quality Gate (Diff Auditor)

    Commander->>Council: Submit Technical Brief (debate.md)
    rect rgb(255, 250, 240)
        Note over Council: Stage 1: Solo Tournament Loop (12 Ironclad Rules)<br/>1. Diverge: Independent rival proposals (PA1, PA2...)<br/>2. Blind Scoring: Cross-evaluation with explicit calculations<br/>3. Feasibility Audit: Strict [CHẶN] tags against hard constraints<br/>4. Freeze & Graveyard: Discard regressions; retire failed ideas<br/>5. Arbitration: Final actionable blueprint saved to ket-qua.md
    end
    Council->>Muscle: Deliver Feasibility-Verified Blueprint (ket-qua.md)
    rect rgb(240, 248, 255)
        Note over Muscle: Stage 2: Heavy Execution ($0 Token Cost)<br/>Reads repository, authors minimal diffs, executes test suites
    end
    Muscle->>Gate: Submit Git Diff for Final Verification
    alt Issues Detected
        Gate-->>Muscle: Line-by-line remediation
        Muscle->>Muscle: Auto-fix code
    else Approved
        Gate-->>Commander: Deliver completed, verified feature
    end
```

---

## 📜 12 Ironclad Rules of the Solo Arena

All deliberations strictly follow [`rules/RULES.md`](rules/RULES.md):

1. **Objective Truth:** The sole goal is the best plan under specified criteria. Acknowledge superior solutions immediately. Defending bad ideas is a direct violation.
2. **5 Rotating Roles:** Proposer (`Đề xuất`), Blind Judge (`Giám khảo`), Developer (`Phát triển`), Feasibility Auditor (`Kiểm định`), Final Arbitrator (`Trọng tài chốt`).
3. **Conflict Hierarchy:** User Directives (`## Tôi`) > Hard Constraints (`## Ràng buộc cứng`) > Rules > AI Opinions.
4. **Factual Honesty:** Missing information must be marked `GIẢ ĐỊNH:`; unverified figures must be marked `ƯỚC TÍNH:`. Zero fabrication.
5. **Banned Polite Consensus:** Superficial praise is strictly forbidden. Changing opinions requires explicit explanation: `ĐỔI Ý: trước tôi cho rằng X, nay là Y, vì Z.`
6. **4-Part Structured Critiques:** Issue, Reason, Severity (`[CHẶN]`, `CAO`, `TRUNG BÌNH`, `THẤP`), and Actionable Fix. Max 3 critiques per turn.
7. **Transparent Weighted Scoring:** 1–10 scale based on defined weights; calculations must be shown explicitly (e.g., `0.35×8 + 0.30×9 = 8.65`). Never score own proposals.
8. **Word Limits & Identity Codes:** Proposals ≤ 300 words, Audits ≤ 350 words, Development ≤ 600 words using immutable IDs (`PA1`, `PB1`).
9. **Deadlock Resolution:** If debate reaches no new insights, output `KHÔNG CÓ Ý MỚI.` After 2 deadlocked rounds, escalate to `CẦN NGƯỜI QUYẾT:`.
10. **Feasibility Gate & Graveyard:** "Infeasible" requires at least one `[CHẶN]` tag. Revisions that degrade score or break feasibility are rolled back to the frozen best. Failing ideas are permanently retired to `graveyard.md`.
11. **Machine-Readable Formats:** Standard tokens (`TÊN:`, `THAY ĐỔI:`, `ĐIỂM PA1: 7.5`, `KHẢ THI: CÓ/KHÔNG`).
12. **Final Deliverable Structure:** Winning proposal and rationale, complete task breakdown table (Step | Task | Time | Cost | Key Risk), runner-up synthesis, and remaining risk mitigation.

---

## 🚀 Quickstart

### Prerequisites
- Python 3.10+
- Installed CLIs:
  - [Google Antigravity CLI](https://antigravity.google) (`agy`)
  - [Anthropic Claude Code CLI](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) (`claude`)
  - [OpenAI Codex CLI](https://github.com/openai/codex) (`codex`)

### 1-Click Install

#### Windows (PowerShell)
```powershell
git clone https://github.com/thanhdau-206/solo.git
cd solo
.\install.ps1
```

#### macOS / Linux (Bash)
```bash
git clone https://github.com/thanhdau-206/solo.git
cd solo
chmod +x install.sh
./install.sh
```

---

## 🎮 How to Run the Solo Tournament

### 1. Define your brief in `debate.md`
```markdown
# ĐỀ BÀI TRANH LUẬN LẬP KẾ HOẠCH

## Tôi
Xây dựng kiến trúc module giao dịch tự động và phòng ngừa rủi ro...

## Mục tiêu
Thiết kế hệ thống nhận diện tín hiệu giao dịch thời gian thực.

## Ràng buộc cứng
1. Thời gian triển khai tối đa 7 ngày.
2. Ngân sách API dưới $50/tháng.
3. Không tự viết ORM hoặc framework cồng kềnh.

## Tiêu chí chấm điểm & Trọng số
| Tiêu chí | Trọng số |
| Tính khả thi & Tuân thủ ràng buộc | 0.35 |
| Độ tinh gọn (Ponytail) | 0.30 |
| Quản trị rủi ro & Xử lý lỗi | 0.20 |
| Tốc độ triển khai | 0.15 |
```

### 2. Launch the Tournament

**Windows (PowerShell 1-Click):**
```powershell
.\solo.ps1 -Brief "debate.md" -Target 8.0
```

**Cross-Platform (Python):**
```powershell
python solo.py --brief debate.md --target 8.0
```

**Linux / macOS (Bash):**
```bash
bash solo.sh --brief debate.md --target 8.0
```

### 3. Review Transcript & Deploy Muscle
- **`tran-dau.md`:** Complete real-time transcript of every clash, score, and critique.
- **`ket-qua.md`:** The finalized battle-tested blueprint.
- Tell Antigravity: *"Triển khai kế hoạch trong ket-qua.md"* to build at $0 token cost!

---

## 📁 Repository Structure

```text
solo/
├── solo.py                  # Universal Multi-AI Tournament Engine (Python)
├── solo.ps1                 # 1-Click Windows PowerShell Runner
├── solo.sh                  # 1-Click macOS/Linux Bash Runner
├── debate.md                # Standard Brief Template
├── rules/
│   └── RULES.md             # The 12 Ironclad Rules of AI Debate
├── bridge/                  # Universal Inter-Agent CLI Bridge
│   ├── __init__.py
│   └── bridge.py            # Bridge router for Claude, Codex, Agy, OpenAI
├── skills/                  # Portable Agent Skills
│   ├── solo/                # Solo Tournament Skill definition
│   │   ├── SKILL.md
│   │   ├── references/
│   │   ├── scripts/
│   │   └── templates/
│   └── ponytail/            # Zero-slop lean code discipline
│       └── SKILL.md
├── install.ps1              # Windows 1-Click Installer
├── install.sh               # macOS/Linux 1-Click Installer
├── requirements.txt         # Minimal dependencies
├── .env.example             # Safe template with zero secrets
└── LICENSE                  # Permissive MIT License
```

---

## 🔒 Security & Privacy Guarantee

- **Zero Credential Persistence:** Solo never stores API keys or tokens in code or git.
- **Local Inter-Process Communication:** All agent deliberations run via local pipes (`stdin`/`stdout`). No third-party relay servers.
- **Isolated Artifacts:** All tournament logs and work folders stay strictly on your local disk in `work/` and `tran-dau.md`.

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

<div align="center">
  <sub>Developed with ⚔️ by <a href="https://github.com/thanhdau-206">thanhdau-206</a> for the autonomous agent era.</sub>
</div>
