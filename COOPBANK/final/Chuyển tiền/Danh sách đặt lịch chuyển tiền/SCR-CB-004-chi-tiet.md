# Danh sách đặt lịch chuyển tiền › Chi tiết

> `SCR-CB-004` · detail · 8 artboards

## 1. Thông tin chung

| Field | Value |
|-------|-------|
| Screen ID | SCR-CB-004 |
| Tên màn hình | Danh sách đặt lịch chuyển tiền › Chi tiết |
| Loại | detail |
| Artboards | calendar-details (59:21424), calendar-details-2 (59:21670), onhold (59:21514), cancel (59:21536), expired (59:21557), popup (59:21446), popup-2 (59:21470), list (59:21325) |
| Wireframes | `ui/calendar-details.png`, `ui/calendar-details-2.png`, `ui/onhold.png`, `ui/cancel.png`, `ui/expired.png`, `ui/popup.png`, `ui/popup-2.png`, `ui/list.png` |

## 2. Mô tả chức năng

Màn chi tiết giao dịch đặt lịch chuyển tiền hiển thị đầy đủ thông tin:

### Thông tin chi tiết:
- Ngày đặt lịch: 25/02/2023
- Trạng thái đặt lịch: Hoạt động / Tạm dừng / Hủy / Hết hạn
- Tài khoản nguồn: 98712313123
- Tài khoản thụ hưởng: 13237899903
- Tên người thụ hưởng: NGUYEN VAN A
- Số tiền: 20,000,000 VND (Hai mươi triệu đồng)
- Loại chuyển tiền: Chuyển tiền định kỳ nội bộ khác chủ
- Ngày thực hiện tiếp theo: 25/07/2023
- Tần suất: Hàng tháng
- Số lần giao dịch: 2
- Ngày bắt đầu: 15/05/2023
- Ngày kết thúc: 15/06/2023
- Nội dung giao dịch: Balance
- Mã đặt lịch: 12312331

### Variants theo trạng thái:
| Trạng thái | Bottom nav | Đặc biệt |
|-----------|-----------|-----------|
| Hoạt động | Danh sách GD · Tạm dừng · Hủy | Variant 2: Nút "Xem các giao dịch đã thực hiện" |
| Tạm dừng | Danh sách GD · Tiếp tục · Hủy | Tab Tiếp tục thay Tạm dừng |
| Hủy | Danh sách GD | Chỉ tab Danh sách GD |
| Hết hạn | Danh sách GD | Chỉ tab Danh sách GD |

### Overlays:
- **Popup xác nhận**: "Quý khách có muốn Tạm dừng giao dịch đặt lịch chuyển tiền không?" + Không/Đồng ý
- **OTP bottom sheet**: "Xác thực giao dịch" + 6 digit PIN input + warning + Xác nhận
- **Danh sách giao dịch**: Bottom sheet lịch sử với ngày, trạng thái (Thành công/Không thành công/Tạm dừng/Hủy), mã GD, phí

## 3. Luồng người dùng (User Flow)

### Flow Tạm dừng:
1. Xem chi tiết (Hoạt động) → Tap "Tạm dừng" tab
2. Popup xác nhận hiện → Tap "Đồng ý"
3. OTP bottom sheet → Nhập 6 digit PIN → Tap "Xác nhận"
4. → Redirect to manage screen with success popup

### Flow Hủy:
1. Xem chi tiết → Tap "Hủy" tab → Tương tự flow Tạm dừng

### Flow Xem lịch sử:
1. Xem chi tiết → Tap "Danh sách giao dịch" tab hoặc "Xem các giao dịch đã thực hiện"
2. Bottom sheet danh sách GD hiện lên với các entries

## 4. UI Components

- **Header**: "Chi tiết giao dịch đặt lịch chuyển tiền" + back + home icon
- **Detail list**: Key-value rows, separator lines
- **Amount display**: VND format + text bằng chữ (Hai mươi triệu đồng)
- **Bottom navigation bar**: 3 tabs với icons (dynamic theo trạng thái)
- **CTA button**: "Xem các giao dịch đã thực hiện" (variant 2)
- **Popup dialog**: Title + message + 2 buttons (secondary/primary)
- **OTP bottom sheet**: Title + instruction + 6 digit cells + warning + CTA
- **Transaction history sheet**: Title + close X + list entries (date, status, mã, phí)

## 5. Yêu cầu phi chức năng

- OTP input auto-focus, auto-advance between cells
- PIN masked after input
- Soft OTP khóa sau 5 lần sai — warning hiển thị rõ
- Popup xác nhận phải dimmed background
- Transaction history sorted by date desc
- Status color coding consistent: xanh=Thành công, đỏ=Không thành công, cam=Tạm dừng, xám=Hủy
