# SCR-GG-005 — Gửi gốc thêm tiền gửi tích luỹ › Kết quả giao dịch

## 1. Mục đích màn hình
Hiển thị kết quả giao dịch gửi gốc thêm thành công, cho phép chia sẻ, lưu ảnh, hoặc thực hiện giao dịch mới.

## 2. Thành phần giao diện

| # | Element | Type | Nội dung | Ghi chú |
|---|---------|------|----------|---------|
| 1 | Header | title | Kết quả giao dịch | Nav: home icon |
| 2 | Logo | brand | Co-opBank | |
| 3 | Status icon | status | ✓ (checkmark) | Green circle |
| 4 | Status text | text | Gửi gốc thêm thành công | |
| 5 | Amount | amount_highlight | 1,000,000 VND | Green, large |
| 6 | Thời gian GD | info | 15/02/2020 22:00 | |
| 7 | TK tiền gửi | info | 9704000012345678 | |
| 8 | TK trích tiền | info | 1231236788923211 | |
| 9 | Mã giao dịch | info | 0982312 | |
| 10 | Chia sẻ | action | Share icon | |
| 11 | Lưu ảnh | action | Save image icon | |
| 12 | CTA primary | button_primary | Tạo giao dịch mới | Full width |
| 13 | CTA secondary | button_secondary | Danh sách tiền gửi | Full width, outline |

## 3. Luồng tương tác
- Tap "Chia sẻ" → native share sheet
- Tap "Lưu ảnh" → save receipt to gallery
- Tap "Tạo giao dịch mới" → SCR-GG-002 (Danh sách TK)
- Tap "Danh sách tiền gửi" → navigate to deposit list
- Tap home → main dashboard

## 4. Nghiệp vụ & Validation
- Mã giao dịch: unique, server-generated
- Thời gian: server timestamp
- Back button disabled (no undo)

## 5. Ghi chú thiết kế
- White card on dark blue background
- Success checkmark: green circle
- Amount: green, large font
- 2 CTAs: primary (filled) + secondary (outline)
- Dashed divider between info fields

![SCR-GG-005](../ui/1205-gui-goc.png)
