# Scripts

## composite-mockup.py

Composite ảnh **content-only** (wireframe) vào **device frame** (khung iPhone) cho mockup hand-drawn. Dùng khi chạy img-to-mockup hoặc md-to-mockup với **reuse device frame** (DEVICE_FRAME_REUSE.md). Tọa độ vùng màn hình: x=83, y=138, w=634, h=1325 (canvas 800×1600, device 90%).

**Phụ thuộc:** `pip install Pillow`

**Một ảnh:**

```bash
python scripts/composite-mockup.py device-frame.png contact-content.png contact-mockup.png
```

**Batch (thư mục chứa *-content.png):**

```bash
python scripts/composite-mockup.py --batch device-frame.png mockups mockups
# Đọc mockups/*-content.png → ghi mockups/*-mockup.png
```

---

## save-figma-section-screenshots.js

Lưu **chỉ từng artboard con** với cấu trúc thư mục tự động từ Figma: `{file name}/{page}/{section}/*.png`. Tool tự lấy file name, page, section từ Figma API. Không chụp ảnh toàn section. Nếu nhiều artboard con trùng tên layer, script thêm hậu tố `-2`, `-3`, ... để không ghi đè.

```bash
node scripts/save-figma-section-screenshots.js <file_key> <node_id> [output_base_dir]
```

**Ví dụ:**

```bash
node scripts/save-figma-section-screenshots.js kPft93N2A3gYOC3YwuXpQR 5197:5929
# → co-op-bank-khcn/chuyen-tien/chuyen-tien-noi-bo-cung-chu/*.png (auto)

node scripts/save-figma-section-screenshots.js kPft93N2A3gYOC3YwuXpQR 5197:5929 ./output
# → output/co-op-bank-khcn/chuyen-tien/chuyen-tien-noi-bo-cung-chu/*.png
```

## Token

Dùng env **`FAT`** hoặc **`FIGMA_ACCESS_TOKEN`** (Personal Access Token từ Figma → Settings → Personal access tokens). Cần scope `file_content:read`.

Script **không** tự load `.env`. Khi chạy từ terminal (hoặc Agent chạy), **bắt buộc** load `.env` trước:

```bash
cd "<project_root>" && set -a && [ -f .env ] && . ./.env && set +a && node scripts/save-figma-section-screenshots.js <file_key> <node_id> [output_base_dir]
```

**Ví dụ đầy đủ:**

```bash
cd "/Users/dataism/Documents/UXreview" && set -a && [ -f .env ] && . ./.env && set +a && node scripts/save-figma-section-screenshots.js kPft93N2A3gYOC3YwuXpQR 5197:5929 ./co-op-bank-khcn
```

## MCP tool

Bật MCP server **figma-save** trong Cursor (`mcp.json`), set `FAT`. Agent gọi **`figma_save_section_screenshots`** (file_key, node_id [, output_base_dir]) — chỉ lưu từng artboard (không ảnh toàn section).

Skill Agent: `.cursor/skills/figma-save-screenshot/SKILL.md`.
