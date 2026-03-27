# SCR-TAT-001 — Tài khoản (Danh sách)

## Tổng quan màn hình

| Thuộc tính | Giá trị |
|:---|:---|
| **screen_id** | SCR-TAT-001 |
| **screen_name_vi** | Tài khoản |
| **screen_type** | list |
| **domain** | banking |
| **artboard_count** | 3 (base + toast + collapsed) |
| **node_ids** | 142:17453, 142:17467, 142:17809 |

## Wireframe References

| File | Role | Mô tả |
|:---|:---|:---|
| `account.png` | base | Danh sách tài khoản đầy đủ (2 thanh toán + 2 tiết kiệm + vay) |
| `account-2.png` | variant_toast | Sau khi copy số TK — toast "Đã chép số tài khoản thành công" |
| `account-8.png` | variant_collapsed | Chỉ 1 TK thanh toán (tiết kiệm + vay collapsed/hidden) |

## Mô tả chức năng

### Mục đích màn hình
Trang tổng hợp tài khoản ngân hàng của user. Hiển thị toàn bộ tài khoản của khách hàng phân theo 3 loại: Thanh toán, Tiết kiệm, Vay. Mỗi loại là một accordion có thể mở/đóng.

### Các thành phần giao diện

| Component | Mô tả | Data |
|:---|:---|:---|
| Header | "Tài khoản" + nút Back (←) + Refresh (↺) | Tiêu đề màn hình |
| Accordion — Tài khoản thanh toán | Header: tên nhóm + số lượng (2) + caret. Body: danh sách TK | 2 thẻ TK |
| Account Card | Số TK (truncated/masked), nhãn "Mặc định", copy icon, số dư khả dụng | Per account |
| Accordion — Tài khoản tiết kiệm | Tổng số dư, collapsed | 25,000,000 VND |
| Accordion — Tài khoản vay | Tổng số dư, collapsed | 11,000,000 VND |
| Toast | "Đã chép số tài khoản thành công" | Triggered by copy action |

### Luồng tương tác

```
User tap account card → navigate to SCR-TAT-002 (Thông tin tài khoản)
User tap caret-arrow-up → collapse/expand accordion section
User tap copy icon → copy account number → show toast
User tap refresh icon → refresh balance data
```

### Trạng thái màn hình

| State | Trigger | Mô tả |
|:---|:---|:---|
| Default | App load | 2 TK thanh toán, 2 tiết kiệm, 1 vay — đầy đủ |
| After Copy | Tap copy icon | Toast "Đã chép số tài khoản thành công" (bottom) |
| Collapsed (1 account) | Query/filter result | Chỉ hiện 1 TK thanh toán — variant 142:17809 |

## OCR Text Inventory

| Text | Role | Ghi chú |
|:---|:---|:---|
| Tài khoản | header_title | Page title |
| Tài khoản thanh toán (2) | section_header | Badge (2) = số lượng TK |
| Tổng số dư khả dụng | label | Aggregate balance label |
| 15,000,000 VND | value_money | Tổng 2 TK thanh toán |
| 12300123123000 | account_number | TK chính (mặc định) |
| Tài khoản mặc định | badge | Indicator TK mặc định |
| Số dư khả dụng | label | Per-account balance |
| 5,000,000 VND | value_money | Số dư TK 1 |
| 12300123123222 | account_number | TK phụ |
| Tài khoản tiết kiệm (2) | section_header | Savings section |
| 25,000,000 VND | value_money | Tổng tiết kiệm |
| Tài khoản vay | section_header | Loan section |
| 11,000,000 VND | value_money | Tổng vay |
| Đã chép số tài khoản thành công | toast | Variant: after copy |

## Icon Inventory

| Icon | Location | Purpose |
|:---|:---|:---|
| caret-arrow-up | Accordion header right | Collapse/expand section |
| copy-icon | Account number right | Copy to clipboard |
| refresh-icon | Header top-right | Refresh balance |

## Consumer Notes (for AI downstream)

- **Accordion pattern**: 3 sections — user có thể collapse từng section để focus
- **Copy UX**: tap copy → instant toast (không cần modal confirm)
- **Mặc định badge**: chỉ 1 TK thanh toán được đánh dấu là mặc định tại một thời điểm
- **Balance display**: Tổng số dư tại header mỗi section; chi tiết per-card hiển thị "Số dư khả dụng"
- **Navigation**: Tap vào card → drill down vào SCR-TAT-002
