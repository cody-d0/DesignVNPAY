# SCR-THE-003 · Lịch sử GD thẻ › Danh sách GD

## Screen Identity
- **screen_id**: SCR-THE-003
- **screen_name**: lich-su-gd-the
- **screen_type**: list (transaction_history)
- **product**: CoopBank Mobile Banking
- **module**: Dịch Vụ Thẻ / Thẻ
- **flow_stage**: list
- **wireframe_images**: [`ui/lsgd-the-2.png`](ui/lsgd-the-2.png), [`ui/lsgd-the-4.png`](ui/lsgd-the-4.png), [`ui/lsgd-the-5.png`](ui/lsgd-the-5.png), [`ui/lsgd-the-6-date-picker.png`](ui/lsgd-the-6-date-picker.png), [`ui/lsgd-the-7-date-picker.png`](ui/lsgd-the-7-date-picker.png)

---

## Screen Purpose
Màn hình tra cứu lịch sử giao dịch thẻ tín dụng. Cho phép người dùng lọc theo khoảng thời gian (1/2/3 tháng hoặc tùy chỉnh), và phân loại giao dịch theo Toàn bộ / Tiền vào / Tiền ra. 

**Giới hạn hệ thống**: Tối đa 3 tháng/lần tra cứu, tối đa 1 năm tổng.

---

## User Story
> "Là khách hàng thẻ tín dụng, tôi muốn xem lịch sử các giao dịch trong khoảng thời gian cụ thể và phân loại theo tiền vào/ra để đối soát chi tiêu."

---

## Information Architecture

### Header
- **Back navigation**: `back_white` → quay lại SCR-THE-001
- **Screen title**: "Lịch sử giao dịch"
- **Home navigation**: `home` icon (right) → Home

### Card Selector Row
| Element | Content |
|---------|---------|
| Card thumbnail | Mastercard icon (64x64) |
| Card number | `123456 **** **** 2345` (masked) |
| Cardholder | `NGUYEN HOANG HIEU` |
| Số dư khả dụng | `20,000,000 VND` |

*Tap card selector để chuyển thẻ (nếu có nhiều thẻ)*

### Filter: Tra cứu giao dịch (`ic_money_tit` icon)
**Info note**: "Khoảng thời gian tìm kiếm giới hạn trong vòng 03 tháng và thời gian tối đa cho phép tìm kiếm trong vòng 01 năm."

**Time filter chips** (single-select):
| Chip | State |
|------|-------|
| `1 tháng` | Selected (default) |
| `2 tháng` | Default |
| `3 tháng` | Default |
| `Khác ▼` | → Opens Date Picker Overlay |

### Transaction Tabs (3 tabs)
| Tab | Filter |
|-----|--------|
| `Toàn bộ` | All transactions |
| `Tiền vào` | Credit only (+) |
| `Tiền ra` | Debit only (-) |

### Transaction List Items
| Element | Example |
|---------|---------|
| Timestamp | `15:00 - 22/10/2018` |
| Description | `MB (270832) (HA chuyen...` (truncated) |
| Amount (+) | `+2,000,000 VND` (bold, green/dark) |
| Amount (-) | `-2,000,000 VND` (bold, red) |

*Tap row → SCR-THE-004 (Chi tiết giao dịch)*

---

## Overlay: Chọn khoảng thời gian (Date Picker)
**Trigger**: Tap "Khác" chip
- **Title**: "Chọn khoảng thời gian" + close `×`
- **Field "Từ ngày"**: Date input → `22/10/2018`
- **Field "Đến ngày"**: Date input → `22/11/2018`
- **CTA**: "Tìm kiếm" (full-width blue button)

---

## Screen States & Variants

### State 1: Default (1 tháng selected, Toàn bộ)
- Hiển thị tất cả GD trong 1 tháng gần nhất
- Mix credit/debit rows

### State 2: Filter "Tiền vào" active
- Chỉ hiển thị rows có `+amount` (màu xanh/đen)
- Empty nếu không có GD tiền vào

### State 3: Filter "Tiền ra" active
- Chỉ hiển thị rows có `-amount` (màu đỏ)
- Empty nếu không có GD tiền ra

### State 4: Date picker mode (sau khi "Khác" → Tìm kiếm)
- Custom date range đang active
- Chip display thay đổi thành custom dates

---

## Navigation Flows
- `back` → SCR-THE-001
- `home` → Home screen
- Tap transaction row → SCR-THE-004
- "Khác" → date picker overlay (self-loop)

---

## Missing Data / Gaps
- ⚠️ **Transaction description bị truncate**: `MB (270832) (HA chuyen...` — thiếu full description, có thể gây confusion
- ⚠️ **Không có tìm kiếm text**: Không có ô search theo tên/số tiền/nội dung
- ⚠️ **Không có tổng kết**: Không hiển thị tổng tiền vào/tiền ra trong period
- ⚠️ **Không có nhóm theo ngày**: Danh sách flat, không group by date header
- ⚠️ **Date picker field không có calendar UI**: Chỉ text input — user phải nhập tay định dạng ngày
- ⚠️ **Không có empty state design**: Khi filter cho kết quả 0 giao dịch, không rõ UI
- ⚠️ **Card selector không swipeable**: Nếu có nhiều thẻ, UX chuyển thẻ không rõ ràng
