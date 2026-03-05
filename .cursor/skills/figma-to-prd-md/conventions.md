# Conventions — figma-to-prd-md

Shared conventions cho Image Path, Output Structure, và AI Badge.
Load file này khi thực hiện Phase 1, 3, 4, 5.

---

## Image Path Convention

- Ảnh nằm trong: `{section}/ui/{filename}.png` (path vật lý: `{output_dir}/{file_name}/{page}/{section}/ui/`).
- Link trong .md: **`ui/{filename}.png`** (relative từ file .md).
- `image_base_url` set: link absolute = `{image_base_url}/{output_dir}/{file_name}/{page}/{section}/ui/{filename}.png`.
- Viewer phải resolve relative path theo baseDir (thư mục chứa file .md) để ảnh hiển thị đúng.
- Verify: trước khi ghi .md, kiểm tra file .png tồn tại trong `{section}/ui/`; thiếu → warning trong Wireframe, không chặn output.

Mọi bước liên quan tới path ảnh (Phase 1d, Phase 3b Wireframe, Phase 5) tuân theo convention trên.

**Section 3 (Wireframe):** Thứ tự 7 block và điều kiện xuất — xem `phases/phase-3-generate.md` § Section 3: Wireframe.

---

## Output Structure

`output_structure = section_folder` (mặc định): mỗi section một folder, ảnh trong folder con `ui/`. Mỗi distinct screen = 1 file .md trong section. Path feature: `{output_dir}/{file_name}/{page}/{section}/{screen-slug}.md`.

Overview: `{output_dir}/{file_name}/{product-slug}-overview.md`. Link tới feature: `./{page}/{section}/{screen-slug}.md`.

**Ví dụ cây thư mục (một section, 3 màn):**

```
{output_dir}/{file_name}/
  {product-slug}-overview.md
  {page}/{section}/
    ui/
      internal-transaction.png
      internal-transaction-2.png
    chuyen-tien-noi-bo.md
    xac-nhan-giao-dich.md
    ket-qua-giao-dich.md
```

---

## AI Badge Convention ("🤖 by AI")

Mọi nội dung do AI suy luận, đề xuất, hoặc bổ sung (INFERRED, COMPextend, case study, UX improvement) **PHẢI** hiển thị bằng blockquote có badge. COMPbase (từ Figma) không có badge.

**Format:** `> **\`🤖 by AI\`** | Nguồn: {citation} | Độ tin cậy: {High/Medium/Low}` rồi dòng trống rồi nội dung.

| Mức | Khi nào dùng |
|-----|-------------|
| **High** | Figma evidence rõ + UX best practice (vd: INFERRED field, touch target) |
| **Medium** | Pattern chung + case study (vd: persona, missing error flow) |
| **Low** | Đề xuất sáng tạo, không evidence (vd: success metrics, competitor feature) |

**Ví dụ — Section 2 User Story (bảng 6 cột, AC dùng `<br>`):**

```markdown
> **`🤖 by AI`** | Nguồn: web-interface.csv#1 + ux-guidelines.csv#22 | Độ tin cậy: High
>
> | Epic chung | Mã US | Tiêu đề | Mô tả chi tiết | Business Rule | Acceptance Criteria |
> |---|---|---|---|---|---|
> | Accessibility | US-050 | Hỗ trợ screen reader | Là người dùng khiếm thị, tôi muốn sử dụng VoiceOver/TalkBack để điều hướng ứng dụng. | Mọi interactive element phải có aria-label. | - Mọi button có accessible name.<br>- Form fields có associated label.<br>- Error messages được announce. |
```

**Quy tắc:** (1) Không dùng `<!-- COMPextend -->`, chỉ blockquote badge. (2) COMPextend/INFERRED luôn trong badge. (3) Case study output luôn badge + citation. (4) COMPbase không badge. (5) Badge đặt ngay sau COMPbase liên quan. (6) Nội dung trong badge đúng format XPOS của section đó.

Ví dụ đầy đủ cho 5 section khác (Chân dung KH, User Flow, Database, NFR, Wireframe): đọc `reference/badge-examples.md`.

---

## DDL reference (Design Data Layer)

Khi cần tham chiếu DDL cho ocr_ux_improvements, augment, hoặc citation:

- **Scope GLOBAL:** `.agents/skills/ui-ux-pro-max/data/` — dùng `ux-guidelines.csv`, `web-interface.csv`, `ux-laws.csv`.
- **Format ddl_ref:** `ux-guidelines.csv#22`, `web-interface.csv#39` (số = row id hoặc đề mục).
- **Contract:** [.cursor/docs/ddl/contract.md](.cursor/docs/ddl/contract.md), [.cursor/docs/ddl/hierarchy.md](.cursor/docs/ddl/hierarchy.md).
