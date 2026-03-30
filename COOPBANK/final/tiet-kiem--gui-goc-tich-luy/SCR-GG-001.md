# SCR-GG-001 — Menu tiền gửi tiết kiệm › Danh mục chức năng

## 1. Mục đích màn hình
Hiển thị danh mục chức năng tiền gửi tiết kiệm, cho phép user chọn 1 trong 5 chức năng: Mở tiền gửi trực tuyến, Tất toán tiền gửi trực tuyến, Rút gốc một phần, Danh sách tiền gửi, Gửi gốc thêm tiền gửi tích luỹ.

## 2. Thành phần giao diện

| # | Element | Type | Nội dung | Ghi chú |
|---|---------|------|----------|---------|
| 1 | Header | title | Tiền gửi tiết kiệm | Dark blue background |
| 2 | Back arrow | navigation | < | Quay lại trang trước |
| 3 | Menu grid | card_container | 5 icons trong grid 3x2 | Rounded corners, white bg |
| 4 | Icon 1 | menu_item | Mở tiền gửi trực tuyến | |
| 5 | Icon 2 | menu_item | Tất toán tiền gửi trực tuyến | |
| 6 | Icon 3 | menu_item | Rút gốc một phần | |
| 7 | Icon 4 | menu_item | Danh sách tiền gửi | |
| 8 | Icon 5 | menu_item | Gửi gốc thêm tiền gửi tích luỹ | |

### Overlay: Popup lỗi (artboard 1207)
| # | Element | Type | Nội dung |
|---|---------|------|----------|
| 1 | Popup title | overlay_title | Thông báo |
| 2 | Popup body | overlay_body | Quý khách không có tài khoản tiền gửi trực tuyến hợp lệ để sử dụng chức năng này |
| 3 | CTA | button | Đóng |

## 3. Luồng tương tác
- Tap "Gửi gốc thêm tiền gửi tích luỹ" → SCR-GG-002 (nếu có TK hợp lệ)
- Tap "Gửi gốc thêm tiền gửi tích luỹ" → Popup "Thông báo" (nếu không có TK hợp lệ)
- Tap "Đóng" trên popup → dismiss popup

## 4. Nghiệp vụ & Validation
- Hệ thống kiểm tra user có ít nhất 1 TK tiền gửi trực tuyến tích luỹ hợp lệ
- Nếu không có → hiển thị popup thông báo lỗi
- Nếu có → navigate sang danh sách TK

## 5. Ghi chú thiết kế
- Background: dark blue gradient (#0A1F44)
- Menu container: white, rounded corners ~16px
- Icon grid: 3 columns, 2 rows
- Popup overlay: blur background, centered white card

![SCR-GG-001](../ui/1200-gui-goc.png)
![SCR-GG-001-overlay](../ui/1207-gui-gocfail.png)
