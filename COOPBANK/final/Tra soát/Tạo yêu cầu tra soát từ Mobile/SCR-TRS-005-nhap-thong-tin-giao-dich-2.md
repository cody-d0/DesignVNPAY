# SCR-TRS-005 — Tạo yêu cầu tra soát › Form nhập thông tin (đã điền)

## 1. Screen Identity
- **Screen ID:** SCR-TRS-005
- **Display Name:** Tạo yêu cầu tra soát › Form nhập thông tin
- **Screen Type:** form
- **Artboards:** Tra soát Mobile 6 (142:29539)
- **Wireframe:** `ui/tra-soat-mobile-6.png`

## 2. User Story
Là người dùng, tôi muốn xem lại thông tin tra soát đã nhập (lý do, nội dung, tài khoản thu phí) và phí tra soát tự động trước khi xác nhận.

## 3. Screen Content (OCR)
| Element | Text | Role |
|:---|:---|:---|
| Header | Tạo yêu cầu tra soát | header_title |
| Section | Thông tin giao dịch | section_header |
| Field | Thời gian giao dịch | field_label |
| Value | 20/02/2025 18:00 | field_value_readonly |
| Field | Mã giao dịch | field_label |
| Value | 12312323 | field_value_readonly |
| Field | Tài khoản nguồn | field_label |
| Value | 1212390002122 | field_value_readonly |
| Link | Chi tiết giao dịch | link_action |
| Section | Thông tin tra soát | section_header |
| Field | Lý do tra soát | field_label |
| Value | Chưa nhận được tiền | field_value_selected |
| Field | Phí tra soát | field_label |
| Value | 5,500 VND | field_value_auto_computed |
| Field | Nội dung tra soát | field_label |
| Counter | 6/500 | char_counter |
| Value | abc123 | field_value_entered |
| Field | Tài khoản thu phí tra soát | field_label |
| Value | 1231232323 | field_value_selected |
| CTA | Tiếp tục | cta_button |

## 4. Functional Requirements
- Hiển thị lại tất cả fields đã điền (editable)
- Phí tra soát: auto-computed từ loại giao dịch (5,500 VND)
- Char counter cho Nội dung tra soát (current/max: 6/500)
- Dropdown Lý do: "Chưa nhận được tiền" selected
- CTA "Tiếp tục" → SCR-TRS-007

## 5. Non-Functional Requirements
- Phí tra soát cần format số có dấu phẩy
- Char counter realtime

## 6. Flow
- **Entry:** SCR-TRS-004 → submit với data đã điền
- **Exit [Chi tiết]:** SCR-TRS-006
- **Exit [Submit]:** SCR-TRS-007 (xác nhận + OTP)
