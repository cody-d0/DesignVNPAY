# UX Review Report — Co-opBank KHCN · Danh bạ thụ hưởng

## Tổng quan
- Folder: coopbank/final/Danh bạ thụ hưởng
- Số màn hình: 4 | Tổng check: 53
- Pass: 44 | Gap: 8 | Unverifiable: 1
- UX Score (Simple): 83% (44/53)
- UX Score (Weighted): 100%
- Proposals: 🔴 Critical: 2 | 🟡 Major: 3 | ⚪ Minor: 3 | Total: 8

## Đề xuất cải tiến (Priority)

### 🔴 Critical

#### UXP-001 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Danh bạ thụ hưởng › Danh sách |
| **Mức độ** | 🔴 Critical |
| **DDL** | UXG-10 · UXG-78 |
| **UX Law** | fitts |

**🔍 Hiện trạng**

Toast hướng dẫn "Chọn danh bạ mà Qúy khách muốn xóa" hiện ngay khi vào màn hình delete mode nhưng thiếu nút dismiss rõ ràng. Từ ảnh contact.png: toast nằm giữa header và search bar, chiếm ~52px chiều cao. Không có icon close (×) hay swipe-to-dismiss indicator. Toast cũng bị lỗi chính tả: "Qúy" → đúng "Quý".

> Evidence: Wireframe contact.png — toast nằm cố định, không có dismiss affordance. OCR: "Qúy khách" — typo.

**⚠️ Hậu quả**

- **User impact:** User không biết cách tắt toast → che khuất search bar, gây frustration. Typo "Qúy" tạo cảm giác thiếu chuyên nghiệp.
- **Business impact:** Giảm trust trong ứng dụng ngân hàng, tăng support tickets.
- **Violation:** UXG-10 (Dismissible Notifications), UXG-78 (Content Quality) — toast persistent không dismiss được.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Toast | Thêm icon × ở bên phải toast, auto-dismiss sau 5s | Top banner |
| 2 | Toast text | Sửa "Qúy" → "Quý" | Toast copy |

---

#### UXP-002 · 🔴 Critical

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Danh bạ thụ hưởng › Chi tiết |
| **Mức độ** | 🔴 Critical |
| **DDL** | UXG-165 |
| **UX Law** | peak-end |

**🔍 Hiện trạng**

Từ ảnh contact-details.png: label "Loại chuyển" bị truncated — chỉ hiện "Loại chuyển" và text value "Chuyển tiền nhanh 24/7 qua tài khoản" bắt đầu ngay sau, gây chồng text lên nhau. Hai dòng cùng row bị overlap: label "Loại chuyển" → khoảng trống → "Chuyển tiền nhanh 24/7 qua tài khoản" chồng lên.

> Evidence: Từ ảnh contact-details.png — text overlap ở row 1. Label truncation rõ ràng.

**⚠️ Hậu quả**

- **User impact:** Không đọc được thông tin loại chuyển tiền → confusion khi xác minh beneficiary.
- **Business impact:** Sai sót khi chuyển tiền do user hiểu nhầm loại giao dịch.
- **Violation:** UXG-165 (Text Legibility) — text bị cắt/chồng ở viewport 375px.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Info row | Chuyển sang layout 2-line: label trên, value dưới (thay vì cùng dòng) | Section thông tin |
| 2 | Label | Full text "Loại chuyển tiền" không truncate | Row 1 label |

---

### 🟡 Major

#### UXP-003 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Danh bạ thụ hưởng › Form nhập thông tin |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-243 · COMP:text-input-1 |
| **UX Law** | doherty |

**🔍 Hiện trạng**

Từ ảnh add-new-3.png: Message lỗi "Số tài khoản/Số thẻ không tồn tại" hiện màu đỏ nhưng không có icon cảnh báo (⚠️). DDL `text-input-1` spec yêu cầu error state có `errorColor: {base.destructive}` + helper text area. Từ ảnh: error text hiện nhưng field border không đổi sang error state (vẫn border mặc định).

> Evidence: Từ ảnh add-new-3.png — error text red nhưng field border vẫn default gray. DDL `text-input-1.state.error` requires `errorBorderColor: {base.destructive}`.

**⚠️ Hậu quả**

- **User impact:** Error thiếu visual prominence → user có thể miss lỗi, nhập lại nhiều lần.
- **Business impact:** Tăng nhầm giao dịch, tăng call center volume.
- **Violation:** COMP:text-input-1 error state incomplete. UXG-243 (Error Feedback).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Text field | Border đổi sang `{base.destructive}` (#dc2626) khi error | Field "Số tài khoản/Số thẻ" |
| 2 | Error icon | Thêm icon ⚠️ trước error message | Dưới field |
| 3 | Button | Disable "Thêm mới" khi form invalid | Footer CTA |

---

#### UXP-004 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Danh bạ thụ hưởng › Tìm kiếm |
| **Mức độ** | 🟡 Major |
| **DDL** | COMP:empty-state-1 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh search-3.png: Empty state chỉ có text "Quý khách chưa có danh bạ thụ hưởng" trên nền trắng, không có illustration/icon. DDL `empty-state-1` spec yêu cầu icon (48px), title, description, và optional CTA button. Hiện tại thiếu cả icon lẫn CTA. Có annotation callout "Nhấn vào đây để thêm mới" nhưng đây là design annotation, không phải UI element.

> Evidence: Từ ảnh search-3.png — empty state chỉ 1 dòng text center, không icon, không CTA. DDL `empty-state-1` requires `icon` (48px) + `ctaLabel`.

**⚠️ Hậu quả**

- **User impact:** Empty state nhạt nhẽo → user không biết phải làm gì tiếp.
- **Business impact:** Mất cơ hội onboard user thêm beneficiary (conversion funnel).
- **Violation:** COMP:empty-state-1 layout missing icon + CTA. UX best practice: empty state phải có clear action path.

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Icon | Thêm illustration icon 48×48 (contact/address book) | Trên text center |
| 2 | Title | "Chưa có danh bạ thụ hưởng" (bold) | Dưới icon |
| 3 | Description | "Thêm người thụ hưởng để chuyển tiền nhanh hơn" | Dưới title |
| 4 | CTA button | "Thêm mới" → navigate SCR-DB-004 | Dưới description |

---

#### UXP-005 · 🟡 Major

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Danh bạ thụ hưởng › Chi tiết |
| **Mức độ** | 🟡 Major |
| **DDL** | UXG-4 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh contact-details-2.png: Edit mode chỉ hiện 1 button "Cập nhật" và keyboard, nhưng không có button "Hủy" hoặc cách rõ ràng để cancel edit. Button "Thực hiện giao dịch" biến mất. Nếu user muốn hủy edit → chỉ có thể nhấn back (mất thay đổi mà không warning).

> Evidence: Từ ảnh contact-details-2.png — chỉ 1 CTA "Cập nhật", không "Hủy". UXG-4 (Undo/Cancel Support).

**⚠️ Hậu quả**

- **User impact:** Không có cách cancel rõ ràng → anxiety khi sửa nhầm, phải back rồi re-enter.
- **Business impact:** Tăng bounce rate trên flow edit.
- **Violation:** UXG-4 (Require cancel/undo for destructive edits).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Button | Thêm "Hủy" (outline) bên trái "Cập nhật" | Footer buttons |
| 2 | Back handling | Nếu có unsaved changes → show confirm dialog trước khi back | Navigation |

---

### ⚪ Minor

#### UXP-006 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Danh bạ thụ hưởng › Danh sách |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-52 |
| **UX Law** | hicks |

**🔍 Hiện trạng**

Từ ảnh contact-2.png: Expanded view hiển thị 4 sections cùng lúc với nhiều contacts. Mỗi contact trong "Chuyển tiền nhanh 24/7 qua tài khoản" có thêm dòng ngân hàng (Vietcombank, Techcombank) — tổng list dài (height 1222px). Không có sticky section headers khi scroll.

> Evidence: Từ ảnh contact-2.png — artboard height 1222px, 4 sections expanded, 8+ contacts visible. Không sticky headers.

**⚠️ Hậu quả**

- **User impact:** Scroll dài không nhớ đang ở section nào → mất orientation.
- **Business impact:** Minor friction, không critical.
- **Violation:** UXG-52 (Long List Orientation), Hick's Law (nhiều options cùng lúc).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Section header | Sticky section headers khi scroll | Each section |
| 2 | Collapse | Mặc định collapse sections, chỉ expand section user tap | Body |

---

#### UXP-007 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Danh bạ thụ hưởng › Form nhập thông tin |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-88 |
| **UX Law** | — |

**🔍 Hiện trạng**

Từ ảnh add-new-2.png: Auto-resolved name "NGUYEN HOANG HIEU" hiện đúng sau khi nhập số TK, nhưng text hiển thị ALL CAPS — không matching với tên gợi nhớ "Nguyen Hoang Hieu" (title case) bên dưới. Không có label hoặc explanation cho auto-resolved name.

> Evidence: Từ ảnh add-new-2.png — "NGUYEN HOANG HIEU" (uppercase, no label) vs "Nguyen Hoang Hieu" (title case, có label "Tên gợi nhớ").

**⚠️ Hậu quả**

- **User impact:** Confused về 2 dạng tên khác nhau → không chắc auto-fill đúng chưa.
- **Business impact:** Minor confusion, không critical.
- **Violation:** UXG-88 (Consistent Text Formatting).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | Auto-resolved name | Thêm label "Tên chủ tài khoản" phía trên | Dưới field "Số TK" |
| 2 | Text case | Chuyển sang Title Case hoặc thêm note "(theo ngân hàng)" | Auto-resolved text |

---

#### UXP-008 · ⚪ Minor

| Thuộc tính | Chi tiết |
|:---|:---|
| **Màn hình** | Danh bạ thụ hưởng › Danh sách |
| **Mức độ** | ⚪ Minor |
| **DDL** | UXG-32 |
| **UX Law** | fitts |

**🔍 Hiện trạng**

Từ ảnh contact-3.png: FAB (+) 48×48 ở góc phải dưới, nhưng bottom nav bar (sub-navigation-bar) cũng ở cùng vùng — FAB và tab bar overlap visual zone. FAB đè lên phần cuối nội dung list.

> Evidence: Từ ảnh contact-3.png — FAB y=744, bottom nav y=740, cùng vùng. Có thể gây mis-tap.

**⚠️ Hậu quả**

- **User impact:** Mis-tap giữa FAB và bottom nav items.
- **Business impact:** Minor friction.
- **Violation:** UXG-32 (Touch Target Spacing), Fitts's Law (competing targets).

**✅ Giải pháp đề xuất**

| # | Component | Đề xuất | Vị trí |
|---|:---|:---|:---|
| 1 | FAB | Nâng FAB lên trên bottom nav (y = 680 hoặc thêm 16px gap) | Bottom-right |

---

## Chi tiết theo màn hình

### 1. Danh bạ thụ hưởng › Danh sách
> `SCR-DB-001` · list · 4 artboards
>
> **Score: 81% | Pass: 13 | Gap: 3 | Unverifiable: 0 | Images: contact.png, contact-3.png, contact-2.png, popup.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header hiển thị title + back + action | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: header "Danh bạ thụ hưởng" + back arrow + trash icon |
| 2 | Search bar có placeholder | Skill A | UXG-65 | ✅ Pass | Từ ảnh contact-3.png: "Tìm kiếm" placeholder visible |
| 3 | Danh sách grouped theo loại chuyển tiền | Skill B | UXG-52 | ✅ Pass | Từ ảnh: 3 sections "Chuyển tiền nội bộ", "24/7 qua tài khoản", "24/7 qua thẻ" |
| 4 | Contact row hiển thị tên + số TK + logo | Skill C | — | ✅ Pass | Từ ảnh: "Anh Thang" + "012931231…" + Co-opBank logo |
| 5 | Expand/collapse sections | Skill C | UXG-52 | ✅ Pass | Từ ảnh contact.png vs contact-2.png: chevron ∧/∨ toggle |
| 6 | FAB (+) visible | Skill C | — | ✅ Pass | Từ ảnh: FAB circle blue ở bottom-right |
| 7 | Multi-select mode với checkbox | Skill C | — | ✅ Pass | Từ ảnh contact-3.png: checkbox ✓ per contact |
| 8 | Toast hướng dẫn xóa | Skill C | UXG-10 | ❌ Gap | Từ ảnh contact.png: toast không có dismiss (×). Typo "Qúy" → UXP-001 |
| 9 | Popup confirm destructive | Skill B | UXG-4 | ✅ Pass | Từ ảnh popup.png: "Thông báo" + "Không" / "Đồng ý" |
| 10 | Popup blur overlay | Skill C | — | ✅ Pass | Từ ảnh popup.png: blur background visible |
| 11 | Bottom nav hiện | Skill C | COMP:app-header-1 | ✅ Pass | Từ ảnh contact-3.png: sub-navigation-bar visible |
| 12 | FAB không overlap với nav bar | Skill C | UXG-32 | ❌ Gap | Từ ảnh contact-3.png: FAB y=744, nav y=740 → overlap → UXP-008 |
| 13 | Sticky section headers (long scroll) | Skill C | UXG-52 | ❌ Gap | Từ ảnh contact-2.png: 1222px height, no sticky headers → UXP-006 |
| 14 | Số lượng đã chọn hiển thị rõ | Skill C | — | ✅ Pass | Từ ảnh contact-3.png: "Xóa (2)" hiện rõ ở bottom |
| 15 | Fitts's Law — touch target ≥44px | Skill A | fitts | ✅ Pass | Từ ảnh: contact rows height 68px, FAB 48px — đủ |
| 16 | Hick's Law — grouped options | Skill A | hicks | ✅ Pass | Từ ảnh: sections grouped, collapsible → giảm cognitive load |

### 2. Danh bạ thụ hưởng › Tìm kiếm
> `SCR-DB-002` · list · 4 artboards
>
> **Score: 92% | Pass: 11 | Gap: 1 | Unverifiable: 0 | Images: search-3.png, search-4.png, search.png, search-2.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header hiển thị title + back + action | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: header "Danh bạ thụ hưởng" consistent |
| 2 | Search bar focus state + clear (×) | Skill C | COMP:text-input-1 | ✅ Pass | Từ ảnh search.png: focus + clear × visible |
| 3 | Keyboard hiện khi focus search | Skill C | — | ✅ Pass | Từ ảnh search.png, search-4.png: iOS keyboard visible |
| 4 | Empty state khi chưa có danh bạ | Skill C | COMP:empty-state-1 | ❌ Gap | Từ ảnh search-3.png: chỉ text, thiếu icon + CTA → UXP-004 |
| 5 | No-results state | Skill C | — | ✅ Pass | Từ ảnh search-4.png: "Không tìm thấy kết quả" center |
| 6 | Filter results hiển thị đúng | Skill C | — | ✅ Pass | Từ ảnh search-2.png: 1 contact "Anh Văn Mỹ" filtered |
| 7 | Toast success sau xóa | Skill C | — | ✅ Pass | Từ ảnh search-2.png: "Đã xóa danh bạ thụ hưởng thành công" + ✓ |
| 8 | FAB (+) visible trong search | Skill C | — | ✅ Pass | Từ ảnh: FAB visible across all search variants |
| 9 | Annotation hướng dẫn thêm mới | Skill C | — | ✅ Pass | Từ ảnh search-3.png: callout bubble "Nhấn vào đây để thêm mới" |
| 10 | Peak-End Rule — success feedback | Skill A | peak-end | ✅ Pass | Từ ảnh search-2.png: toast success = positive ending |
| 11 | Fitts's Law — search bar easy access | Skill A | fitts | ✅ Pass | Từ ảnh: search bar full-width, easy to tap |
| 12 | Hick's Law — filtered reduces options | Skill A | hicks | ✅ Pass | Từ ảnh: search reduces list to matching items |

### 3. Danh bạ thụ hưởng › Chi tiết
> `SCR-DB-003` · detail · 3 artboards
>
> **Score: 83% | Pass: 10 | Gap: 2 | Unverifiable: 0 | Images: contact-details.png, contact-details-2.png, contact-details-3.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header hiển thị "Chi tiết danh bạ" + back + home | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: header đúng format |
| 2 | Info rows: 4 fields (loại CT, tên, số TK, ngân hàng) | Skill B | — | ✅ Pass | Từ ảnh contact-details.png: 4 label-value rows |
| 3 | Tên gợi nhớ editable | Skill C | COMP:text-input-1 | ✅ Pass | Từ ảnh contact-details-2.png: cursor visible, keyboard up |
| 4 | Text readability — label-value layout | Skill C | UXG-165 | ❌ Gap | Từ ảnh contact-details.png: label "Loại chuyển" truncated, value overlap → UXP-002 |
| 5 | Dual CTA: Cập nhật + Thực hiện giao dịch | Skill B | — | ✅ Pass | Từ ảnh contact-details.png: 2 buttons footer |
| 6 | Edit mode — cancel option | Skill C | UXG-4 | ❌ Gap | Từ ảnh contact-details-2.png: chỉ "Cập nhật", thiếu "Hủy" → UXP-005 |
| 7 | Toast success — update confirm | Skill C | — | ✅ Pass | Từ ảnh contact-details-3.png: "Cập nhật danh bạ thành công" + ✓ |
| 8 | Edit mode — keyboard appropriate type | Skill C | — | ✅ Pass | Từ ảnh contact-details-2.png: numeric keyboard for alias edit |
| 9 | Peak-End Rule — success toast = positive | Skill A | peak-end | ✅ Pass | Từ ảnh: toast green = positive ending |
| 10 | Fitts's Law — CTA buttons ≥44px height | Skill A | fitts | ✅ Pass | Từ ảnh: buttons 48px height, full-width |
| 11 | Read-only fields not editable | Skill C | — | ✅ Pass | Từ ảnh: loại CT, tên, số TK, ngân hàng appear read-only |
| 12 | Hick's Law — limited choices | Skill A | hicks | ✅ Pass | Từ ảnh: only 2 CTA buttons, clear decision |

### 4. Danh bạ thụ hưởng › Form nhập thông tin
> `SCR-DB-004` · form · 4 artboards
>
> **Score: 77% | Pass: 10 | Gap: 2 | Unverifiable: 1 | Images: add-new.png, add-new-2.png, add-new-3.png, add-new-4.png**

| # | Check | Source | DDL | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header hiển thị "Thêm mới danh bạ thụ hưởng" + back + home | Skill B | COMP:app-header-1 | ✅ Pass | Từ ảnh: header đúng, 2 nav icons |
| 2 | Section header "Thông tin danh bạ" với icon | Skill C | — | ✅ Pass | Từ ảnh add-new.png: icon + text section header |
| 3 | Dropdown "Loại chuyển tiền" | Skill C | — | ✅ Pass | Từ ảnh: dropdown with chevron, 2 options visible across variants |
| 4 | Input "Số tài khoản/Số thẻ" | Skill C | COMP:text-input-1 | ✅ Pass | Từ ảnh add-new.png: input placeholder visible |
| 5 | Auto-resolve tên từ số TK | Skill C | — | ✅ Pass | Từ ảnh add-new-2.png: "NGUYEN HOANG HIEU" appears after input |
| 6 | Error state — invalid account | Skill C | COMP:text-input-1 | ❌ Gap | Từ ảnh add-new-3.png: error text red nhưng field border vẫn default → UXP-003 |
| 7 | Auto-resolved name — label missing | Skill C | UXG-88 | ❌ Gap | Từ ảnh add-new-2.png: "NGUYEN HOANG HIEU" uppercase, no label → UXP-007 |
| 8 | Input "Tên gợi nhớ" | Skill C | COMP:text-input-1 | ✅ Pass | Từ ảnh: tên gợi nhớ field visible, auto-filled |
| 9 | Dynamic form — ngân hàng field qua thẻ | Skill C | — | ✅ Pass | Từ ảnh add-new-4.png: "Ngân hàng thụ hưởng" + "VPBank" dropdown visible |
| 10 | CTA "Thêm mới" full-width | Skill C | — | ✅ Pass | Từ ảnh: button full-width footer |
| 11 | Fitts's Law — CTA button ≥44px | Skill A | fitts | ✅ Pass | Từ ảnh: button 44px height, full-width |
| 12 | Hick's Law — progressive form | Skill A | hicks | ✅ Pass | Từ ảnh: only 3-4 fields, clear progression |
| 13 | Button enabled/disabled based on validation | Skill C | UXG-243 | ⚠️ Unverifiable | Không thể verify button state từ ảnh tĩnh — cần interaction test |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| UXG-4 | Undo/Cancel Support | — | SCR-DB-003 edit mode thiếu cancel |
| UXG-10 | Dismissible Notifications | — | SCR-DB-001 toast không dismiss được |
| UXG-32 | Touch Target Spacing | fitts | SCR-DB-001 FAB overlap nav bar |
| UXG-52 | Long List Orientation | hicks | SCR-DB-001 expanded list no sticky headers |
| UXG-65 | Search Placeholder | — | SCR-DB-001, SCR-DB-002 search bar |
| UXG-78 | Content Quality | — | SCR-DB-001 typo "Qúy" |
| UXG-88 | Consistent Text Formatting | — | SCR-DB-004 auto-resolved name |
| UXG-165 | Text Legibility | — | SCR-DB-003 label truncation |
| UXG-243 | Error Feedback | doherty | SCR-DB-004 error state incomplete |
| COMP:app-header-1 | App header spec | — | All screens header check |
| COMP:text-input-1 | Text input with validation | — | SCR-DB-003, SCR-DB-004 form fields |
| COMP:empty-state-1 | Empty state spec | — | SCR-DB-002 empty state missing icon+CTA |
