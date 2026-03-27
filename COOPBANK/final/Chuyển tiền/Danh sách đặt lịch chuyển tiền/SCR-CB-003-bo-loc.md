# Danh sách đặt lịch chuyển tiền › Bộ lọc

> `SCR-CB-003` · list · 2 artboards

## 1. Thông tin chung

| Field | Value |
|-------|-------|
| Screen ID | SCR-CB-003 |
| Tên màn hình | Danh sách đặt lịch chuyển tiền › Bộ lọc |
| Loại | list |
| Artboards | filter (59:21155), filter-2 (59:21238) |
| Wireframes | `ui/filter.png`, `ui/filter-2.png` |

## 2. Mô tả chức năng

Bottom sheet bộ lọc giúp user tìm kiếm giao dịch đặt lịch theo 2 chế độ:

### Mode 1: Theo trạng thái lệnh
- Radio button "Theo trạng thái lệnh" (selected)
- Dropdown "Loại chuyển tiền": Tất cả
- Dropdown "Trạng thái lệnh": Hoạt động
- CTA "Tìm kiếm"

### Mode 2: Theo thời gian
- Radio button "Theo thời gian" (selected)
- Dropdown "Loại chuyển tiền": Tất cả
- Date picker "Từ ngày", "Đến ngày" với calendar icon
- Annotation: "Truy vấn các lệnh đặt lịch chuyển tiền có Ngày thực hiện tiếp theo trong khoảng thời gian tìm kiếm"
- CTA "Tìm kiếm"

## 3. Luồng người dùng (User Flow)

1. User tap filter icon → Bottom sheet hiện lên
2. Chọn mode (radio buttons): Theo trạng thái lệnh / Theo thời gian
3. Chọn giá trị dropdown → Loại chuyển tiền, Trạng thái
4. (Mode thời gian) Chọn Từ ngày, Đến ngày bằng date picker
5. Tap "Tìm kiếm" → Đóng bottom sheet, hiển thị kết quả filtered
6. Tap X → Đóng bottom sheet không áp dụng

## 4. UI Components

- **Bottom sheet**: Slide up, close X góc phải
- **Radio button group**: 2 options (Theo trạng thái lệnh / Theo thời gian)
- **Dropdown fields**: Loại chuyển tiền, Trạng thái lệnh (with chevron icon)
- **Date picker fields**: Từ ngày, Đến ngày (with calendar icon)
- **Annotation text**: Gray text giải thích logic truy vấn
- **CTA button**: "Tìm kiếm" full-width, primary style

## 5. Yêu cầu phi chức năng

- Bottom sheet giữ state khi toggle giữa 2 modes
- Date picker format DD/MM/YYYY
- Validation: Từ ngày ≤ Đến ngày
- Annotation text phải wrap đẹp, không bị cắt
- Kết quả tìm kiếm phải filter server-side
