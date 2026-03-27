# SCR-PIN-001 — Dịch vụ thẻ › Danh sách

> **Module:** Dịch vụ thẻ | **Section:** Đặt mã PIN thẻ | **Flow Stage:** Entry  
> **Screen ID:** SCR-PIN-001 | **Type:** Danh sách  
> **Primary image:** `ui/danh-sach-the-26.png`

---

## Section 1 — Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Tên màn hình | Dịch vụ thẻ |
| Loại màn hình | Danh sách (Card Hub) |
| URL/Deeplink | `coopbank://card/services` |
| Platform | iOS + Android |
| Flow stage | Entry point |
| Preceding screen | Home / Tab bottom nav |
| Succeeding screen | Cài đặt mã PIN (SCR-PIN-002) |

---

## Section 2 — Mô tả chức năng

Màn hình **Dịch vụ thẻ** là trung tâm quản lý thẻ ngân hàng của người dùng. Cung cấp:

- **Carousel thẻ** — Hiển thị danh sách thẻ tín dụng (3 thẻ), điều hướng bằng mũi tên trái/phải
- **Quick Action Grid** — 4 chức năng nhanh: Sao kê, Thanh toán thẻ tín dụng, Lịch sử giao dịch, **Cài đặt PIN thẻ**
- **Thông tin thẻ** — Hiển thị masked: Số thẻ, Tên chủ thẻ, Loại thẻ, Trạng thái, Hạn mức khả dụng
- **CTA chính** — "Chi tiết thẻ"

Entry point vào luồng Đặt mã PIN: người dùng tap **Cài đặt PIN thẻ** trong action grid.

---

## Section 3 — Nội dung văn bản (OCR)

| Element | Text | Role |
|---|---|---|
| Page title | Dịch vụ thẻ | header_title |
| Card type | Thẻ tín dụng (3) | section_label + badge |
| Card brand | Co-opBank | brand_logo |
| Menu item 1 | Sao kê | action_trigger |
| Menu item 2 | Thanh toán thẻ tín dụng | action_trigger |
| Menu item 3 | Lịch sử giao dịch | action_trigger |
| Menu item 4 | **Cài đặt PIN thẻ** | action_trigger *(trigger to PIN flow)* |
| Section header | Thông tin thẻ | section_title |
| Field: Số thẻ | 1234 \*\*\*\* \*\*\*\* 1121 | masked_data |
| Field: Tên | NGUYEN VAN A | data |
| Field: Loại thẻ | Thẻ chính ★ | data_with_badge |
| Field: Trạng thái | Hoạt động | status_badge |
| Field: Hạn mức | \*\*\*\*\*\*\*\* VND | masked_data |
| CTA | Chi tiết thẻ | primary_action |

---

## Section 4 — Icons & Interactions

| Icon | Vị trí | Category | Action |
|---|---|---|:---|
| ic_back | Top-left | nav | Quay lại màn trước |
| ic_arrow_left | Card carousel | nav | Card trước |
| ic_arrow_right | Card carousel | nav | Card sau |
| ic_saoke | Grid col 1 | trigger | Mở Sao kê |
| ic_thanhtoan | Grid col 2 | trigger | Mở Thanh toán |
| ic_lichsu | Grid col 3 | trigger | Mở Lịch sử GD |
| **ic_pinthe** | **Grid col 4** | **trigger** | **Mở Cài đặt PIN → SCR-PIN-002** |
| ic_eye | Số thẻ row | toggle | Hiện/ẩn số thẻ |
| ic_eye | Hạn mức row | toggle | Hiện/ẩn hạn mức |
| ic_star_red | Loại thẻ row | decoration | Đánh dấu thẻ chính |

---

## Section 5 — UX Gaps (Preliminary)

1. **Masked data accessibility** — Hạn mức khả dụng hiển thị `"******** VND"` nhưng không thể reveal; ic_eye ở Số thẻ cho phép reveal nhưng trải nghiệm không nhất quán
2. **Action grid overflow** — 4 items hiển thị trực tiếp; nếu có thêm action trong tương lai sẽ cần pattern mở rộng (scroll / more button)
3. **Badge count "3"** — Số thẻ hiển thị nhưng không có indicator cho thẻ đang xem là thẻ nào trong 3 thẻ (pagination dots không đủ)
4. **Carousel discoverability** — Mũi tên carousel có thể bị overlap bởi card art; cần kiểm tra contrast

---

## Section 6 — UX Signal Inference (Phase 4e)

> **Scope:** `screen` | **scope_id:** `SCR-PIN-001` | **Domain:** `banking`  
> **Patterns matched:** `carousel_with_count`, `status_indicator`, `masked_field_no_toggle`  
> **DDL refs grounded by:** `ddl-context.json` (banking product)

### Flows inferred

| Signal | Flow | DDL Ref |
|---|---|---|
| `carousel_with_count` — "Thẻ tín dụng (3)" | Carousel điều hướng 3 thẻ; Miller's Law: ≤7 items ✅ | `ux-laws.csv#miller` |
| `security_flow_entry` — "Cài đặt PIN thẻ" | Entry to PIN setup flow; phải visually distinct (Von Restorff) | `ux-guidelines.csv#219` |

### Components inferred

| Component | Pattern ID | State inferred | DDL Ref |
|---|---|---|---|
| `status_badge` | status_indicator | "Hoạt động" — text+color redundant (accessible ✅) | `ux-guidelines.csv#180` |
| `masked_data_field` | masked_field_no_toggle | "Hạn mức" masked nhưng không có reveal toggle (inconsistent với Số thẻ có ic_eye) → **GAP** | `ux-guidelines.csv#197` |
| `card_carousel` | carousel_with_count | 3 states: active/default/default | — |
| `menu_grid_4` | action_grid | 4 items, không có visual distinction cho security action | `ux-guidelines.csv#219` |

### UX Improvements (prd_extension)

1. **Thêm reveal toggle cho "Hạn mức khả dụng"** — ic_eye đồng nhất với pattern Số thẻ  
   `ddl_ref: ux-guidelines.csv#197 (Input Labels)`
2. **Visual distinction cho "Cài đặt PIN thẻ"** — thêm badge màu amber hoặc highlight border để Von Restorff effect  
   `ddl_ref: ux-guidelines.csv#219 (Contrast Readability)`
3. **Pagination indicator rõ hơn** — thay/bổ sung pagination dots bằng "Thẻ 1/3" text label  
   `ddl_ref: ux-laws.csv#miller`
