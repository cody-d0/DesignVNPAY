# Tính năng Markdown Viewer

## 🎨 Themes

Viewer hỗ trợ 4 theme:
1. **Light** — sáng, nền trắng
2. **Dark** — tối, nền xanh đậm
3. **Light Mesh** — sáng + gradient mesh background
4. **Dark Mesh** — tối + gradient mesh background

## 🔍 Search

- Gõ vào ô search để lọc file
- Debounce 200ms
- Tìm theo tên file, đường dẫn, folder
- Shortcut: nhấn `/` để focus search

## 📋 Paste-and-Go

Dán (Ctrl+V) đường dẫn file vào ô search:
- Tự nhận diện path (absolute hoặc relative)
- Gọi `POST /api/file` để lấy nội dung
- Mở trực tiếp file không cần navigate

## 🖱️ Drag & Drop

Kéo thả file vào viewer để xem:
- `.md`, `.markdown`, `.mdx`, `.mdc`, `.rst`, `.txt`
- `.json` — hiển thị tree view với expand/collapse
- `.yaml`, `.yml` — syntax highlight
- `.csv` — hiển thị dạng bảng
- `.svg` — preview trực tiếp

## 📂 Folder Tree

- Cây thư mục hiển thị file theo folder
- Click header để collapse/expand
- Trạng thái lưu vào localStorage
- Keyboard: Enter/Space để toggle

## ⏰ Auto Refresh

- Poll `/api/revision` mỗi 5 giây
- Poll `/api/files` mỗi 30 giây
- Webhook: `POST /api/refresh` → client sync ngay
- Visibility API: tạm dừng khi tab ẩn
