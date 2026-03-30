# SCR-TAT-003 — My QR (Chi tiết)

## Tổng quan màn hình

| Thuộc tính | Giá trị |
|:---|:---|
| **screen_id** | SCR-TAT-003 |
| **screen_name_vi** | My QR |
| **screen_type** | detail |
| **domain** | banking |
| **artboard_count** | 2 (base + toast_saved) |
| **node_ids** | 142:17609, 142:17646 |

## Wireframe References

| File | Role | Mô tả |
|:---|:---|:---|
| `account-6.png` | base | Màn hình My QR — hiển thị mã QR, owner info, 2 CTAs |
| `account-7.png` | variant_toast_saved | Sau khi lưu ảnh — toast "Đã lưu ảnh mã QR thành công" |

## Mô tả chức năng

### Mục đích màn hình
Màn hình hiển thị mã VietQR cá nhân của khách hàng. Dùng để nhận tiền bằng cách chia sẻ QR. Đây là full-screen modal (không phải một tab/page độc lập) — được trigger từ tài khoản chi tiết hoặc menu.

### Các thành phần giao diện

| Component | Mô tả | Data |
|:---|:---|:---|
| Header | "My QR" (top-left) + X button (top-right) | Tiêu đề + close |
| Bank Logo | Co-opBank logo phía trên QR | Brand identity |
| QR Code | Mã QR dạng vuông (VietQR standard) | Generated từ account number |
| Owner Info | Tên khách hàng (bold caps) + số tài khoản + tên ngân hàng + chi nhánh | Account data |
| CTA Left | "Lưu ảnh" (outlined/light) | Save QR image to gallery |
| CTA Right | "Chia sẻ" (filled/dark blue) | Share via OS share sheet |
| Toast | "Đã lưu ảnh mã QR thành công" (bottom, dark with check) | Success feedback |

### Owner Information display

| Field | Value (demo) |
|:---|:---|
| Tên chủ tài khoản | NGUYEN HOANG KHAI |
| Số tài khoản | 1400205513145 |
| Ngân hàng | Ngân hàng Co-opBank - Chi nhánh Láng Hạ |

### Luồng tương tác

```
Entry: from SCR-TAT-002 / SCR-TAT-001 (My QR action)
Tap X (close) → navigate back to SCR-TAT-002
Tap "Lưu ảnh" → save QR to gallery → show toast (account-7.png)
Tap "Chia sẻ" → OS share sheet
Toast tự dismiss sau ~2-3 giây
```

### Trạng thái màn hình

| State | Trigger | Artboard |
|:---|:---|:---|
| Default | Entry | account-6.png |
| After save image | Tap "Lưu ảnh" | account-7.png (toast) |

## OCR Text Inventory

| Text | Role | Ghi chú |
|:---|:---|:---|
| My QR | header_title | |
| NGUYEN HOANG KHAI | account_owner_name | Tên in hoa |
| 1400205513145 | account_number_qr | Số TK |
| Ngân hàng Co-opBank - Chi nhánh Láng Hạ | bank_branch | |
| Lưu ảnh | button_secondary | Save to gallery |
| Chia sẻ | button_primary | Share via OS |
| Đã lưu ảnh mã QR thành công | toast | Variant: after save |

## Icon Inventory

| Icon | Location | Purpose |
|:---|:---|:---|
| close-x | Top-right header | Close modal, back to account detail |
| qr-code | Center | VietQR payment code display |
| co-opbank-logo | Above QR | Bank brand identity |
| check-toast | Toast icon | Success indicator |

## Consumer Notes (for AI downstream)

- **VietQR standard**: QR code theo chuẩn VietQR — scan được bởi các app ngân hàng/ví điện tử
- **Full-screen modal**: Layout không có bottom nav — dẫn đến close-only exit (nút X)
- **Save flow**: Lưu ảnh → toast (không interrupt main screen) → QR vẫn hiển thị
- **Share flow**: OS share sheet (không có custom UI trong Figma)
- **Typography owner**: Tên khách hàng ALL CAPS, bold, prominent — readable khi user chia sẻ chụp màn hình
- **Color CTA**: 2 buttons không đối xứng về hierarchy (Lưu ảnh outlined, Chia sẻ filled) — Chia sẻ là primary CTA
