# Tư duy đơn giản hóa với agent (Agentic)

> Tài liệu kết xuất từ [image-extraction-preference.md](image-extraction-preference.md) và triết lý skill-creator — dạng **rules + decision flow** cho agent và người thiết kế skill.  
> **Cách làm việc + case studies khác:** [cach-lam-viec-simplify-agent.md](cach-lam-viec-simplify-agent.md) — nguyên tắc chung và nhiều case (ảnh, folder PRD, Figma, schema, review UX) để áp dụng hoặc thêm case mới.

---

## 1. Nguyên tắc một dòng

**Cho agent input trực tiếp (path, data, context) và để agent dùng capability sẵn có; không mặc định bảo agent đi xây tool/script khi việc đó có thể thay bằng "agent + input".**

Ví dụ: thay vì "xây tool OCR" → cho agent **path ảnh** + instruction trích xuất; agent dùng Read(path) + vision.

---

## 2. Agent rules (khi nhận request)

### 2.1 Rule tổng quát

| Khi user nói / muốn | Agent làm | Agent không làm (trừ khi có lý do rõ) |
|---------------------|-----------|--------------------------------------|
| "Trích xuất / đọc nội dung từ ảnh" | Nhận **path ảnh** (hoặc list path), đọc bằng tool Read/file, trích xuất theo format user yêu cầu (text, bảng, layout, UI elements). | Không đề xuất hoặc viết script OCR (Tesseract, batch) trừ khi: batch không tương tác, cần bbox, hoặc môi trường không có vision. |
| "Làm OCR" / "Image to text" | Coi như "đọc ảnh tại path và trả về nội dung" — dùng **agent + path ảnh**. | Không tạo skill/script riêng "chỉ để OCR". |
| "Phân tích wireframe / form / màn hình từ ảnh" | Đọc ảnh từ path, trích text + layout + thành phần (label, nút, icon) bằng vision. | Không thêm pipeline OCR script. |

### 2.2 Rule khi tạo / sửa skill

- **Planning (skill mới):** Nếu skill liên quan trích xuất từ ảnh → thiết kế **input = path ảnh** (hoặc danh sách path), **instruction = đọc ảnh (tool) + trích xuất theo format**. Chỉ thêm script OCR khi: batch không tương tác, cần bbox, hoặc không có vision.
- **SKILL.md:** Bước "extract from image" phải ghi rõ: **path ảnh + đọc bằng tool (agent vision)**, không mặc định gọi script OCR.

---

## 3. Decision flow (agentic)

```
User request liên quan "ảnh → nội dung" / "OCR" / "trích xuất từ ảnh"
    │
    ├─ Có path ảnh (hoặc user có thể cung cấp path)?
    │       │
    │       YES → Dùng agent vision: Read(path) + prompt trích xuất.
    │             Output: text / bảng / structured theo yêu cầu.
    │
    └─ Yêu cầu đặc biệt?
            │
            ├─ Batch CI/headless, không có agent trong vòng lặp? → OCR script/API.
            ├─ Cần bbox/coordinates từng ký tự? → OCR script hoặc Vision API có bbox.
            └─ Môi trường không có model vision? → OCR script (fallback).
```

---

## 4. Contract: Input / Output

**Mô hình "agent + path ảnh" (ưu tiên):**

- **Input:** path ảnh từ workspace (vd. `section/ui/screen.png`) hoặc list path; optional: format output (text, json, ocr_full_table-like).
- **Hành vi:** Agent gọi tool đọc file ảnh (Read với path), dùng vision để trích xuất nội dung theo instruction.
- **Output:** Nội dung có ngữ nghĩa (text, layout, labels, UI elements) — không chỉ raw OCR.

**Khi nào không dùng contract trên:** batch không tương tác, cần bbox, headless không vision. Khi đó dùng OCR script/API và ghi rõ trong skill.

---

## 5. Anti-pattern

- **Anti-pattern:** "Trích xuất từ ảnh" → nghĩ ngay "cần OCR" → thiết kế skill/script Tesseract, verify-env, pipeline gate.
- **Hệ quả:** Skill phình ra; nhiều use case chỉ cần "agent + path ảnh" đã đủ và tốt hơn (semantic, layout).
- **Cách sửa:** Ưu tiên **agent + path ảnh**; chỉ thêm script khi có điều kiện rõ (batch, bbox, no-vision).

---

## 6. Tham chiếu

- **Cách làm việc + case studies (ảnh, PRD, Figma, schema, review):** [cach-lam-viec-simplify-agent.md](cach-lam-viec-simplify-agent.md)
- Chi tiết case ảnh: [image-extraction-preference.md](image-extraction-preference.md)
- Skill-creator: `.agents/skills/skill-creator/SKILL.md` (Step 2 Planning, Step 4 Learn Proven Design Patterns)
- OCR execution (figma-to-prd-md): `.cursor/skills/figma-to-prd-md/phases/phase-2-inventory.md` § 2g — agent vision từ path, không Tesseract/script.
