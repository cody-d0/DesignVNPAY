# Cách làm việc: Tư duy đơn giản hóa với agent (Case studies)

> **Mục đích:** Một cách làm việc (tư duy) có thể tái sử dụng: ưu tiên **cho agent input trực tiếp** và **capability sẵn có** thay vì bảo agent đi xây tool/script. Tài liệu gồm nguyên tắc chung + nhiều case study để áp dụng hoặc mở rộng.

---

## 1. Nguyên tắc chung

**Một dòng:**  
Cho agent **input trực tiếp** (path, URL, id, data) và để agent dùng **capability sẵn có** (Read, vision, MCP, v.v.); **không mặc định** bảo agent xây tool/script khi việc đó có thể thay bằng "agent + input".

**Công thức:**

| Thay vì… | Làm… |
|----------|------|
| "Xây tool / script để làm X" | Cho agent **input cần thiết** + instruction; agent dùng tool/capability đã có để làm X. |
| Nghĩ "bài toán X = cần công nghệ Y" | Hỏi: "Agent đã có thể làm X với input gì chưa?" → Nếu có → dùng; nếu không hoặc có ràng buộc đặc biệt → mới xem xét script/tool. |

**Khi nào vẫn cần script/tool:**  
Batch không tương tác (CI, headless), cần output máy móc (exit code, format cố định), cần capability agent không có (bbox, realtime API), hoặc môi trường không có agent trong vòng lặp.

---

## 2. Case studies

### Case 1: Trích xuất từ ảnh (Image / OCR)

| Khía cạnh | Nội dung |
|-----------|----------|
| **Khuynh hướng** | "Trích xuất từ ảnh" → nghĩ "cần OCR" → xây script Tesseract, pipeline, verify-env. |
| **Cách làm việc** | Cho agent **path ảnh** (hoặc list path). Agent dùng **Read(path)** + **vision** để trích text, layout, UI elements. |
| **Input** | Path từ workspace (vd. `section/ui/screen.png`) hoặc danh sách path. |
| **Capability dùng** | Tool đọc file ảnh + model vision (semantic, không chỉ raw OCR). |
| **Khi nào vẫn dùng script** | Batch CI/headless, cần bbox từng ký tự, môi trường không có vision. |
| **Tham chiếu** | [image-extraction-preference.md](image-extraction-preference.md), [agentic-simplify-thinking.md](agentic-simplify-thinking.md) § 2–3. |

---

### Case 2: Phân tích folder PRD / nhiều file .md

| Khía cạnh | Nội dung |
|-----------|----------|
| **Khuynh hướng** | "Phân tích toàn bộ folder PRD" → viết script crawl thư mục, parse .md, build AST, rồi mới cho agent. |
| **Cách làm việc** | Cho agent **path folder** (`prd_folder`) + (tùy chọn) `include_files[]`, `exclude_files[]`, `overview_file`. Agent **đọc từng file** bằng **Read(path)** theo thứ tự skill/pipeline quy định; không cần script crawl/parse riêng. |
| **Input** | `prd_folder`, optional: overview path, include/exclude list. |
| **Capability dùng** | Read(file_path), list_dir nếu cần; skill/pipeline định nghĩa thứ tự và format output. |
| **Khi nào vẫn dùng script** | CI chạy trên N file không có agent trong vòng lặp; cần index/artifact cố định (vd. manifest) được build trước. |
| **Tham chiếu** | `.cursor/agents/prd-full-pipeline.md` (Input Contract), `.cursor/docs/call-on-demand-intent-router.md` (PRD path). |

---

### Case 3: Đọc thiết kế từ Figma

| Khía cạnh | Nội dung |
|-----------|----------|
| **Khuynh hướng** | "Lấy nội dung từ Figma" → viết script gọi REST API, export asset, parse JSON file, tự maintain token. |
| **Cách làm việc** | Cho agent **Figma URL** (hoặc fileKey + nodeId). Agent dùng **MCP** (vd. `get_design_context`) để đọc design context, variables, components, screenshot. Không cần script export/parse riêng cho đọc. |
| **Input** | Figma URL (design/board/make) hoặc fileKey + nodeId. |
| **Capability dùng** | Figma MCP (read): get_design_context, get_screenshot, get_metadata. |
| **Khi nào vẫn dùng script** | Batch export N frame ra file (vd. figma-save-screenshot); CI không có agent; cần format export cố định (SVG, PDF). |
| **Tham chiếu** | `.cursor/docs/agent-figma-plugin-interaction.md` (Read = MCP), skill figma-to-prd-md, figma-implement-design. |

---

### Case 4: Tham chiếu schema / API / tài liệu

| Khía cạnh | Nội dung |
|-----------|----------|
| **Khuynh hướng** | "Query BigQuery / dùng API" → mỗi lần bảo agent "re-discover" schema hoặc viết connector gọi API thay agent. |
| **Cách làm việc** | Lưu **references/schema.md** (hoặc API doc, DDL) trong skill/project. Cho agent **path file** (hoặc context đã load). Agent **đọc khi cần** và trả lời query; không cần script "kết nối DB" hay re-discover mỗi lần. |
| **Input** | Path tới file tham chiếu (schema, API spec, token map) hoặc chunk đã được load vào context. |
| **Capability dùng** | Read(path), hoặc references đã có trong skill. |
| **Khi nào vẫn dùng script** | Thực thi query/API thật (run query, gửi request) cần deterministic, credential, audit; agent chỉ đọc doc và sinh query/code. |
| **Tham chiếu** | Skill-creator Step 2 (BigQuery example: `references/schema.md`); design-data-layer, temp1.json. |

---

### Case 5: Review UX / PRD từ artifact có sẵn

| Khía cạnh | Nội dung |
|-----------|----------|
| **Khuynh hướng** | "Review UX" → build tool thu thập ảnh, parse PRD, gọi API review riêng. |
| **Cách làm việc** | Cho agent **path folder** (PRD .md + ảnh trong `ui/`) hoặc **path file** (feature .md, screen_inventory). Agent **đọc file + ảnh** (Read + vision), đối chiếu DDL/guidelines và sinh báo cáo review. Có thể kết hợp MCP Figma nếu user cho URL. |
| **Input** | Path folder PRD, hoặc path file .md + path ảnh; optional: Figma URL. |
| **Capability dùng** | Read(.md, .png), vision, MCP Figma (nếu có URL), DDL/ux-guidelines trong references. |
| **Khi nào vẫn dùng script** | Batch review N repo không tương tác; cần report format cố định (JSON/HTML) do tool khác consume. |
| **Tham chiếu** | review-ux, ux-review-pipe, figma-to-prd-md Phase 2g-bis (OCR reconciliation). |

---

## 3. Checklist trước khi bảo agent "xây tool"

- [ ] **Đã cho agent đủ input chưa?** (path, URL, id, list file)
- [ ] **Agent đã có tool/capability đọc input đó chưa?** (Read, MCP, vision)
- [ ] **Ràng buộc có bắt buộc script không?** (batch không tương tác, exit code, bbox, no-vision, v.v.)
- Nếu cả ba: đủ input + có capability + không bắt buộc script → **ưu tiên "agent + input"**, không thiết kế script trước.

---

## 4. Decision flow tổng quát

```
User muốn "lấy / phân tích / chuyển đổi" từ nguồn X
    │
    ├─ Có thể cho agent "định danh" X (path / URL / id)?
    │       │
    │       YES → Agent đã có tool đọc X (Read / MCP / vision)?
    │               │
    │               YES → Dùng agent + input. Định nghĩa output format (text, JSON, bảng).
    │               NO  → Cân nhắc script/tool chỉ khi không thể thêm capability.
    │
    └─ Ràng buộc đặc biệt? (batch CI, headless, bbox, no-vision, format máy móc)
            │
            YES → Script / API / pipeline phù hợp; ghi rõ trong skill khi nào dùng.
```

---

## 5. Thêm case study mới (template)

Điền vào bảng sau và thêm vào § 2:

| Khía cạnh | Nội dung |
|-----------|----------|
| **Khuynh hướng** | User/team thường nghĩ gì → dẫn đến "xây tool"? |
| **Cách làm việc** | Cho agent **input gì**; agent dùng **capability gì** (tool/có sẵn). |
| **Input** | Path / URL / id / list? |
| **Capability dùng** | Read, MCP, vision, …? |
| **Khi nào vẫn dùng script** | Batch, headless, format cố định, capability thiếu? |
| **Tham chiếu** | File/skill liên quan. |

---

## 6. Liên kết với tài liệu khác

- **Rules + decision flow (agentic):** [agentic-simplify-thinking.md](agentic-simplify-thinking.md)
- **Case ảnh chi tiết:** [image-extraction-preference.md](image-extraction-preference.md)
- **Skill-creator:** `.agents/skills/skill-creator/SKILL.md` (Learn Proven Design Patterns)
- **Intent router:** `.cursor/docs/call-on-demand-intent-router.md`
- **Figma ↔ Agent:** `.cursor/docs/agent-figma-plugin-interaction.md`
