# SCR-GG-002 — Gửi gốc thêm tiền gửi tích luỹ › Danh sách tài khoản

## 1. Mục đích màn hình
Hiển thị danh sách tài khoản tiền gửi trực tuyến tích luỹ để user chọn TK cần gửi gốc thêm.

## 2. Thành phần giao diện

| # | Element | Type | Nội dung | Ghi chú |
|---|---------|------|----------|---------|
| 1 | Header | title | Gửi gốc thêm tiền gửi tích luỹ | Dark blue |
| 2 | Back arrow | navigation | < | |
| 3 | Filter icon | trigger | 🔽 | Bộ lọc TK |
| 4 | Instruction | text | Chọn tài khoản tiền gửi trực tuyến để gửi gốc thêm | |
| 5 | Section header | section | Tài khoản trực tuyến tích luỹ (2) | Số lượng TK |
| 6 | Total balance label | label | Tổng số dư gốc | |
| 7 | Total balance value | amount | 25,000,000 VND | Bold, blue |
| 8 | Balance card (x3) | card | STK: 12300123123000 | Repeating |
| 9 | Effective date | date | Ngày hiệu lực: 20/09/2021 | |
| 10 | Maturity date | date | Ngày đáo hạn: 21/09/2025 | |
| 11 | Current balance | amount | 5,000,000 VND | Per card |

## 3. Luồng tương tác
- Tap balance card → SCR-GG-003 (Form nhập thông tin gửi gốc)
- Tap balance card (long press / detail) → SCR-GG-006 (Chi tiết TK)
- Tap filter icon → filter/sort options
- Tap back → SCR-GG-001

## 4. Nghiệp vụ & Validation
- Chỉ hiển thị TK tích luỹ có trạng thái hợp lệ (active, chưa tất toán)
- Tổng dư gốc = sum(dư gốc hiện tại) của tất cả TK hiển thị
- Số trong ngoặc = count TK hợp lệ

## 5. Ghi chú thiết kế
- Cards: white, rounded corners, shadow
- Each card shows: STK, ngày hiệu lực, ngày đáo hạn, số dư gốc hiện tại
- Piggy icon decoration trên mỗi card
- Scrollable list

![SCR-GG-002](../ui/1201-gui-goc.png)
