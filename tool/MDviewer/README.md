# Markdown Viewer (Local Host)

Thư mục riêng để host markdown viewer local. Chạy server từ đây để xem nội dung .md của project.

## Quick Start

```bash
cd viewer
python3 serve-markdown.py
```

Mở trình duyệt: **http://localhost:9999**

**Lưu ý:** Nếu port 9999 đang dùng (vd. server khác), dừng process đó hoặc sửa `PORT` trong `serve-markdown.py`.

## Tự động cập nhật danh sách file (không cần commit/manifest)

Khi chạy qua `serve-markdown.py`, viewer dùng **GET /api/files** — quét **chỉ** folder **MarkdownSV**.  
Tab **Cập nhật gần nhất** và **All** chỉ sync với MarkdownSV (không manifest folder root hay folder khác).  
**Kéo thả** file .md/.json: không giới hạn phạm vi — có thể thả file từ bất kỳ thư mục nào trên máy để xem trước.

Thêm **folder mới** hoặc thêm/sửa/xóa file .md trong MarkdownSV → **chỉ cần refresh trang** (hoặc đợi ~30s polling) — không cần chạy `generate-manifest.py` hay commit.

**Webhook sync:** Gọi `POST /api/refresh` khi MarkdownSV thay đổi → client (poll `/api/revision` mỗi 5s) sẽ tự load lại danh sách (sync/pruning folder không tồn tại). Ví dụ: `./trigger-refresh.sh` hoặc `curl -X POST http://localhost:9999/api/refresh`. Có thể gắn vào git hook, file watcher hoặc cron.

**File tĩnh** (co-op-bank, XPOS PRD, v.v.) được serve từ MarkdownSV — click vào file để xem nội dung.

**Wireframe / ASCII box-drawing:** Viewer tối ưu cho wireframe dạng text trong PRD (bảng, form vẽ bằng `|`, `-`, `+`): code block hiển thị monospace, không wrap, scroll ngang. Bọc nội dung trong \`\`\` … \`\`\` (tùy chọn \`\`\`ascii\`\`\` hoặc \`\`\`text\`\`\`). Xem [.cursor/docs/markdownsv-ascii-wireframe-display.md](../.cursor/docs/markdownsv-ascii-wireframe-display.md).

### Cách 2: File watcher (khi không dùng server)

Nếu mở `index.html` trực tiếp (file://) hoặc dùng server khác:

**Python:**
```bash
pip install watchdog
python3 watch-manifest.py
```

**Node:**
```bash
npm install
npm run watch
```

Watcher theo dõi thư mục **MarkdownSV**, khi có .md thay đổi → tự chạy `generate-manifest.py`. Không cần commit.

## Cấu trúc

```
viewer/
├── index.html            # SPA
├── files.json            # Manifest (tạo bởi generate-manifest.py)
├── generate-manifest.py  # Quét .md → files.json
├── serve-markdown.py     # Local server + /api/files, /api/revision, POST /api/refresh (webhook)
├── trigger-refresh.sh    # Gọi webhook để client sync (git hook / watcher / cron)
├── watch-manifest.py     # File watcher (optional)
├── content root: ../MarkdownSV  # Chỉ quét và serve từ MarkdownSV
├── deploy-github-pages.sh
├── githooks/pre-commit
├── install-manifest-hook.sh
└── README.md
```

## Deploy GitHub Pages

```bash
cd viewer
./deploy-github-pages.sh
```

Script copy `index.html`, `files.json`, và nội dung `content/` lên branch `gh-pages`.

## Cập nhật manifest thủ công

```bash
python3 generate-manifest.py
```

## Pre-commit hook (manifest tự động khi commit)

```bash
./install-manifest-hook.sh
```

Mỗi lần commit sẽ chạy `generate-manifest.py` và add `files.json` nếu có thay đổi.
