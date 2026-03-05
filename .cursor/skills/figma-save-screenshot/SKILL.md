---
name: figma-save-screenshot
description: "Tool cho Agent: lưu ảnh từ Figma xuống local — chỉ lưu từng artboard (frame con), không chụp ảnh toàn section. Hỗ trợ link section hoặc page."
---

# Figma Save Screenshot — Tool cho Agent

**Tool dùng khi lưu ảnh từ Figma:** **`figma_save_section_screenshots`**. Cho kết quả: **chỉ từng artboard con** (không có ảnh toàn section), tự tạo cấu trúc thư mục theo Figma (file name → page → section). Dùng **Figma REST API** (GET /v1/images).

Hỗ trợ **hai loại node_id**:
- **Section/frame node** → 1 folder, chỉ các artboard con (từng frame). Nếu section không có con thì lưu ảnh chính node đó.
- **Page node** → N folders (1 per section), mỗi folder chỉ chứa các artboard của section đó.

## Khi nào dùng

- **Lưu ảnh từ Figma về local:** gọi **`figma_save_section_screenshots`** (file_key, node_id [, output_base_dir]). Kết quả: thư mục `{file name}/{page}/{section}/` chứa **chỉ từng artboard** (không có file ảnh toàn section).
- **Link page (nhiều section):** gọi 1 lần với page node_id → tool tự lặp qua từng section, tạo một folder per section.
- Skill **figma-to-prd-md** Phase 1d: dùng `figma_save_section_screenshots` cho mỗi section/screen để có ảnh từng artboard trong thư mục section.
- Bất kỳ task "export Figma frame/section as PNG" hoặc "lưu screenshot Figma".

## Contract (Tool)

**Tool chính — dùng duy nhất:**

| Tool | Mô tả |
|------|--------|
| **`figma_save_section_screenshots`** | Nhận link Figma section **hoặc page** (node_id): tự tạo `{file name}/{page}/{section}/`, lưu **chỉ từng artboard con** (không chụp ảnh toàn section). Khi node_id là page, tự lặp qua tất cả section. Node không có children vẫn lưu được ảnh node đó. |

### figma_save_section_screenshots

| Tham số | Bắt buộc | Mô tả |
|---------|----------|--------|
| `file_key` | Có | File key từ Figma URL. |
| `node_id` | Có | Section node ID **hoặc Page node ID**. Tool tự detect loại node. |
| `output_base_dir` | Không | Thư mục gốc (default: cwd). Tool tự tạo `{file_name}/{page}/{section}/` bên trong. |

**Cấu trúc thư mục — Section mode (node_id là section):**

```
{output_base_dir} / {Figma file name} / {Figma page name} / {Figma section name} /
    {artboard-1-slug}.png      (từng frame/artboard con)
    {artboard-2-slug}.png
    ...
```

(Không có file `{section-slug}.png` — đã bỏ bước chụp toàn section.)

**Cấu trúc thư mục — Page mode (node_id là page):**

```
{output_base_dir} / {Figma file name} / {Figma page name} /
    {section-1-slug} /
        {artboard-1-slug}.png
        ...
    {section-2-slug} /
        {artboard-1-slug}.png
        ...
    ...
```

**Ví dụ — Section mode:** File "Co-op Bank KHCN", page "Package 2", section "Chuyển tiền nội bộ cùng chủ":

```
co-op-bank-khcn/
  package-2/
    chuyen-tien-noi-bo-cung-chu/
      internal-transaction.png
      internal-transaction-2.png
      ...
```

**Ví dụ — Page mode:** File "Co-op Bank KHCN", page "Package 2" (có 3 section):

```
co-op-bank-khcn/
  package-2/
    danh-ba-thu-huong/
      contact.png
      ...
    chuyen-tien-noi-bo-khac-chu/
      internal-transaction.png
      internal-transaction-2.png
      ...
```

**Nhiều section cùng file:** Mỗi section = một thư mục riêng dưới cùng `{file_name}/{page}/`. Không ghi đè nhau.

**Artboards trùng tên:** Tool tự thêm hậu tố `-2`, `-3`, ... để mỗi file PNG là duy nhất.

**Quy tắc cho Agent:**

- Luôn dùng **`figma_save_section_screenshots`** khi lưu ảnh từ Figma — mỗi lần chạy chỉ ra **từng artboard** (không có ảnh toàn section).
- Khi user cung cấp **link page** (node-id của page): gọi **một lần** với page node_id — tool tự xử lý tất cả sections.
- Khi user cung cấp **link section**: gọi với section node_id như bình thường.
- Node không có children (frame đơn) vẫn dùng được: tool lưu ảnh node đó.

## Token

Dùng biến môi trường **`FAT`** hoặc **`FIGMA_ACCESS_TOKEN`** (Personal Access Token từ Figma: Settings → Personal access tokens). Scope cần: `file_content:read`. Tool đọc theo thứ tự: `FAT` → `FIGMA_ACCESS_TOKEN`.

## Ưu tiên gọi

Khi MCP server **figma-save** đã bật trong Cursor (đăng ký trong `mcp.json`), Agent **ưu tiên** gọi MCP tool. Fallback: chạy lệnh terminal (xem mục dưới).

## Chạy script từ terminal (fallback)

Script Node **không** tự load `.env`. Agent chạy `node scripts/...` mà không load `.env` trước thì thiếu token và script sẽ fail.

**Quy tắc bắt buộc khi chạy script bằng terminal:**

1. `cd` về thư mục gốc project (workspace root).
2. Load `.env`: `set -a && [ -f .env ] && . ./.env && set +a`
3. Chạy script: `node scripts/...`

**Fallback (khi không dùng MCP):**

```bash
cd "<project_root>" && set -a && [ -f .env ] && . ./.env && set +a && node scripts/save-figma-section-screenshots.js <file_key> <node_id> [output_base_dir]
```

Token nằm trong `.env` dưới tên `FAT` hoặc `FIGMA_ACCESS_TOKEN`. Nếu thiếu token sau khi load `.env` → script báo lỗi rõ, Agent không chạy tiếp.

**Output khi thành công:** in ra đường dẫn file đã lưu (stdout). Exit code 0.

**Output khi lỗi:** in thông báo lỗi ra stderr, exit code 1.

## Điều kiện

- **FAT** hoặc **FIGMA_ACCESS_TOKEN** phải có trong `.env` hoặc env shell.
- Script: `scripts/save-figma-section-screenshots.js`.
- Node.js có sẵn (không cần cài thêm package).

## Tích hợp với figma-to-prd-md

Trong **Phase 1d** (Get screenshots), Agent dùng **`figma_save_section_screenshots`**:

- Với mỗi section hoặc screen (node_id section/top-level frame): gọi `figma_save_section_screenshots(file_key, node_id, output_base_dir)`.
- Kết quả: thư mục `{output_base_dir}/{file_name}/{page}/{section}/` chứa **chỉ từng artboard** (không có ảnh toàn section).

## Tối ưu (v2.0)

- **Parallel:** getNodeName + getImageUrl chạy song song; download children song song (limit 5).
- **Timeout:** API 30s, download 60s.
- **Retry:** 1 lần retry cho lỗi 5xx/mạng, delay 2s.
- **Error:** Parse Figma error body (403/404/429/5xx) trả message rõ ràng.

---
*Generated by VNPAY Agentic Framework*
