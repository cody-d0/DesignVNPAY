# Danh sách đặt lịch chuyển tiền › Quản lý

> `SCR-CB-002` · list · 4 artboards

## 1. Thông tin chung

| Field | Value |
|-------|-------|
| Screen ID | SCR-CB-002 |
| Tên màn hình | Danh sách đặt lịch chuyển tiền › Quản lý |
| Loại | list |
| Artboards | manage (59:21068), manage-empty-1 (59:21506), manage-empty-2 (59:21510), manage-menu (59:21578) |
| Wireframes | `ui/manage.png`, `ui/manage-2.png`, `ui/manage-3.png`, `ui/manage-4.png` |

## 2. Mô tả chức năng

Màn hình quản lý đặt lịch chuyển tiền hiển thị danh sách card được nhóm theo **loại chuyển tiền** (Nội bộ khác chủ, Nội bộ cùng chủ). Mỗi card có thêm title loại và icon vertical-dot (3 chấm) để mở menu quản lý.

### Các state:
- **Có dữ liệu**: Danh sách card nhóm theo loại, mỗi card có icon 3 chấm
- **Popup thành công**: "Tạm dừng lệnh chuyển tiền thành công" + nút Đóng
- **Empty state 1**: "Qúy khách không có giao dịch đặt lịch chuyển tiền nào đang Hoạt động. Vui lòng sử dụng bộ lọc..."
- **Empty state 2**: "Không có kết quả tìm kiếm"
- **Bottom menu**: "Quản lý đặt lịch" → Tạm dừng lệnh đặt lịch / Hủy lệnh đặt lịch

## 3. Luồng người dùng (User Flow)

1. User mở quản lý → Hiển thị danh sách card theo loại chuyển tiền
2. Tap icon 3 chấm trên card → Hiện bottom menu "Quản lý đặt lịch"
3. Chọn "Tạm dừng lệnh đặt lịch" hoặc "Hủy lệnh đặt lịch" → Flow xác nhận
4. Sau xác nhận → Hiện popup thành công
5. Nếu không có GD Hoạt động → Hiện empty state với hướng dẫn dùng bộ lọc
6. Nếu filter không có kết quả → Hiện "Không có kết quả tìm kiếm"

## 4. UI Components

- **Header bar**: Title "Quản lý đặt lịch chuyển tiền" + back + filter
- **Tab bar**: "Danh sách đặt lịch chuyển tiền" (selected)
- **Card groups**: Mỗi nhóm có title loại chuyển tiền + vertical-dot menu
- **Popup (overlay)**: Check icon + message + nút "Đóng"
- **Bottom menu (overlay)**: Title "Quản lý đặt lịch" + close X + 2 action items (Tạm dừng, Hủy) với icon
- **Empty states**: Text centered, hướng dẫn sử dụng bộ lọc

## 5. Yêu cầu phi chức năng

- Popup xác nhận phải dimmed background
- Bottom menu slide up animation
- Empty state text rõ ràng, hướng dẫn user cách tìm GD
- Sau action thành công phải refresh danh sách
