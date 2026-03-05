# Nguyên nhân: View MD từ homepage thiếu nội dung so với kéo thả

## Triệu chứng

- **Kéo thả** file .md vào viewer → hiển thị **đủ** nội dung (ví dụ mục 8 có 13 dòng).
- **Truy cập từ homepage local** (click file trong danh sách) → cùng file đó lại chỉ thấy **một phần** (ví dụ mục 8 chỉ 3 dòng).

## Nguyên nhân đã xác định

### 1. Cache trình duyệt (chính)

- Khi mở file từ homepage, trang dùng **fetch(URL)** (HTTP) để tải nội dung .md.
- Trình duyệt **cache** response theo URL. Nếu trước đó bạn đã mở bản overview cũ (chỉ 3 dòng), lần sau click lại từ homepage sẽ nhận **bản cache** thay vì file mới trên disk.
- Khi **kéo thả**, viewer đọc file bằng **FileReader** trực tiếp từ ổ đĩa → không qua HTTP → **không dùng cache** → luôn thấy nội dung mới nhất.

### 2. Khác nguồn danh sách file (khi dùng index.html ở root)

- **Viewer** (chạy `viewer/serve-markdown.py`, port 9999): danh sách lấy từ **GET /api/files** → chỉ quét **MarkdownSV** → có đủ file `co-op-bank-khcn`.
- **Root** (chạy `python -m http.server` ở thư mục gốc, port 8000): danh sách lấy từ **files.json** tĩnh. File `files.json` ở root **không** chứa thư mục **MarkdownSV** (được generate từ toàn bộ project, có thể không gồm MarkdownSV). → Trên homepage root **không thấy** Co-op Bank trong list; nếu bạn click vào file overview khác (ví dụ XPOS) thì sẽ thấy nội dung khác (ví dụ chỉ 3 dòng ở mục tương ứng).

## Cách xử lý

1. **Dùng viewer khi xem MarkdownSV**  
   Chạy: `cd viewer && python serve-markdown.py` → mở http://localhost:9999. Danh sách từ /api/files, đủ file Co-op Bank.

2. **Tránh cache cũ khi mở từ homepage**  
   - Hard refresh: `Ctrl+Shift+R` / `Cmd+Shift+R` khi đang xem file đó.  
   - Hoặc DevTools → Network → bật "Disable cache" rồi tải lại.

3. **Server viewer đã thêm Cache-Control cho file .md**  
   File .md khi tải qua viewer được gửi kèm `Cache-Control: no-cache` để trình duyệt không dùng bản cache cũ, giúp "truy cập từ homepage" luôn thấy nội dung mới nhất.
