---
name: pdr-analyze
description: "Phân tích case và variant từ output PDR Extract, kết hợp Mô tả màn hình + ui-ux-pro-max + temp1.json để suy luận case có thể xảy ra, biến thể component, state, và giá trị thiếu. Dùng khi cần phân tích case, variant, state coverage, hoặc token mapping từ PDR."
---

# PDR Analyze -- Skill 2

Phân tích case và variant component từ kết quả PDR Extract. Đây là bước thứ hai trong pipeline 2 skill (xem rule `pdr-component-pipeline.mdc`).

## Khi nào dùng

- Phân tích case có thể xảy ra từ mô tả PDR
- Suy luận biến thể và state của component
- Map token từ temp1.json
- Liệt kê giá trị thiếu (token, state, behavior)
- Bổ sung UX proposal cho component

## Input

- **Output Skill 1**: Component Registry + Screen Registry + Cross-references
- **Cột "Mô tả" gốc**: text vision từ bảng Mô tả màn hình (giữ nguyên trong Skill 1 output)
- **ui-ux-pro-max data**: file CSV tại `.agents/skills/ui-ux-pro-max/data/`
- **temp1.json**: token hierarchy
- **design_handoff** (optional, from Skill 0): colors (HEX), typography, style, component specs, color token proposals. Khi có, dùng để resolve missing tokens thay vì chỉ ghi `missing_token`.
- **target_mode**: `Mobile` (mặc định, mobile-first) hoặc `Desktop`

## Quy trình 4 bước

### Bước 1 -- Phân tích "Mô tả" để suy case ngầm

Cột "Mô tả" trong bảng Mô tả màn hình là **vision text** -- chứa thông tin ngầm về case, state, và biến thể mà PDR không liệt kê tường minh.

Với mỗi component trong Component Registry, đọc cột `description` và tìm:

**1a. Hành vi có điều kiện:**
- Pattern: "khi...", "nếu...thì...", "hoặc", "trường hợp"
- Mỗi nhánh điều kiện = 1 case
- Vd: "Nút Thêm hoặc bộ nút (+/-/Số lượng) **khi đã chọn**" -> 2 case: chưa chọn vs đã chọn

**1b. Nhiều state trong mô tả:**
- Pattern: "ẩn/hiện", "mờ đi", "đã khóa / đang mở", "chuyển sang"
- Mỗi cặp = variant có state riêng
- Vd: "Tag trạng thái" -> ít nhất 2 variant: active / locked

**1c. Gợi ý tương tác:**
- Pattern: "đếm ngược", "hỗ trợ", "tự động", "kéo", "cuộn"
- Tương tác ngụ ý state: loading, countdown, animation
- Vd: "đếm ngược thời gian gửi lại (60s)" -> state: counting + state: can_resend

**1d. Biến thể dữ liệu:**
- Pattern: liệt kê nhiều item trong ngoặc, "Ví dụ:", format khác nhau
- Mỗi loại dữ liệu khác nhau = variant
- Vd: "Hiển thị Ảnh, Mã (Màu xám), Tên (Đen), Giá (Đỏ), và Tag trạng thái" -> Card có nhiều sub-element, Tag là variant

**1e. Cross-reference behavior (từ Skill 1):**
- Lấy `behavior_rules` từ Component Registry
- Mỗi business rule có thể sinh case: validate success / validate fail, locked / unlocked
- Vd: "status=False ẩn sản phẩm" -> case: product visible vs product hidden

Mỗi case suy ra phải:
- Ghi rõ `trigger` (điều gì gây ra case)
- Ghi rõ `expected_behavior` (UI phản ứng thế nào)
- Đánh `COMPbase` nếu có evidence trực tiếp từ PDR
- Đánh `COMPextend` nếu là suy luận mở rộng từ UX

### Bước 2 -- Suy luận với ui-ux-pro-max (mở rộng 6 CSV)

Với mỗi component, tra cứu **6 file CSV** để bổ sung state, pattern, color, typography, style, và icon:

**2a. `data/ux-guidelines.csv`** (giữ nguyên)

Cấu trúc: `No, Category, Issue, Platform, Description, Do, Don't, ..., Severity`

Match theo `Category` phù hợp với `component_group`:

| component_group | Category match |
|----------------|---------------|
| `Input/Form` | Forms, Interaction, Touch |
| `Navigation/Action` | Navigation, Touch, Interaction |
| `Cards/Lists` | Layout, Touch, Performance |
| `Layout` | Layout, Animation |
| `Search/Filter` | Interaction, Performance |
| `Info/Feedback` | Animation, Interaction |
| `Special` | Layout, Touch, Interaction |

Với mỗi row match:
- Kiểm tra component đã có state/behavior tương ứng chưa
- Nếu thiếu -> thêm vào COMPextend với `ux_rule_ref` = `ux-guidelines#{No}: {Issue}`
- Ưu tiên Severity: Critical > High > Medium > Low

**2b. `data/web-interface.csv`**

Cấu trúc: `No, Category, Issue, Keywords, Platform, Description, Do, Don't, ..., Severity`

Match theo `Category`:

| component_group | Category match |
|----------------|---------------|
| `Input/Form` | Forms, Accessibility, Focus |
| `Navigation/Action` | Accessibility, Focus |
| `Cards/Lists` | Performance, State |
| `Layout` | Anti-Pattern |
| `Info/Feedback` | Accessibility, State |
| `Special` | Accessibility, State |

Với mỗi row match:
- Kiểm tra cột `Do` -- component đã tuân thủ chưa
- Nếu chưa -> thêm COMPextend proposal với `ux_rule_ref` = `web-interface#{No}: {Issue}`

**2c. `data/colors.csv`** (MỚI)

Cấu trúc: `No, Product Type, Primary (Hex), Secondary (Hex), CTA (Hex), Background (Hex), Text (Hex), Border (Hex), Notes`

Dùng khi component cần color token mà temp1.json không có:
- Match `Product Type` với product type từ overview (vd: "POS" -> gần "Productivity Tool" hoặc "Service Landing Page")
- Lấy HEX values cho: primary, secondary, CTA, background, text, border
- Nếu có `design_handoff.colors` -> ưu tiên design_handoff trước, colors.csv là fallback
- Output: proposed color values kèm `resolved_from: colors.csv#{No}`

**2d. `data/typography.csv`** (MỚI)

Cấu trúc: `No, Font Pairing Name, Category, Heading Font, Body Font, Mood/Style Keywords, Best For, Google Fonts URL, CSS Import, Tailwind Config, Notes`

Dùng khi component cần typography spec:
- Nếu có `design_handoff.typography` -> dùng trực tiếp (ưu tiên)
- Nếu không -> match `Mood/Style Keywords` hoặc `Best For` với product type
- Output: heading font, body font, CSS import cho component
- `resolved_from: typography.csv#{No}` hoặc `resolved_from: design_handoff`

**2e. `data/styles.csv`** (MỚI)

Cấu trúc: `No, Style Category, Type, Keywords, ..., Design System Variables`

Dùng cột `Design System Variables` để lấy CSS variables sẵn có:
- Match style từ `design_handoff.style.name` hoặc từ product type reasoning
- Trích `Design System Variables` cho: `--border-radius`, `--shadow`, `--transition-duration`, etc.
- Output: CSS variable tokens kèm `resolved_from: styles.csv#{No}`

**2f. `data/icons.csv`** (MỚI)

Dùng khi component có icon (vd: bottom-bar icons, statistic-cards chart icon, search icon):
- Match component_group hoặc component_key với icon recommendations
- Output: icon set suggestion (Heroicons/Lucide), specific icon name nếu có
- Ghi vào COMPextend proposals với `ux_rule_ref: icons.csv`

**Output bước 2** (tích lũy): danh sách COMPextend proposals kèm `ux_rule_ref` và `priority` (Critical/High/Medium/Low). Bao gồm color proposals, typography specs, CSS variables, và icon recommendations.

### Bước 3 -- Map token (Mobile-First + Resolution Chain)

**Nguyên tắc mobile-first**: Luôn resolve token từ `"4. Custom".modes.Mobile` trước. Desktop values chỉ ghi trong cột `desktop_override` khi khác Mobile.

**3a. Token có sẵn trong temp1.json (collection "4. Custom"):**

| Token | Mobile Value (BASELINE) | Desktop Override (nếu khác) | Áp dụng cho |
|-------|------------------------|----------------------------|-------------|
| `heading-xl` | `{text.3xl.font-size}` | `{text.5xl.font-size}` | Header chính |
| `heading-lg` | `{text.3xl.font-size}` | `{text.4xl.font-size}` | Section headers |
| `heading-md` | `{text.3xl.font-size}` | same | Sub-headers |
| `heading-sm` | `{text.2xl.font-size}` | same | Labels lớn |
| `container-padding-x` | `{spacing.6}` | same | Padding ngang container |
| `section-padding-y` | `{spacing.16}` | `{spacing.24}` | Padding dọc section |
| `section-title-gap-*` | `{spacing.4}` - `{spacing.5}` | `{spacing.4}` - `{spacing.6}` | Khoảng cách title-to-content |

**3b. Resolution Chain (thứ tự ưu tiên khi token thiếu):**

```
1. temp1.json "4. Custom".modes.Mobile   (token có sẵn)
2. design_handoff.colors                 (HEX values từ Skill 0)
3. design_handoff.component_specs        (CSS specs từ Skill 0)
4. colors.csv (product type match)       (HEX values từ CSV)
5. styles.csv (Design System Variables)  (CSS variables từ CSV)
6. Fallback: missing_token + proposed_name + proposed_value
```

**3c. Quy tắc map:**
- Component có typography -> map `heading-*` token, dùng **Mobile value** làm baseline
- Component là container/section -> map `container-padding-x`, `section-padding-y` (Mobile values)
- Component cần color -> tra chain 2-4 để lấy proposed HEX value
- Component cần shadow/border-radius -> tra chain 5 để lấy CSS variable
- Ghi `resolved_from`: `temp1.json` | `design_handoff` | `colors.csv` | `styles.csv` | `missing`

**3d. Token thiếu (chỉ khi cả 5 bước chain không resolve):**
- Thêm vào `missing_tokens` với:
  - `proposed_token_name`: tên đề xuất theo convention `{group}.{purpose}`
  - `proposed_value`: giá trị đề xuất nếu có (từ chain hoặc UX convention)
  - `group`: nhóm (typography / spacing / color / border / shadow)
  - `mode`: Mobile (baseline)
  - `resolved_from`: `missing`

**3e. Mobile-first touch/interaction tokens:**
- Mọi component interactive phải có `touch_target >= 44x44px` -> đánh dấu COMPbase (mobile-first requirement)
- Bottom bar, buttons, links, input fields -> kiểm tra touch target

### Bước 4 -- Tổng hợp output

Compile 3 bước trên thành output Markdown gồm 3 section chính:

## Output

### 1. Case Matrix

```markdown
## 1. Case Matrix

| # | Screen | Component | Case | Trigger | Expected Behavior | Source | Status |
|---|--------|-----------|------|---------|-------------------|--------|--------|
```

- `Case`: mô tả ngắn gọn case
- `Trigger`: điều gì kích hoạt case
- `Expected Behavior`: UI phản ứng ra sao
- `Source`: citation anchor (vd: `inventory-management.md#Wireframe > Mô tả màn hình, STT 3`)
- `Status`: `COMPbase` hoặc `COMPextend`

Sắp xếp: COMPbase trước, COMPextend sau, trong mỗi nhóm sắp theo Screen.

### 2. Component Variants & States

```markdown
## 2. Component Variants & States

| # | component_key | Variant | States | Description | Token Ref | Proposed Value | Resolved From | Source |
|---|---------------|---------|--------|-------------|-----------|---------------|---------------|--------|
```

- `Variant`: tên biến thể (vd: `card-item--active`, `card-item--locked`)
- `States`: danh sách state áp dụng, từ tập: `default`, `focus`, `active`, `disabled`, `loading`, `error`, `success`, `empty`
- `Token Ref`: token reference nếu có (vd: `{4. Custom.heading-md}`) hoặc `missing_token`
- `Proposed Value`: giá trị đề xuất khi resolved từ chain (HEX, px, rem). Rỗng nếu có token ref trực tiếp.
- `Resolved From`: `temp1.json` | `design_handoff` | `colors.csv` | `styles.csv` | `missing`
- `Source`: `COMPbase` kèm citation hoặc `COMPextend` kèm `ux_rule_ref`

### 3. Missing Values

```markdown
## 3. Missing Values

### 3.1 Missing Tokens (chỉ tokens không resolve được qua chain)
| component_key | Proposed Token | Proposed Value | Group | Mode | Resolved From |
|---------------|---------------|---------------|-------|------|---------------|

### 3.2 Resolved Tokens (tokens đã resolve qua chain, không có trong temp1.json)
| component_key | Token Name | Resolved Value | Group | Resolved From |
|---------------|-----------|---------------|-------|---------------|

### 3.3 Unspecified Behaviors
| component_key | What is missing | Recommendation |
|---------------|----------------|----------------|

### 3.4 COMPextend UX Additions
| component_key | Proposal | ux_rule_ref | Priority |
|---------------|----------|-------------|----------|
```

**3.1 Missing Tokens**: token cần mà cả resolution chain đều không resolve được. Số lượng mục tiêu: < 30% tổng tokens.
**3.2 Resolved Tokens**: token không có trong temp1.json nhưng đã resolve qua design_handoff, colors.csv, hoặc styles.csv. Ghi rõ giá trị đề xuất.
**3.3 Unspecified Behaviors**: hành vi PDR không nói rõ, đánh dấu UNSPECIFIED kèm đề xuất xử lý.
**3.4 COMPextend UX Additions**: bổ sung UX từ ui-ux-pro-max, sắp theo Priority (Critical -> High -> Medium -> Low).

## Ràng buộc

- Mọi case COMPbase phải có citation PDR.
- Mọi case COMPextend phải có `ux_rule_ref`.
- Không sáng tạo case vô căn cứ -- mọi suy luận đều phải dựa trên text "Mô tả" hoặc behavior_rules hoặc UX CSV evidence.
- Token map bắt đầu từ `4. Custom` collection (Mobile mode) trong temp1.json, rồi qua resolution chain.
- Missing tokens phải có `proposed_token_name` theo naming convention: `{group}.{purpose}` (vd: `color.status-active`, `border.radius-card`).
- Missing tokens nên có `proposed_value` nếu resolve được từ chain (HEX, px, rem).
- Mục tiêu: tỷ lệ `missing_token` (không resolve) < 30% tổng tokens cần.
- Liệt kê đầy đủ -- không bỏ sót component nào từ Skill 1 output.
- Mobile-first: touch_target >= 44x44px cho interactive components là COMPbase requirement.
