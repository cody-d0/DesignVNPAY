# SCR-TAT-002 — Thông tin tài khoản (Chi tiết)

## Tổng quan màn hình

| Thuộc tính | Giá trị |
|:---|:---|
| **screen_id** | SCR-TAT-002 |
| **screen_name_vi** | Thông tin tài khoản |
| **screen_type** | detail |
| **domain** | banking |
| **artboard_count** | 4 (base_default + base_toast + overlay_modal + loading) |
| **node_ids** | 142:17482, 142:17506, 142:17583, 142:17820 |

## Wireframe References

| File | Role | Mô tả |
|:---|:---|:---|
| `account-3.png` | base_with_toast | Màn hình chi tiết + badge "Tài khoản thanh toán mặc định" (đã set mặc định) |
| `account-4.png` | base_default | Màn hình chi tiết — trạng thái thông thường (radio chưa active) |
| `account-5.png` | overlay_confirm_modal | Modal "Thông báo" xác nhận đặt TK mặc định (nền mờ) |
| `account-9.png` | loading_state | Loading spinner (đang tải dữ liệu TK) |

## Mô tả chức năng

### Mục đích màn hình
Màn hình chi tiết tài khoản thanh toán. Hiển thị toàn bộ thông tin: chủ TK, số dư, lãi suất, thấu chi. Cho phép đặt làm tài khoản mặc định. Bottom nav 4 chức năng chính (lịch sử, chuyển tiền, nạp tiền, thanh toán).

### Các thành phần giao diện

| Component | Mô tả | Data |
|:---|:---|:---|
| Header | "Thông tin tài khoản" + Back (←) + Home (⌂) | Tiêu đề + nav icons |
| Badge TK mặc định | Xanh lá, dấu tick — "Tài khoản thanh toán mặc định" | State: đã set mặc định |
| Radio "Đặt làm mặc định" | Row action — "Đặt làm tài khoản thanh toán mặc định" | State: chưa set |
| Account Type Section | "Tài khoản thanh toán" + wallet icon + caret-right | Selector |
| Info Rows | Label-value pairs, text biểu ticket | 12 fields |
| Modal Overlay | "Thông báo" + body + Hủy + Xác nhận | Confirm dialog |
| Loading Spinner | Circle spinner dưới header | Loading state |
| Bottom Nav | 4 tabs: Lịch sử / Chuyển tiền / Nạp tiền / Thanh toán | Persistent nav với badge đỏ |

### Thông tin chi tiết tài khoản (Info Rows)

| Label | Value (demo) | Kiểu |
|:---|:---|:---|
| Tên chủ tài khoản | HA NGUYEN QUANG | Tên khách hàng |
| Số tài khoản | 012547288 | Số TK |
| Chi nhánh mở | Lang Ha | Chi nhánh |
| Số dư thực tế | 12,000,000 VND | Số dư |
| Số dư khả dụng | 12,000,000 VND | Số dư |
| Số tiền phong tòa | 0 VND | Phong tỏa |
| Lãi cộng dồn | 215 VND | Lãi |
| Lãi suất tài khoản thanh toán | 0.1% | Lãi suất |
| Hạn mức thấu chi | 0 VND | Thấu chi |
| Lãi thấu chi | 0 VND | Thấu chi |
| Lãi suất thấu chi | 0.1% | Lãi suất thấu chi |
| Ngày mở tài khoản | 20/02/2019 | Ngày mở |

*Lưu ý: Screen cắt dưới cùng (scrollable) — có thể có thêm fields.*

### Modal Overlay: Xác nhận đặt TK mặc định

| Element | Content |
|:---|:---|
| Modal title | "Thông báo" |
| Body | "Quý khách có muốn đặt tài khoản 12332300011 làm tài khoản thanh toán mặc định?" |
| Button left | "Hủy" (secondary) |
| Button right | "Xác nhận" (primary/blue) |
| Background | Nền mờ (dimmed overlay) |

### Luồng tương tác

```
Tap "Đặt làm TK mặc định" → open modal (account-5.png)
Modal → Hủy → dismiss modal → return to account-4.png
Modal → Xác nhận → set default → navigate/update → account-3.png (with badge)
Tap caret-right gần account type → switch account
Tap bottom-nav "Lịch sử giao dịch" → SCR-TAT-004
Tap home icon → navigate to Home
Loading spinner (account-9.png): radio unchecked, spinner above = data loading
```

### Trạng thái màn hình

| State | Trigger | Artboard |
|:---|:---|:---|
| Default (not default account) | Entry from SCR-TAT-001 | account-4.png |
| Default account | After set default / already default | account-3.png |
| Confirm modal open | Tap "Đặt làm mặc định" | account-5.png |
| Loading | Data fetching | account-9.png |

## OCR Text Inventory

| Text | Role | Ghi chú |
|:---|:---|:---|
| Thông tin tài khoản | header_title | |
| Tài khoản thanh toán mặc định | badge_success | Variant: account-3 |
| Đặt làm tài khoản thanh toán mặc định | action_row | CTA to set default |
| Tài khoản thanh toán | section_header | |
| Tên chủ tài khoản | label | |
| HA NGUYEN QUANG | value_name | |
| Số tài khoản | label | |
| 012547288 | value_account_number | |
| Chi nhánh mở | label | |
| Lang Ha | value_branch | |
| Số dư thực tế | label | |
| 12,000,000 VND | value_money | |
| Số dư khả dụng | label | |
| 12,000,000 VND | value_money | |
| Số tiền phong tòa | label | |
| 0 VND | value_money | |
| Lãi cộng dồn | label | |
| 215 VND | value_money | |
| Lãi suất tài khoản thanh toán | label | |
| 0.1% | value_percent | |
| Hạn mức thấu chi | label | |
| 0 VND | value_money | |
| Lãi thấu chi | label | |
| 0 VND | value_money | |
| Lãi suất thấu chi | label | |
| 0.1% | value_percent | |
| Ngày mở tài khoản | label | |
| 20/02/2019 | value_date | |
| Thông báo | modal_title | Overlay |
| Quý khách có muốn đặt tài khoản 12332300011... | modal_body | Overlay |
| Hủy | button_secondary | Modal |
| Xác nhận | button_primary | Modal |
| Lịch sử giao dịch | bottom_nav_label | |
| Chuyển tiền | bottom_nav_label | |
| Nạp tiền | bottom_nav_label | |
| Thanh toán | bottom_nav_label | |

## Icon Inventory

| Icon | Location | Purpose |
|:---|:---|:---|
| wallet | Account type header | Account type indicator |
| caret-arrow-right | Account row right | Switch between accounts |
| radio-button | "Đặt làm mặc định" row | Toggle default state |
| spinner | Header below (loading state) | Loading indicator |
| home | Header top-right | Navigate to home |
| history-icon | Bottom nav | Transaction history |
| transfer-icon | Bottom nav | Money transfer |
| topup-icon | Bottom nav | Top-up |
| payment-icon | Bottom nav | Payment |

## Consumer Notes (for AI downstream)

- **Thông tin theo trục đứng**: 12 label-value pairs — dài, scrollable, không có phân section rõ ràng
- **Modal pattern**: "Thông báo" = iOS-style alert dialog với 2 buttons ngang
- **Default account flow**: Radio tap → confirm modal → server call → badge hiển thị
- **Bottom nav badges**: Các icon bottom nav có badge đỏ (notification count)
- **Scrollable content**: Screen cắt ("Ngày mở tài khoản" là field cuối visible) — thực tế có thể có thêm fields
- **Loading state**: Spinner xuất hiện phía trên nội dung (giữa header và content) khi đang load
