# SCR-TRS-007 — Tạo yêu cầu tra soát › Xác nhận giao dịch

## 1. Screen Identity
- **Screen ID:** SCR-TRS-007
- **Display Name:** Tạo yêu cầu tra soát › Xác nhận giao dịch
- **Screen Type:** confirm
- **Artboards:** Tra soát Mobile 8 (142:29739) — base + OTP overlay
- **Wireframe:** `ui/tra-soat-mobile-8.png`
- **Overlay:** Modal Dialog "Xác thực giao dịch" (score 8/12)

## 2. User Story
Là người dùng, tôi muốn xem lại toàn bộ thông tin tra soát lần cuối và xác thực bằng OTP để đảm bảo yêu cầu chính xác trước khi gửi.

## 3. Screen Content (OCR)
| Element | Text | Role |
|:---|:---|:---|
| Header | Tạo yêu cầu tra soát | header_title |
| Section | Thông tin giao dịch | section_header |
| Value | 20/02/2025 | readonly_field_value |
| Value | 12312929 | readonly_field_value |
| Value | 1212390002122 | readonly_field_value |
| Link | Chi tiết giao dịch > | link_action |
| Section | Thông tin tra soát | section_header |
| Value | Chưa nhận được tiền | readonly_field_value |
| Value | abc123 | readonly_field_value |
| Value | 1234232323 | readonly_field_value |
| Modal Title | Xác thực giao dịch | modal_title |
| Instruction | Quý khách vui lòng nhập mã OTP đã được gửi về số điện thoại 098****123 | modal_instruction |
| CTA | Xác nhận | modal_cta_button |

## 4. Functional Requirements
**Base screen (confirm):**
- Hiển thị toàn bộ thông tin tra soát dạng read-only (summary)
- Link "Chi tiết giao dịch >" vẫn hoạt động

**OTP Modal overlay:**
- Modal dialog (không phải bottom sheet) xuất hiện trên base screen
- Dimmed background làm mờ base screen
- Title: "Xác thực giao dịch"
- 6-digit OTP input (digit-input components)
- Số điện thoại masked: 098****123
- Close button (X) để đóng modal → cancel
- Button "Xác nhận" → submit OTP → SCR-TRS-008

## 5. Non-Functional Requirements (Security-critical)
- OTP masking: digits hiển thị dạng "•" sau khi nhập
- Auto-focus ô tiếp theo sau khi nhập mỗi digit
- OTP timeout: hiển thị countdown
- Retry policy: tối đa N lần nhập sai
- PII protection: số điện thoại masked

## 6. Flow
- **Entry:** SCR-TRS-005 → CTA "Tiếp tục"
- **Overlay trigger:** Modal OTP tự động xuất hiện
- **Exit [OTP Submit]:** SCR-TRS-008 (kết quả)
- **Exit [Cancel/X]:** Quay lại SCR-TRS-005
