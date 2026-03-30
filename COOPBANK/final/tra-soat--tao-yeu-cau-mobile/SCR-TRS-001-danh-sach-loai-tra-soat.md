# SCR-TRS-001 — Tạo yêu cầu tra soát › Danh sách

## 1. Screen Identity
- **Screen ID:** SCR-TRS-001
- **Display Name:** Tạo yêu cầu tra soát › Danh sách
- **Screen Type:** list
- **Artboards:** Tra soát Mobile 1 (142:29619)
- **Wireframe:** `ui/tra-soat-mobile-1.png`

## 2. User Story
Là người dùng Co-opBank Mobile, tôi muốn chọn loại tra soát khiếu nại phù hợp để bắt đầu quy trình tạo yêu cầu tra soát một cách nhanh chóng.

## 3. Screen Content (OCR)
| Element | Text | Role |
|:---|:---|:---|
| Header | Tra soát khiếu nại | header_title |
| Tab active | Tạo yêu cầu | tab_active |
| Tab inactive | Tra cứu yêu cầu | tab_inactive |
| Item 1 | Tra soát giao dịch qua Mobilebanking | list_item |
| Item 2 | Tra soát khác | list_item |

## 4. Functional Requirements
- Tab navigation: "Tạo yêu cầu" / "Tra cứu yêu cầu"
- Danh sách 2 loại tra soát (có thể mở rộng)
- Tap vào item → navigate đến màn hình form tương ứng
- Icon minh họa per loại tra soát

## 5. Non-Functional Requirements
- Load time < 1s
- Accessible: tab indicator đủ contrast
- Support VoiceOver/TalkBack cho list items

## 6. Flow
- **Entry:** Main navigation → Tra soát khiếu nại
- **Exit:** Tạo yêu cầu → SCR-TRS-002 (form nhập thông tin)
- **Exit:** Tra cứu yêu cầu → [out of scope]
