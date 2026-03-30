# SCR-TRS-003 — Tạo yêu cầu tra soát › Tìm kiếm giao dịch

## 1. Screen Identity
- **Screen ID:** SCR-TRS-003
- **Display Name:** Tạo yêu cầu tra soát › Tìm kiếm giao dịch
- **Screen Type:** search
- **Artboards:** Tra soát Mobile 4 (142:29327), Tra soát Mobile 10 (194:195580) — empty state
- **Wireframes:** `ui/tra-soat-mobile-4.png`, `ui/tra-soat-mobile-10.png`

## 2. User Story
Là người dùng, tôi muốn xem danh sách giao dịch phù hợp với tiêu chí đã nhập và chọn giao dịch cần tra soát, hoặc nhận thông báo khi không có kết quả.

## 3. Screen Content (OCR)
| Element | Text | Role |
|:---|:---|:---|
| Header | Danh sách giao dịch | header_title |
| Search | Tìm kiếm | search_placeholder |
| Date | 29/09/2025 | transaction_date |
| Amount | -5,000,000 VND | transaction_amount |
| TxID | #123123 | transaction_id |
| Badge | Label 2 | transaction_badge |
| Description | NGUYEN VAN A chuyen tien | transaction_description |
| Date | 28/09/2025 | transaction_date |
| Amount | -1,200,000 VND | transaction_amount |
| TxID | #123124 | transaction_id |
| Description | NGUYEN VAN B chuyen khoan | transaction_description |
| Empty | Không có kết quả tìm kiếm | empty_state_message |

## 4. Functional Requirements
- Search bar inline (filter theo mã GD / sender name)
- Danh sách transaction items: date + amount + ID + badge + description
- Empty state: "Không có kết quả tìm kiếm" khi search không match
- Keyboard visible khi search active
- Tap item → SCR-TRS-004

## 5. Non-Functional Requirements
- Lazy load nếu list > 20 items
- Search debounce 300ms

## 6. Flow
- **Entry:** SCR-TRS-002 → submit form
- **Exit [Select]:** SCR-TRS-004 (form nhập thông tin)
- **Variant:** Empty state khi không có kết quả
