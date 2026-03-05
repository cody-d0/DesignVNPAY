# Nội dung ASCII / box-drawing trong Markdown và hiển thị tối ưu (markdownSV)

## Nội dung dạng này là gì?

Đây là **wireframe / mockup low-fi dạng text** (ASCII art, box-drawing), thường dùng trong PRD, spec, hoặc tài liệu kỹ thuật để mô tả giao diện bằng ký tự thuần văn bản.

- **Ký tự dùng:** `|`, `-`, `+`, `[`, `]`, khoảng trắng, đôi khi `●` (trạng thái).
- **Mục đích:** Mô tả bảng (table), form, nút bấm, layout màn hình mà không cần công cụ vẽ — dễ version control, dễ đọc trong repo.
- **Ví dụ:** SCR-BO-006 (DS User BO), SCR-BO-007 (Form Thêm/Sửa User) với bảng cột Email, Tên, PB, Quyền, TT và form có ô nhập, dropdown, nút LƯU/HỦY.

## Cách hiển thị / viewer tối ưu

Để layout không vỡ và dễ đọc:

1. **Font monospace (fixed-width)** — Bắt buộc. Font proportional sẽ làm lệch cột và “hộp” vẽ bằng ký tự.
2. **Giữ nguyên khoảng trắng và xuống dòng** — Nội dung phải nằm trong **code block** (fenced với ```) để render thành `<pre><code>...</code></pre>; không wrap dòng (white-space: pre).
3. **Scroll ngang khi dòng dài** — Không ép wrap; cho phép scroll ngang để giữ đúng căn chỉnh.
4. **Đủ tương phản** — Nền và chữ rõ (theme sáng/tối của viewer đã hỗ trợ).

## markdownSV đã hỗ trợ

Viewer (viewer/index.html) được chỉnh để hiển thị tối ưu nội dung dạng này:

- **`.markdown-body pre`:** font monospace, `white-space: pre`, `overflow-x: auto`, scroll ngang khi cần.
- **`.markdown-body pre code`:** kế thừa font, `white-space: pre`, không wrap.
- **Code block với ngôn ngữ `ascii` hoặc `text`:** dùng thêm class (ví dụ `language-ascii`, `language-text`) để có thể tùy chỉnh riêng (font-size, letter-spacing) nếu cần.

**Cách dùng trong .md:** bọc wireframe trong fenced code block. Có thể gắn ngôn ngữ `ascii` hoặc `text` để rõ ý:

````markdown
```ascii
+----------------------------------+
| SCR-BO-006 — DS User BO          |
| Email    | Tên     | PB   | TT   |
|----------+--------+------+------|
| a@x.com  | Admin  | Tech |  ●   |
+----------------------------------+
[+ Thêm User]
```
````

Không bắt buộc phải dùng `ascii`/`text`; mọi code block đều được render với font monospace và không wrap, phù hợp cho box-drawing.

## Tóm tắt

- **Nội dung:** Wireframe/mockup UI bằng ký tự (ASCII/box-drawing) trong PRD/spec.
- **Viewer tối ưu:** Monospace, preformatted (pre), không wrap, scroll ngang.
- **markdownSV:** Đã cấu hình sẵn trong viewer; chỉ cần đặt nội dung trong code block (``` … ```) trong file .md.
