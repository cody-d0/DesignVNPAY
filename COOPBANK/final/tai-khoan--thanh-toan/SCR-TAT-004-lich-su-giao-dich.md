# SCR-TAT-004 — Lịch sử giao dịch (Danh sách)

## Tổng quan màn hình

| Thuộc tính | Giá trị |
|:---|:---|
| **screen_id** | SCR-TAT-004 |
| **screen_name_vi** | Lịch sử giao dịch |
| **screen_type** | list |
| **domain** | banking |
| **artboard_count** | 5 (base + empty + filter_empty + filter_filled + calendar) |
| **node_ids** | 142:17684, 142:17785, 142:17713, 142:17749, 142:17530 |

## Wireframe References

| File | Role | Mô tả |
|:---|:---|:---|
| `transaction-history.png` | base | Danh sách giao dịch (1 tuần, có kết quả) |
| `transaction-history-2.png` | variant_empty | Trạng thái empty ("Không có kết quả tìm kiếm") |
| `transaction-historyfilter.png` | overlay_filter_empty | Bottom-sheet "Chọn khoảng thời gian" (ngày chưa chọn) |
| `transaction-historyfilter-2.png` | overlay_filter_filled | Bottom-sheet filter (đã chọn ngày: 22/10/2018 → 22/11/2018) |
| `timepicker.png` | overlay_calendar | Calendar grid "Từ ngày" (Tháng 6 2021) |

## Mô tả chức năng

### Mục đích màn hình
Màn hình tra cứu lịch sử giao dịch của tài khoản thanh toán mặc định. User có thể lọc theo khoảng thời gian bằng quick chips hoặc tùy chỉnh qua date range picker. Giao dịch được phân loại theo Toàn bộ / Tiền vào / Tiền ra.

### Các thành phần giao diện

| Component | Mô tả | Data |
|:---|:---|:---|
| Header | "Lịch sử giao dịch" + Back (←) + Home (⌂) | |
| Account Card | Tên TK mặc định + số TK (masked) + số dư khả dụng | Active account info |
| Section Header | "Tra cứu giao dịch" + disclaimer giới hạn thời gian | Search constraints notice |
| Quick Filter Chips | 1 tuần / 2 tuần / 1 tháng / Khác▾ | Date range filters |
| Tabs | Toàn bộ / Tiền vào / Tiền ra | Transaction direction |
| Transaction List | Danh sách giao dịch — timestamp + description (truncated) + amount | Scrollable |
| Empty State | "Không có kết quả tìm kiếm" | No data state |
| Filter Bottom Sheet | "Chọn khoảng thời gian" + Từ ngày + Đến ngày + Tìm kiếm | Date range input |
| Calendar Picker | Grid tháng — Tháng 6 2021, các ngày available | Date selection |

### Account Card (top)

| Field | Value (demo) |
|:---|:---|
| Tên | Tài khoản thanh toán mặc định |
| Số TK | 9099798712313123 |
| Số dư khả dụng | 20,000,000 VND |

### Quick Filter Chips

| Chip | State | Action |
|:---|:---|:---|
| 1 tuần | Active (dark bg) | Load 7 days data — default |
| 2 tuần | Normal | Load 14 days data |
| 1 tháng | Normal | Load 30 days data |
| Khác▾ | Normal + dropdown | Open filter bottom sheet |

### Transaction List Item

| Field | Data | Ghi chú |
|:---|:---|:---|
| Timestamp | 15:00 - 22/10/2018 | Giờ + ngày |
| Description | MB (270832) (HA chuyen... | Truncated — tap to see detail |
| Amount | +2,000,000 VND (green) / -2,000,000 VND (red) | Color-coded debit/credit |

### Giới hạn tra cứu (Disclaimer)
> "Khoảng thời gian tìm kiếm giới hạn trong vòng 03 tháng và thời gian tối đa cho phép tìm kiếm trong vòng 01 năm"

### Filter Bottom Sheet

| Element | Content |
|:---|:---|
| Title | "Chọn khoảng thời gian" |
| Close | X button (top-right) |
| Input 1 | "Từ ngày" + calendar icon |
| Input 2 | "Đến ngày" + calendar icon |
| Button | "Tìm kiếm" (primary, full-width) |
| Filled state | "22/10/2018" / "22/11/2018" |

### Calendar Picker

| Element | Content |
|:---|:---|
| Header | "Từ ngày" (left) + "Xong" (right) |
| Month header | "Tháng 6 2021" + caret right (next month) |
| Weekdays | T2 T3 T4 T5 T6 T7 CN |
| Selected day | 4 (highlighted circle, today-like) |
| Available day | 22 (blue, selectable) |
| Grid | 6×7 standard calendar grid |

### Luồng tương tác

```
Entry: from SCR-TAT-002 (bottom nav "Lịch sử giao dịch")
Tap chip (1 tuần/2 tuần/1 tháng) → quick filter, reload list
Tap chip "Khác" → open filter bottom sheet (transaction-historyfilter.png)
In bottom sheet: tap calendar icon → open calendar picker (timepicker.png)
Calendar: tap day → setdate → tap "Xong" → back to bottom sheet with date filled
Bottom sheet: tap "Tìm kiếm" → filter results
Results empty → show empty state (transaction-history-2.png)
```

### Trạng thái màn hình

| State | Trigger | Artboard |
|:---|:---|:---|
| Default (1 tuần, có kết quả) | Entry | transaction-history.png |
| Empty state | No results for filter | transaction-history-2.png |
| Filter bottom sheet (empty) | Tap "Khác" chip | transaction-historyfilter.png (overlay) |
| Filter bottom sheet (filled) | After date selection | transaction-historyfilter-2.png (overlay) |
| Calendar picker | Tap calendar icon in filter | timepicker.png (overlay) |

## OCR Text Inventory

| Text | Role | Ghi chú |
|:---|:---|:---|
| Lịch sử giao dịch | header_title | |
| Tài khoản thanh toán mặc định | account_label | Card header |
| 9099798712313123 | account_number | |
| Số dư khả dụng | label | |
| 20,000,000 VND | value_money | |
| Tra cứu giao dịch | section_header | |
| Khoảng thời gian tìm kiếm giới hạn trong vòng 03 tháng... | disclaimer | Search limit notice |
| 1 tuần | chip_active | Quick filter default |
| 2 tuần | chip | |
| 1 tháng | chip | |
| Khác | chip_dropdown | Opens filter |
| Toàn bộ | tab_active | All transactions |
| Tiền vào | tab | Credits only |
| Tiền ra | tab | Debits only |
| 15:00 - 22/10/2018 | transaction_timestamp | |
| MB (270832) (HA chuyen... | transaction_description | Truncated |
| +2,000,000 VND | transaction_credit | |
| -2,000,000 VND | transaction_debit | |
| Không có kết quả tìm kiếm | empty_state_message | Empty state |
| Chọn khoảng thời gian | bottomsheet_title | Filter overlay |
| Từ ngày | input_label | |
| Đến ngày | input_label | |
| 22/10/2018 | input_date_value | Filled state |
| 22/11/2018 | input_date_value | Filled state |
| Tìm kiếm | button_primary | Filter search |
| Tháng 6 2021 | calendar_month_header | Calendar picker |
| T2 T3 T4 T5 T6 T7 CN | calendar_weekdays | |
| Từ ngày | calendar_header_label | |
| Xong | calendar_done_button | |

## Icon Inventory

| Icon | Location | Purpose |
|:---|:---|:---|
| chip-filter | Quick filter row | Date range selection |
| segmented-control | Below chips | Tab Toàn bộ/Tiền vào/Tiền ra |
| calendar | Filter bottom sheet date fields | Open calendar picker |
| close-x | Filter bottom sheet top-right | Close filter overlay |
| home | Header top-right | Navigate to home |
| caret-arrow-right | Month header (calendar) | Navigate to next month |

## Consumer Notes (for AI downstream)

- **3-month limit**: App giới hạn tra cứu 3 tháng/request, tối đa 1 năm — disclaimer cần hiển thị rõ
- **Quick vs custom filter**: Quick chips (1/2/4 tuần, 1 tháng) và custom date range — 2 flow khác nhau
- **Bottom sheet + calendar cascade**: Chip → bottom sheet → calendar picker — 3 layer overlay cho date selection
- **Transaction truncation**: Description bị cắt (ellipsis) — UX issue: user không biết nội dung đầy đủ
- **Color coding**: +amount = green, -amount = red — theo convention ngân hàng VN
- **Empty state**: Khi "Khác" được chọn nhưng khoảng thời gian không có TX → empty state đơn giản (chỉ text)
- **Tabs không có count badge**: Toàn bộ/Tiền vào/Tiền ra không có số lượng — mất tổng quan
