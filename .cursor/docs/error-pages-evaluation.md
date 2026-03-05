# Đánh giá trang lỗi (404, 500, …)

## Kết quả kiểm tra

### Trước khi sửa
- Ảnh bạn gửi cho thấy **trang lỗi mặc định của Python**: "Error response", "Error code: 404", "Message: File not found.", font serif, nền trắng, không CTA.
- Nguyên nhân: trong project có **hai server**:
  - **viewer/serve-markdown.py** — SPA (index.html, /api/files, port 9999) — đã có trang lỗi tùy chỉnh.
  - **serve-markdown.py** (thư mục gốc) — Markdown Viewer kiểu cũ (/view?file=…) — trước đây **chưa** có trang lỗi tùy chỉnh.
- Nếu chạy `python serve-markdown.py` từ **thư mục gốc**, mọi 404/500 đều trả về trang mặc định của Python → đúng với ảnh.

### Sau khi sửa
- **viewer/serve-markdown.py**: giữ nguyên — đã có sẵn trang lỗi HTML (Inter, card, nút "Về trang chủ").
- **serve-markdown.py** (gốc): đã bổ sung **cùng bộ** trang lỗi:
  - Override `send_error()` → trả HTML thay vì trang mặc định.
  - Các mã: 400, 403, 404, 405, 500, 502, 503 với tiêu đề + mô tả tiếng Việt.
  - Design: token giống viewer (Inter, --color-cta, card, nút CTA, accessibility).
- Sửa thêm: 500 hiển thị đúng chi tiết lỗi (trước đó dùng `f'Error: {{str(e)}}'` nên in ra literal `{str(e)}`).

## Tiêu chí (ui-ux-pro-max) — đạt

| Tiêu chí | Trạng thái |
|----------|------------|
| Phân biệt mã lỗi (404, 500, …) | ✅ Mỗi mã có tiêu đề + mô tả riêng |
| Thông báo thân thiện, tiếng Việt | ✅ Không còn "Error response" / "Nothing matches the given URI" |
| CTA rõ ràng | ✅ Nút "Về trang chủ" (link /) |
| Đồng bộ design viewer | ✅ Inter, màu CTA, card, spacing |
| Accessibility | ✅ role="main", aria-labelledby, focus ring nút |
| Chi tiết kỹ thuật khi 5xx | ✅ Chỉ với 500+, trong block "Chi tiết:" |

## Cách kiểm tra

### Chạy đúng server (có trang lỗi tùy chỉnh)

**Bắt buộc chạy từ thư mục `viewer`** (server SPA dùng MarkdownHandler với send_error override):

```bash
cd "/Users/dataism/Documents/UXreview/viewer"
python3 serve-markdown.py
```

Khi chạy đúng, terminal sẽ có dòng:
`Trang lỗi 404/500: dùng giao diện tùy chỉnh (card, nút "Về trang chủ")`

**Nếu chạy** `python3 serve-markdown.py` **từ thư mục gốc** (UXreview/): đó là server *khác* (Markdown Viewer cũ, /view?file=…). Server gốc đã được bổ sung cùng bộ trang lỗi — nếu vẫn thấy "Error response" thì cần **tắt process cũ** (đang giữ port 9999) rồi chạy lại.

### Xác nhận đang xem trang lỗi tùy chỉnh

1. Mở URL không tồn tại: http://localhost:9999/package-2/chuyen-tien-noi-bo-khac-chu/xyz  
2. **Trang đúng**: card trắng, chữ "404", "Not Found", đoạn "Không tìm thấy trang hoặc tệp...", nút **Về trang chủ**.  
3. **Trang sai** (mặc định Python): chữ "Error response", "Error code: 404", "Message: File not found."  
4. **View Source** (Cmd+U / Ctrl+U): tìm `<!-- Markdown Viewer custom error page` hoặc "Về trang chủ" — nếu có là trang tùy chỉnh.

### Nếu vẫn thấy "Error response"

1. **Dừng mọi process trên port 9999**  
   ```bash
   lsof -i :9999
   kill <PID>
   ```
2. Chạy lại từ **viewer**: `cd viewer && python3 serve-markdown.py`  
3. Thử lại http://localhost:9999/duong-dan-bat-ky

## Tóm tắt

- **Đánh giá**: Logic trang lỗi trong `viewer/serve-markdown.py` đúng; ảnh "Error response" là do đang chạy server **ở thư mục gốc** chưa có trang lỗi tùy chỉnh.
- **Đã xử lý**: Thêm cùng bộ trang lỗi vào `serve-markdown.py` (gốc) và sửa hiển thị chi tiết lỗi 500. Cả hai cách chạy server đều trả về trang lỗi đẹp, thống nhất.
