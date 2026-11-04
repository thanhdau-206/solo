---
name: solo
description: >-
  Kỹ năng độc quyền của người dùng (tùy biến 80% từ kiến trúc gốc). Điều phối đấu trường lập kế hoạch
  đa tác tử (Claude Code + Codex/ChatGPT + Gemini/Antigravity) dưới 12 điều luật thép: cấm đồng thuận xã giao,
  bắt lỗi [CHẶN], chấm chéo ẩn danh, đóng băng bản tối ưu và chuyển giao Antigravity thực thi $0 token.
  Kích hoạt khi người dùng gõ /solo, "solo", "chạy solo", "đấu solo", "solo mode", "hội đồng solo", "solo plan".
argument-hint: "[start|status|resume]"
license: Personal / Proprietary
---

# Solo: Multi-AI Planning Tournament ⚔️🧠

**Solo** là kỹ năng lập kế hoạch kỹ thuật đa tác tử (Multi-AI Planning Council) độc quyền của bạn, được xây dựng dựa trên nguyên lý kết hợp tư duy đa mô hình và thực thi tinh gọn:
1. **Claude (Anthropic):** Bậc thầy tư duy kiến trúc, lường trước edge cases, phản biện sắc sảo.
2. **Codex / ChatGPT (OpenAI):** Sáng tạo giải pháp thay thế, pattern tối ưu, kiểm tra thuật toán.
3. **Gemini / Antigravity (Google):** Trọng tài chốt, đánh giá khả thi trên toàn bộ codebase ($0 token).

---

## 📜 12 Điều Luật Thép Của Đấu Trường Solo

Mọi lượt thảo luận phải tuyệt đối tuân thủ file luật tại [`references/RULES.md`](./references/RULES.md):
1. **Mục đích:** Tìm phương án tối ưu nhất theo tiêu chí đề bài, không phải để thắng tranh luận. Thừa nhận ngay khi ý AI khác tốt hơn.
2. **5 Vai trò xoay vòng:** Đề xuất, Giám khảo (chấm chéo), Phát triển, Kiểm định (bắt lỗi), Trọng tài chốt.
3. **Thứ tự ưu tiên khi mâu thuẫn:** `## Tôi` (Người dùng) > Ràng buộc cứng > Luật này > Ý kiến AI.
4. **Trung thực tuyệt đối:** Thiếu thông tin phải ghi `GIẢ ĐỊNH: ...`, số liệu không nguồn phải ghi `ƯỚC TÍNH: ...`. Cấm bịa đặt.
5. **Cấm đồng thuận xã giao:** Cấm khen sáo rỗng ("ý hay", "rất hợp lý"). Đổi ý phải ghi rõ: `ĐỔI Ý: trước tôi cho rằng X, nay là Y, vì Z.`
6. **Cấu trúc phản biện 4 phần:** Vấn đề, Lý do, Mức độ (`[CHẶN]`, `CAO`, `TRUNG BÌNH`, `THẤP`), Cách sửa. Tối đa 3 phản biện/lượt.
7. **Chấm điểm minh bạch:** Thang 1–10 kèm trọng số, nêu rõ phép tính (VD: `0.35×8 + 0.30×9 = ...`). Cấm tự chấm bài của mình.
8. **Độ dài & Định danh:** Đề xuất ≤ 300 chữ, Giám khảo/Kiểm định ≤ 350 chữ, Phát triển ≤ 600 chữ. Đánh mã `PA1`, `PB1`...
9. **Xử lý bế tắc:** Không có ý mới ghi `KHÔNG CÓ Ý MỚI.` Tranh cãi quá 2 vòng chuyển vào mục `CẦN NGƯỜI QUYẾT:`.
10. **Kiểm định khả thi & Nghĩa địa:** Kết luận không khả thi chỉ có hiệu lực khi có lỗi mức `[CHẶN]`. Bản tốt nhất được đóng băng. Bản sửa làm giảm điểm hoặc hỏng tính khả thi sẽ bị hủy ngay. Phương án thất bại vào `graveyard.md`.
11. **Định dạng máy đọc:** `TÊN: ...`, `THAY ĐỔI: ...`, `ĐIỂM PA1: 7.5`, `KHẢ THI: CÓ / KHÔNG`, `ĐIỂM: 7.5`.
12. **Bản chốt hoàn chỉnh:** Gồm phương án chọn, bảng kế hoạch (Bước | Việc cụ thể | Thời gian | Chi phí | Rủi ro chính), ghép ý mạnh từ phương án thua, và rủi ro còn lại.

---

## 🚀 Cách Thức Antigravity Tự Động Xử Lý Khi Kích Hoạt Kỹ Năng

Khi người dùng gõ `/solo` hoặc yêu cầu *"Chạy solo cho bài toán X"*:

### 1. Tiếp nhận & Đóng gói đề bài (`debate.md`)
- Nếu người dùng đã có file `debate.md`, Antigravity dùng trực tiếp file đó.
- Nếu người dùng mô tả đề bài trực tiếp trong chat, Antigravity tự động trích xuất và ghi thành file `debate.md` chuẩn gồm 4 phần:
  - `## Tôi`: Ý định chính của người dùng.
  - `## Mục tiêu`: Bài toán cần giải quyết.
  - `## Ràng buộc cứng`: Thời gian, chi phí, công nghệ, bảo mật.
  - `## Tiêu chí chấm điểm & Trọng số`: Bảng điểm có trọng số.

### 2. Khởi chạy đấu trường (`solo.py` / `solo.ps1`)
Antigravity tự động chạy lệnh trong terminal:
```powershell
python "C:\Users\Admin\.agents\skills\solo\scripts\solo.py" --brief debate.md --target 8.0
```
- Nếu chạy PowerShell cục bộ: `.\solo.ps1 -Brief "debate.md"`

### 3. Trình bày kết quả & Bàn giao Kế hoạch
- Hiển thị tóm tắt bảng xếp hạng các phương án (`ranking.txt`).
- Hiển thị kế hoạch chốt từ `ket-qua.md`.
- Bắt đầu thực thi Stage 2 (Muscle) ngay khi người dùng duyệt, tuân thủ kỷ luật **Ponytail**.
