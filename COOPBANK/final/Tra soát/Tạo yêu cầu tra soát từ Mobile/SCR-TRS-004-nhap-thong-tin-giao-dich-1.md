# SCR-TRS-004 — Tạo yêu cầu tra soát › Form nhập thông tin (trống)

## 1. Screen Identity
- **Screen ID:** SCR-TRS-004
- **Display Name:** Tạo yêu cầu tra soát › Form nhập thông tin
- **Screen Type:** form
- **Artboards:** Tra soát Mobile 5 (142:29438)
- **Wireframe:** `ui/tra-soat-mobile-5.png`

## 2. User Story
Là người dùng, sau khi chọn giao dịch cần tra soát, tôi muốn điền thông tin lý do và nội dung tra soát để gửi yêu cầu.

## 3. Screen Content (OCR)
| Element | Text | Role |
|:---|:---|:---|
| Header | Tạo yêu cầu tra soát | header_title |
| Section | Thông tin giao dịch | section_header |
| Row | Thời gian giao dịch: 20/02/2025 18:00 | readonly_field |
| Row | Mã giao dịch: 12312529 | readonly_field |
| Row | Tài khoản nguồn: 1212390002122 | readonly_field |
| Link | Chi tiết giao dịch > | link_action |
| Section | Thông tin tra soát | section_header |
| Label | Lý do tra soát | field_label_dropdown |
| Label | Nội dung tra soát | field_label_textarea |
| Label | Tài khoản thu phí tra soát | field_label_dropdown |
| CTA | Tiếp tục | cta_button |

## 4. Functional Requirements
- Section 1 (read-only): hiển thị tóm tắt giao dịch đã chọn
- Link "Chi tiết giao dịch >" → SCR-TRS-006
- Dropdown: Lý do tra soát (required)
- Textarea: Nội dung tra soát (free text, optional)
- Dropdown: Tài khoản thu phí tra soát (required)
- CTA "Tiếp tục" chỉ active khi Lý do + Tài khoản đã chọn

## 5. Non-Functional Requirements
- Validation trước khi submit
- Placeholder text cho dropdown chưa chọn

## 6. Flow
- **Entry:** SCR-TRS-003 → tap transaction item
- **Exit [Chi tiết]:** SCR-TRS-006 (chi tiết giao dịch)
- **Exit [Submit]:** SCR-TRS-005 (form đã điền)
