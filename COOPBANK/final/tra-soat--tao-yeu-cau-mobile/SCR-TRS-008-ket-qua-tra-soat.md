# SCR-TRS-008 — Tạo yêu cầu tra soát › Kết quả giao dịch

## 1. Screen Identity
- **Screen ID:** SCR-TRS-008
- **Display Name:** Tạo yêu cầu tra soát › Kết quả giao dịch
- **Screen Type:** result
- **Artboards:** Tra soát Mobile 9 (142:29593)
- **Wireframe:** `ui/tra-soat-mobile-9.png`

## 2. User Story
Là người dùng, sau khi xác thực OTP thành công, tôi muốn thấy mã tra soát và thông tin xác nhận, đồng thời có thể chia sẻ/lưu ảnh hoặc tạo yêu cầu mới.

## 3. Screen Content (OCR)
| Element | Text | Role |
|:---|:---|:---|
| Header | Kết quả giao dịch | header_title |
| Brand | Co-opBank | brand_logo_text |
| Status | Quý khách đã lập yêu cầu tra soát thành công! | success_message |
| Row | Mã tra soát: UT123123 | result_field |
| Row | Lý do tra soát: Chưa nhận được tiền | result_field |
| Row | Thời gian tra soát: 29/09/2025 12:30 | result_field |
| Info | Co-opBank sẽ xử lý yêu cầu và cập nhật kết quả xử lý tới Quý khách trong thời gian tra soát quy định. | info_text |
| Action | Chia sẻ | action_button_secondary |
| Action | Lưu ảnh | action_button_secondary |
| CTA | Tạo yêu cầu mới | cta_button_primary |

## 4. Functional Requirements
- Success state với green checkmark icon
- Hiển thị: Mã tra soát + Lý do + Thời gian
- Info text về thời gian xử lý của ngân hàng
- Chia sẻ: share sheet (OS native)
- Lưu ảnh: screenshot → Gallery
- CTA "Tạo yêu cầu mới" → SCR-TRS-001 (reset flow)
- Home icon → main screen

## 5. Non-Functional Requirements
- No back button (unidirectional flow sau confirm)
- Receipt layout đẹp cho share/save

## 6. Flow
- **Entry:** SCR-TRS-007 → OTP submit thành công
- **Exit [Tạo yêu cầu mới]:** SCR-TRS-001
- **Exit [Home]:** Main screen
