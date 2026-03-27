# UX Review Report — Thay đổi thông tin tích luỹ

**Product:** Co-opBank Mobile Banking
**Section:** Thay đổi thông tin tích luỹ định kỳ
**Domain:** Banking
**Generated:** 2026-03-23T18:50:00+07:00
**Pipeline:** Skill A (signal inference + DDL) → Skill B (PRD context + DDL) → Skill C (DDL-grounded vision review)

## Tổng quan

| Metric | Value |
|:---|:---|
| Screens | 4 |
| Tổng check: 38 | Pass: 15 | Gap: 16 | Unverifiable: 7 |
| UX Score: 39% | Weighted: 0% |

---


**Total checks:** 38  
**Pass:** 15 | **Gap:** 16 | **Unverifiable:** 7  
**Simple Score:** 39%  
**Weighted Score:** 39%## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Thông tin tài khoản tiết kiệm › Chi tiết |
|:---|:---|
| **Vấn đề** | PII Exposure — 3 số tài khoản hiển thị đầy đủ không mask (012547288, 1231231232, 123123123123) |
| **Gap ref** | Check #5 |
| **DDL** | Product Context: "Security-first. Trust paramount." |
| **Giải pháp** | Mask partial: hiển thị dạng ****7288, ****1232, ****3123. Chỉ hiện đầy đủ sau xác thực biometrics/PIN |

---

#### UXP-002 · Critical
| **Màn hình** | Thay đổi thông tin tích luỹ định kỳ › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | PII Exposure Form — Số tài khoản tiền gửi 9099798712313123 và TK trích tiền 12312313123133 hiển thị đầy đủ không mask |
| **Gap ref** | Check #10 |
| **DDL** | Product Context: "Security-first. Trust paramount." |
| **Giải pháp** | Mask partial: ****3123, ****3133. Dùng dropdown hiển thị masked + last 4 digits |

---

#### UXP-003 · Critical
| **Màn hình** | Xác thực giao dịch › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | OTP Resend + Error Missing — DDL otp-input-1 spec yêu cầu canResend state + countdown timer + error state (red border, shake). Từ ảnh: chỉ có 6 ô tĩnh + nút Xác nhận, KHÔNG có nút Gửi lại, KHÔNG có artboard cho wrong PIN |
| **Gap ref** | Check #6, Check #2, Check #1 |
| **DDL** | COMP:otp-input-1 (canResend, timeLeft, error states) |
| **Giải pháp** | Thêm: (1) Nút "Gửi lại mã" với countdown 60s; (2) Error state: 6 ô viền đỏ + shake animation + "Mã PIN không đúng. Còn {N} lần thử"; (3) Lock state... |

---

#### UXP-004 · Major
| **Màn hình** | Thông tin tài khoản tiết kiệm › Chi tiết |
|:---|:---|
| **Vấn đề** | Information Overload — Từ ảnh: 22 fields liệt kê liên tục không section divider, không visual grouping. Cognitive load cao |
| **Gap ref** | Check #2 |
| **DDL** | UXG-165, Hick's Law |
| **Giải pháp** | Phân nhóm 4 sections với divider: (1) Thông tin cơ bản (Tên, Số TK, Chi nhánh, Loại SP), (2) Kỳ hạn & Lãi suất (Kỳ hạn, Ngày, Lãi suất, Lãi cộng dồ... |

---

#### UXP-005 · Major
| **Màn hình** | Thay đổi thông tin tích luỹ định kỳ › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Input Validation Missing — Từ ảnh: Input "Số tiền tích luỹ định kỳ" chỉ có helper text tĩnh. DDL text-input-1 yêu cầu error state, helperText dynamic, validationState. Thiếu inline validation khi nhập < 1,000,000 |
| **Gap ref** | Check #2 |
| **DDL** | COMP:text-input-1 (error, helperText, validationState, focused states) |
| **Giải pháp** | Thêm: (1) Error border đỏ + "Số tiền tối thiểu 1.000.000 đồng" khi < 1M; (2) Auto-format VND khi nhập (1000000 → 1.000.000); (3) Focus state: highl... |

---

#### UXP-006 · Major
| **Màn hình** | Thay đổi thông tin tích luỹ định kỳ › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Toggle Label Accessibility — Từ ảnh: Toggle ON (xanh filled) vs OFF (xám outlined) có visual OK nhưng KHÔNG có text label "Đang bật"/"Đang tắt". Screen reader thiếu state info |
| **Gap ref** | Check #1, Check #7 |
| **DDL** | UXG-165: "Labels should clearly indicate the current state" |
| **Giải pháp** | Thêm accessible label bên phải toggle: "Đang bật" (xanh) / "Đã tắt" (xám). ARIA: aria-checked + aria-label |

---

#### UXP-007 · Major
| **Màn hình** | Xác thực giao dịch › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | OTP Cell Size Mismatch — DDL otp-input-1 spec: cellSize=48px. Từ ảnh: cells ước lượng ~44px. Thiếu active focus indicator trên cell đang nhập |
| **Gap ref** | Check #1, Check #2, Check #6 |
| **DDL** | COMP:otp-input-1 (cellSize=48px, activeIndex state) |
| **Giải pháp** | Tăng cell size lên 48px theo DDL spec. Thêm active border (2px solid primary) cho cell đang focus (activeIndex). Filled cells hiển thị dot mask |

---

#### UXP-008 · Major
| **Màn hình** | Kết quả thay đổi › Kết quả giao dịch |
|:---|:---|
| **Vấn đề** | Transaction Details Missing — Từ ảnh: Success popup chỉ có checkmark + message + "Đóng". DDL receipt-preview-1 spec (items, subtotal, paymentMethod) không được sử dụng. Thiếu mã giao dịch, thời gian, before/after values |
| **Gap ref** | Check #2, Check #6 |
| **DDL** | COMP:receipt-preview-1 (items, subtotal, paymentMethod), UXG-165 |
| **Giải pháp** | Hiển thị: mã GD (FT2603xxxxx), thời gian (15:30 23/03/2026), thay đổi: Số tiền tích luỹ 0→5.000.000, Trạng thái tích luỹ Tắt→Bật. Nút "Lưu biên lai" |

---

#### UXP-009 · Minor
| **Màn hình** | Thông tin tài khoản tiết kiệm › Chi tiết |
|:---|:---|
| **Vấn đề** | Bottom Navigation Active State — Từ ảnh: 4 tab bottom nav (Tất toán tiền gửi trực tuyến, Thay đổi thông tin tích luỹ, Lịch sử giao dịch, Chức năng khác). Không tab nào có active color/indicator nổi bật |
| **Gap ref** | Check #4 |
| **DDL** | COMP:bottom-tab-bar-1 (activeTabIndex), UXG-243 |
| **Giải pháp** | Tab "Thay đổi thông tin tích luỹ" cần active color (primary blue) + bottom indicator bar 2px |

---

#### UXP-010 · Minor
| **Màn hình** | Thay đổi thông tin tích luỹ định kỳ › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Popup Button Hierarchy — Từ ảnh (TLTG-5): "Huỷ" và "Đồng ý" cùng style text button, không phân biệt primary/secondary action |
| **Gap ref** | Check #7, Check #1 |
| **DDL** | UXG-165 |
| **Giải pháp** | "Đồng ý": filled primary button (background-primary, text-white). "Huỷ": text-only hoặc outlined secondary |

---

#### UXP-011 · Minor
| **Màn hình** | Thay đổi thông tin tích luỹ định kỳ › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Number Formatting Error — Metadata helper text "23,1000,000" sai comma grouping. Chuẩn VND: 23.100.000 hoặc 23,100,000 |
| **Gap ref** | Check #9 |
| **DDL** | — |
| **Giải pháp** | Chuẩn hoá theo locale vi-VN: dùng dấu chấm phân cách hàng nghìn (23.100.000 VND) |

---

#### UXP-012 · Minor
| **Màn hình** | Thay đổi thông tin tích luỹ định kỳ › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Dropdown Truncation Risk — Từ ảnh: TK trích tiền "12312313123133" hiển thị đầy đủ trong dropdown. Trên thiết bị nhỏ (320pt width) có thể bị cắt |
| **Gap ref** | Check #10 |
| **DDL** | — |
| **Giải pháp** | Truncate giữa: "1231...3133" hoặc hiển thị masked ****3133. Expandable dropdown cho full number |

---

#### UXP-013 · Minor
| **Màn hình** | Xác thực giao dịch › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | Loading State Missing — Không có artboard cho loading khi verify Soft OTP PIN. Doherty Threshold: feedback <400ms |
| **Gap ref** | Check #7, Check #10 |
| **DDL** | UXG-165, Doherty Threshold |
| **Giải pháp** | Thêm loading indicator trên nút "Xác nhận" (spinner replace text) hoặc full-screen loading overlay với "Đang xác thực..." |

---

#### UXP-014 · Minor
| **Màn hình** | Kết quả thay đổi › Kết quả giao dịch |
|:---|:---|
| **Vấn đề** | Single Action — Từ ảnh: Chỉ có nút "Đóng". Thiếu secondary actions cho next task |
| **Gap ref** | Check #3 |
| **DDL** | — |
| **Giải pháp** | Thêm: "Xem chi tiết tài khoản" (link text) hoặc "Về trang chủ" (secondary button) bên dưới nút Đóng |

---

#### UXP-015 · Minor
| **Màn hình** | Thông tin tài khoản tiết kiệm › Chi tiết |
|:---|:---|
| **Vấn đề** | Scroll Indicator Missing — Từ ảnh: Screen dài ~1246px (gấp ~1.5x viewport), hiển thị nhiều fields nhưng không có visual scroll indicator hoặc "xem thêm" |
| **Gap ref** | Check #2 |
| **DDL** | UXG-165 |
| **Giải pháp** | Thêm subtle scroll indicator (gradient fade bottom edge) hoặc sticky header khi scroll |

---

## Chi tiết theo màn hình

### 1. Thông tin tài khoản tiết kiệm › Chi tiết

> `SCR-TK-001` · detail · 1 artboard

**Score: 40% | Pass: 4 | Gap: 3**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Header back/home affordance | Skill C | COMP:app-header-1 | Pass | Từ ảnh: Back arrow (←) top-left, Home icon (🏠) top-right, title "Thông tin tài khoản" centered. DDL spec: back + title + action — matched |
| 2 | Information hierarchy & grouping | Skill A+C | UXG-165, Hick's Law | Gap | Từ ảnh: 22 fields liệt kê liên tục (Tên chủ TK → Phương thức tất toán) không section divider, không visual grouping, font size đồng nhất. Cognitive load cao |
| 3 | Data scrollability | Skill C | UXG-165 | Unverifiable | Screen ~1246px (gấp 1.5x viewport 812px). Không thấy scroll indicator trong ảnh tĩnh. Nhiều fields bị ẩn dưới fold |
| 4 | Bottom nav active state | Skill C | COMP:bottom-tab-bar-1, UXG-243 | Gap | Từ ảnh: 4 tab bottom nav — tất cả cùng style icon+label, không tab nào có active indicator hoặc highlight color. DDL spec yêu cầu activeTabIndex |
| 5 | Account number PII exposure | Skill B+C | Product Context | Gap | Từ ảnh: "012547288" (Số TK tiền gửi), "1231231232" (TK trích tiền), "123123123123" (TK nhận gốc lãi) — 3 số hiển thị đầy đủ. "Security-first" context yêu cầu partial masking |
| 6 | Touch target bottom nav | Skill C | COMP:bottom-tab-bar-1, Fitts's Law | Pass | Từ ảnh: Bottom nav ~88px height, icon 24px + label per tab. Touch target ≥ 44px — adequate |
| 7 | Typography contrast | Skill C | WCAG AA | Pass | Từ ảnh: Label text dark grey (#333) on white background. Value text black (#000) on white. Est. contrast ≥ 7:1 — PASS WCAG AA (4.5:1) |
| 8 | Empty state handling | Skill A | COMP:empty-state-1 | Unverifiable | Không có artboard cho empty state (0 transactions, no data). DDL empty-state-1 spec (icon + heading + text + button) available nhưng không có evidence |
| 9 | Section icon semantics | Skill C | — | Pass | Từ ảnh: "Tài khoản tiết kiệm" có piggy bank icon (🐷). Icon semantic phù hợp product category |
| 10 | Scroll position persistence | Skill A | — | Unverifiable | User scroll xuống xem fields dưới fold → navigate away → return: scroll position có được duy trì? Không thể verify từ ảnh tĩnh |

---

### 2. Thay đổi thông tin tích luỹ định kỳ › Form nhập thông tin

> `SCR-TK-002` · form · 4 artboards

**Score: 50% | Pass: 6 | Gap: 5**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Toggle state visual clarity | Skill C | UXG-165 | Gap | Từ ảnh TLTG-2: Toggle ON = xanh filled circle. TLTG-3: Toggle OFF = xám outlined. Visual OK nhưng KHÔNG có text label "Đang bật"/"Đã tắt" bên cạnh. Screen reader thiếu state info |
| 2 | Input field validation states | Skill A+C | COMP:text-input-1 | Gap | Từ ảnh TLTG-2: Input "Số tiền tích luỹ định kỳ" chỉ hiện helper text tĩnh "Số tiền tối thiểu 1.000.000 đồng". DDL spec: error (red border), validationState, focused highlight — tất cả missing |
| 3 | Input format hint | Skill C | — | Pass | Từ ảnh TLTG-2: Helper "Số tiền tối thiểu 1.000.000 đồng" + "Số tiền tích luỹ định kỳ hiện tại là 23,100,000 đồng" — context rõ ràng |
| 4 | Conditional form toggle behavior | Skill C | — | Pass | Từ ảnh: TLTG-3 (OFF) ẩn input fields. TLTG-2 (ON) hiện đầy đủ fields. Behavior nhất quán, conditional display logic đúng |
| 5 | CTA button positioning & affordance | Skill C | Fitts's Law | Pass | Từ ảnh TLTG-2: "Tiếp tục" full-width button, bottom position, solid blue primary. Touch target lớn ≥ 48px height — adequate |
| 6 | Popup confirmation clarity | Skill C | — | Pass | Từ ảnh TLTG-5: "Thông báo" popup centered, dimmed/blur background, "Quý khách có muốn thay đổi thông tin tích luỹ định kỳ không?" message rõ ràng |
| 7 | Popup button hierarchy | Skill C | UXG-165 | Gap | Từ ảnh TLTG-5: "Huỷ" (left) và "Đồng ý" (right) cùng style text button, cùng font weight. Primary action thiếu visual prominence (filled vs outlined) |
| 8 | Form state preservation | Skill A+C | — | Unverifiable | Không có artboard cho return-from-popup state. Toggle + input values persistence khi Huỷ → return không verify được |
| 9 | Number formatting consistency | Skill C | — | Gap | Từ ảnh TLTG-2: Helper text "23,1000,000" — comma placement sai (should be 23,100,000 hoặc 23.100.000). Inconsistency format gây confusion |
| 10 | PII account numbers in form | Skill B+C | Product Context | Gap | Từ ảnh TLTG-2: "9099798712313123" (TK tiền gửi), "12312313123133" (TK trích tiền) hiển thị đầy đủ không mask. Security-first context yêu cầu masking |
| 11 | Dropdown selector affordance | Skill C | — | Pass | Từ ảnh TLTG-2: "Tài khoản trích tiền" dropdown với arrow (▼) indicator. Từ ảnh: affordance có, user biết tappable |
| 12 | Account card info density | Skill C | — | Pass | Từ ảnh TLTG-2: Blue card top hiển thị TK tiền gửi + số dư hiện tại 20,000,000 VND. Hierarchy rõ: icon, TK number, balance |

---

### 3. Xác thực giao dịch › Xác nhận giao dịch

> `SCR-TK-003` · confirm · 1 artboard

**Score: 40% | Pass: 4 | Gap: 5**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | OTP input cell design | Skill A+C | COMP:otp-input-1 | Gap | Từ ảnh TLTG-6: 6 ô outlined square ~44px, empty placeholder. DDL spec: cellSize=48px, activeIndex state (focus border), digit mask (dot). Vision: cells đều thiếu active focus indicator |
| 2 | OTP resend mechanism | Skill A+C | COMP:otp-input-1 | Gap | Từ ảnh TLTG-6: Không có nút "Gửi lại" hoặc countdown timer anywhere trong bottom sheet. DDL spec yêu cầu canResend + timeLeft + countdown-timer child component |
| 3 | Security warning visibility | Skill C | — | Pass | Từ ảnh TLTG-6: "Lưu ý: Soft OTP sẽ bị khoá nếu Quý khách nhập sai PIN 5 lần liên tiếp" — text hiển thị rõ ở bottom section |
| 4 | Bottom sheet close affordance | Skill C | — | Pass | Từ ảnh TLTG-6: Close (×) icon top-right corner, touch target adequate. Rõ ràng tappable |
| 5 | Keyboard auto-show | Skill C | COMP:otp-input-1 | Unverifiable | Từ ảnh TLTG-6: Không thấy virtual keyboard. DDL spec: keyboardType="number-pad". Ảnh tĩnh không verify auto-show behavior |
| 6 | Error state wrong PIN | Skill A+C | COMP:otp-input-1 | Gap | Không có artboard cho wrong PIN scenario. DDL spec yêu cầu: error=true → red border cells, shake animation, error message "Mã PIN không đúng", remaining attempts counter |
| 7 | Loading state verification | Skill C | UXG-165, Doherty Threshold | Gap | Không có artboard cho loading state khi verify OTP. Doherty: system phải phản hồi < 400ms. Cần loading indicator trên nút "Xác nhận" |
| 8 | Base screen dimming & overlay | Skill C | — | Pass | Từ ảnh TLTG-6: Base screen (form) dimmed + blur. Bottom sheet nổi bật trên overlay. Visual hierarchy rõ ràng |
| 9 | CTA button affordance | Skill C | Fitts's Law | Pass | Từ ảnh TLTG-6: "Xác nhận" full-width blue button bottom sheet. Touch target lớn, primary style. Adequate |
| 10 | Transaction summary pre-auth | Skill B | UXG-165 | Gap | Từ ảnh TLTG-6: Bottom sheet chỉ có "nhập mã PIN". Thiếu summary giao dịch (thay đổi gì, từ giá trị nào → giá trị nào) trước khi xác thực. User không biết mình đang xác nhận thay đổi gì |

---

### 4. Kết quả thay đổi › Kết quả giao dịch

> `SCR-TK-004` · result · 1 artboard

**Score: 17% | Pass: 1 | Gap: 3**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Success feedback clarity | Skill C | Peak-End Rule | Pass | Từ ảnh TLTG-7: Checkmark (✓) xanh centered, message "Quý khách đã thay đổi thông tin tích luỹ định kỳ thành công". Positive ending |
| 2 | Transaction details completeness | Skill B+C | COMP:receipt-preview-1, UXG-165 | Gap | Từ ảnh TLTG-7: Popup chỉ có icon + message + "Đóng". DDL receipt-preview-1 spec (items, subtotal, paymentMethod) available. Thiếu: mã GD, thời gian, before/after values |
| 3 | Action after success | Skill C | — | Gap | Từ ảnh TLTG-7: Chỉ có link "Đóng". Thiếu secondary action: "Xem chi tiết TK" hoặc "Về trang chủ" |
| 4 | Popup dismiss behavior | Skill C | — | Unverifiable | Tap bên ngoài popup: đóng hay không? Back button behavior? Không verify được từ ảnh tĩnh |
| 5 | Success animation | Skill C | — | Unverifiable | Checkmark static trong ảnh. Peak-End Rule suggests animation (scale-up, fade-in) cải thiện positive feeling. Cần verify |
| 6 | Receipt save option | Skill B | COMP:receipt-preview-1 | Gap | Không có option lưu/chia sẻ biên lai thay đổi. DDL receipt spec supports save functionality. Banking context: user cần evidence cho thay đổi tài khoản |

---

## DDL References

| Ref | Type | Used in |
|:---|:---|:---|
| COMP:app-header-1 | Component | SCR-TK-001 (header check) |
| COMP:bottom-tab-bar-1 | Component | SCR-TK-001 (bottom nav active state, touch target) |
| COMP:text-input-1 | Component | SCR-TK-002 (validation, error state, focused) |
| COMP:otp-input-1 | Component | SCR-TK-003 (cell design, resend, error, activeIndex) |
| COMP:receipt-preview-1 | Component | SCR-TK-004 (transaction details, receipt save) |
| COMP:empty-state-1 | Component | SCR-TK-001 (empty state handling) |
| UXG-165 | Guideline | Multiple screens (labels, feedback, grouping, confirmation) |
| UXG-243 | Guideline | SCR-TK-001 (navigation active state) |
| Fitts's Law | UX Law | SCR-TK-001, SCR-TK-002, SCR-TK-003 (touch targets, CTA) |
| Hick's Law | UX Law | SCR-TK-001 (information overload, cognitive load) |
| Peak-End Rule | UX Law | SCR-TK-004 (success feedback, positive ending) |
| Doherty Threshold | UX Law | SCR-TK-003 (loading feedback < 400ms) |
| Product: Security-first | Context | SCR-TK-001, SCR-TK-002 (PII exposure) |
| Product: Trust paramount | Context | SCR-TK-003 (transaction summary pre-auth) |
