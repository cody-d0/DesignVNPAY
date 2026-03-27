# SCR-TKTK-002 — Tài khoản Tiết kiệm › Chi tiết tài khoản

**Screen ID:** SCR-TKTK-002  
**Figma Nodes:** 154:188243 (1401), 154:188177 (1402), 154:188202 (1403)  
**Screen Type:** detail  
**Domain:** Banking — Savings Account Detail  
**Variants:** 3 (Tiền gửi tích lũy default | Tích lũy linh động | Tiền gửi lĩnh lãi định kỳ)

---

## 1. Overview

Màn hình chi tiết thông tin một tài khoản tiết kiệm cụ thể, hiển thị đầy đủ thông số sản phẩm: thông tin khách hàng, loại sản phẩm, kỳ hạn, lãi suất, số dư gốc, ngày đáo hạn, hình thức tích lũy và phương thức tất toán. Có 3 biến thể tương ứng với các loại sản phẩm tiết kiệm khác nhau. CTA bottom bar thay đổi theo loại sản phẩm.

---

## 2. User Story

> **Là** khách hàng Co-opBank,  
> **Tôi muốn** xem toàn bộ thông tin chi tiết tài khoản tiết kiệm của mình,  
> **Để** kiểm tra kỳ hạn, lãi suất, số dư và thực hiện các thao tác (tất toán, thay đổi thông tin, xem lịch sử GD).

---

## 3. Screen Content (OCR)

| # | Text | Category |
|---|------|----------|
| 1 | Thông tin tài khoản | header_title |
| 2 | Tài khoản tiết kiệm | sub_header |
| 3 | Tên chủ tài khoản | label |
| 4 | HA NGUYEN QUANG | value_name |
| 5 | Số tài khoản | label |
| 6 | 012547288 | account_number |
| 7 | Chi nhánh mở/PGD | label |
| 8 | CN Lang Ha | value |
| 9 | Loại sản phẩm | label |
| 10 | Tiền gửi tích lũy | product_type |
| 11 | Kỳ hạn | label |
| 12 | 1 tháng | value |
| 13 | Ngày mở ban đầu | label |
| 14 | 15/03/2024 | value_date |
| 15 | Ngày hiệu lực | label |
| 16 | 15/03/2024 | value_date |
| 17 | Ngày đáo hạn | label |
| 18 | 15/03/2025 | value_date |
| 19 | Số dư gốc ban đầu | label |
| 20 | 10,000,000 VND | value_amount |
| 21 | Số dư gốc hiện tại | label |
| 22 | 10,000,000 VND | value_amount |
| 23 | Số tiền phong tỏa | label |
| 24 | 0 VND | value_amount |
| 25 | Lãi suất cộng dồn | label |
| 26 | 213 VND | value_amount |
| 27 | Hình thức tích lũy | label |
| 28 | Tích lũy định kỳ tự động | value |
| 29 | Chu kỳ tích lũy | label |
| 30 | 1 tháng | value |
| 31 | Ngày tích lũy tiếp theo | label |
| 32 | 15/05/2024 | value_date |
| 33 | Số tiền tích lũy định kỳ | label |
| 34 | 213 VND | value_amount |
| 35 | Tài khoản trích tiền | label |
| 36 | 1231231232 | account_number |
| 37 | Lãi suất | label |
| 38 | 0.1% | value_rate |
| 39 | Trạng thái tích lũy | label |
| 40 | Hoạt động | value_status |
| 41 | Phương thức đáo hạn | label |
| 42 | Đáo hạn cuối kỳ | value |
| 43 | Tài khoản nhận gốc lãi | label |
| 44 | 1231231232 | account_number |
| 45 | Phương thức tất toán/ rút gốc | label |
| 46 | Tất toán/ rút gốc online | value |
| 47 | Tất toán tiền gửi trực tuyến | action_button |
| 48 | Thay đổi t.tin tích lũy định kỳ | action_button |
| 49 | Gửi gốc thêm tiền gửi tích lũy | action_button |
| 50 | Rút gốc một phần | action_button |
| 51 | Lịch sử giao dịch | action_button |
| 52 | Chức năng khác | action_button |
| 53 | Tiền gửi lĩnh lãi định kỳ hàng tháng | product_type |
| 54 | 2 tháng | value |

**Icons:** caret-arrow-left (back, top-left), home (top-right), saving-red-icon (decoration, content-top), ic_tattoan (bottom-bar-1), ic_edit/ic_plus/ic_rutgoc (bottom-bar-2 — varies by variant), ic_report (bottom-bar-3), morefunction (bottom-bar-4)

---

## 4. Variants

| Variant | Artboard | Loại SP | CTA riêng |
|---------|----------|---------|-----------|
| Default | 1401 | Tiền gửi tích lũy | Thay đổi t.tin tích lũy định kỳ |
| Linh động | 1402 | Tiền gửi tích lũy (linh động) | Gửi gốc thêm |
| Lĩnh lãi | 1403 | Tiền gửi lĩnh lãi định kỳ hàng tháng | Rút gốc một phần |

---

## 5. Flow & Navigation

- **Entry:** Từ SCR-TKTK-001 (tap account card)
- **Exit (LSGD):** ic_report (bottom-bar) → SCR-TKTK-003
- **Back:** caret-arrow-left → SCR-TKTK-001
- **Home:** home icon → Home screen

---

## 6. UX Signal Notes

- Danh sách trường rất dài — cần scroll nhiều
- CTA bottom bar cố định — không bị scroll ẩn
- Icon `ic_report` là trigger key → LSGD
- Tên viết tắt "Thay đổi t.tin tích lũy định kỳ" — thiếu rõ ràng
- "Lãi suất cộng dồn" = 213 VND cho tài khoản 10M — có vẻ là số quá nhỏ (test data)
- NFR: Sensitive data (số TK, tên chủ TK) không có masking
