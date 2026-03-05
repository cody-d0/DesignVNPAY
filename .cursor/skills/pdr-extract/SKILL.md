---
name: pdr-extract
description: "Kết xuất component từ file .md PDR với 3 bước: ngữ cảnh overview, parse Mô tả màn hình, đối chiếu hành vi. Output là Component Registry có citation. Dùng khi cần trích xuất component, screen registry, hoặc behavior rules từ PDR."
---

# PDR Extract -- Skill 1

Kết xuất component từ hệ thống tài liệu .md PDR. Đây là bước đầu tiên trong pipeline 2 skill (xem rule `pdr-component-pipeline.mdc`).

## Khi nào dùng

- Kết xuất danh sách component từ file .md chức năng
- Xây dựng screen registry từ PDR
- Trích behavior rules ảnh hưởng component
- Chuẩn bị dữ liệu đầu vào cho Skill 2 (pdr-analyze)

## Input

- `feature_md` (bắt buộc): đường dẫn file .md chức năng cụ thể
- `overview_md` (bắt buộc): đường dẫn file .md overview

## Quy trình 3 bước

### Bước 1 -- Ngữ cảnh từ Overview

Đọc file `overview_md` để nắm bức tranh tổng thể:

1. **Phạm vi sản phẩm**
   - Mục `In Scope (MVP)`: xác định tính năng nào thuộc phạm vi
   - Mục `Out of Scope & Roadmap`: xác định giới hạn, không suy luận ngoài scope

2. **Tính năng liên quan**
   - Bảng `Cấu trúc tài liệu PRD`: liệt kê module nào liên quan đến feature đang xét
   - `User Flow chính`: vị trí feature trong luồng tổng thể

3. **Điểm tích hợp**
   - Mục `Hệ thống cần tích hợp`: Firebase, VNPAY QR MMS, v.v.
   - Ảnh hưởng đến component (vd: nếu có VNPAY QR -> có thể có QR Container)

Output bước 1 (nội bộ, không xuất ra user):
- `scope_mvp[]`: danh sách tính năng MVP
- `scope_excluded[]`: danh sách tính năng ngoài scope
- `integrations[]`: danh sách hệ thống tích hợp
- `related_modules[]`: danh sách module liên quan

### Bước 2 -- Parse bảng "Mô tả màn hình"

Đọc file `feature_md`, tìm section `Wireframe > Mô tả màn hình`.

Bảng có format:
```
| STT | Tên màn hình | Loại thành phần | Mô tả |
```

Với mỗi dòng, trích xuất:

| Trường | Nguồn | Mô tả |
|--------|-------|-------|
| `stt` | Cột STT | Số thứ tự |
| `screen_name` | Cột "Tên màn hình" | Tên màn hình chứa component |
| `prd_type` | Cột "Loại thành phần" | Giá trị thô từ PDR |
| `component_key` | Chuẩn hóa từ `prd_type` | Kebab-case: "Input Field" -> `input-field`, "Card Item" -> `card-item`, "Search Bar" -> `search-bar` |
| `description` | Cột "Mô tả" | Text mô tả nguyên bản -- giữ nguyên, đây là vision text cho Skill 2 |
| `component_group` | Phân loại từ `prd_type` | Một trong các nhóm dưới |

**Bảng phân nhóm component:**

| Nhóm | Các loại thường gặp |
|------|-------------------|
| `Input/Form` | Input Field, Pin Input, OTP Input, Pass Fields, Form Section, Read-only Field, Switch |
| `Layout` | Header, Footer, Sticky Footer, Bottom Bar, Separator |
| `Navigation/Action` | Button, Action Link, Link, Logout Button |
| `Search/Filter` | Search Bar, Dropdown Filter, Filter Tabs |
| `Cards/Lists` | Card Item, Product Card, Order Card, Statistic Cards, List Item, Recent Orders List |
| `Info/Feedback` | Infobox, Helper Text, Growth Label, Success Header, Success Popup, Timer, Dialog |
| `Special` | Upload Area, QR Code Container, Payment Options, Bill Detail, Order Detail Summary |

Nếu `prd_type` không khớp nhóm nào:
- Phân nhóm dựa trên mô tả
- Đánh dấu `NEW_KEY_CANDIDATE`
- Không tự ý gộp vào key đã có

### Bước 3 -- Đối chiếu hành vi

Quét các section khác trong `feature_md` để bổ sung behavior rules cho từng component:

**3a. Từ User Flow:**
- Dò bảng `Bước | Tên màn hình | Tên hành động | Kết quả`
- Match `Tên màn hình` với `screen_name` từ Bước 2
- Trích `Tên hành động` + `Kết quả` thành behavior rule
- Citation: `{feature_md}#User Flow > {tên luồng}`

**3b. Từ User Story:**
- Dò bảng `Epic chung | Mã US | Tiêu đề | ... | Business Rule | Acceptance Criteria`
- Cột `Business Rule`: trích rule ảnh hưởng component (vd: "Mã hàng hóa là duy nhất")
- Cột `Acceptance Criteria`: trích điều kiện ngụ ý state (vd: "Validate đầy đủ Mã, Tên, Giá")
- Citation: `{feature_md}#User Story > {Mã US}`

**3c. Tham chiếu chéo module:**
- Tìm markdown link `[text](./other-file.md)` trong User Story hoặc Mô tả
- Ghi nhận cross-reference: module nào ảnh hưởng module nào, impact gì
- Citation: `{feature_md}#User Story > {Mã US}` hoặc `{feature_md}#Wireframe`

**3d. Từ Non-functional requirement:**
- Trích yêu cầu ảnh hưởng trực tiếp đến UI (vd: "Hỗ trợ Empty State", "Toast notification")
- Citation: `{feature_md}#Non-functional requirement`

## Output

Output Markdown gồm 3 bảng:

### Screen Registry

```markdown
## Screen Registry

| Screen | Components Count | Source |
|--------|-----------------|--------|
| {screen_name} | {số component thuộc màn hình} | {feature_md}#Wireframe |
```

### Component Registry

```markdown
## Component Registry

| # | Screen | prd_type | component_key | group | description | behavior_rules |
|---|--------|----------|---------------|-------|-------------|----------------|
| {stt} | {screen_name} | {prd_type} | {component_key} | {component_group} | {description gốc} | {danh sách rule, mỗi rule kèm citation} |
```

Ghi chú:
- Cột `description` giữ nguyên text gốc từ PDR, không tóm tắt hay chỉnh sửa.
- Cột `behavior_rules` chứa danh sách rule, format: `rule_text [source: anchor]`
- Mọi dòng là COMPbase (có evidence PDR trực tiếp).

### Cross-references

```markdown
## Cross-references

| Source Module | Target Module | Impact | Citation |
|--------------|---------------|--------|----------|
| {file hiện tại} | {file được tham chiếu} | {mô tả ảnh hưởng} | {anchor chứa link} |
```

## Ràng buộc

- Chỉ trích từ anchor hợp lệ (Wireframe, User Flow, User Story, DB, NFR, Phạm vi).
- Không suy luận behavior nếu không có anchor evidence.
- Mọi dòng output phải có citation.
- Output skill này là COMPbase thuần -- không đề xuất, không mở rộng.
- Giữ nguyên cột "Mô tả" cho Skill 2 dùng làm vision text.
