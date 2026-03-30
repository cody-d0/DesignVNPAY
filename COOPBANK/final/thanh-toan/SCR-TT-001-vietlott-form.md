# SCR-TT-001 — Thanh toán Vietlott › Form nhập thông tin

> `SCR-TT-001` · form · 1 artboard

## 1. User Flow

| Bước | Hành động | Kết quả |
|------|-----------|---------|
| 1 | User chọn dịch vụ "Mua xổ số Vietlott SMS" từ SDK | Chuyển sang màn thanh toán Vietlott |
| 2 | Xem tài khoản nguồn (tự động chọn TK mặc định) | Hiển thị số TK + số dư khả dụng |
| 3 | Tap chevron dropdown TK nguồn (nếu có nhiều TK) | Hiển thị danh sách TK để chọn |
| 4 | Xem thông tin thanh toán (Dịch vụ, Mã thanh toán, Số tiền) | Dữ liệu từ SDK, read-only |
| 5 | Nhấn "Tiếp tục" | Chuyển sang SCR-TT-002 (Xác nhận giao dịch) |
| 6 | Nhấn back arrow | Quay lại SDK |
| 7 | Nhấn home icon | Về trang chủ CoopBank |

## 2. User Story

**US-001:** Là khách hàng, tôi muốn xem tổng hợp thông tin thanh toán Vietlott từ SDK để xác nhận trước khi tiếp tục.

- AC1: Hiển thị tài khoản nguồn với số TK + số dư khả dụng
- AC2: Hiển thị thông tin dịch vụ (Mua xổ số Vietlott SMS)
- AC3: Hiển thị mã thanh toán và số tiền giao dịch
- AC4: Nút "Tiếp tục" chuyển sang xác nhận giao dịch

## 3. Mô tả màn hình (Wireframe)

### Variants

| # | Variant | Ảnh | Mô tả |
|---|---------|-----|-------|
| 1 | Form thanh toán Vietlott | ![thanh-toan-vietlot](ui/thanh-toan-vietlot.png) | Header navy, account card blue, section thông tin thanh toán, CTA "Tiếp tục" |

### Thành phần UI

| Thành phần | Loại | Mô tả |
|------------|------|-------|
| Header | Navigation bar | "Thanh toán mua xổ số Vietlott", back arrow trái, home icon phải |
| Account card | Card component | Logo CoopBank, số TK 9099798712313123, "Số dư khả dụng: 20,000,000 VND", chevron dropdown |
| Section header | Label | "Thông tin thanh toán" với icon cảnh báo đỏ |
| Info row: Dịch vụ | Label-value pair | "Dịch vụ" — "Mua xổ số Vietlott SMS" |
| Info row: Mã thanh toán | Label-value pair | "Mã thanh toán" — "123123" |
| Info row: Số tiền | Label-value pair | "Số tiền giao dịch" — "50,000 VND" |
| CTA primary | Button | "Tiếp tục" full-width, sticky bottom |

## 4. Database / Entities

| Entity | Fields | Constraints |
|--------|--------|-------------|
| VietlottPayment | id, service_type, payment_code, amount, source_account_id | amount > 0, service_type = "Vietlott SMS" |
| SourceAccount | id, account_number, available_balance, bank_logo | available_balance >= amount |

## 5. NFR

- **Bảo mật:** Số TK hiển thị đầy đủ (in-app, user đã authen)
- **Hiệu năng:** SDK prefill data — không cần API call thêm
- **Trải nghiệm:** Read-only form, user chỉ review + chọn TK nguồn
