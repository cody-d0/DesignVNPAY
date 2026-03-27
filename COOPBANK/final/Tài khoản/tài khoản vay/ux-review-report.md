# UX Review Report — Tài khoản vay
## Co-opBank Mobile Banking

**Figma Source:** `aYeSAVi94QlI4i4rL3xtmR` · node `142:17846`
**Generated:** 2026-03-23
**Domain:** banking
**Screens reviewed:** 4
**Pipeline:** figma-to-ux-review v1 · Skills A+B+C · DDL-grounded

---


**Total checks:** 45  
**Pass:** 16 | **Gap:** 29 | **Unverifiable:** 0  
**Simple Score:** 36%  
**Weighted Score:** 36%## Tổng quan

| Metric | Value |
|--------|-------|
| Tổng check | 0 |
| Pass: 0 \| Gap: 0 \| Unverifiable: 0 | — |
| UX Score | 0% |

---

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Thông tin tài khoản vay › Chi tiết |
|:---|:---|
| **Vấn đề** | Thiếu CTA "Trả nợ" / "Thanh toán khoản vay" — người dùng không thể thực hiện action quan trọng nhất |
| **Gap ref** | Check #3 |
| **DDL** | — |
| **Giải pháp** | Thêm primary CTA "Trả nợ ngay" ở bottom action bar (height ≥ 44px, CTA color #CA8A04) |

---

#### UXP-002 · Critical
| **Màn hình** | Tài khoản › Danh sách |
|:---|:---|
| **Vấn đề** | Số tài khoản `12300123123000` hiển thị đầy đủ không masked |
| **Gap ref** | Check #8 |
| **DDL** | — |
| **Giải pháp** | Mask by default: `123001••••••000`, toggle show/hide bằng eye icon |

---

#### UXP-003 · Critical
| **Màn hình** | Thông tin tài khoản vay › Chi tiết |
|:---|:---|
| **Vấn đề** | PII (tên, số TK) không masked — HA NGUYEN QUANG, 012547288 exposed |
| **Gap ref** | Check #4 |
| **DDL** | — |
| **Giải pháp** | Mask tên: "HA •••••• QUANG", số TK: "•••••••288" với toggle eye icon |

---

#### UXP-004 · Critical
| **Màn hình** | Chi tiết giao dịch › Chi tiết |
|:---|:---|
| **Vấn đề** | Không có trạng thái giao dịch (Thành công / Thất bại / Đang xử lý) |
| **Gap ref** | Check #4 |
| **DDL** | — |
| **Giải pháp** | Thêm status badge ngay dưới header (màu xanh/đỏ/vàng tùy trạng thái) |

---

#### UXP-005 · Critical
| **Màn hình** | Lịch sử giao dịch › Danh sách |
|:---|:---|
| **Vấn đề** | Số TK `90997987123123123` trong balance card không masked |
| **Gap ref** | Check #5 |
| **DDL** | — |
| **Giải pháp** | Mask: `90997••••••23123`, toggle eye icon trên balance card |

---

#### UXP-006 · Major
| **Màn hình** | Tài khoản › Danh sách |
|:---|:---|
| **Vấn đề** | Section headers accordion (~24px height) dưới 44px minimum touch target |
| **Gap ref** | Check #4, Check #6 |
| **DDL** | — |
| **Giải pháp** | Tăng row height accordion lên ≥ 44px (thêm padding-y: 12px) |

---

#### UXP-007 · Major
| **Màn hình** | Tài khoản › Danh sách |
|:---|:---|
| **Vấn đề** | Không có empty state khi user chưa có khoản vay |
| **Gap ref** | Check #3, Check #10 |
| **DDL** | — |
| **Giải pháp** | Thêm COMP:empty-state-1: icon=loan, title="Chưa có khoản vay", CTA="Tìm hiểu vay" |

---

#### UXP-008 · Major
| **Màn hình** | Thông tin tài khoản vay › Chi tiết |
|:---|:---|
| **Vấn đề** | 17 label-value rows không có nhóm logic — khó scan |
| **Gap ref** | Check #3 |
| **DDL** | — |
| **Giải pháp** | Nhóm thành 4 sections: Thông tin định danh / Chi tiết khoản vay / Tình trạng nợ / Lịch trả nợ |

---

#### UXP-009 · Major
| **Màn hình** | Thông tin tài khoản vay › Chi tiết |
|:---|:---|
| **Vấn đề** | Typo: "Ngày trả nợ lãitiếp theo" — thiếu space giữa "lãi" và "tiếp" |
| **Gap ref** | Check #7 |
| **DDL** | — |
| **Giải pháp** | Sửa thành "Ngày trả nợ lãi tiếp theo" |

---

#### UXP-010 · Major
| **Màn hình** | Thông tin tài khoản vay › Chi tiết |
|:---|:---|
| **Vấn đề** | Ngày đáo hạn (30/12/2021) đã qua nhưng không có visual alert |
| **Gap ref** | Check #8 |
| **DDL** | — |
| **Giải pháp** | Thêm badge "Đã đáo hạn" màu đỏ kế ngày + banner cảnh báo top màn hình |

---

#### UXP-011 · Major
| **Màn hình** | Chi tiết giao dịch › Chi tiết |
|:---|:---|
| **Vấn đề** | Typo: "Tra no vay T2" — thiếu dấu câu, viết tắt không chuẩn |
| **Gap ref** | Check #5 |
| **DDL** | — |
| **Giải pháp** | Hiển thị đầy đủ "Trả nợ vay Tháng 2" hoặc mô tả đủ nghĩa |

---

#### UXP-012 · Major
| **Màn hình** | Chi tiết giao dịch › Chi tiết |
|:---|:---|
| **Vấn đề** | Không có CTA download/share biên lai — màn hình đọc-only, ~400px trống |
| **Gap ref** | Check #7 |
| **DDL** | — |
| **Giải pháp** | Thêm bottom action bar: "Tải biên lai" (PDF) + "Chia sẻ" |

---

#### UXP-013 · Major
| **Màn hình** | Lịch sử giao dịch › Danh sách |
|:---|:---|
| **Vấn đề** | Filter chips height ~28px — dưới 44px minimum touch target |
| **Gap ref** | Check #6, Check #3 |
| **DDL** | — |
| **Giải pháp** | Tăng chip height lên 44px (padding-y: 8px → 16px) |

---

#### UXP-014 · Major
| **Màn hình** | Lịch sử giao dịch › Danh sách |
|:---|:---|
| **Vấn đề** | Help text 2 dòng ngay dưới header — cognitive overload, không thể dismiss |
| **Gap ref** | Check #7 |
| **DDL** | — |
| **Giải pháp** | Collapse thành icon ℹ️ tap-to-expand tooltip, hoặc chỉ show once và dismiss |

---

#### UXP-015 · Major
| **Màn hình** | Lịch sử giao dịch › Danh sách |
|:---|:---|
| **Vấn đề** | Không có empty state cho khoảng thời gian không có giao dịch |
| **Gap ref** | Check #10 |
| **DDL** | — |
| **Giải pháp** | Thêm COMP:empty-state-1: "Không có giao dịch trong khoảng thời gian này" |

---

#### UXP-016 · Minor
| **Màn hình** | Tài khoản › Danh sách |
|:---|:---|
| **Vấn đề** | Refresh icon thiếu aria-label và tooltip |
| **Gap ref** | Check #9 |
| **DDL** | — |
| **Giải pháp** | Thêm aria-label="Làm mới" + long-press tooltip |

---

#### UXP-017 · Minor
| **Màn hình** | Tài khoản › Danh sách |
|:---|:---|
| **Vấn đề** | Không có loading/skeleton state khi fetch data |
| **Gap ref** | Check #11, Check #12 |
| **DDL** | — |
| **Giải pháp** | Thêm skeleton loading per accordion row |

---

#### UXP-018 · Minor
| **Màn hình** | Thông tin tài khoản vay › Chi tiết |
|:---|:---|
| **Vấn đề** | Màn hình 978px không có scroll indicator |
| **Gap ref** | Check #10 |
| **DDL** | — |
| **Giải pháp** | Thêm scrollbar indicator hoặc fade gradient ở bottom |

---

#### UXP-019 · Minor
| **Màn hình** | Chi tiết giao dịch › Chi tiết |
|:---|:---|
| **Vấn đề** | Transaction ID "4153-87675" không có copy-to-clipboard |
| **Gap ref** | Check #6 |
| **DDL** | — |
| **Giải pháp** | Thêm copy icon kế value, tap → copy + toast "Đã sao chép" |

---

#### UXP-020 · Minor
| **Màn hình** | Lịch sử giao dịch › Danh sách |
|:---|:---|
| **Vấn đề** | Chip "Khác" không có calendar icon affordance |
| **Gap ref** | Check #11 |
| **DDL** | — |
| **Giải pháp** | Thêm calendar icon trong chip: "📅 Khác" |

---

#### UXP-021 · Minor
| **Màn hình** | Lịch sử giao dịch › Danh sách |
|:---|:---|
| **Vấn đề** | Credit/Debit dùng màu xanh dương thay vì xanh lá/đỏ chuẩn |
| **Gap ref** | Check #9 |
| **DDL** | — |
| **Giải pháp** | Credit: #16A34A (green.600), Debit: #DC2626 (red.600) + TOKEN base.destructive |

---

#### UXP-022 · Minor
| **Màn hình** | Lịch sử giao dịch › Danh sách |
|:---|:---|
| **Vấn đề** | Không có lazy load / pull-to-refresh |
| **Gap ref** | Check #3 |
| **DDL** | — |
| **Giải pháp** | Infinite scroll (20 items/page) + pull-to-refresh gesture |

---

## Chi tiết theo màn hình

### 1. Tài khoản Tổng quan (`SCR-TAV-001`)

> `SCR-TAV-001` · list · 1 artboard

**Score: 42% | Pass: 5 | Gap: 7**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|---------|
| 1 | App header back button present | Skill A | COMP:app-header-1 | Pass | Từ ảnh: back arrow visible in header left slot |
| 2 | App header right action slot present | Skill A | COMP:app-header-1 | Pass | Từ ảnh: refresh icon in right slot |
| 3 | Empty state design for 0 loan accounts | Skill A | COMP:empty-state-1 | Gap | DDL empty-state-1 requires icon+title+CTA. From ảnh: no empty state visible |
| 4 | Accordion touch target ≥ 44px | Skill A | fitts | Gap | From ảnh: section header row ~24px height — below 44px minimum |
| 5 | Hick's Law — choice reduction via accordion | Skill A | hick | Pass | 3 accordion groups effectively reduce visible choices |
| 6 | Accordion touch target ≥ 44px (guideline) | Skill B | UXG-061 | Gap | Section header rows below 44px minimum touch area |
| 7 | Balance values formatted with thousands separator | Skill B | UXG-022 | Pass | 15,000,000 / 25,000,000 / 11,000,000 properly formatted |
| 8 | Account number masked by default | Skill B | UXG-189 | Gap | 12300123123000 fully visible, no masking |
| 9 | Refresh icon has accessible label | Skill B | UXG-213 | Gap | No aria-label or tooltip visible on refresh icon |
| 10 | Empty state for 0 data sections | Skill B | UXG-074 | Gap | No empty state design present |
| 11 | Expand/collapse has visible chevron direction | Skill B | UXG-243 | Pass | caret-arrow-up indicates expanded state |
| 12 | Loading skeleton state | Skill B | UXG-165 | Gap | No skeleton loading state found |

### 2. Thong tin tai khoan vay (`SCR-TAV-002`)

> `SCR-TAV-002` · detail · 1 artboard

**Score: 33% | Pass: 4 | Gap: 8**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|---------|
| 1 | App header back + home present | Skill A | COMP:app-header-1 | Pass | Từ ảnh: back arrow + home icon both visible |
| 2 | Single primary CTA reduces cognitive load | Skill A | hick | Gap | CTA "Lịch sử giao dịch" present but critical "Trả nợ" action missing |
| 3 | CTA "Lịch sử giao dịch" ≥ 44px | Skill A | fitts | Pass | Bottom CTA appears ~44px height — OK |
| 4 | PII masked by default | Skill B | UXG-189 | Gap | HA NGUYEN QUANG + 012547288 fully visible |
| 5 | Information grouped into logical sections | Skill B | UXG-022 | Gap | 17 rows as flat list — no grouping visible |
| 6 | Date format DD/MM/YYYY consistent | Skill B | UXG-035 | Pass | 30/12/2020 / 30/12/2021 / 28/02/2021 consistent |
| 7 | Typo: "Ngày trả nợ lãitiếp theo" | Skill B | UXG-035 | Gap | Missing space — "lãitiếp" should be "lãi tiếp" |
| 8 | Overdue date shows visual alert badge | Skill B | UXG-074 | Gap | Ngày đáo hạn 30/12/2021 past — no badge or warning |
| 9 | Primary action "Trả nợ" present | Skill B | UXG-061 | Gap | No repayment CTA — critical omission for banking |
| 10 | Scroll indicator for long content | Skill B | UXG-243 | Gap | 978px screen, no scroll indicator visible |
| 11 | Skeleton loading state | Skill B | UXG-165 | Gap | No skeleton for 17 data rows |
| 12 | Header variant branded (not DDL default) | Skill C | COMP:app-header-1 | Pass | Navy header is branded variant — acceptable deviation |

### 3. Chi tiet giao dich (`SCR-TAV-003`)

> `SCR-TAV-003` · detail · 1 artboard

**Score: 44% | Pass: 4 | Gap: 5**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|---------|
| 1 | App header back + home present | Skill A | COMP:app-header-1 | Pass | Từ ảnh: back arrow + home icon visible |
| 2 | Numpad correctly absent (read-only) | Skill A | COMP:numpad-1 | Pass | No numpad — correct for detail view |
| 3 | Share/download receipt action | Skill A | hick | Gap | 0 primary actions — missing download + share |
| 4 | Transaction status badge | Skill B | UXG-074 | Gap | No status badge (Thành công/Thất bại) anywhere |
| 5 | Typo: "Tra no vay T2" | Skill B | UXG-035 | Gap | Missing diacritics + abbreviation — "Trả nợ vay Tháng 2" needed |
| 6 | Transaction ID copy-to-clipboard | Skill B | UXG-198 | Gap | 4153-87675 — no copy icon or interaction |
| 7 | Receipt download CTA in blank area | Skill B | UXG-061 | Gap | ~400px blank area — no CTA for download/share |
| 8 | Header WCAG contrast | Skill C | TOKEN:base.background | Pass | Navy (#1A3A6B est.) on white text → ~7:1 PASS WCAG AA |
| 9 | Amount WCAG contrast | Skill C | TOKEN:base.foreground | Pass | Dark bold text on white → >7:1 PASS WCAG AA |

### 4. Lich su giao dich (`SCR-TAV-004`)

> `SCR-TAV-004` · list · 1 artboard

**Score: 25% | Pass: 3 | Gap: 9**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|---------|
| 1 | App header back + home present | Skill A | COMP:app-header-1 | Pass | Both visible in header |
| 2 | Empty state for 0 results | Skill A | COMP:empty-state-1 | Gap | DDL icon+title+CTA required. From ảnh: no empty state design |
| 3 | Filter chips ≥ 44px | Skill A | fitts | Gap | Chips ~28px from screenshot — below 44px minimum |
| 4 | 4 filter options ≤ 5 (Hick) | Skill A | hick | Pass | 4 chips — under Hick threshold |
| 5 | Account number masked in balance card | Skill B | UXG-189 | Gap | 90997987123123123 fully visible |
| 6 | Chip filter touch target ≥ 44px | Skill B | UXG-061 | Gap | Chips ~28px height — below minimum |
| 7 | Help text dismissible or collapsed | Skill B | UXG-022 | Gap | 2-line help text cannot be dismissed |
| 8 | Transaction descriptions meaningful | Skill B | UXG-035 | Gap | "TK thang 1/2/3" are placeholders — real data must be meaningful |
| 9 | Credit/Debit color coding | Skill B | UXG-022 | Gap | Blue used for credit — should be green (#16A34A) |
| 10 | Empty state for no-results | Skill B | UXG-074 | Gap | No empty state design |
| 11 | Custom date chip calendar affordance | Skill B | UXG-243 | Gap | "Khác" chip no calendar icon |
| 12 | Pull-to-refresh / lazy load | Skill B | UXG-165 | Pass | Acceptable for current scope (no explicit violation visible) |

---

## DDL References

| Ref | Full Name | Source |
|-----|-----------|--------|
| COMP:app-header-1 | Mobile app header — back + title + right slot | DDL component_specs |
| COMP:empty-state-1 | Empty state — icon + title + desc + CTA | DDL component_specs |
| COMP:numpad-1 | Numeric keypad for amount input | DDL component_specs |
| fitts | Fitts's Law — touch targets ≥ 44×44px | DDL ux_laws (auto-trigger) |
| hick | Hick's Law — reduce choices to reduce decision time | DDL ux_laws (auto-trigger) |
| UXG-022 | Visual hierarchy and information grouping | DDL guidelines (High) |
| UXG-035 | Copy quality — no typos, complete content | DDL guidelines (High) |
| UXG-061 | Touch targets and CTA completeness | DDL guidelines (High) |
| UXG-074 | Error prevention and feedback states | DDL guidelines (High) |
| UXG-165 | Loading states and skeleton patterns | DDL guidelines (Major) |
| UXG-189 | PII masking and privacy by default | DDL guidelines (Critical) |
| UXG-198 | Copy-to-clipboard for identifiers | DDL guidelines (Minor) |
| UXG-213 | Icon accessibility labels | DDL guidelines (Minor) |
| UXG-243 | Affordance clarity for interactive elements | DDL guidelines (Minor) |
| TOKEN:base.foreground | #0A0A0A (neutral.950) — body text color | DDL resolved_tokens |
| TOKEN:base.destructive | #DC2626 (red.600) — error/debit color | DDL resolved_tokens |
| TOKEN:base.muted-foreground | #737373 (neutral.500) — muted text | DDL resolved_tokens |
