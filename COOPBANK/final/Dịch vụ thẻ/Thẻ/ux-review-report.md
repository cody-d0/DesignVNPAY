# UX Review Report — Dịch Vụ Thẻ / Thẻ
## CoopBank Mobile Banking

**Module**: Dịch Vụ Thẻ / Thẻ · **Figma Node**: `142:33334`  
**Screens**: 4 · **Artboards**: 29 (+5 overlays) · **DDL Context**: ddl-context.json v1  
**Skills run**: A (component-aware) · B (guideline cross-ref) · C (vision per biên)  
**DDL Components matched**: otp-input-1, app-header-1, empty-state-1, numpad-1, receipt-preview-1  
**Laws auto-triggered**: Fitts's Law (SCR-001,002,004), Hick's Law (SCR-001,002,004), Peak-End Rule (SCR-001,004)

---


**Total checks:** 48  
**Pass:** 16 | **Gap:** 31 | **Unverifiable:** 1  
**Simple Score:** 33%  
**Weighted Score:** 33%## Gate D Results (Phase 2a-pre)

| Screen | Icons | Categories |
|--------|------:|------------|
| SCR-THE-001 | 5 | trigger:2, navigation:1, decoration:1, feedback:1 |
| SCR-THE-002 | 1 | trigger:1 |
| SCR-THE-003 | 4 | navigation:3, trigger:1 |
| SCR-THE-004 | 1 | navigation:1 |
| **Total** | **11** | 4 screens · Gate D: PASS |

## Gate E Results (Phase 2d.4)

```
✅ 1. edges.length = 6 (>0)
✅ 2. All from/to screens exist in boundaries
⚠️ 3. 3 overlay self-loops (allowed: overlay_trigger type)
✅ 4. Icon edges (3) all have trigger_icon + confidence
✅ 5. Coverage: 100% (4/4 screens)
Gate E: PASS
```

## 2d.5 Boundary Consistency: ✅ No SUGGEST_SPLIT or SUGGEST_MERGE flags

---

### 1. Dịch vụ thẻ › Danh sách thẻ (SCR-THE-001)

> `SCR-THE-001` · list (card_management_hub) · 12 artboards (incl. 3 overlays)

**Score: 35% | Pass: 7 | Gap: 12**

| # | Check | Category | DDL Ref | Verdict | Evidence |
|---|-------|----------|---------|----------|--------|
| 1 | Quick action grid ẩn khi thẻ khoá thay vì disable | Interaction | UXG-175 (Loading Buttons) | Gap | Artboard locked-state: 3 quick actions visible, 1 hidden. No tooltip/explanation |
| 2 | Quick action "Sao kê", "Cài đặt PIN" thiếu destination rõ ràng | Interaction | UXG-176 (Error Feedback) | Gap | Design không define destination screens cho 2/4 actions |
| 3 | otp-input-1: `canResend` state missing (Quên PIN?) | Component | COMP:otp-input-1 | Gap | DDL spec requires canResend + Gửi lại button. Screenshots: PIN overlay không có resend |
| 4 | otp-input-1: attempt counter missing | Component | COMP:otp-input-1 | Gap | DDL spec: `timeLeft` state for countdown. Design: chỉ text cảnh báo tĩnh |
| 5 | otp-input-1: ARIA label cho từng ô nhập PIN | Accessibility | UXG-183 (ARIA Labels) | Gap | 6 cells không có accessible label. Screen reader fail |
| 6 | otp-input-1: per-cell visual feedback (active/error/filled) | Component | COMP:otp-input-1 | Gap | DDL spec: activeIndex state. Artboard: cells static, không có active indicator |
| 7 | app-header-1: back/home icon buttons thiếu ARIA label | Accessibility | UXG-243 (Icon Button Labels) | Gap | back_white, home icons không có visible text/label |
| 8 | empty-state-1: thiếu CTA button (`hasCta` state) | Component | COMP:empty-state-1 | Gap | DDL spec: hasCta state. Design: text only, không có "Đăng ký thẻ ngay" CTA |
| 9 | empty-state-1: thiếu illustration/icon | Component | COMP:empty-state-1 | Gap | DDL spec: icon slot. Design: text only |
| 10 | Số thẻ masked inconsistency vs hạn mức masked | Interaction | UXG-180 (Color Only) | Gap | Partial mask (last 4) vs full mask — 2 patterns khác nhau |
| 11 | Carousel dots: không accessible, không có "1/3" indicator | Accessibility | UXG-183 (ARIA Labels) | Gap | Dots không có label. Swipe gesture không confirm |
| 12 | Status badges: color-only, không có icon prefix | Accessibility | UXG-180 (Color Only) | Gap | "Hoạt động" (green), "Khoá" (pink) — màu duy nhất, không có icon |
| 13 | Fitts's Law: Quick action touch targets | Interaction | fitts | Unverifiable | Cần đo actual pixel size từ design spec |
| 14 | otp-input-1: 6 cells present | Component | COMP:otp-input-1 | Pass | Overlay PIN: 6 cells layout đúng |
| 15 | app-header-1: title + back button present | Component | COMP:app-header-1 | Pass | "Dịch vụ thẻ" header với back button |
| 16 | Card carousel present (swipe affordance) | Interaction | — | Pass | Carousel với prev/next + dots |
| 17 | numpad-1: standard 3×4 layout | Component | COMP:numpad-1 | Pass | Số 0 ở cuối — correct mobile keypad |
| 18 | Toast feedback pattern | Interaction | UXG-221 (Loading Indicators) | Pass | "Sao chép thành công" toast visible |
| 19 | Filter chips present | Interaction | — | Pass | Tab bar và chips có active state |
| 20 | Brand color consistency | Layout | — | Pass | CoopBank blue nhất quán toàn bộ |

---

### 2. Thông tin thẻ › Chi tiết thẻ (SCR-THE-002)

> `SCR-THE-002` · detail (card_detail) · 3 artboards

**Score: 40% | Pass: 4 | Gap: 6**

| # | Check | Category | DDL Ref | Verdict | Evidence |
|---|-------|----------|---------|----------|--------|
| 1 | Thiếu CTA "Thanh toán dư nợ" khi xem thông tin dư nợ | Interaction | fitts (Fitts's Law) | Gap | Screen chỉ informational. Không có sticky CTA bottom. VCB/Techcombank đều có |
| 2 | Hạn mức tín dụng không có progress bar/utilization visual | Layout | UXG-162 (Content Jumping) | Gap | "Hạn mức khả dụng còn lại: 78M" — text only, không có visual indicator |
| 3 | Ngày đến hạn không có conditional highlight (<7 ngày) | Feedback | UXG-176 (Error Feedback) | Gap | "29/12/2025" plain text — không countdown, không màu cảnh báo |
| 4 | Label-value row spacing quá dense (~8px) | Layout | UXG-162 | Gap | Từ ảnh: rows quá gần nhau, không đủ breathing room |
| 5 | app-header-1: icon buttons thiếu ARIA label | Accessibility | UXG-243 (Icon Button Labels) | Gap | home/back buttons không có visible text |
| 6 | Section divider giữa 2 sections không đủ visual separation | Layout | — | Gap | Chỉ header text, không có divider line/color |
| 7 | receipt-preview-1: thông tin thẻ hiển thị label-value pattern | Component | COMP:receipt-preview-1 | Pass | Layout label:value đúng pattern |
| 8 | Masked card number hiển thị | Interaction | — | Pass | `1234 **** **** 1121` — partial mask |
| 9 | Screen type: detail (read-only) | Layout | — | Pass | Không có input forms — đúng screen type |
| 10 | Hick's Law: 2 sections, không overwhelm | Interaction | hick | Pass | Chỉ 2 sections rõ ràng, cognitive load thấp |

---

### 3. Lịch sử GD thẻ › Danh sách GD (SCR-THE-003)

> `SCR-THE-003` · list (transaction_history) · 8 artboards (+2 overlays)

**Score: 44% | Pass: 4 | Gap: 5**

| # | Check | Category | DDL Ref | Verdict | Evidence |
|---|-------|----------|---------|----------|--------|
| 1 | Date picker: text input thay vì calendar picker | Forms | UXG-197 (Input Labels) | Gap | "Khác" overlay: 2 text inputs `dd/mm/yyyy`, không có calendar UI. Error-prone |
| 2 | Date picker: thiếu quick presets (Tuần này, Tháng này) | Forms | UXG-204 (Submit Feedback) | Gap | Không có preset options, phải nhập tay |
| 3 | Transaction list: không có grouping by date + daily total | Layout | — | Gap | Flat chronological list. VCB/MB đều group by date |
| 4 | Transaction description bị truncate, không expandable | Interaction | UXG-176 | Gap | "MB (270832) (HA chuyen..." — truncated, tap detail cũng không full |
| 5 | Filter state persistence khi back không định nghĩa rõ | Interaction | UXG-147 (Back Button) | Gap | Không rõ filter "Tiền vào" có giữ khi navigate → back |
| 6 | Card selector rõ ràng | Interaction | — | Pass | Thẻ thumbnail + masked number + name — clear |
| 7 | Filter chips active state | Interaction | — | Pass | Dark background vs light — rõ ràng |
| 8 | Tab active state (underline) | Interaction | — | Pass | Red underline active tab — clear affordance |
| 9 | Amount color coding (+/-) | Interaction | UXG-180 | Pass | Green credits, red debits |

---

### 4. Lịch sử GD thẻ › Chi tiết GD (SCR-THE-004)

> `SCR-THE-004` · detail (transaction_detail) · 4 artboards

**Score: 11% | Pass: 1 | Gap: 8**

| # | Check | Category | DDL Ref | Verdict | Evidence |
|---|-------|----------|---------|----------|--------|
| 1 | receipt-preview-1: chỉ 4/11 fields vs DDL spec | Component | COMP:receipt-preview-1 | Gap | DDL: merchant, location, channel, status, dispute CTA, share. Figma: Mã GD, Ngày, Số tiền, Nội dung only |
| 2 | Thiếu merchant name | Content | COMP:receipt-preview-1 | Gap | "QUET THE" ≠ merchant name. VCB/TCB đều có |
| 3 | Thiếu kênh GD (POS/Online/ATM) | Content | COMP:receipt-preview-1 | Gap | Không distinguish POS vs online vs ATM |
| 4 | Thiếu trạng thái GD (Thành công/Đang xử lý) | Feedback | UXG-221 (Loading Indicators) | Gap | Không có status field |
| 5 | Thiếu "Khiếu nại giao dịch" CTA | Interaction | UXG-176 (Error Feedback) | Gap | Banking regulation yêu cầu. VCB/MB đều có |
| 6 | "QUET THE" nội dung kỹ thuật all-caps | Content | — | Gap | Cần map: QUET THE → "Thanh toán tại POS" |
| 7 | Screen 80% whitespace | Layout | — | Gap | 4 rows ~40% height, còn lại trống |
| 8 | Peak-End Rule: screen kết thúc flow thanh toán | Interaction | peak-end | Gap | Màn hình kết thúc transaction nhưng không có positive closure (receipt, share, CTA) |
| 9 | Số tiền GD present | Content | — | Pass | "2,000,000 VND" hiển thị |

---

## Đề xuất cải tiến (Priority)

### 🔴 Critical

#### UXP-001 · 🔴 Critical
| **Màn hình** | Dịch vụ thẻ › Danh sách thẻ (SCR-THE-001) |
|:---|:---|
| **Vấn đề** | OTP/PIN overlay thiếu canResend state + "Gửi lại" button — user kẹt nếu không nhận mã |
| **Gap ref** | Check #3 (SCR-THE-001) |
| **DDL** | COMP:otp-input-1 (canResend, Gửi lại button) |
| **Giải pháp** | Thêm "Gửi lại mã" button (disabled 60s) + countdown timer trong PIN overlay |

---

#### UXP-002 · 🔴 Critical
| **Màn hình** | Dịch vụ thẻ › Danh sách thẻ (SCR-THE-001) |
|:---|:---|
| **Vấn đề** | PIN overlay thiếu attempt counter — text cảnh báo tĩnh, user không biết còn bao nhiêu lần thử |
| **Gap ref** | Check #4 (SCR-THE-001) |
| **DDL** | COMP:otp-input-1 (timeLeft state) |
| **Giải pháp** | Thay text "bị khóa sau 5 lần" bằng dynamic "Còn X lần thử" counter |

---

#### UXP-003 · 🔴 Critical
| **Màn hình** | Lịch sử GD thẻ › Chi tiết GD (SCR-THE-004) |
|:---|:---|
| **Vấn đề** | Receipt chỉ có 4/11 fields theo DDL spec — thiếu merchant, channel, status, dispute CTA, share |
| **Gap ref** | Check #1, #2, #3, #4, #5 (SCR-THE-004) |
| **DDL** | COMP:receipt-preview-1 |
| **Giải pháp** | Bổ sung: merchant name, kênh GD (POS/Online/ATM), trạng thái, "Khiếu nại giao dịch" CTA |

---

### 🟡 Major

#### UXP-004 · 🟡 Major
| **Màn hình** | Thông tin thẻ › Chi tiết thẻ (SCR-THE-002) |
|:---|:---|
| **Vấn đề** | Thiếu CTA "Thanh toán dư nợ" khi xem thông tin dư nợ — screen chỉ informational |
| **Gap ref** | Check #1 (SCR-THE-002) |
| **DDL** | Fitts's Law |
| **Giải pháp** | Thêm sticky CTA "Thanh toán dư nợ" ở bottom. VCB/Techcombank đều có pattern này |

---

#### UXP-005 · 🟡 Major
| **Màn hình** | Lịch sử GD thẻ › Danh sách GD (SCR-THE-003) |
|:---|:---|
| **Vấn đề** | Date picker dùng text input thay vì calendar UI — error-prone, thiếu presets |
| **Gap ref** | Check #1, #2 (SCR-THE-003) |
| **DDL** | UXG-197 (Input Labels) · UXG-204 (Submit Feedback) |
| **Giải pháp** | (1) Thay text input bằng native date picker, (2) Thêm preset: "Tuần này", "Tháng này", "3 tháng" |

---

#### UXP-006 · 🟡 Major
| **Màn hình** | Dịch vụ thẻ › Danh sách thẻ (SCR-THE-001) |
|:---|:---|
| **Vấn đề** | Empty state thiếu illustration + CTA button — DDL empty-state-1 requires icon + hasCta |
| **Gap ref** | Check #8, #9 (SCR-THE-001) |
| **DDL** | COMP:empty-state-1 (hasCta, icon states) |
| **Giải pháp** | Thêm illustration icon + "Đăng ký thẻ ngay" CTA button theo DDL spec |

---

#### UXP-007 · 🟡 Major
| **Màn hình** | Thông tin thẻ › Chi tiết thẻ (SCR-THE-002) |
|:---|:---|
| **Vấn đề** | Hạn mức tín dụng text-only — thiếu progress bar/utilization visual |
| **Gap ref** | Check #2 (SCR-THE-002) |
| **DDL** | UXG-162 (Content Jumping) |
| **Giải pháp** | Thêm progress bar: "Đã sử dụng 22M / 100M" với visual indicator |

---

#### UXP-008 · 🟡 Major
| **Màn hình** | Dịch vụ thẻ › Danh sách thẻ (SCR-THE-001) |
|:---|:---|
| **Vấn đề** | Quick action grid ẩn khi thẻ khoá — không disable với tooltip giải thích |
| **Gap ref** | Check #1 (SCR-THE-001) |
| **DDL** | UXG-175 (Loading Buttons) |
| **Giải pháp** | Disable actions + tooltip "Thẻ đang bị khoá. Vui lòng mở khoá để sử dụng" |

---

#### UXP-009 · 🟡 Major
| **Màn hình** | Lịch sử GD thẻ › Chi tiết GD (SCR-THE-004) |
|:---|:---|
| **Vấn đề** | Nội dung "QUET THE" all-caps kỹ thuật — cần map sang ngôn ngữ user-friendly |
| **Gap ref** | Check #6 (SCR-THE-004) |
| **DDL** | — |
| **Giải pháp** | Map: QUET THE → "Thanh toán tại POS", CHUYEN TIEN → "Chuyển tiền" |

---

#### UXP-010 · 🟡 Major
| **Màn hình** | Lịch sử GD thẻ › Danh sách GD (SCR-THE-003) |
|:---|:---|
| **Vấn đề** | Transaction list flat chronological — thiếu grouping by date + daily total |
| **Gap ref** | Check #3 (SCR-THE-003) |
| **DDL** | — |
| **Giải pháp** | Group transactions by date với daily total header. VCB/MB đều có pattern này |

---

### ⚪ Minor

#### UXP-011 · ⚪ Minor
| **Màn hình** | Dịch vụ thẻ › Danh sách thẻ (SCR-THE-001) |
|:---|:---|
| **Vấn đề** | Status badges sử dụng color-only (green/pink) — accessibility issue |
| **Gap ref** | Check #12 (SCR-THE-001) |
| **DDL** | UXG-180 (Color Only) |
| **Giải pháp** | Thêm icon prefix: ✅ "Hoạt động", 🔒 "Khoá" — WCAG compliant |

---

#### UXP-012 · ⚪ Minor
| **Màn hình** | Lịch sử GD thẻ › Danh sách GD (SCR-THE-003) |
|:---|:---|
| **Vấn đề** | Transaction description bị truncate, không expandable |
| **Gap ref** | Check #4 (SCR-THE-003) |
| **DDL** | UXG-176 (Error Feedback) |
| **Giải pháp** | Cho phép tap to expand full description, hoặc hiển thị full trong detail screen |

---

*Skills: A (component-aware, DDL-grounded) · B (UXG refs from ddl-context.json) · C (vision per biên)*  
*DDL Prefetch: 7 components · 69 guidelines · 60 laws · 8 auto-triggered*  
*Gate D: PASS (11 icons/4 screens) · Gate E: PASS (6 edges, 100% coverage)*

