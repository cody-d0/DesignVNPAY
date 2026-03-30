# SCR-TRS-002 — Tạo yêu cầu tra soát › Form nhập thông tin

## 1. Screen Identity
- **Screen ID:** SCR-TRS-002
- **Display Name:** Tạo yêu cầu tra soát › Form nhập thông tin
- **Screen Type:** form
- **Artboards:** Tra soát Mobile 2 (142:29385), Tra soát Mobile 3 (142:29427) — variants
- **Wireframes:** `ui/tra-soat-mobile-2.png`, `ui/tra-soat-mobile-3.png`

## 2. User Story
Là người dùng, tôi muốn nhập tiêu chí tìm kiếm (loại giao dịch, tài khoản, khoảng thời gian) để lọc ra giao dịch cần tra soát.

## 3. Screen Content (OCR)
| Element | Text | Role |
|:---|:---|:---|
| Header | Tra soát khiếu nại | header_title |
| Section | Thông tin tra soát | section_header |
| Label | Loại giao dịch | field_label |
| Value | Tất cả | field_value_selected |
| Label | Tài khoản tra soát | field_label |
| Value | 12312323 | field_value |
| Label | Từ ngày | field_label |
| Value | 12/09/2025 | field_value_date |
| Label | Đến ngày | field_label |
| Value v1 | 19/09/2025 | date_variant_7days |
| Value v2 | 12/10/2025 | date_variant_1month |
| CTA | Tìm kiếm | cta_button |

## 4. Functional Requirements
- Dropdown: Loại giao dịch (default: Tất cả)
- Dropdown: Tài khoản tra soát (pre-filled nếu có)
- Date picker: Từ ngày — Đến ngày (date range)
- Validate: Đến ngày ≥ Từ ngày; range ≤ giới hạn hệ thống
- CTA "Tìm kiếm" → navigate SCR-TRS-003

## 5. Non-Functional Requirements
- Date format: DD/MM/YYYY
- Default range: 7 ngày hoặc 30 ngày
- Validation error inline

## 6. Flow
- **Entry:** SCR-TRS-001 → chọn loại tra soát
- **Exit [Submit]:** SCR-TRS-003 (danh sách giao dịch)
- **Variants:** Mobile 2 (7 ngày) / Mobile 3 (1 tháng)
