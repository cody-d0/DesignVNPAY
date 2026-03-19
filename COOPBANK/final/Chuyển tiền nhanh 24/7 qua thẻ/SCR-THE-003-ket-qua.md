# SCR-THE-003 — Chuyển tiền nhanh 24/7 qua thẻ › Kết quả giao dịch

> `SCR-THE-003` · result · 1 artboard (CTNST_6)

## 1. User Flow

| Bước | Hành động | Kết quả |
|:-----|:----------|:--------|
| 1 | Sau xác thực OTP thành công | Hiển thị kết quả giao dịch |
| 2 | Xem chi tiết kết quả | Biên nhận giao dịch đầy đủ |
| 3 | Tap "Chia sẻ" | Share biên nhận qua apps |
| 4 | Tap "Lưu ảnh" | Save biên nhận ra gallery |
| 5 | Tap "Tạo giao dịch mới" | Quay lại SCR-THE-001 |
| 6 | Tap ic_backhome | Về trang chủ |

## 2. User Story

| US | Mô tả | AC |
|:---|:------|:---|
| US-006 | Người dùng nhận kết quả giao dịch thành công | AC1: Hiển thị trạng thái "Chuyển tiền thành công" + icon checkmark. AC2: Hiển thị đầy đủ chi tiết: thời gian, tên, số thẻ, ngân hàng, mã GD, nội dung. AC3: Hỗ trợ chia sẻ và lưu ảnh biên nhận. |

## 3. Mô tả màn hình

### Variant 1: Kết quả thành công (CTNST_6)
![Kết quả giao dịch](ui/chuyen-tien-nhanh-247-qua-the-6.png)

- Header: gradient xanh navy, title "Kết quả giao dịch", icon ic_backhome (home) trái
- Card biên nhận (receipt card, bo góc, nền trắng, shadow):
  - Logo Co-opBank + icon checkmark xanh
  - "Chuyển tiền thành công" (text xanh)
  - "20,000,000 VND" (text xanh lớn, bold)
  - Divider line
  - Chi tiết giao dịch (readonly rows):
    - Thời gian giao dịch: 22:00 15/02/2020
    - Tên người thụ hưởng: NGUYEN TUNG (chữ hoa)
    - Số thẻ thụ hưởng: 9704000012345678
    - Ngân hàng thụ hưởng: BIDV - Ngân hàng đầu tư và phát triển Việt Nam (multi-line)
    - Mã giao dịch: 0982312
    - Nội dung: Merry Christmas
  - Action row: icon "Chia sẻ" + icon "Lưu ảnh"
- CTA: "Tạo giao dịch mới" (full-width, xanh navy)

## 4. Database / API

| Entity | Fields | Constraints |
|:-------|:-------|:------------|
| TransactionResult | status, timestamp, beneficiary_name, card_number, bank_name, transaction_code, content, amount | readonly |

## 5. NFR

| Loại | Yêu cầu |
|:-----|:--------|
| Bảo mật | Mã giao dịch unique, không hiển thị thông tin nhạy cảm thừa |
| Hiệu năng | Hiển thị < 1s sau xác thực |
| Trải nghiệm | Chia sẻ/lưu ảnh 1-tap. Biên nhận đẹp, chuyên nghiệp |
