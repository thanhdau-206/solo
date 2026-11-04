#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
solo.py — Solo Multi-AI Planning & Debate Tournament Engine
Owner: Personal Edition (Customized Multi-AI Planning Council)
Orchestrates Claude, Codex (ChatGPT), and Gemini/Antigravity under 12 strict rules.
"""

import os
import sys
import re
import time
import shutil
import argparse
import subprocess
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# Ensure UTF-8 across all operating systems
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def find_cli(name: str) -> Optional[str]:
    """Locate CLI binary across PATH and user directories."""
    found = shutil.which(name)
    if found:
        return found
    home = Path.home()
    if sys.platform == "win32":
        candidates = [
            home / "AppData" / "Roaming" / "npm" / f"{name}.cmd",
            home / "AppData" / "Roaming" / "npm" / f"{name}.ps1",
            home / "AppData" / "Local" / name / "bin" / f"{name}.exe",
            home / ".gemini" / "bin" / f"{name}.cmd",
            home / ".gemini" / "bin" / f"{name}.exe",
            Path(r"C:\Program Files\Git\bin\bash.exe"),
        ]
        for c in candidates:
            if c.exists():
                return str(c)
    return None

class SoloTournament:
    def __init__(
        self,
        brief_path: str = "debate.md",
        rules_path: Optional[str] = None,
        log_path: str = "tran-dau.md",
        work_dir: str = "work",
        result_path: str = "ket-qua.md",
        per_ai: int = 2,
        target_score: float = 8.0,
        fix_max: int = 2,
        loop_max: int = 10,
        gen_max: int = 3,
        stall_max: int = 2,
        ais: Optional[List[str]] = None,
        timeout: int = 300
    ):
        self.brief_path = Path(brief_path)
        self.log_path = Path(log_path)
        self.work_dir = Path(work_dir)
        self.result_path = Path(result_path)
        self.per_ai = per_ai
        self.target_score = target_score
        self.fix_max = fix_max
        self.loop_max = loop_max
        self.gen_max = gen_max
        self.stall_max = stall_max
        self.ais = ais or ["Claude", "Codex", "Gemini"]
        self.timeout = timeout
        self.ask_task = "Làm đúng nhiệm vụ trong nội dung được gửi kèm."

        # Auto-detect rules file
        candidate_rules = []
        if rules_path:
            candidate_rules.append(Path(rules_path))
        candidate_rules.extend([
            Path("rules/RULES.md"),
            Path(".agents/skills/solo/references/RULES.md"),
            Path.home() / ".gemini" / "config" / "skills" / "solo" / "references" / "RULES.md",
            Path("references/RULES.md")
        ])

        self.rules_path = None
        for r in candidate_rules:
            if r.exists():
                self.rules_path = r
                break

        if not self.rules_path:
            raise FileNotFoundError("Không tìm thấy file luật RULES.md")

        if not self.brief_path.exists():
            raise FileNotFoundError(f"Không tìm thấy file đề bài: {self.brief_path}")

    def say(self, message: str):
        print(f"\033[1;33m{message}\033[0m")
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(f"\n> **{message}**\n\n")

    def call_ai(self, ai: str, prompt_file: Path) -> str:
        prompt_content = prompt_file.read_text(encoding="utf-8")
        out_file = self.work_dir / f".out_{ai}.txt"

        if ai == "Claude":
            bin_path = find_cli("claude") or "claude"
            try:
                proc = subprocess.run(
                    [bin_path, "-p", "-"],
                    input=prompt_content,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    shell=(sys.platform == "win32"),
                    timeout=self.timeout
                )
                return proc.stdout.strip() or proc.stderr.strip()
            except Exception as e:
                return f"[Claude Error]: {e}"

        elif ai == "Codex":
            bin_path = find_cli("codex") or "codex"
            try:
                proc = subprocess.run(
                    [bin_path, "exec", "--skip-git-repo-check", "--ephemeral", "-o", str(out_file), "-"],
                    input=prompt_content,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    shell=(sys.platform == "win32"),
                    timeout=self.timeout
                )
                if out_file.exists():
                    text = out_file.read_text(encoding="utf-8").strip()
                    if text:
                        return text
                return proc.stdout.strip() or proc.stderr.strip()
            except Exception as e:
                return f"[Codex Error]: {e}"

        elif ai == "Gemini":
            bin_gemini = find_cli("gemini")
            bin_agy = find_cli("agy")
            use_agy = True
            if bin_gemini:
                try:
                    chk = subprocess.run([bin_gemini, "--version"], capture_output=True, shell=True)
                    if chk.returncode == 0:
                        use_agy = False
                except Exception:
                    use_agy = True

            target_bin = bin_agy if use_agy else (bin_gemini or "gemini")
            try:
                proc = subprocess.run(
                    [target_bin, "-p", "-"],
                    input=prompt_content,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    shell=(sys.platform == "win32"),
                    timeout=self.timeout
                )
                return proc.stdout.strip() or proc.stderr.strip()
            except Exception as e:
                return f"[Gemini/Antigravity Error]: {e}"

        return f"[Error]: Unknown AI {ai}"

    def ask(self, ai: str, role: str, task: str, *context_files: Path) -> str:
        pf = self.work_dir / f".prompt_{ai}_{int(time.time()*1000)%10000}.md"
        prompt_lines = [
            "# LUẬT",
            self.rules_path.read_text(encoding="utf-8"),
            "",
            "# ĐỀ BÀI",
            self.brief_path.read_text(encoding="utf-8"),
            ""
        ]

        for cf in context_files:
            if cf.exists() and cf.stat().st_size > 0:
                prompt_lines.extend([
                    f"# NGỮ CẢNH: {cf.name}",
                    cf.read_text(encoding="utf-8"),
                    ""
                ])

        prompt_lines.extend([
            f"# NHIỆM VỤ CỦA BẠN — {ai}, vai {role}",
            task,
            ""
        ])

        pf.write_text("\n".join(prompt_lines), encoding="utf-8")

        print(f"\n\033[1;36m▶ {ai} – {role}\033[0m")
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(f"\n## {ai} – {role}\n\n")

        response = self.call_ai(ai, pf)

        print(response)
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(response + "\n\n")

        return response

    def alive(self, pid: str) -> bool:
        dead_file = self.work_dir / "dead.txt"
        if not dead_file.exists():
            return True
        dead_list = dead_file.read_text(encoding="utf-8").splitlines()
        return pid not in [d.strip() for d in dead_list if d.strip()]

    def author(self, pid: str) -> str:
        author_file = self.work_dir / "pool" / f"{pid}.author"
        if author_file.exists():
            return author_file.read_text(encoding="utf-8").strip()
        return "Unknown"

    def ids_alive(self) -> List[str]:
        pool_dir = self.work_dir / "pool"
        if not pool_dir.exists():
            return []
        ids = []
        for f in sorted(pool_dir.glob("PA*.md"), key=lambda p: int(re.sub(r"\D", "", p.stem) or 0)):
            pid = f.stem
            if self.alive(pid):
                ids.append(pid)
        return ids

    def build_alive(self):
        pool_alive = self.work_dir / "pool_alive.md"
        lines = []
        for pid in self.ids_alive():
            content = (self.work_dir / "pool" / f"{pid}.md").read_text(encoding="utf-8")
            lines.append(f"\n## {pid}\n\n{content}\n")
        pool_alive.write_text("\n".join(lines), encoding="utf-8")

    def diverge(self, gen_round: int):
        self.say(f"ĐỢT TẠO PHƯƠNG ÁN {gen_round}")
        pool_dir = self.work_dir / "pool"
        existing = list(pool_dir.glob("PA*.md"))
        n = len(existing)

        for ai in self.ais:
            for _ in range(self.per_ai):
                n += 1
                pid = f"PA{n}"
                self.build_alive()
                task = (
                    "Viết MỘT phương án mới cho đề bài, KHÁC HẲN về hướng đi so với các phương án trong ngữ cảnh. "
                    "Không lặp lại lý do thất bại trong nghĩa địa. Dòng đầu: 'TÊN: <tên ngắn>'. Tối đa 300 chữ."
                )
                resp = self.ask(
                    ai, f"Đề xuất {pid}", task,
                    self.work_dir / "pool_alive.md",
                    self.work_dir / "graveyard.md"
                )
                (self.work_dir / "pool" / f"{pid}.md").write_text(resp, encoding="utf-8")
                (self.work_dir / "pool" / f"{pid}.author").write_text(ai, encoding="utf-8")

    def score_pool(self):
        self.say("CHẤM CHÉO")
        self.build_alive()
        scores_map: Dict[str, List[float]] = {}

        for ai in self.ais:
            eval_ids = [pid for pid in self.ids_alive() if self.author(pid) != ai]
            if not eval_ids:
                continue
            ids_str = " ".join(eval_ids)
            task = (
                f"Chấm các phương án: {ids_str} theo bảng tiêu chí trong đề bài (thang 10, có trọng số). "
                f"Phương án vi phạm ràng buộc cứng thì tối đa 4 điểm. KẾT THÚC bằng đúng mỗi phương án một dòng theo mẫu:\n"
                f"ĐIỂM PA1: 7.5"
            )
            resp = self.ask(ai, "Giám khảo", task, self.work_dir / "pool_alive.md")
            clean_resp = resp.replace("*", "")
            matches = re.findall(r"ĐIỂM\s+(PA\d+)\s*:\s*([0-9]+(?:[.,][0-9]+)?)", clean_resp, re.IGNORECASE)
            for m_pid, m_score in matches:
                m_pid = m_pid.upper()
                if m_pid in eval_ids:
                    s_val = float(m_score.replace(",", "."))
                    scores_map.setdefault(m_pid, []).append(s_val)

        ranking = []
        for pid, s_list in scores_map.items():
            avg = sum(s_list) / len(s_list)
            ranking.append((pid, avg))

        ranking.sort(key=lambda x: x[1], reverse=True)
        ranking_file = self.work_dir / "ranking.txt"
        ranking_lines = [f"{pid} {score:.2f}" for pid, score in ranking]
        ranking_file.write_text("\n".join(ranking_lines), encoding="utf-8")

        table_lines = ["\n### Bảng xếp hạng\n", "| Phương án | Điểm TB |", "|---|---|"]
        for pid, score in ranking:
            table_lines.append(f"| {pid} | {score:.2f} |")
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write("\n".join(table_lines) + "\n\n")

    def pick(self) -> Optional[Tuple[str, float]]:
        ranking_file = self.work_dir / "ranking.txt"
        if not ranking_file.exists():
            return None
        for line in ranking_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) >= 2:
                pid, score_str = parts[0], parts[1]
                if self.alive(pid):
                    return pid, float(score_str)
        return None

    def bury(self, pid: str):
        self.say(f"LOẠI {pid} — xem lý do trong nghĩa địa")
        with open(self.work_dir / "dead.txt", "a", encoding="utf-8") as f:
            f.write(f"{pid}\n")

        p_file = self.work_dir / "pool" / f"{pid}.md"
        first_lines = "\n".join(p_file.read_text(encoding="utf-8").splitlines()[:3]) if p_file.exists() else ""
        issues_file = self.work_dir / "issues.md"
        blockers = []
        if issues_file.exists():
            for line in issues_file.read_text(encoding="utf-8").splitlines():
                if "[CHẶN]" in line.upper():
                    blockers.append(line.strip())
                    if len(blockers) >= 5:
                        break

        with open(self.work_dir / "graveyard.md", "a", encoding="utf-8") as f:
            f.write(f"\n## {pid} — BỊ LOẠI (không khả thi sau {self.fix_max} lần sửa)\n\n")
            f.write(f"{first_lines}\n\nLý do:\n" + "\n".join(blockers) + "\n\n")

    def run(self):
        if self.work_dir.exists():
            shutil.rmtree(self.work_dir)
        (self.work_dir / "pool").mkdir(parents=True, exist_ok=True)
        (self.work_dir / "dead.txt").write_text("", encoding="utf-8")
        (self.work_dir / "graveyard.md").write_text("", encoding="utf-8")
        (self.work_dir / "scores.txt").write_text("", encoding="utf-8")

        start_time_str = time.strftime("%d/%m/%Y %H:%M")
        self.log_path.write_text(f"# TRẬN ĐẤU SOLO — {start_time_str}\n\n", encoding="utf-8")

        gen = 1
        self.diverge(gen)
        self.score_pool()

        loop_count = 0
        done_reason = ""
        best_plan_ok = False
        best_score = 0.0

        while not done_reason:
            pick_res = self.pick()
            if not pick_res:
                if gen >= self.gen_max:
                    done_reason = "hết-phương-án"
                    break
                gen += 1
                self.diverge(gen)
                self.score_pool()
                continue

            cur_id, cur_score = pick_res
            dev_ai = self.author(cur_id)
            self.say(f"CHỌN {cur_id} (điểm {cur_score:.2f}) — {dev_ai} phát triển")

            shutil.copy2(self.work_dir / "pool" / f"{cur_id}.md", self.work_dir / "best.md")
            shutil.copy2(self.work_dir / "best.md", self.work_dir / "work.md")
            best_score = 0.0
            best_plan_ok = False
            fix_count = 0
            stall_count = 0
            (self.work_dir / "issues.md").write_text("", encoding="utf-8")

            while True:
                loop_count += 1
                if loop_count > self.loop_max:
                    done_reason = "hết-lượt"
                    break

                self.say(f"VÒNG {loop_count} — {cur_id}")
                dev_task = (
                    "Phát triển phương án thành kế hoạch chi tiết theo mục 12 của luật. "
                    "Nếu có danh sách vấn đề: CHỈ sửa đúng các vấn đề đó (ưu tiên [CHẶN] rồi CAO), "
                    "giữ nguyên phần còn lại. Mở đầu bằng mục 'THAY ĐỔI:' liệt kê đã sửa gì. Được viết tới 600 chữ."
                )
                cand_resp = self.ask(
                    dev_ai, f"Phát triển {cur_id}", dev_task,
                    self.work_dir / "work.md",
                    self.work_dir / "issues.md"
                )
                (self.work_dir / "cand.md").write_text(cand_resp, encoding="utf-8")

                (self.work_dir / "issues.md").write_text("", encoding="utf-8")
                is_feasible = True
                crit_scores = []

                for c_ai in self.ais:
                    if c_ai == dev_ai:
                        continue
                    crit_task = (
                        "Kiểm tra kế hoạch này. (1) Khả thi: đối chiếu từng ràng buộc cứng trong đề bài. "
                        "Vấn đề khiến kế hoạch KHÔNG THỂ thực hiện thì gắn nhãn [CHẶN] và nêu đúng ràng buộc bị vi phạm. "
                        "(2) Các vấn đề khác theo mục 6 của luật. Tối đa 3 phản biện, 350 chữ. Không nhắc lại vấn đề đã được sửa. "
                        "KẾT THÚC bằng đúng 2 dòng:\n"
                        "KHẢ THI: CÓ   (hoặc KHẢ THI: KHÔNG)\n"
                        "ĐIỂM: 7.5"
                    )
                    crit_resp = self.ask(c_ai, f"Kiểm định {cur_id}", crit_task, self.work_dir / "cand.md")
                    (self.work_dir / f"crit_{c_ai}.md").write_text(crit_resp, encoding="utf-8")

                    clean_crit = crit_resp.replace("*", "")
                    if re.search(r"KHẢ\s+THI\s*:\s*KHÔNG", clean_crit, re.IGNORECASE) and "[CHẶN]" in clean_crit.upper():
                        is_feasible = False

                    score_match = re.findall(r"ĐIỂM\s*:\s*([0-9]+(?:[.,][0-9]+)?)", clean_crit, re.IGNORECASE)
                    if score_match:
                        crit_scores.append(float(score_match[-1].replace(",", ".")))

                    with open(self.work_dir / "issues.md", "a", encoding="utf-8") as f:
                        f.write(f"### Từ {c_ai}\n\n{crit_resp}\n\n")

                round_score = (sum(crit_scores) / len(crit_scores)) if crit_scores else 0.0
                is_better = round_score > best_score

                if is_feasible:
                    if not best_plan_ok or is_better:
                        shutil.copy2(self.work_dir / "cand.md", self.work_dir / "best.md")
                        best_score = round_score
                        best_plan_ok = True
                        stall_count = 0
                        self.say(f"✅ Khả thi — điểm {round_score:.2f} — NHẬN làm bản tốt nhất")
                    else:
                        stall_count += 1
                        self.say(f"↩️ Khả thi nhưng điểm {round_score:.2f} không hơn {best_score:.2f} — GIỮ bản cũ (lần {stall_count})")

                    shutil.copy2(self.work_dir / "best.md", self.work_dir / "work.md")
                    fix_count = 0

                    if best_score >= self.target_score:
                        done_reason = "đạt-mục-tiêu"
                        break
                    if stall_count >= self.stall_max:
                        done_reason = "hội-tụ"
                        break
                else:
                    fix_count += 1
                    if best_plan_ok:
                        self.say("❌ Bản sửa làm hỏng tính khả thi — BỎ bản sửa, quay về bản tốt nhất")
                        shutil.copy2(self.work_dir / "best.md", self.work_dir / "work.md")
                    else:
                        self.say(f"❌ Chưa khả thi (lần {fix_count}, cho phép sửa {self.fix_max} lần)")
                        shutil.copy2(self.work_dir / "cand.md", self.work_dir / "work.md")

                    if fix_count > self.fix_max:
                        if best_plan_ok:
                            done_reason = "hội-tụ"
                            break
                        else:
                            self.bury(cur_id)
                            break

        self.say(f"KẾT THÚC: {done_reason}")
        if best_plan_ok:
            arbitrator_ai = "Gemini" if "Gemini" in self.ais else self.ais[0]
            arb_task = (
                f"Viết KẾ HOẠCH CUỐI CÙNG theo mục 12 của luật, dựa trên bản tốt nhất. "
                f"Ghép ý mạnh từ các phương án khác nếu không phá vỡ tính khả thi. "
                f"Lý do kết thúc: {done_reason}. "
                f"Nếu chưa đạt điểm mục tiêu {self.target_score}, nêu rõ còn thiếu gì trong mục CẦN NGƯỜI QUYẾT."
            )
            final_res = self.ask(
                arbitrator_ai, "Trọng tài chốt", arb_task,
                self.work_dir / "best.md",
                self.work_dir / "issues.md",
                self.work_dir / "pool_alive.md",
                self.work_dir / "graveyard.md"
            )
            self.result_path.write_text(final_res, encoding="utf-8")
            print(f"\n\033[1;32mXong. Kế hoạch cuối: {self.result_path} — diễn biến: {self.log_path}\033[0m")
        else:
            graveyard_text = (self.work_dir / "graveyard.md").read_text(encoding="utf-8") if (self.work_dir / "graveyard.md").exists() else ""
            self.result_path.write_text(
                f"# CHƯA CÓ PHƯƠNG ÁN KHẢ THI\n\nLý do kết thúc: {done_reason}\n\n{graveyard_text}\n",
                encoding="utf-8"
            )
            print(f"\n\033[1;31mKhông tìm được phương án khả thi. Xem {self.result_path} — có thể ràng buộc trong đề bài quá chặt.\033[0m")

def main():
    parser = argparse.ArgumentParser(description="Solo Multi-AI Planning & Debate Tournament")
    parser.add_argument("--brief", default="debate.md", help="Đường dẫn file đề bài (mặc định: debate.md)")
    parser.add_argument("--rules", default=None, help="Đường dẫn file luật (mặc định: tự động tìm RULES.md)")
    parser.add_argument("--log", default="tran-dau.md", help="Đường dẫn file ghi diễn biến (mặc định: tran-dau.md)")
    parser.add_argument("--result", default="ket-qua.md", help="Đường dẫn file kết quả (mặc định: ket-qua.md)")
    parser.add_argument("--per-ai", type=int, default=2, help="Số phương án mỗi AI đưa ra mỗi đợt")
    parser.add_argument("--target", type=float, default=8.0, help="Điểm tối thiểu để chốt")
    parser.add_argument("--fix-max", type=int, default=2, help="Số lần sửa tối đa trước khi loại phương án")
    parser.add_argument("--loop-max", type=int, default=10, help="Tổng số vòng lặp tối đa")
    parser.add_argument("--gen-max", type=int, default=3, help="Số đợt tạo phương án mới tối đa")
    parser.add_argument("--stall-max", type=int, default=2, help="Số lần sửa liên tiếp không tốt hơn thì hội tụ")

    args = parser.parse_args()

    tournament = SoloTournament(
        brief_path=args.brief,
        rules_path=args.rules,
        log_path=args.log,
        result_path=args.result,
        per_ai=args.per_ai,
        target_score=args.target,
        fix_max=args.fix_max,
        loop_max=args.loop_max,
        gen_max=args.gen_max,
        stall_max=args.stall_max
    )
    tournament.run()

if __name__ == "__main__":
    main()
