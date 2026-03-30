# SCR-GG-004 — Gửi gốc thêm tiền gửi tích luỹ › Xác nhận giao dịch

## 1. Mục đích màn hình
Xác nhận thông tin giao dịch gửi gốc thêm trước khi thực hiện. Bao gồm overlay OTP bottom sheet để xác thực.

## 2. Thành phần giao diện

| # | Element | Type | Nội dung | Ghi chú |
|---|---------|------|----------|---------|
| 1 | Header | title | Xác nhận giao dịch | Nav: back |
| 2 | Instruction | text | Quý khách vui lòng kiểm tra thông tin giao dịch đã khởi tạo | Banner blue |
| 3 | TK tiền gửi trực tuyến | read_only | 98712313123 | |
| 4 | Loại sản phẩm | read_only | Tiền gửi tích luỹ | |
| 5 | Kỳ hạn | read_only | 1 tháng | |
| 6 | Lãi suất | read_only | 5% | |
| 7 | Số tiền gửi thêm | amount | 20,000,000 VND | + "Hai mươi triệu đồng" (red) |
| 8 | Ngày đáo hạn | read_only | 20/10/2025 | |
| 9 | Hình thức tích luỹ | read_only | Tích luỹ linh động | |
| 10 | TK trích tiền | read_only | 12312312312312 | |
| 11 | Auth method | dropdown | Soft OTP | Chọn phương thức xác thực |
| 12 | CTA | button_primary | Tiếp tục | Full width |

### Overlay: OTP Bottom Sheet (artboard 1204)
| # | Element | Type | Nội dung |
|---|---------|------|----------|
| 1 | Title | overlay_title | Xác thực giao dịch |
| 2 | Close | icon_button | × |
| 3 | Instruction | text | Quý khách vui lòng nhập mã PIN của Soft OTP để xác thực giao dịch |
| 4 | OTP cells | input_cells | 6 digit cells |
| 5 | Warning | text | Lưu ý: Soft OTP sẽ bị khoá nếu Quý khách nhập sai PIN 5 lần liên tiếp |
| 6 | CTA | button_primary | Xác nhận |

## 3. Luồng tương tác
- Review thông tin → Tap "Tiếp tục" → OTP bottom sheet hiện lên
- Nhập 6 digit PIN → Tap "Xác nhận" → SCR-GG-005 (Kết quả)
- Tap × → đóng OTP sheet
- Tap back → SCR-GG-003

## 4. Nghiệp vụ & Validation
- Số tiền hiển thị cả số và chữ (Hai mươi triệu đồng)
- Soft OTP: 6 digit PIN
- Lock sau 5 lần nhập sai liên tiếp
- Auth methods: Soft OTP (default), có thể thêm phương thức khác

## 5. Ghi chú thiết kế
- Amount text: red color cho phần chữ
- OTP bottom sheet: white bg, rounded top corners
- Blur background khi OTP hiện
- 6 digit cells: masked input

![SCR-GG-004](../ui/1203-gui-goc.png)
![SCR-GG-004-overlay](../ui/1204-gui-goc.png)
