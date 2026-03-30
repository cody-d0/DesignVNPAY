# SCR-TKTK-001 — Tài khoản Tiết kiệm › Danh sách

**Screen ID:** SCR-TKTK-001  
**Figma Node:** 154:188229 (`1400 Tài khoản Tiết kiệm`)  
**Screen Type:** list  
**Domain:** Banking — Savings Account

---

## 1. Overview

Màn hình danh sách tổng quan tài khoản của người dùng Co-opBank, gộp tất cả loại tài khoản (Thanh toán, Tiết kiệm, Vay) thành 1 view. Phần "Tài khoản tiết kiệm" hiển thị ở trạng thái mở rộng, liệt kê từng sổ tiết kiệm kèm số dư gốc và ngày đáo hạn.

---

## 2. User Story

> **Là** khách hàng Co-opBank Mobile Banking,  
> **Tôi muốn** xem tổng quan tất cả tài khoản của mình (thanh toán, tiết kiệm, vay),  
> **Để** nắm bắt nhanh số dư và trạng thái tài chính hiện tại.

---

## 3. Screen Content (OCR)

| # | Text | Category |
|---|------|----------|
| 1 | Tài khoản | header_title |
| 2 | Tài khoản thanh toán (2) | section_header |
| 3 | Tổng số dư khả dụng | label |
| 4 | 15,000,000 VND | value_amount |
| 5 | Tài khoản tiết kiệm (2) | section_header |
| 6 | Tổng số dư gốc | label |
| 7 | 25,000,000 VND | value_amount |
| 8 | 12300123123000 | account_number |
| 9 | Ngày đến hạn: 20/09/2021 | label_date |
| 10 | Tiền gửi tích luỹ | product_type |
| 11 | Số dư gốc hiện tại | label |
| 12 | 5,000,000 VND | value_amount |
| 13 | 12300123123000 | account_number |
| 14 | Ngày đến hạn: 20/09/2021 | label_date |
| 15 | Tiền gửi trực tuyến lãi cuối kỳ | product_type |
| 16 | Số dư gốc hiện tại | label |
| 17 | 20,000,000 VND | value_amount |
| 18 | Tài khoản vay | section_header |
| 19 | Tổng số dư khả dụng | label |
| 20 | 11,000,000 VND | value_amount |

**Icons:** caret-arrow-left (nav-back, top-left), caret-arrow-down (collapse section, right), caret-arrow-up (expand section, right), ic_acc_red (account decoration, card-left)

---

## 4. Flow & Navigation

- **Entry:** Từ Home screen tab "Tài khoản"
- **Exit:** Tap vào thẻ tài khoản tiết kiệm → SCR-TKTK-002 (Thông tin TK)
- **Back:** caret-arrow-left → màn hình trước

---

## 5. UX Signal Notes

- Section headers dạng accordion (expand/collapse) — `caret-arrow-down/up`
- Số dư tổng ở header section, số dư từng tài khoản con ở card
- Ngày đến hạn nổi bật trong từng card tiết kiệm
- Không có CTA action trực tiếp từ list (phải vào detail)
