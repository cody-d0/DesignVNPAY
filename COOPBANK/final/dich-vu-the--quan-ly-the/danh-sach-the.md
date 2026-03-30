# SCR-THE-001 · Dịch vụ thẻ › Danh sách thẻ

## Screen Identity
- **screen_id**: SCR-THE-001
- **screen_name**: danh-sach-the
- **screen_type**: list (card_management_hub)
- **product**: CoopBank Mobile Banking
- **module**: Dịch Vụ Thẻ / Thẻ
- **flow_stage**: entry
- **wireframe_images**: [`ui/danh-sach-the-1.png`](ui/danh-sach-the-1.png), [`ui/danh-sach-the-5-hoat-yong.png`](ui/danh-sach-the-5-hoat-yong.png), [`ui/danh-sach-the-6-yang-khoa.png`](ui/danh-sach-the-6-yang-khoa.png), [`ui/danh-sach-the-7-cho-kich-hoat.png`](ui/danh-sach-the-7-cho-kich-hoat.png), [`ui/danh-sach-the-8-the-phu.png`](ui/danh-sach-the-8-the-phu.png), [`ui/danh-sach-the-12-trong.png`](ui/danh-sach-the-12-trong.png), [`ui/danh-sach-the-mo-rong-1.png`](ui/danh-sach-the-mo-rong-1.png), [`ui/danh-sach-the-xac-thuc-otp.png`](ui/danh-sach-the-xac-thuc-otp.png), [`ui/danh-sach-the-thong-tin-the-2.png`](ui/danh-sach-the-thong-tin-the-2.png)

---

## Screen Purpose
Màn hình trung tâm quản lý thẻ tín dụng Co-opBank. Người dùng xem tổng quan tất cả thẻ (tối đa 35 thẻ theo carousel), thực hiện quick actions, và xem thông tin tóm tắt thẻ đang chọn. Entry point cho các nghiệp vụ thẻ: sao kê, thanh toán, lịch sử, cài đặt PIN.

---

## User Story
> "Là khách hàng có thẻ tín dụng Co-opBank, tôi muốn xem nhanh trạng thái thẻ và điều hướng đến các nghiệp vụ liên quan từ một màn hình trung tâm."

---

## Information Architecture

### Header
- **Back navigation**: `back_white` (icon) → quay lại màn hình trước
- **Screen title**: "Dịch vụ thẻ"

### Card Carousel Section
- **Tab selector**: "Thẻ tín dụng" `[3]` (badge số lượng thẻ)
- **Card visual**: Card artwork Co-opBank với logo + Mastercard badge
- **Carousel navigation**: `<` `>` arrows (nếu có nhiều thẻ)
- **Indicator dots**: Position trong carousel

### Quick Action Grid (2-row layout)
| Hàng 1 | Label | Trigger |
|--------|-------|---------|
| `ic_sao_ke` | Sao kê | (chưa xác định destination) |
| `ic_thanh_toan` | Thanh toán thẻ tín dụng | (chưa xác định) |
| `ic_tthd_line` | Lịch sử giao dịch | → SCR-THE-003 |
| `ic_soft_line` | Cài đặt PIN thẻ | (chưa xác định) |

### Card Info Section (collapsed/expanded states)
| Field | Value Example | Visibility |
|-------|--------------|------------|
| `ic_money_tit` + "Thông tin thẻ" | — | Section header |
| Số thẻ | `1234 **** **** 1121` | Masked + eye toggle |
| Tên chủ thẻ | `NGUYEN VAN A` | Visible |
| Loại thẻ | `Thẻ chính ⭐` | Badge |
| Trạng thái thẻ | `Hoạt động` (green) | Status badge |
| Hạn mức khả dụng | `******** VND` | Masked + eye toggle |

**Expand toggle**: Mũi tên `∨` để mở rộng thêm thông tin

### Primary CTA
- **"Chi tiết thẻ"** button (full-width, blue) → SCR-THE-002

---

## Screen States & Variants

### State 1: Thẻ hoạt động (default)
- Trạng thái thẻ: `Hoạt động` (badge xanh lá)
- Hiển thị đầy đủ quick actions 4 items

### State 2: Thẻ khoá bởi khách hàng
- Trạng thái thẻ: `Khoá bởi khách hàng` (badge đỏ/hồng)
- Quick action grid: chỉ hiện 3 items (không có Thanh toán tín dụng)

### State 3: Chờ kích hoạt
- CTA thay thành: **"Kích hoạt thẻ"** (thay vì "Chi tiết thẻ")
- Quick action grid: chỉ hiện "Thông tin thẻ" và "Kích hoạt thẻ"

### State 4: Thẻ phụ (sub-card)
- Loại thẻ badge: `Thẻ phụ` (không có star icon)
- Quick action grid: chỉ 2 items: `Lịch sử giao dịch` + `Cài đặt PIN thẻ`

### State 5: Trạng thái trống (chưa có thẻ)
- Empty state: "Quý khách chưa có thẻ tín dụng tại Co-opBank. Vui lòng mở thẻ để sử dụng."
- No quick actions, no card info section

### State 6: Mở rộng (expanded info card)
- Quick action grid hiển thị thêm row `∨` expand
- Xem thêm thông tin thẻ bên dưới

---

## Overlays & Bottom Sheets

### Overlay 1: Xác thực giao dịch (PIN Auth)
**Trigger**: trigger từ action yêu cầu xác thực
- **Title**: "Xác thực giao dịch"
- **Instruction**: "Quý khách vui lòng nhập mã PIN thẻ để xác thực giao dịch"
- **Warning**: "Lưu ý: PIN thẻ sẽ bị khóa nếu Qúy khách nhập sai PIN 5 lần liên tiếp"
- **Input**: 6-cell PIN input (masked)
- **Keyboard**: Custom numeric keypad (0-9 + xoá)
- **CTA**: "Xác nhận"

### Overlay 2: Thông tin thẻ (Card Info Sheet)
**Trigger**: tap vào "Thông tin thẻ" section hoặc eye toggle full card number
- **Title**: "Thông tin thẻ" + close `×`
- **Số thẻ**: `1234 5678 9101 1121` (full, unmasked) + copy icon
- **Tên chủ thẻ**: `NGUYEN VAN A`
- **Ngày phát hành**: `01/2026`
- **Ngày hết hạn**: `01/2030`

**Toast sau copy**: "Sao chép số thẻ thành công" (success toast, bottom)

---

## Navigation Flows
- `back_white` → previous screen (Home / Dịch vụ ngân hàng)
- **"Chi tiết thẻ"** → SCR-THE-002 (Thông tin thẻ full)
- **"Lịch sử giao dịch"** quick action → SCR-THE-003
- **"Sao kê"** → (ngành Sao kê - chưa định nghĩa)
- **"Thanh toán thẻ tín dụng"** → (flow Thanh toán - ngoài scope)
- **"Cài đặt PIN thẻ"** → (flow Cài đặt PIN - ngoài scope)
- **[Overlay] Xác thực giao dịch** → self, dismiss → remain on SCR-THE-001

---

## Missing Data / Gaps
- ⚠️ **"Sao kê"** destination không được xác định trong flow
- ⚠️ **"Thanh toán thẻ tín dụng"** destination không thuộc scope module này
- ⚠️ **"Cài đặt PIN thẻ"** destination không thuộc scope module này
- ⚠️ Carousel thẻ có tối đa bao nhiêu thẻ hiển thị cùng lúc? (vẽ 3 dots → giả định max 3)
- ⚠️ PIN Auth: trigger condition nào kích hoạt overlay? (thanh toán? xem số thẻ?)
