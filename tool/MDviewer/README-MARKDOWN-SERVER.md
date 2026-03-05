# Markdown Viewer Server

Local server cho markdown viewer SPA. Chạy từ thư mục `viewer/`.

## Quick Start

```bash
cd viewer
python3 serve-markdown.py
```

Mở: **http://localhost:9999**

## Tính năng

- **SPA** — index.html với folder view, search, theme light/dark
- **Live file list** — GET /api/files quét filesystem mỗi request, không cần manifest hay commit
- **Thêm file .md mới** → refresh trang là thấy
- Không dependency bên ngoài (Python stdlib)

## Port

Mặc định: 9999. Sửa biến `PORT` trong `serve-markdown.py` nếu cần.
