# SCR-TT-003 — Thanh toán Vietlott › Kết quả giao dịch

> `SCR-TT-003` · result · 1 artboard

## 1. User Flow

| Bước | Hành động | Kết quả |
|------|-----------|---------|
| 1 | OTP xác thực thành công từ SCR-TT-002 | Hiển thị kết quả thành công |
| 2 | Nhấn "Chia sẻ" | Share biên nhận qua apps |
| 3 | Nhấn "Lưu ảnh" | Lưu screenshot biên nhận vào gallery |
| 4 | Nhấn "Tạo giao dịch mới" | Quay lại SCR-TT-001 |
| 5 | Nhấn home icon | Về trang chủ CoopBank |

## 2. User Story

**US-001:** Là khách hàng, tôi muốn thấy kết quả thanh toán Vietlott thành công rõ ràng.

- AC1: Hiển thị checkmark + "Thanh toán thành công" + số tiền (green)
- AC2: Chi tiết: thời gian GD, dịch vụ, mã TT, mã GD
- AC3: Actions: chia sẻ, lưu ảnh

**US-002:** Là khách hàng, tôi muốn tạo giao dịch mới hoặc về home.

- AC1: CTA "Tạo giao dịch mới" (outlined)
- AC2: Home icon ở header

## 3. Mô tả màn hình (Wireframe)

### Variants

| # | Variant | Ảnh | Mô tả |
|---|---------|-----|-------|
| 1 | Kết quả thành công | ![thanh-toan-vietlot](ui/thanh-toan-vietlot.png) | Card result trắng trên nền navy, checkmark, amount green, actions |

### Thành phần UI

| Thành phần | Loại | Mô tả |
|------------|------|-------|
| Header | Navigation bar | "Kết quả giao dịch", home icon trái |
| Result card | Card component | Logo CoopBank, checkmark circle xanh, "Thanh toán thành công", "50,000 VND" green |
| Detail rows | Label-value pairs | Thời gian GD, Dịch vụ, Mã TT, Mã GD |
| Action icons | Icon + label | "Chia sẻ" (share icon), "Lưu ảnh" (save icon) |
| CTA outlined | Button | "Tạo giao dịch mới" outlined style |

## 4. Database / Entities

| Entity | Fields | Constraints |
|--------|--------|-------------|
| TransactionResult | transaction_id, status, amount, timestamp, service, payment_code, reference_code | status IN ("success", "failed", "pending") |

## 5. NFR

- **Bảo mật:** Không hiển thị số TK nguồn trên result (đã mask)
- **Hiệu năng:** Page load < 1s sau OTP success
- **Trải nghiệm:** Peak-end positive — success prominent, green amount, checkmark animation
