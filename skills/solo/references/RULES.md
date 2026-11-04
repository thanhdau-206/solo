# LUẬT CHUNG CHO CUỘC TRANH LUẬN GIỮA CÁC AI

Áp dụng cho mọi AI tham gia (Claude, Codex, Gemini, Antigravity). Đọc kỹ trước khi viết bất kỳ lượt nào.

## 1. Mục đích
- Mục tiêu là tìm ra **phương án tốt nhất theo tiêu chí trong đề bài**, không phải thắng tranh luận.
- Phương án của AI khác tốt hơn thì phải thừa nhận. Bảo vệ ý mình khi nó sai là vi phạm luật.

## 2. Các vai
Mỗi lượt, phần NHIỆM VỤ sẽ ghi rõ bạn đang đóng vai nào. Một AI có thể đóng nhiều vai ở các lượt khác nhau.

| Vai | Làm gì | Chấm gì |
|---|---|---|
| Đề xuất | Đưa MỘT phương án mới, khác hẳn các phương án đã có | Không chấm |
| Giám khảo | Chấm các phương án gốc (PA1, PA2…) để chọn ra phương án đem phát triển | Chỉ phương án KHÔNG phải của mình |
| Phát triển | Biến phương án được chọn thành kế hoạch chi tiết, sửa theo kiểm định | Không chấm |
| Kiểm định | Kiểm tra tính khả thi và chấm bản kế hoạch đang phát triển | Chỉ kế hoạch KHÔNG phải mình phát triển |
| Trọng tài chốt | Viết kế hoạch cuối cùng | Không chấm |

## 3. Thứ tự ưu tiên khi có mâu thuẫn
1. Dòng do người dùng viết (tiêu đề `## Tôi`)
2. Ràng buộc cứng trong đề bài
3. Luật này
4. Ý kiến của các AI

## 4. Trung thực với dữ kiện
- Chỉ dựa trên đề bài, nội dung thảo luận và kiến thức đã biết chắc.
- Thông tin thiếu thì ghi `GIẢ ĐỊNH: ...`. Không tự bịa.
- Con số không có nguồn thì ghi `ƯỚC TÍNH: ...` kèm cách ước tính.
- Không chắc thì nói không chắc.

## 5. Cấm đồng thuận xã giao
- Cấm khen chung chung ("ý hay", "rất hợp lý"…).
- Đồng ý thì nói rõ đồng ý **điểm nào** và **vì sao**.
- Chỉ được đổi ý khi có lập luận hoặc dữ kiện mới, và phải ghi: `ĐỔI Ý: trước tôi cho rằng X, nay là Y, vì Z.`
- Không được nhượng bộ chỉ để kết thúc tranh luận.

## 6. Cách phản biện
Mỗi phản biện (mã PB1, PB2…) phải đủ 4 phần:
- **Vấn đề:** chỗ sai hoặc yếu, trích đúng mã ý bị phản biện (VD: PA2.3)
- **Lý do:** vì sao đó là vấn đề, có dữ kiện hoặc lập luận
- **Mức độ:** một trong 4 mức
  - `[CHẶN]` — vi phạm ràng buộc cứng, phải nêu đúng ràng buộc nào
  - `CAO` — không vi phạm ràng buộc nhưng ảnh hưởng lớn đến kết quả
  - `TRUNG BÌNH`
  - `THẤP`
- **Cách sửa:** đề xuất cụ thể

Quy tắc thêm:
- Mỗi lượt tối đa **3 phản biện**, chọn 3 vấn đề nặng nhất.
- Trước khi bác một ý, tóm tắt lại ý đó ở dạng mạnh nhất (1 câu) để chắc mình hiểu đúng.
- Đánh vào lập luận, không đánh vào AI đã viết nó.
- Không bắt bẻ câu chữ.

## 7. Chấm điểm
- Chấm theo bảng tiêu chí và trọng số trong đề bài, thang 1–10 cho từng tiêu chí, mỗi điểm kèm 1 câu lý do.
- Không chấm bài của chính mình (xem mục 2).
- Chấm trên nội dung, không đoán tác giả.
- Điểm tổng phải ghi rõ phép tính trước khi ra kết quả. VD: `0.3×8 + 0.2×6 + 0.5×7 = 7.1`
- Bảng tiêu chí KHÔNG được đổi giữa các vòng.

## 8. Hình thức mỗi lượt
- Độ dài tối đa:
  - Đề xuất: 300 chữ
  - Giám khảo, Kiểm định: 350 chữ
  - Phát triển: 600 chữ
  - Trọng tài chốt: không giới hạn
- Đánh mã cố định:
  - Phương án: `PA1`, `PA2`… Ý nhỏ bên trong: `PA1.1`, `PA1.2`…
  - Phản biện: `PB1`, `PB2`…
- Chỉ viết phần của mình. Không sửa, xóa phần người khác.
- Không lặp lại ý đã có. Chỉ trích mã ý.

## 9. Khi bế tắc hoặc hết ý
- Không còn gì mới thì chỉ ghi: `KHÔNG CÓ Ý MỚI.`
- Bất đồng đã qua 2 vòng mà chưa ngã ngũ thì ghi vào mục `CẦN NGƯỜI QUYẾT:` kèm 2 lựa chọn và hệ quả của từng lựa chọn. Không tiếp tục cãi.

## 10. Khả thi và vòng lặp
**Định nghĩa khả thi:** kế hoạch KHÔNG vi phạm ràng buộc cứng nào trong đề bài (tiền, thời gian, nhân lực, kỹ năng, công cụ) và mọi bước đều có người làm được với nguồn lực hiện có.

- Kết luận "không khả thi" chỉ có hiệu lực khi có ít nhất một phản biện mức `[CHẶN]`. Không có `[CHẶN]` thì coi là khả thi.
- Không được gắn `[CHẶN]` cho chuyện "có thể làm tốt hơn". Đó là mức CAO hoặc TRUNG BÌNH.
- Khi sửa: chỉ sửa đúng các vấn đề được nêu, ưu tiên `[CHẶN]` rồi CAO. Cấm viết lại toàn bộ — đó là nguyên nhân khiến kế hoạch càng sửa càng lệch.
- Bản tốt nhất được đóng băng. Bản sửa chỉ thay thế khi vẫn khả thi VÀ điểm cao hơn. Nếu không, bản sửa bị bỏ.
- Phương án sửa nhiều lần vẫn không khả thi thì bị loại vào **nghĩa địa** kèm lý do. Phương án mới sau đó phải tránh đúng các lý do này.
- Kiểm định chỉ đưa vấn đề mới. Vấn đề đã được sửa không nhắc lại.

## 11. Định dạng bắt buộc để máy đọc được
Các dòng dưới đây viết **văn bản thuần**: không in đậm, không `**`, không thêm `/10`, mỗi dòng đứng riêng.
- Đề xuất: dòng đầu tiên là `TÊN: <tên ngắn>`
- Phát triển: dòng đầu tiên là `THAY ĐỔI:` rồi liệt kê đã sửa gì
- Giám khảo: kết thúc bằng mỗi phương án một dòng, dạng `ĐIỂM PA1: 7.5`
- Kiểm định: kết thúc bằng đúng 2 dòng
  ```
  KHẢ THI: CÓ
  ĐIỂM: 7.5
  ```
  (hoặc `KHẢ THI: KHÔNG`)

## 12. Kết quả cuối cùng
Bản chốt phải gồm:
1. Phương án được chọn và lý do (dựa trên điểm chấm)
2. Bảng kế hoạch: Bước | Việc cụ thể | Thời gian | Chi phí | Rủi ro chính
3. Các ý được ghép từ phương án thua
4. Rủi ro còn lại và cách theo dõi
5. Mục `CẦN NGƯỜI QUYẾT` (nếu còn)
