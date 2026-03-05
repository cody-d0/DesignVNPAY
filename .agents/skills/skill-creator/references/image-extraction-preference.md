# Image extraction: Agent + path vs OCR script

## Case

- **Thực tế:** Agent lấy thông tin từ ảnh rất dễ — chỉ cần path ảnh và tool đọc ảnh (vd. Read với file ảnh), agent có thể trích xuất text + layout + thành phần UI với kết quả tốt (hiểu ngữ nghĩa, không chỉ raw text).
- **Khuynh hướng khi tạo skill:** Đi theo hướng OCR → build script (Tesseract, verify-env, batch script) vì nghĩ "trích xuất từ ảnh = cần OCR".
- **Hệ quả:** Skill phình ra (script, env check, pipeline gate), trong khi nhiều use case chỉ cần "agent + path ảnh" là đủ và thường cho chất lượng tốt hơn (semantic, layout, UI elements).

## Nguyên nhân

1. **Mental model:** "Image → text" gợi đến OCR (Tesseract, API) nên dễ mặc định thêm script.
2. **Skill-creator gợi ý script** khi "same code rewritten repeatedly" hoặc "deterministic reliability" — với extraction từ ảnh, agent đọc ảnh mỗi lần không phải "rewrite code", mà là dùng capability sẵn có.
3. **Không phân biệt rõ:** (a) agent đọc ảnh từ path và mô tả/trích xuất theo prompt vs (b) pipeline batch cần output máy móc (bbox, exit code, không có agent trong vòng lặp).

## Guideline: Khi nào dùng gì

| Nhu cầu | Ưu tiên | Lý do |
|--------|--------|-------|
| Trích xuất thông tin từ ảnh (text, label, nút, form, màn hình) cho phân tích / PRD / doc | **Agent + path ảnh** | Agent có vision; kết quả có ngữ nghĩa, layout; ít lỗi hơn OCR thuần; không cần script, không phụ thuộc Tesseract. |
| Một skill "chỉ làm một việc là OCR" | **Không cần skill riêng** | Công việc thực tế là "đọc ảnh tại path và trả về nội dung" — agent + path đã đáp ứng; skill chỉ cần mô tả input (path/list path) và output (format text/structured). |
| Batch không tương tác: CI chạy trên N ảnh, không có agent trong vòng lặp | OCR script / API | Cần deterministic, exit code, output format cố định. |
| Yêu cầu bbox/coordinates từng ký tự hoặc tích hợp với tool khác (Figma, design tool) | OCR script hoặc Vision API có bbox | Agent vision thường không trả về bbox chi tiết. |
| Môi trường headless, không có model vision | OCR script | Fallback khi agent không đọc ảnh được. |

## Áp dụng khi tạo skill

- **Bước Planning (Step 2):** Nếu skill liên quan "trích xuất từ ảnh", "image to text", "đọc nội dung ảnh":
  1. Ưu tiên **không** thêm script OCR.
  2. Thiết kế skill: input = path ảnh (hoặc danh sách path), instruction = agent đọc ảnh (tool Read/file) và trích xuất theo format (text, bảng, ocr_full_table-like, v.v.).
  3. Chỉ thêm script OCR khi có lý do rõ: batch không tương tác, cần bbox, hoặc môi trường không có vision.
- **Trong SKILL.md:** Nếu có bước "extract from image", ghi rõ: dùng **path ảnh + đọc ảnh bằng tool (agent vision)**, không mặc định gọi script OCR.

## Tóm tắt

- **Agent + path ảnh** = đủ và thường tốt hơn cho trích xuất có ngữ nghĩa (PRD, wireframe, form, UI).
- **OCR script** = dùng khi batch/headless, bbox, hoặc tích hợp tool không có vision.
- Khi tạo skill mới: ưu tiên "agent kết hợp với path img" trước; chỉ thêm OCR script khi có yêu cầu cụ thể không thỏa mãn bằng agent.
