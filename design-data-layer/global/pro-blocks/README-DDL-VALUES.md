# design-data-layer/pro-blocks — Context và áp dụng value information

> Tài liệu mô tả cấu trúc value trong design-data-layer (DDL) và các cách áp dụng vào pro-blocks (React + Tailwind / shadcn).

---

## 1. Context

### 1.1 pro-blocks là gì

- **Vị trí:** `design-data-layer/pro-blocks/` — các block UI dùng lại được (buttons, sign-in, sign-up, sections, page-headers, navbars, settings, app-shells, …).
- **Stack:** React ("use client"), Tailwind CSS, component từ `@/components/ui/*` (Button, Input, Label, DropdownMenu, …).
- **Cách dùng style hiện tại:** Tailwind class names (semantic và utility), **không** import trực tiếp file JSON trong `design-data-layer/global/`.

### 1.2 design-data-layer/global — value information

| File | Collection | Mode | Nội dung chính |
|------|------------|------|-----------------|
| `tailwind.json` | TailwindCSS | Default | spacing, width, height, border-radius, colors (tailwind colors.*), font-size/line-height, font-weight, shadow, blur |
| `theme-default.json` | Theme | Default | colors (accent/background/border/primary/… -light/-dark), font, breakpoint, container, text.*, radius, shadow |
| `mode-light.json` | Mode | Light | base.* (alias → Theme colors.*-light), alpha.*, custom.* |
| `mode-dark.json` | Mode | Dark | base.* (alias → Theme colors.*-dark), … |
| `custom-desktop.json` | Custom | Desktop | heading-xl/lg/md/sm (font-family, font-size, line-height, font-weight), container-padding-x, section-padding-y, section-title-gap-* |
| `custom-mobile.json` | Custom | Mobile | Cùng nhóm token, giá trị khác (ví dụ section-padding-y, section-title-gap-*) |

**Định dạng token:**

- Mỗi token có thể có:
  - `$type`: `color` | `float` | `string`
  - `$value`: giá trị literal (số, chuỗi, `#hex`, `rgba(...)`) hoặc **reference** `{path.to.token}` (ví dụ `{colors.background-light}`, `{spacing.6}`, `{text.3xl.font-size}`).
- Reference cần **resolve** theo thứ tự hierarchy: TailwindCSS → Theme → Mode → Custom (theo [.cursor/docs/ddl/hierarchy.md](.cursor/docs/ddl/hierarchy.md) và token-variables-standard).

---

## 2. Pro-blocks đang dùng gì (map với DDL)

Pro-blocks dùng Tailwind class; nhiều class tương ứng với token trong DDL.

### 2.1 Semantic colors (→ Mode base.*)

| Tailwind class (trong pro-blocks) | DDL token (sau resolve) | File nguồn |
|-----------------------------------|-------------------------|------------|
| `bg-background` | `base.background` | mode-light / mode-dark |
| `text-foreground` | `base.foreground` | mode-* |
| `text-muted-foreground` | `base.muted-foreground` | mode-* |
| `border-border` | `base.border` | mode-* |
| `border-primary` | `base.primary` | mode-* |
| `bg-muted` | `base.muted` | mode-* |
| `bg-primary`, `text-primary-foreground` | `base.primary`, `base.primary-foreground` | mode-* |
| `hover:bg-muted` | `base.muted` | mode-* |

Chuỗi resolve: `base.background` (mode) → `$value`: `{colors.background-light}` (theme) → `{tailwind colors.base.white}` (tailwind) → `#ffffff`.

### 2.2 Spacing / layout (→ Tailwind + Custom)

| Tailwind class | DDL token có thể | Ghi chú |
|----------------|-------------------|--------|
| `p-4`, `px-4`, `pt-4`, `gap-4` | `spacing.4` (tailwind) = 16 | tailwind.json |
| `p-6`, `px-6`, `gap-6` | `spacing.6` = 24 hoặc Custom `container-padding-x` | custom-*.json có container-padding-x |
| `space-y-2`, `space-y-4`, `gap-2`, `gap-6` | `spacing.2`, `spacing.4`, `spacing.6` | tailwind.json |
| `lg:px-6`, `px-4` | Custom `container-padding-x` (Desktop vs Mobile) | custom-desktop.json, custom-mobile.json |
| `pt-4 md:pt-6`, `pb-4 md:pb-6` | Custom `section-padding-y`, `section-title-gap-*` | custom-*.json |

### 2.3 Typography

| Tailwind class | DDL token có thể | Ghi chú |
|----------------|-------------------|--------|
| `text-sm`, `text-base`, `text-2xl`, `text-3xl` | `text.sm/base/2xl/3xl` (font-size, line-height) | theme-default.json |
| `font-bold` | `font-weight.bold` | theme-default.json |
| `tracking-tight` | (có thể mở rộng trong Custom letter-spacing) | custom-*.json heading-* |

---

## 3. Cách áp dụng value information vào pro-blocks

### 3.1 Build time: Sinh CSS variables / Tailwind theme từ DDL (khuyến nghị)

- **Ý tưởng:** Script đọc `design-data-layer/global/*.json`, resolve reference (TailwindCSS → Theme → Mode → Custom), xuất ra:
  - **Option A:** File CSS (`:root`, `[data-theme="dark"]`) với biến `--background`, `--foreground`, `--muted`, `--spacing-*`, v.v. App (hoặc Tailwind) dùng các biến này.
  - **Option B:** Cập nhật `tailwind.config.*` (theme.extend.colors, theme.extend.spacing) từ giá trị đã resolve.
- **Ưu điểm:** Pro-blocks không đổi code; chỉ cần build pipeline (ví dụ `node scripts/ddl-to-tailwind.js`) và theme/CSS được nạp từ DDL.
- **Resolution:** Cần implement bước resolve `{path.to.token}` (đệ quy, theo hierarchy); số → px hoặc rem tùy convention (ví dụ spacing.6 → 24 → `1.5rem` hoặc `24px`).

### 3.2 Runtime: Provider đọc DDL và inject CSS variables

- **Ý tưởng:** Load JSON (mode-light / mode-dark, custom-desktop / custom-mobile) theo theme/mode/breakpoint; resolve references; set `document.documentElement.style.setProperty('--background', resolvedValue)` (hoặc inject `<style>`).
- **Ưu điểm:** Đổi theme/mode/desktop-mobile không cần build lại.
- **Nhược:** Cần resolver chạy trên client; phải load đủ file (tailwind, theme, mode, custom) để resolve.

### 3.3 Mapping table / token dictionary (doc + validation)

- **Ý tưởng:** Giữ bảng map **Tailwind class ↔ DDL token** (như mục 2) làm tài liệu; dùng cho:
  - Review: pro-blocks có dùng đúng semantic token không (ví dụ không hardcode `#fff` mà dùng `bg-background`).
  - Validation: script hoặc lint rule kiểm tra class names trong pro-blocks có nằm trong danh sách “allowed” tương ứng DDL.
- **Output:** File [pro-blocks-token-map.json](pro-blocks-token-map.json) trong cùng thư mục (mappings + source_files); có thể dùng cho agent/skill hoặc lint.

### 3.4 Resolve reference — quy tắc

- **Format reference:** `{path.to.token}` — path là key lồng nhau (ví dụ `tailwind colors.neutral.100`, `colors.background-light`, `base.background`).
- **Thứ tự resolve:** (1) TailwindCSS, (2) Theme, (3) Mode, (4) Custom. Mode chọn theo `data-theme` hoặc user preference (Light/Dark); Custom chọn theo viewport/breakpoint (Desktop/Mobile).
- **Literal:** Nếu `$value` không bắt đầu bằng `{` thì dùng trực tiếp (số, string, color).
- **Circular reference:** Cần detect và báo lỗi.

---

## 4. Gợi ý bước tiếp theo

1. **Resolver:** Viết script (Node) đọc toàn bộ `design-data-layer/global/*.json`, merge theo scope/mode, resolve `$value` dạng `{...}` thành giá trị cuối (color hex/rgba, number). Output: flat object `{ "base.background": "#ffffff", "spacing.6": 24, ... }`.
2. **Sinh theme:** Từ output resolver, sinh `tailwind.config` theme (colors, spacing, borderRadius, …) hoặc file CSS variables; tích hợp vào app đang dùng pro-blocks.
3. **Mapping table:** Cập nhật bảng Tailwind class ↔ DDL token (mục 2) thành file chuẩn (JSON/MD) trong repo; dùng cho review và (tùy chọn) lint.
4. **Doc:** Ghi rõ trong README pro-blocks: “Values are driven by design-data-layer; run `scripts/ddl-to-tailwind.js` (hoặc tương đương) to regenerate theme.”

---

## 5. Tài liệu tham khảo

- [.cursor/docs/ddl/README.md](.cursor/docs/ddl/README.md) — DDL overview, hierarchy.
- [.cursor/docs/ddl/hierarchy.md](.cursor/docs/ddl/hierarchy.md) — GLOBAL vs PRODUCT, resolution order.
- [.cursor/docs/ddl/contract.md](.cursor/docs/ddl/contract.md) — Query contract, token_view.
- [.cursor/skills/token-variables-standard/SKILL.md](.cursor/skills/token-variables-standard/SKILL.md) — Token reference format `{collection.token}`, hierarchy.
- [scripts/split-token-to-ddl.js](scripts/split-token-to-ddl.js) — Input DDL từ token.json (Figma export).
