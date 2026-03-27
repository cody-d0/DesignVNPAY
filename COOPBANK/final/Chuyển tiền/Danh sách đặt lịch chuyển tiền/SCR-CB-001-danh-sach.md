# Danh sách đặt lịch chuyển tiền › Danh sách

> `SCR-CB-001` · list · 1 artboard

## 1. Thông tin chung

| Field | Value |
|-------|-------|
| Screen ID | SCR-CB-001 |
| Tên màn hình | Danh sách đặt lịch chuyển tiền › Danh sách |
| Loại | list |
| Artboards | calendar (59:20996) |
| Wireframes | `ui/calendar.png` |

## 2. Mô tả chức năng

Màn hình hiển thị danh sách tất cả các giao dịch đặt lịch chuyển tiền dưới dạng card. Mỗi card hiển thị:
- Tên người thụ hưởng (NGUYEN THI LAN ANH, QUY TIN DUNG NHAN..., NGUYEN VAN A)
- Số tiền (2,000,000 VND)
- Tần suất (1 ngày/lần, Hàng tháng, 7 ngày/lần, Không lặp lại)
- Ngày thực hiện tiếp theo (nếu có)
- Trạng thái (Hoạt động, Đã hủy, Hết hạn, Tạm dừng)

Header có title "Danh sách đặt lịch chuyển tiền" với icon back và filter.

## 3. Luồng người dùng (User Flow)

1. User mở màn hình → Hiển thị danh sách card đặt lịch
2. Scroll để xem tất cả giao dịch
3. Tap icon filter (góc trên phải) → Mở bộ lọc (SCR-CB-003)
4. Tap vào 1 card → Xem chi tiết (SCR-CB-004)
5. Tap back → Quay lại màn trước

## 4. UI Components

- **Header bar**: Title center + back arrow left + filter icon right
- **Card list** (scrollable): Mỗi card có:
  - Bank logo icon (home) + tên thụ hưởng + số tiền (xanh dương)
  - Row: Tần suất — giá trị
  - Row: Ngày thực hiện tiếp theo — giá trị (chỉ hiện khi Hoạt động/Tạm dừng)
  - Row: Trạng thái — badge màu (xanh=Hoạt động, đỏ=Đã hủy/Hết hạn, cam=Tạm dừng)

## 5. Yêu cầu phi chức năng

- Danh sách hỗ trợ scroll vô hạn (infinite scroll hoặc pagination)
- Card phải hiển thị đủ thông tin để user phân biệt nhanh trạng thái
- Trạng thái color coding nhất quán với design system
- Format tiền tệ VND có dấu phẩy phân cách hàng nghìn
