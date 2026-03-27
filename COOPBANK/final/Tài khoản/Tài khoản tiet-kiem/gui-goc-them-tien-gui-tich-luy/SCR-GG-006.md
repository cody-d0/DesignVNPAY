# SCR-GG-006 — Chi tiết tài khoản tiết kiệm › Chi tiết

## 1. Mục đích màn hình
Hiển thị toàn bộ thông tin chi tiết tài khoản tiết kiệm tích luỹ (15+ fields) với bottom tab bar cho các thao tác nhanh.

## 2. Thành phần giao diện

| # | Element | Type | Nội dung | Ghi chú |
|---|---------|------|----------|---------|
| 1 | Header | title | Thông tin tài khoản | Nav: back + home |
| 2 | Section title | section | Tài khoản tiết kiệm | Piggy icon |
| 3 | Tên chủ TK | read_only | HA NGUYEN QUANG | |
| 4 | Số TK tiền gửi | read_only | 012547288 | |
| 5 | Chi nhánh/PGD | read_only | CN Lang Ha | |
| 6 | Loại sản phẩm | read_only | Tiền gửi tích luỹ | |
| 7 | Kỳ hạn | read_only | 1 tháng | |
| 8 | Ngày mở ban đầu | read_only | 15/03/2024 | |
| 9 | Ngày hiệu lực | read_only | 15/03/2024 | |
| 10 | Ngày đáo hạn | read_only | 15/03/2025 | |
| 11 | Số dư gốc ban đầu | amount | 10,000,000 VND | |
| 12 | Số dư gốc hiện tại | amount | 10,000,000 VND | |
| 13 | Số tiền phong tỏa | amount | 0 VND | |
| 14 | Lãi suất | value | 0.1% | |
| 15 | Lãi cộng dồn | amount | 213 VND | |
| 16 | Hình thức tích luỹ | read_only | Tích luỹ linh động | |
| 17 | Phương thức đáo hạn | read_only | Đáo hạn cuối kỳ | |
| 18 | TK nhận gốc lãi | read_only | 123123123123 | |
| 19 | PT tất toán/rút gốc | read_only | Tất toán rút gốc tại Quầy | |

### Bottom Tab Bar
| # | Tab | Icon | Action |
|---|-----|------|--------|
| 1 | Tất toán tiền gửi trực tuyến | tattoan | Navigate to tất toán flow |
| 2 | Gửi gốc thêm tiền gửi tích luỹ | guigoc | Navigate to SCR-GG-003 |
| 3 | Lịch sử giao dịch | lichsu | Navigate to transaction history |
| 4 | Chức năng khác | chucnangkhac | More options |

## 3. Luồng tương tác
- Scroll để xem toàn bộ thông tin (content > viewport)
- Tap tab "Gửi gốc thêm" → SCR-GG-003
- Tap back → SCR-GG-002

## 4. Nghiệp vụ & Validation
- Tất cả fields read-only
- Số dư gốc hiện tại có thể ≠ ban đầu (đã gửi thêm/rút)
- Lãi cộng dồn: tính tự động realtime

## 5. Ghi chú thiết kế
- Scrollable content (375x1039 > viewport 812)
- Bottom tab bar: fixed, 4 icons + labels
- Clean layout: label-value pairs, alternating rows

![SCR-GG-006](../ui/1206-gui-gocchi-tiet-tk.png)
