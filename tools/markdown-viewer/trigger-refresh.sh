#!/usr/bin/env sh
# Gọi webhook POST /api/refresh để client (poll /api/revision) sync danh sách theo MarkdownSV.
# Dùng sau khi thêm/xóa/sửa file trong MarkdownSV (vd. từ git hook, file watcher, cron).
BASE="${MARKDOWN_VIEWER_URL:-http://localhost:9999}"
curl -s -X POST "${BASE}/api/refresh"
