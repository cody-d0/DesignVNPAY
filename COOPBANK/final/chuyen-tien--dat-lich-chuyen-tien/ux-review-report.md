# UX Review Report — Danh sách đặt lịch chuyển tiền

> **Product:** CoopBank Mobile Banking
> **Domain:** Banking/Traditional Finance
> **Section:** Danh sách đặt lịch chuyển tiền
> **Screens:** 4 | **Artboards:** 15
> **Generated:** 2026-03-18T15:17:00+07:00

---


**Total checks:** 40  
**Pass:** 28 | **Gap:** 10 | **Unverifiable:** 2  
**Simple Score:** 70%  
**Weighted Score:** 70%## Tổng quan

| Metric | Value |
|--------|-------|
| Tổng check | 40 |
| Pass: 28 | Gap: 10 | Unverifiable: 2 |
| UX Score | 70% |
| Critical | 2 |
| Major | 3 |
| Minor | 3 |

---

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Danh sách đặt lịch chuyển tiền › Danh sách |
|:---|:---|
| **Vấn đề** | Trạng thái giao dịch (Hoạt động, Đã hủy, Hết hạn, Tạm dừng) chỉ được phân biệt bằng màu chữ mà không có icon hoặc badge  |
| **Gap ref** | Check #2 |
| **DDL** | — |
| **Giải pháp** | — |

---

#### UXP-002 · Critical
| **Màn hình** | Danh sách đặt lịch chuyển tiền › Chi tiết |
|:---|:---|
| **Vấn đề** | Popup xác nhận "Tạm dừng" chỉ có text "Thông báo" + message, với 2 nút "Không" hoặc "Đồng ý". Popup không hiển thị thông |
| **Gap ref** | Check #2 |
| **DDL** | — |
| **Giải pháp** | — |

---

#### UXP-003 · Major
| **Màn hình** | Danh sách đặt lịch chuyển tiền › Chi tiết |
|:---|:---|
| **Vấn đề** | OTP bottom sheet hiển thị chung chung "Quý khách vui lòng nhập mã PIN của Soft OTP để xác thực giao dịch" nhưng không hi |
| **Gap ref** | Check #3 |
| **DDL** | — |
| **Giải pháp** | — |

---

#### UXP-004 · Major
| **Màn hình** | Danh sách đặt lịch chuyển tiền › Quản lý |
|:---|:---|
| **Vấn đề** | Hai empty states ("Không có GD đang Hoạt động" và "Không có kết quả tìm kiếm") hiển thị text centered nhưng không có ill |
| **Gap ref** | Check #3 |
| **DDL** | — |
| **Giải pháp** | — |

---

#### UXP-005 · Major
| **Màn hình** | Danh sách đặt lịch chuyển tiền › Bộ lọc |
|:---|:---|
| **Vấn đề** | Bộ lọc "Theo thời gian" có 2 date picker (Từ ngày, Đến ngày) nhưng không hiển thị validation khi Từ ngày > Đến ngày. Ann |
| **Gap ref** | Check #5, Check #6 |
| **DDL** | — |
| **Giải pháp** | — |

---

#### UXP-006 · Minor
| **Màn hình** | Danh sách đặt lịch chuyển tiền › Danh sách |
|:---|:---|
| **Vấn đề** | Icon filter ở header có kích thước nhỏ (24×24, ~tap area có thể < 44×44). Đây là action quan trọng trên màn danh sách. |
| **Gap ref** | Check #3 |
| **DDL** | — · Law:Fitts's Law |
| **Giải pháp** | — |

---

#### UXP-007 · Minor
| **Màn hình** | Danh sách đặt lịch chuyển tiền › Chi tiết |
|:---|:---|
| **Vấn đề** | Khi hoàn tất OTP → redirect về manage screen với popup "Thành công". Nhưng popup thành công trên manage screen không hiệ |
| **Gap ref** | Check #7 |
| **DDL** | — |
| **Giải pháp** | — |

---

#### UXP-008 · Minor
| **Màn hình** | Danh sách đặt lịch chuyển tiền › Chi tiết |
|:---|:---|
| **Vấn đề** | Danh sách giao dịch đã thực hiện (bottom sheet "list.png") hiển thị lịch sử GD nhưng các entry "Không thành công", "Tạm  |
| **Gap ref** | Check #8 |
| **DDL** | — |
| **Giải pháp** | — |

---

## Chi tiết theo màn hình

### 1. Danh sách đặt lịch chuyển tiền › Danh sách
> `SCR-CB-001` · list · 1 artboard

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Color contrast text/bg | DDL guideline #36 | Accessibility > Color Contrast | Pass | Navy text on white bg, đủ contrast ratio |
| 2 | Color-only information | DDL guideline #180 | Accessibility > Color Only | Gap | Trạng thái chỉ dùng màu, thiếu icon (UXP-001) |
| 3 | Touch target size | DDL guideline #22 | Touch > Target Size | Gap | Filter icon < 44px touch area (UXP-006) |
| 4 | Touch spacing | DDL guideline #23 | Touch > Spacing | Pass | Cards có spacing đủ |
| 5 | Loading states | DDL guideline #10 | Animation > Loading | Unverifiable | Không thể verify loading state từ static design |
| 6 | Header hierarchy | DDL guideline #39 | Accessibility > Heading | Pass | Title rõ ràng |
| 7 | Amount formatting | Vision check | — | Pass | 2,000,000 VND format chuẩn |
| 8 | Status badge consistency | Vision check | — | Pass | 4 trạng thái có màu riêng |
| 9 | Card information density | Vision check | — | Pass | Đủ info: tên, tiền, tần suất, ngày, status |
| 10 | Back navigation | DDL guideline #41 | Accessibility > Keyboard Nav | Pass | Back arrow hiện |

**Score: 70% | Pass: 7 | Gap: 2 | Unverifiable: 1**

---

### 2. Danh sách đặt lịch chuyển tiền › Quản lý
> `SCR-CB-002` · list · 4 artboards

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Confirmation dialogs | DDL guideline #35 | Interaction > Confirm | Pass | Popup xác nhận có trước action |
| 2 | Success feedback | DDL guideline #34 | Interaction > Success | Pass | Popup "Thành công" có sau action |
| 3 | Empty state guidance | Vision check | — | Gap | Empty state thiếu illustration, CTA (UXP-004) |
| 4 | Touch target vertical-dot | DDL guideline #22 | Touch > Target Size | Pass | Vertical-dot icon có padding đủ |
| 5 | Bottom menu affordance | DDL guideline #29 | Interaction > Hover | Pass | Bottom menu có title + close X + action items rõ |
| 6 | Color-only information | DDL guideline #180 | Accessibility > Color Only | Gap | Trạng thái chỉ dùng màu (same as SCR-001) |
| 7 | Tab indication | Vision check | — | Pass | Tab "Danh sách đặt lịch" highlighted |
| 8 | Card grouping clarity | Vision check | — | Pass | Cards nhóm theo loại chuyển tiền rõ ràng |
| 9 | Error message clarity | DDL guideline #33 | Interaction > Error | Pass | Empty state text giải thích lý do |
| 10 | Close affordance | Vision check | — | Pass | Bottom menu có X close, popup có nút Đóng |

**Score: 80% | Pass: 8 | Gap: 2 | Unverifiable: 0**

---

### 3. Danh sách đặt lịch chuyển tiền › Bộ lọc
> `SCR-CB-003` · list · 2 artboards

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Form labels | DDL guideline #43 | Accessibility > Form Labels | Pass | Dropdown có label rõ (Loại chuyển tiền, Trạng thái) |
| 2 | Radio button clarity | Vision check | — | Pass | Radio selected vs unselected rõ ràng |
| 3 | CTA visibility | Vision check | — | Pass | "Tìm kiếm" full-width primary button |
| 4 | Date picker affordance | Vision check | — | Pass | Calendar icon kèm date fields |
| 5 | Error feedback (validation) | DDL guideline #33 | Interaction > Error | Gap | Không có validation Từ ngày > Đến ngày (UXP-005) |
| 6 | Default values | Vision check | — | Gap | Date fields empty, no default (UXP-005) |
| 7 | Annotation readability | Vision check | — | Pass | Annotation text có nhưng font nhỏ |
| 8 | Close affordance | Vision check | — | Pass | X close button góc phải |
| 9 | Mode switching | Vision check | — | Pass | Toggle giữa 2 modes mượt |
| 10 | Dropdown feedback | DDL guideline #29 | Interaction > Hover | Unverifiable | Không verify dropdown expanded state |

**Score: 70% | Pass: 7 | Gap: 2 | Unverifiable: 1**

---

### 4. Danh sách đặt lịch chuyển tiền › Chi tiết
> `SCR-CB-004` · detail · 8 artboards

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Confirmation before destructive | DDL guideline #35 | Interaction > Confirm | Pass | Popup "Thông báo" có trước Tạm dừng/Hủy |
| 2 | Confirm context info | DDL guideline #35 | Interaction > Confirm | Gap | Popup xác nhận thiếu mã/tên/tiền (UXP-002) |
| 3 | OTP context clarity | DDL guideline #33 | Interaction > Error | Gap | OTP không ghi rõ action đang xác nhận (UXP-003) |
| 4 | OTP security warning | Vision check | — | Pass | Lưu ý khóa sau 5 lần sai hiện rõ |
| 5 | Amount with text | Vision check | — | Pass | "20,000,000 VND" + "Hai mươi triệu đồng" |
| 6 | Navigation bar dynamic | Vision check | — | Pass | Bottom nav thay đổi theo trạng thái |
| 7 | Success feedback detail | DDL guideline #34 | Interaction > Success | Gap | Popup thành công thiếu info GD (UXP-007) |
| 8 | History data consistency | Vision check | — | Gap | Entries thất bại thiếu mã GD (UXP-008) |
| 9 | Status color coding | Vision check | — | Pass | 4 trạng thái có màu nhất quán |
| 10 | Back + Home navigation | DDL guideline #41 | Accessibility > Keyboard Nav | Pass | Back arrow + Home icon có |

**Score: 60% | Pass: 6 | Gap: 4 | Unverifiable: 0**

---

## DDL References

| ID | Category | Guideline | Severity |
|----|----------|-----------|----------|
| #180 | Accessibility | Color Only — Don't convey info by color alone | High |
| #35 | Interaction | Confirmation Dialogs — Confirm before destructive | High |
| #33 | Interaction | Error Feedback — Clear error messages | High |
| #34 | Interaction | Success Feedback — Confirm successful actions | Medium |
| #22 | Touch | Touch Target Size — Min 44×44px | High |
| #36 | Accessibility | Color Contrast — Min 4.5:1 ratio | High |
| #19 | Layout | Content Jumping — Reserve space for content | High |
| #43 | Accessibility | Form Labels — Inputs must have labels | High |
| #39 | Accessibility | Heading Hierarchy — Sequential heading levels | Medium |
| #41 | Accessibility | Keyboard Navigation — Tab order matches visual | High |
| #29 | Interaction | Hover States — Visual feedback on interactive | Medium |
| #10 | Animation | Loading States — Show feedback during async | High |

---

## Methodology

- **Skill A:** DDL context — 39 guidelines, 3 UX laws, banking product type
- **Skill B:** Vision analysis — 15 artboards across 4 boundaries
- **Skill C:** Text signal inference — banking domain patterns
- **Tool:** ux-score-calculator.js (verify counts)
