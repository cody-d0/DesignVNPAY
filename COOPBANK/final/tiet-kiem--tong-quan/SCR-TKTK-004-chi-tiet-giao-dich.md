# SCR-TKTK-004 — Tài khoản Tiết kiệm › Chi tiết Giao dịch

**Screen ID:** SCR-TKTK-004  
**Figma Node:** 154:188273 (`1414 Tài khoản Tiết kiệm - Chi tiết GD`)  
**Screen Type:** detail  
**Domain:** Banking — Transaction Detail

---

## 1. Overview

Màn hình chi tiết một giao dịch cụ thể trong tài khoản tiết kiệm. Hiển thị các thông tin định danh giao dịch: mã GD, ngày giờ giao dịch, số tiền và nội dung. Màn hình đơn giản, chỉ có 1 section thông tin.

---

## 2. User Story

> **Là** khách hàng Co-opBank,  
> **Tôi muốn** xem chi tiết đầy đủ một giao dịch tiết kiệm cụ thể,  
> **Để** xác minh tính chính xác và lưu trữ thông tin giao dịch nếu cần.

---

## 3. Screen Content (OCR)

| # | Text | Category |
|---|------|----------|
| 1 | Chi tiết giao dịch | header_title |
| 2 | Thông tin giao dịch | section_header |
| 3 | Số giao dịch | label |
| 4 | 4153-87675 | transaction_id |
| 5 | Ngày giao dịch | label |
| 6 | 30/12/2020 10:20 | value_datetime |
| 7 | Số tiền giao dịch | label |
| 8 | 2,000,000 VND | value_amount |
| 9 | Nội dung giao dịch | label |
| 10 | Tien tiet kiem | value_text |

**Icons:** caret-arrow-left (nav-back, top-left), home (nav-home, top-right), savings-logo-red (decoration, section-header-left)

---

## 4. Flow & Navigation

- **Entry:** Từ SCR-TKTK-003 (tap transaction row)
- **Back:** caret-arrow-left → SCR-TKTK-003
- **Home:** home icon → Home screen

---

## 5. UX Signal Notes

- Màn hình cực kỳ thưa — chỉ 4 fields thông tin
- "Nội dung giao dịch: Tien tiet kiem" — không có dấu tiếng Việt, thiếu chuyên nghiệp
- Không có nút "Chia sẻ" hoặc "Tải biên lai" — thiếu tính năng quan trọng
- Không có trạng thái giao dịch (thành công/thất bại/đang xử lý)
- Không có icon hoặc màu sắc phân biệt loại GD (vào/ra)
- NFR: Thiếu chức năng export/share receipt — banking standard
