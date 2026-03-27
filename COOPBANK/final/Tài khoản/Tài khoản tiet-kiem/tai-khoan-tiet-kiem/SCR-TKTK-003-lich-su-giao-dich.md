# SCR-TKTK-003 — Tài khoản Tiết kiệm › Lịch sử Giao dịch

**Screen ID:** SCR-TKTK-003  
**Figma Nodes:** 154:188284 (1410), 154:188369 (1411), 154:188345 (1412), 154:188314 (1413)  
**Screen Type:** list  
**Domain:** Banking — Transaction History  
**Variants:** 4 (Initial | Date picker overlay | Empty state | Results list)

---

## 1. Overview

Màn hình lịch sử giao dịch của một tài khoản tiết kiệm cụ thể. Cho phép tra cứu giao dịch theo khoảng thời gian (1 tuần / 2 tuần / 1 tháng / Khác), phân loại theo tab (Toàn bộ / Tiền vào / Tiền ra), và xem danh sách giao dịch. Artboard 1411 chứa overlay bottom sheet "Chọn khoảng thời gian" với date picker.

---

## 2. User Story

> **Là** khách hàng Co-opBank,  
> **Tôi muốn** tra cứu lịch sử giao dịch tài khoản tiết kiệm theo khoảng thời gian và loại giao dịch,  
> **Để** kiểm soát dòng tiền và xác minh các giao dịch đã thực hiện.

---

## 3. Screen Content (OCR)

| # | Text | Category |
|---|------|----------|
| 1 | Lịch sử giao dịch | header_title |
| 2 | Tài khoản tiền gửi | section_header |
| 3 | 9099798712313123 | account_number |
| 4 | Số dư gốc hiện tại | label |
| 5 | 20,000,000 VND | value_amount |
| 6 | Tra cứu giao dịch | section_header |
| 7 | Khoảng thời gian tìm kiếm giới hạn trong vòng 03 tháng và thời gian tối đa cho phép tìm kiếm trong vòng 01 năm | info_text |
| 8 | 1 tuần | filter_option |
| 9 | 2 tuần | filter_option |
| 10 | 1 tháng | filter_option |
| 11 | Khác | filter_option |
| 12 | Toàn bộ | tab_label |
| 13 | Tiền vào | tab_label |
| 14 | Tiền ra | tab_label |
| 15 | 15:00 - 22/10/2018 | transaction_time |
| 16 | MB (270832) | transaction_id |
| 17 | HA chuyen... | transaction_desc |
| 18 | +2,000,000 VND | transaction_amount_in |
| 19 | Rut goc | transaction_desc |
| 20 | -2,000,000 VND | transaction_amount_out |
| 21 | Chọn khoảng thời gian | overlay_title |
| 22 | Từ ngày | label |
| 23 | 22/10/2018 | value_date |
| 24 | Đến ngày | label |
| 25 | 22/11/2018 | value_date |
| 26 | Tìm kiếm | cta_button |
| 27 | Không có kết quả tìm kiếm | empty_state |

**Icons:** caret-arrow-left (nav-back), home (nav-home), ic_acc_red (account icon, card), caret-arrow-down (filter button Khác), close-x (overlay close, top-right), calendar (date picker fields), drop_down_black (dropdown in overlay)

---

## 4. Variants

| Variant | Artboard | State |
|---------|----------|-------|
| Initial + Results | 1410 | Filter với 1 tuần selected, danh sách GD |
| Date picker overlay | 1411 | Bottom sheet "Chọn khoảng thời gian" open |
| Empty state | 1412 | Không tìm thấy kết quả |
| Results list | 1413 | Danh sách GD sau khi lọc |

---

## 5. Flow & Navigation

- **Entry:** Từ SCR-TKTK-002 (tap ic_report)
- **Exit:** Tap dòng GD → SCR-TKTK-004
- **Back:** caret-arrow-left → SCR-TKTK-002

---

## 6. UX Signal Notes

- Cảnh báo giới hạn tìm kiếm (03 tháng / 1 năm) dưới dạng paragraph — khó đọc
- Overlay date picker cần close-x affordance rõ ràng
- Empty state "Không có kết quả tìm kiếm" — không có gợi ý thử lại
- Transaction ID "HA chuyen..." bị truncate — không đủ thông tin nhận diện
- NFR: Số tài khoản 16 chữ số không có dấu phân cách — khó đọc
- Tabs Tiền vào/Tiền ra không highlight khi active (cần verify từ ảnh 1413)
