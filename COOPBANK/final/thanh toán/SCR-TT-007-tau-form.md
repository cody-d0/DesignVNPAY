# SCR-TT-007 — Thanh toán vé tàu › Form nhập thông tin

> `SCR-TT-007` · form · 2 artboards (chiều đi only + khứ hồi)

## 1. User Flow

| Bước | Hành động | Kết quả |
|------|-----------|---------|
| 1 | User đặt vé tàu từ SDK (ga, ngày, tàu, ghế) | Chuyển sang thanh toán |
| 2 | Xem TK nguồn | TK + số dư |
| 3 | Xem thông tin thanh toán (Tổng tiền, Giảm, Tổng TT) | Read-only |
| 4 | Xem thông tin chiều đi (Ga, ngày giờ, chuyến, ghế, số vé) | From SDK |
| 5 | (Khứ hồi) Xem thông tin chiều về | Variant 2 only |
| 6 | Xem thông tin khách hàng (Tên, SĐT, Email) | Prefilled |
| 7 | Nhấn "Tiếp tục" | → SCR-TT-008 |

## 2. User Story

**US-001:** Là khách hàng, tôi muốn xem tổng hợp thông tin đặt vé tàu trước khi thanh toán.

- AC1: Thông tin thanh toán: Tổng tiền, Giảm, Tổng TT
- AC2: Thông tin chiều đi: Ga khởi hành → Ga đến, ngày giờ, mã tàu, ghế, số vé
- AC3: (Khứ hồi) Thông tin chiều về: tương tự chiều đi
- AC4: Thông tin khách hàng: Tên NGUYEN VAN A, SĐT, Email

## 3. Mô tả màn hình (Wireframe)

### Variants

| # | Variant | Ảnh | Mô tả |
|---|---------|-----|-------|
| 1 | Chiều đi only (1071px) | ![thanh-toan-ve-tau-1](ui/thanh-toan-ve-tau-1.png) | TK nguồn, TT thanh toán, chiều đi (7 rows), KH (3 rows) |
| 2 | Khứ hồi (1407px) | ![thanh-toan-ve-tau-2](ui/thanh-toan-ve-tau-2.png) | Thêm section chiều về (7 rows), total ~20 info rows |

### Thành phần UI

| Thành phần | Loại | Mô tả |
|------------|------|-------|
| Header | Navigation bar | "Thanh toán vé tàu", back + home |
| Account card | Card | Logo, TK, số dư 20M VND, chevron |
| Section: Thông tin TT | Info | Tổng tiền 20K, Giảm 100K, Tổng TT 80K (*data mâu thuẫn*) |
| Section: Chiều đi | Info (red header) | Ga KH: Hà Nội, Ga đến: Sài Gòn, 1/08/2025 19:30, SE1, Ghế 5+6 Toa 1, 2 vé |
| Section: Chiều về | Info (red header) | Chỉ variant 2: Sài Gòn → Sài Gòn (*data copy lỗi*) |
| Section: Thông tin KH | Info (red header) | NGUYEN VAN A, 090619882, email |
| CTA | Button | "Tiếp tục" sticky bottom |

## 4. Database / Entities

| Entity | Fields | Constraints |
|--------|--------|-------------|
| TrainPayment | id, total, discount, final_amount, customer_name, phone, email | final = total - discount, total >= discount |
| TrainTrip | trip_id, departure_station, arrival_station, datetime, train_code, seats, ticket_count, direction | direction IN ("outbound", "return") |

## 5. NFR

- **Bảo mật:** Dữ liệu session-scoped từ SDK
- **Hiệu năng:** Long scroll (1407px max) — cần collapsible sections
- **Data Quality:** "Tổng tiền: 20,000" < "Giảm: 100,000" = mâu thuẫn logic
- **Data Quality:** Chiều về ga đến = "Sài Gòn" (should be "Hà Nội") = copy error
