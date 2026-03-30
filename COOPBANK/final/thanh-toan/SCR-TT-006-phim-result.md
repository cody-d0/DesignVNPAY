# SCR-TT-006 — Thanh toán vé xem phim › Kết quả giao dịch

> `SCR-TT-006` · result · 1 artboard

## 1. User Flow

| Bước | Hành động | Kết quả |
|------|-----------|---------|
| 1 | OTP success từ SCR-TT-005 | Hiển thị kết quả |
| 2 | Nhấn "Chia sẻ" | Share biên nhận |
| 3 | Nhấn "Lưu ảnh" | Lưu screenshot |
| 4 | Nhấn "Tạo giao dịch mới" | Quay lại flow |
| 5 | Nhấn home | Về trang chủ |

## 2. User Story

**US-001:** Là khách hàng, tôi muốn thấy kết quả thanh toán vé xem phim thành công.

- AC1: Checkmark + "Thanh toán thành công" + 100,000 VND (green)
- AC2: Chi tiết: thời gian, dịch vụ, nhà cung cấp (CGV), mã TT, tên KH, mã GD
- AC3: Lưu ý mã đặt chỗ gửi email/SMS trong 30 phút
- AC4: Hotline hỗ trợ (hiện tại placeholder XXXXX)

## 3. Mô tả màn hình (Wireframe)

### Variants

| # | Variant | Ảnh | Mô tả |
|---|---------|-----|-------|
| 1 | Kết quả thành công | ![1003thanh-toan-ve-xem-phim](ui/1003thanh-toan-ve-xem-phim.png) | Result card, 6 detail rows, lưu ý vàng, CTA outlined |

### Thành phần UI

| Thành phần | Loại | Mô tả |
|------------|------|-------|
| Header | Navigation bar | "Kết quả giao dịch", home icon |
| Result card | Card | CoopBank logo, checkmark, "Thanh toán thành công", 100K VND green |
| Detail rows | 6 label-value | Thời gian, Dịch vụ, Nhà CC, Mã TT, Tên KH, Mã GD |
| Actions | Icon + label | "Chia sẻ", "Lưu ảnh" |
| Notice | Warning box | Lưu ý mã đặt chỗ + tổng đài XXXXX |
| CTA outlined | Button | "Tạo giao dịch mới" |

## 4. Database / Entities

| Entity | Fields | Constraints |
|--------|--------|-------------|
| MovieResult | transaction_id, status, amount, timestamp, service, provider, payment_code, customer_name, reference_code, booking_code_sent | status = "success" |

## 5. NFR

- **Bảo mật:** Mã đặt chỗ gửi riêng (email/SMS), không hiển thị trên result
- **Trải nghiệm:** Hotline "XXXXX" = placeholder, cần số thật
- **Peak-end:** Kết thúc positive — success card + actions rõ ràng
