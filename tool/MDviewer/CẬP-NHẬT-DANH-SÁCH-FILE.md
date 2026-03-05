# Cập nhật danh sách file

## Khi chạy qua serve-markdown.py (localhost)

**Không cần làm gì.** Server dùng GET /api/files — danh sách luôn theo filesystem. Thêm/sửa/xóa .md → refresh trang.

## Khi dùng files.json (static / GitHub Pages)

Chạy:

```bash
python3 generate-manifest.py
```

Hoặc dùng watcher: `python3 watch-manifest.py` (cần `pip install watchdog`).

Hoặc pre-commit hook: `./install-manifest-hook.sh` — mỗi commit tự cập nhật files.json.
