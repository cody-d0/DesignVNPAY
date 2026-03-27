# SCR-GG-003 — Gửi gốc thêm tiền gửi tích luỹ › Form nhập thông tin

## 1. Mục đích màn hình
Form nhập thông tin giao dịch gửi gốc thêm tiền gửi tích luỹ: hiển thị thông tin TK (read-only) và cho phép nhập số tiền gửi thêm.

## 2. Thành phần giao diện

| # | Element | Type | Nội dung | Ghi chú |
|---|---------|------|----------|---------|
| 1 | Header | title | Gửi gốc thêm tiền gửi tích luỹ | Nav: back + home |
| 2 | Account card | info_card | TK tiền gửi: 9099798712313123 | Số dư gốc: 20,000,000 VND |
| 3 | Section 1 | section_header | Thông tin tài khoản | Icon: person |
| 4 | Loại sản phẩm | read_only | Tiết kiệm tích luỹ | |
| 5 | Hình thức tích luỹ | read_only | Tích luỹ linh động | |
| 6 | Kỳ hạn | read_only | 1 tháng | |
| 7 | Ngày đáo hạn | read_only | 20/10/2025 | |
| 8 | Section 2 | section_header | Thông tin giao dịch | Icon: dollar |
| 9 | Số tiền gửi thêm | input | 1,000,000 | Unit: VND |
| 10 | Helper text | hint | Số tiền gửi tối thiểu là 1,000,000 VND | |
| 11 | TK trích tiền | dropdown | 12312313123133 | Caret down icon |
| 12 | Lãi suất | read_only | 5% | |
| 13 | Note banner | info_banner | Lưu ý: Số tiền nộp thêm trong kỳ... | Teal/green bg |
| 14 | CTA | button_primary | Tiếp tục | Full width |

## 3. Luồng tương tác
- Nhập số tiền gửi thêm → validate min amount
- Tap dropdown TK trích tiền → bottom sheet chọn TK
- Tap "Tiếp tục" → SCR-GG-004 (Xác nhận giao dịch)
- Tap back → SCR-GG-002

## 4. Nghiệp vụ & Validation
- Số tiền gửi thêm tối thiểu: 1,000,000 VND
- Số tiền phải là bội số của đơn vị tiền tệ
- TK trích tiền: chỉ TK thanh toán có đủ số dư
- Lãi suất: hiển thị theo kỳ hạn + loại sản phẩm (read-only)

## 5. Ghi chú thiết kế
- Account card: red/white gradient, rounded corners
- 2 sections phân cách rõ ràng
- Input field: underline style
- Note banner: teal/green background, rounded corners
- CTA: dark blue, full width, bottom anchored

![SCR-GG-003](../ui/1202-gui-goc.png)
