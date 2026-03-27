# Format Registry — Các mẫu template đã xử lý

> **Self-learning document.** Mỗi khi converter gặp format mới,
> agent reason → adapt → append template mới vào cuối file này.

---

## Cách dùng

`convert.py` đọc file này runtime tại:
```
references/format-registry.md
```

Mỗi template entry chứa:
1. **ID** — `FMT-NNN`
2. **Modules áp dụng** — danh sách modules dùng format này
3. **Pattern** — regex hoặc structural description
4. **Extraction logic** — cách extract data từ format này
5. **Ngày phát hiện** — timestamp

---

## Registry

### FMT-001 · H1 Title-Dash

**Modules:** 17/28 (Chuyển tiền NB khác chủ, chuyen-tien-noi-bo-cung-chu, ...)

```
Pattern:  # UX Review Report — {Module Name}
Regex:    ^#\s+UX\s+Review\s+Report\s+—\s+(.+)$
Extract:  group(1) → module_name
```

---

### FMT-002 · H1 Title-Dash-Dot

**Modules:** 8/28 (Huỷ Voice OTT, Thanh toán dư nợ thẻ, ...)

```
Pattern:  # UX Audit — {Module} · {Product}
Regex:    ^#\s+UX\s+Audit\s+—\s+(.+?)\s+·\s+(.+)$
Extract:  group(1) → module_name, group(2) → product_name
```

---

### FMT-003 · H1 Title-Dash-Pipe

**Modules:** 3/28 (Chỉnh sửa Voice, ...)

```
Pattern:  # UX Review Report — {Module} | {Product}
Regex:    ^#\s+UX\s+Review\s+Report\s+—\s+(.+?)\s+\|\s+(.+)$
Extract:  group(1) → module_name, group(2) → product_name
```

---

### FMT-010 · Metadata Bold-Inline (EN keys)

**Modules:** 23/28

```
Pattern:  **Product:** Co-opBank Mobile Banking
          **Section:** Đăng ký Voice
          **Generated:** 2026-03-23
Regex:    ^\*\*(\w[\w\s]*?):\*\*\s*(.+)$
Extract:  group(1).lower() → key via META_ALIASES, group(2) → value
```

---

### FMT-011 · Metadata Blockquote (EN keys)

**Modules:** 5/28 (Đăng ký Voice, ...)

```
Pattern:  > **Section:** Đăng ký Voice
          > **Figma:** `aYeSAVi94QlI4i4rL3xtmR` · node `194:195716`
Regex:    ^>\s*\*\*(\w[\w\s]*?):\*\*\s*(.+)$
Extract:  Same as FMT-010, strip `> ` prefix first
```

---

### FMT-012 · Metadata Bold-Inline (VN keys)

**Modules:** 5/28 (Huỷ Voice OTT, ...)

```
Pattern:  **Sản phẩm:** Co-opBank Mobile Banking
          **Ngày audit:** 2026-03-23
Regex:    Same as FMT-010
Extract:  key.lower() → META_ALIASES_VN → canonical key
```

**VN key alias map:**
```python
META_ALIASES_VN = {
    "sản phẩm": "product_name",
    "module": "module_name",
    "ngày audit": "generated_at",
    "tổng check": "check_count",
    "tổng màn hình": "screen_count",
}
```

---

### FMT-020 · Check Table Header — Category+Severity

**Modules:** Đăng ký Voice, một số modules khác

```
Pattern:  | # | Check | Category | Severity | Verdict | Evidence |
Columns:  [0]=num [1]=check [2]=category [3]=severity [4]=verdict [5]=evidence
```

---

### FMT-021 · Check Table Header — Category+DDL

**Modules:** ~15 modules

```
Pattern:  | # | Check | Category | DDL Ref | Verdict | Evidence |
Columns:  [0]=num [1]=check [2]=category [3]=ddl_ref [4]=verdict [5]=evidence
```

---

### FMT-022 · Check Table Header — Source+DDL

**Modules:** Chỉnh sửa Voice, Huỷ Voice OTT, ~5 modules

```
Pattern:  | # | Check | Source | DDL Ref | Verdict | Evidence |
Columns:  [0]=num [1]=check [2]=source [3]=ddl_ref [4]=verdict [5]=evidence
Mapping:  source → category via CATEGORY_MAP
```

---

### FMT-030 · Screen Heading — Inline SCR-ID

**Modules:** 7/28

```
Pattern:  ### 1. Screen Name (`SCR-XXX-001`)
Regex:    ^###\s+\d+\.\s+(.+?)\s*\(`?(SCR-\w+-\d+)`?\)
Extract:  group(1) → screen_name, group(2) → screen_id
```

---

### FMT-031 · Screen Heading — Fallback SCR-ID

**Modules:** 21/28 (75% — đây là format phổ biến nhất!)

```
Pattern:  ### 1. Screen Name
          > `SCR-XXX-001` · form · 2 artboards
Regex heading:  ^###\s+\d+\.\s+(.+)$
Regex meta:     ^>\s*`(SCR-\w+-\d+)`\s*·\s*(\w+)\s*·\s*(\d+)\s*artboard
Extract:  heading → screen_name, meta → screen_id + screen_type + artboard_count
```

---

### FMT-040 · UXP Block — With Emoji

**Modules:** 3/28

```
Pattern:  #### UXP-001 · 🔴 Critical
Regex:    ^####\s+(UXP-\d+)\s*·\s*(?:🔴|🟡|⚪)\s*(Critical|Major|Minor)
Extract:  group(1) → uxp_id, group(2) → severity
```

---

### FMT-041 · UXP Block — Without Emoji

**Modules:** 25/28

```
Pattern:  #### UXP-001 · Critical
Regex:    ^####\s+(UXP-\d+)\s*·\s*(Critical|Major|Minor)
Extract:  group(1) → uxp_id, group(2) → severity
```

---

### FMT-050 · UXP Fields — Key-Value Table

**Modules:** 28/28 (consistent!)

```
Pattern:  | **Màn hình** | Screen Name (SCR-ID) |
          | **Vấn đề** | Problem description |
          | **Gap ref** | Check #1, #2 |
          | **DDL** | COMP:xxx |
          | **Giải pháp** | Solution text |
Regex:    ^\|\s*\*\*(.+?)\*\*\s*\|\s*(.+?)\s*\|
Required keys: Màn hình, Vấn đề, Gap ref, DDL, Giải pháp
```

---

### FMT-060 · Evidence Image Reference — "Từ ảnh"

**Modules:** 16/28

```
Pattern:  Từ ảnh account-3.png: Toggle ON có màu xanh...
Regex:    Từ ảnh\s+([a-zA-Z0-9_-]+(?:\.png)?)
Extract:  group(1) → image_filename
```

---

### FMT-061 · Evidence Image Reference — "From image"

**Modules:** 1/28

```
Pattern:  From image tra-soat-5.png: ...
Regex:    From image[: ]+([a-zA-Z0-9_-]+(?:\.png)?)
Extract:  group(1) → image_filename
```

---

### FMT-062 · Evidence Image Reference — "Vision:"

**Modules:** 2/28

```
Pattern:  Vision: ❌ Quick actions hidden...
Extract:  No direct image ref — use SCR-ID → inventory fallback
```

---

### FMT-063 · Evidence Image Reference — None

**Modules:** 4/28

```
Pattern:  No image references in evidence text
Extract:  Use artboard-index.json or screen_inventory.json fallback
```

---

### FMT-070 · Manifest Key — Canonical

**Modules:** 17/28

```
Keys: screen_count, artboard_count, overlay_count
```

---

### FMT-071 · Manifest Key — Plural "s" Variant

**Modules:** 2/28

```
Keys: screens_count, artboards_count, overlays_detected
Mapping: screens_count → screen_count (strip 's')
```

---

### FMT-072 · Manifest Key — Missing

**Modules:** 9/28

```
Key absent → derive from screen_inventory.json: len(screens)
```

---

## Template cho format mới

Khi phát hiện format mới, copy template sau và điền:

```markdown
### FMT-XXX · [Tên ngắn gọn]

**Modules:** [module name(s)]
**Ngày phát hiện:** YYYY-MM-DD
**Phát hiện bởi:** [converter run hoặc manual]

\`\`\`
Pattern:  [raw text mẫu]
Regex:    [regex pattern]
Extract:  [extraction logic]
\`\`\`

**Context:** [Tại sao format này khác — root cause]
```
