# UX Review Report — Thay đổi phương thức tất toán/ rút gốc

**Product:** Co-opBank Mobile Banking
**Section:** Thay đổi phương thức tất toán/ rút gốc
**Domain:** Banking
**Generated:** 2026-03-23T22:43:00+07:00
**Pipeline:** Skill A (signal inference + DDL) → Skill B (PRD context + DDL) → Skill C (DDL-grounded vision review)

## Tổng quan

| Metric | Value |
|:---|:---|
| Screens | 4 |
| Tổng check: 33 | Pass: 15 | Gap: 14 | Unverifiable: 4 |
| UX Score: 45% | Weighted: 100% |

---


**Total checks:** 33  
**Pass:** 15 | **Gap:** 14 | **Unverifiable:** 4  
**Simple Score:** 45%  
**Weighted Score:** 45%## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Thông tin tài khoản tiết kiệm › Danh sách |
|:---|:---|
| **Vấn đề** | PII Exposure — Số tài khoản "012547288" và "1231231232" hiển thị đầy đủ không mask trên màn thông tin chi tiết |
| **Gap ref** | Check #3 |
| **DDL** | Product Context: "Security-first. Trust paramount." |
| **Giải pháp** | Mask partial: hiển thị dạng ****7288, ****1232. Chỉ reveal đầy đủ sau xác thực biometrics/PIN |

---

#### UXP-002 · Critical
| **Màn hình** | Đổi phương thức tất toán/ rút gốc › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | OTP Resend Missing — DDL otp-input-1 spec yêu cầu canResend state + countdown timer + error state (red border, shake). Từ ảnh 1505: 6 ô tĩnh + nút "Xác nhận" KHÔNG có nút "Gửi lại mã", KHÔNG có countdown, KHÔNG có wrong-PIN artboard |
| **Gap ref** | Check #6, Check #7, Check #5 |
| **DDL** | COMP:otp-input-1 (canResend, timeLeft, countdown-timer-1 child, error state) |
| **Giải pháp** | Thêm: (1) Nút "Gửi lại mã" với countdown 60s; (2) Error state: 6 ô viền đỏ + shake animation + "Mã PIN không đúng. Còn {N} lần thử"; (3) Lock state... |

---

#### UXP-003 · Critical
| **Màn hình** | Xác thực khuôn mặt — Kết quả › Kết quả giao dịch |
|:---|:---|
| **Vấn đề** | Error Message Insufficient — Từ ảnh 1504: "Ảnh xác thực khuôn mặt không hợp lệ. Quý khách vui lòng thử lại" là generic error. Thiếu hướng dẫn cụ thể: lý do lỗi (ánh sáng, góc, cử động), không có retry count, không biết còn bao nhiêu lần thử |
| **Gap ref** | Check #2 |
| **DDL** | Product Context: "Trust paramount." UXG-183 (Error Recovery) |
| **Giải pháp** | Thêm: (1) Specific reason visubial (icon ánh sáng / góc mặt / cử động); (2) Retry counter "Lần thử X/3"; (3) Help link "Gặp vấn đề? Xem hướng dẫn" |

---

#### UXP-004 · Major
| **Màn hình** | Thông tin tài khoản tiết kiệm › Danh sách |
|:---|:---|
| **Vấn đề** | Information Overload — Từ ảnh 1500: 20+ fields liệt kê liên tục không section divider, không visual grouping, font size đồng nhất. Cognitive load cao. Screen dài 1131px (gấp 1.4× viewport) |
| **Gap ref** | Check #4, Check #6 |
| **DDL** | UXG-165, Hick's Law, Miller's Law |
| **Giải pháp** | Phân nhóm 4 sections với divider: (1) Thông tin cơ bản, (2) Kỳ hạn & Lãi suất, (3) Tích luỹ định kỳ, (4) Phương thức tất toán. Thêm scroll indicato... |

---

#### UXP-005 · Major
| **Màn hình** | Đổi phương thức tất toán/ rút gốc › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Confirmation Popup Button Hierarchy — Từ ảnh 1502-2: "Huỷ" và "Đồng ý" cùng style, không phân biệt primary/secondary action. User có thể nhầm |
| **Gap ref** | Check #3, Check #4 |
| **DDL** | UXG-165 |
| **Giải pháp** | "Đồng ý": filled primary button (background-primary, text-white). "Huỷ": text-only hoặc outlined secondary button |

---

#### UXP-006 · Major
| **Màn hình** | Đổi phương thức tất toán/ rút gốc › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Transaction Summary Missing in OTP — Từ ảnh 1505: Bottom-sheet Soft OTP chỉ có "nhập mã PIN". Thiếu transaction summary: đổi từ phương thức nào → phương thức nào. User không biết đang xác nhận thay đổi gì |
| **Gap ref** | Check #4, Check #3 |
| **DDL** | UXG-165, Product Context: "Trust paramount." |
| **Giải pháp** | Thêm summary dòng đầu bottom-sheet: "Thay đổi: Tất toán/ rút gốc online → Tại quầy" trước OTP input |

---

#### UXP-007 · Major
| **Màn hình** | Thông tin tài khoản tiết kiệm › Danh sách |
|:---|:---|
| **Vấn đề** | Success Popup Missing Details — Từ ảnh 1506: Popup thành công chỉ có checkmark + message "Quý khách đã thay đổi phương thức tất toán/ rút gốc thành công" + "Đóng". DDL receipt-preview-1 spec không được sử dụng. Thiếu: phương thức mới, thời gian, mã giao dịch |
| **Gap ref** | Check #7, Check #4, Check #6 |
| **DDL** | COMP:receipt-preview-1, UXG-165 |
| **Giải pháp** | Thêm: Phương thức mới "Tất toán/ rút gốc online", thời gian thay đổi, 1 button "Xem chi tiết tài khoản" bên cạnh "Đóng" |

---

#### UXP-008 · Major
| **Màn hình** | Xác thực khuôn mặt — Chụp › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Loading Feedback Missing — Từ ảnh 1503: Không có progress indicator trong quá trình auto-capture và xử lý ảnh. Doherty Threshold: feedback phải < 400ms. Thiếu loading-spinner-1 khi processing |
| **Gap ref** | Check #3 |
| **DDL** | COMP:loading-spinner-1, Doherty Threshold |
| **Giải pháp** | Thêm: (1) Circular progress trên khung oval khi processing; (2) Text "Đang xử lý..." dưới khung; (3) DDL loading-spinner-1 overlay khi verify serve... |

---

#### UXP-009 · Minor
| **Màn hình** | Đổi phương thức tất toán/ rút gốc › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | OTP Cell Size Mismatch — DDL otp-input-1 spec: cellSize=48px. Từ ảnh 1505: cells ước lượng ~44px (343px total / 6 cells ÷ spacing ≈ 44px). Thiếu active focus indicator trên cell đang nhập |
| **Gap ref** | Check #5, Check #6, Check #7 |
| **DDL** | COMP:otp-input-1 (cellSize=48px, activeIndex state) |
| **Giải pháp** | Tăng cell size lên 48px theo DDL spec. Thêm active border (2px solid primary) cho cell focus (activeIndex). Filled cells dùng dot mask |

---

#### UXP-010 · Minor
| **Màn hình** | Thông tin tài khoản tiết kiệm › Danh sách |
|:---|:---|
| **Vấn đề** | Bottom-menu Only 2 Items — Từ ảnh 1501: Bottom-menu "Chức năng khác" chỉ có 2 items (Giấy xác nhận, Đổi phương thức tất toán/ rút gốc). Thiếu title label mô tả context tài khoản (số tài khoản) trong header bottom-menu |
| **Gap ref** | Check #6, Check #4 |
| **DDL** | UXG-165 |
| **Giải pháp** | Thêm vào header bottom-menu: "Tài khoản ****7288 — Chức năng khác" để user xác nhận đang thao tác đúng tài khoản |

---

#### UXP-011 · Minor
| **Màn hình** | Xác thực khuôn mặt — Chụp › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | No Cancel Option — Từ ảnh 1503: Màn camera face scan không có nút "Huỷ" rõ ràng. Back arrow ở header nhỏ khó thấy. User bị "trapped" nếu muốn thoát |
| **Gap ref** | Check #4 |
| **DDL** | UXG-184 (User Control and Freedom) |
| **Giải pháp** | Thêm nút "Huỷ" / "Thoát" ở góc dưới hoặc text button rõ hơn bên dưới khung camera |

---

#### UXP-012 · Minor
| **Màn hình** | Xác thực khuôn mặt — Kết quả › Kết quả giao dịch |
|:---|:---|
| **Vấn đề** | Buttons Equal Weight — Từ ảnh 1504: "Thoát" và "Thử lại" cùng style, cùng prominence. Primary action (Thử lại) không được nhấn mạnh |
| **Gap ref** | Check #3 |
| **DDL** | UXG-165, Fitts's Law |
| **Giải pháp** | "Thử lại": filled primary button. "Thoát": outlined secondary hoặc text button |

---

## Chi tiết theo màn hình

### 1. Thông tin tài khoản tiết kiệm › Danh sách

> `SCR-TK4-001` · list · 3 artboards

**Score: 50% | Pass: 5 | Gap: 4 | Unverifiable: 1**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Header back/home affordance | Skill C | COMP:app-header-1 | Pass | Từ ảnh 1500: Back arrow (←) top-left, Home icon top-right, title "Thông tin tài khoản" centered. DDL app-header-1 spec: back + title + action — matched |
| 2 | Account info completeness | Skill C | UXG-165 | Pass | Từ ảnh 1500: Đầy đủ các trường key: Tên chủ TK, Số TK, Chi nhánh, Loại sản phẩm, Kỳ hạn, Ngày đáo hạn, Số dư, Lãi suất, Trạng thái |
| 3 | PII exposure — account numbers | Skill B+C | Product Context: Security-first | Gap | Từ ảnh 1500: "012547288" và "1231231232" hiển thị đầy đủ không mask. "Security-first" context yêu cầu partial masking cho sensitive financial data |
| 4 | Information hierarchy & grouping | Skill A+C | UXG-165, Hick's Law | Gap | Từ ảnh 1500: 20+ fields liệt kê liên tục không section divider, font size đồng nhất. Screen dài 1131px (gấp 1.4× viewport 812px). Cognitive load cao |
| 5 | Bottom-menu overlay discoverability | Skill C | UXG-165 | Pass | Từ ảnh 1500: "Chức năng khác" CTA rõ ràng ở bottom. Từ ảnh 1501: Bottom-menu overlay xuất hiện đúng với items liên quan |
| 6 | Bottom-menu context header | Skill B | UXG-165 | Gap | Từ ảnh 1501: Bottom-menu header chỉ ghi "Chức năng khác" không có context TK nào. Khi multiple accounts: không rõ đang thao tác TK nào |
| 7 | Success popup feedback | Skill C | COMP:receipt-preview-1, Peak-End Rule | Gap | Từ ảnh 1506: Popup chỉ có icon + message + "Đóng". Thiếu: phương thức mới, thời gian, mã giao dịch, nút "Xem chi tiết" |
| 8 | Touch targets bottom CTAs | Skill C | Fitts's Law | Pass | Từ ảnh 1500: Bottom nav ~88px height bao gồm các CTA. Touch target phù hợp ≥ 44px |
| 9 | Typography contrast | Skill C | WCAG AA | Pass | Từ ảnh 1500: Label text dark (#333) on white. Value text black on white. Est. contrast ≥ 7:1 — PASS WCAG AA |
| 10 | Scroll indicator for long content | Skill C | UXG-165 | Unverifiable | Screen 1131px vs ~812px viewport. Không thấy scroll indicator trong ảnh tĩnh. Cần kiểm tra trên device |

---

### 2. Đổi phương thức tất toán/ rút gốc › Form nhập thông tin

> `SCR-TK4-002` · form · 5 artboards

**Score: 50% | Pass: 6 | Gap: 5**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Radio button clarity | Skill C | UXG-165 | Pass | Từ ảnh 1502: Radio check (●) + label "Tất toán / rút gốc online" vs radio uncheck (○) + "Tại quầy". Selection state rõ ràng |
| 2 | Confirmation popup content | Skill C | UXG-165 | Pass | Từ ảnh 1502-2: "Thông báo" + "Quý khách có chắc chắn thay đổi phương thức tất toán/ rút gốc của tài khoản không?" — message đủ rõ ràng |
| 3 | Popup button hierarchy | Skill B+C | UXG-165 | Gap | Từ ảnh 1502-2: "Huỷ" và "Đồng ý" cùng style text button. Primary action (Đồng ý) không có visual prominence. Thiếu filled vs outlined phân biệt |
| 4 | Transaction summary in OTP sheet | Skill B+C | UXG-165, Product Context: Trust paramount | Gap | Từ ảnh 1505: Bottom-sheet Soft OTP chỉ có "nhập mã PIN". Thiếu tóm tắt giao dịch đang xác thực (đổi từ → sang phương thức nào) |
| 5 | OTP cell design & active state | Skill A+C | COMP:otp-input-1 | Gap | Từ ảnh 1505: 6 ô cells ~44px, không có active focus indicator. DDL spec: cellSize=48px, activeIndex state (2px primary border). Cả 2 specs thiếu |
| 6 | OTP resend mechanism | Skill A+C | COMP:otp-input-1 (canResend, countdown-timer-1) | Gap | Từ ảnh 1505: Không có "Gửi lại mã" button và không có countdown timer. DDL otp-input-1 spec yêu cầu canResend + timeLeft + countdown-timer-1 child |
| 7 | OTP error state for wrong PIN | Skill A | COMP:otp-input-1 (error state) | Gap | Không có artboard wrong-PIN scenario. DDL spec: error=true → red border cells, shake animation, error message với remaining attempts |
| 8 | Biometric error message clarity | Skill C | UXG-183 | Pass | Từ ảnh 1502-3: "Giao dịch yêu cầu xác thực bằng Facepay. Quý khách vui lòng đăng ký 'Thu thập sinh trắc học'..." — message đủ rõ lý do và hướng giải quyết |
| 9 | Expired ID error handling | Skill C | UXG-183 | Pass | Từ ảnh 1502-4: "Giấy tờ của Quý khách đã hết hạn. Quý khách vui lòng thu thập lại thông tin sinh trắc học..." + "Thay đổi" CTA — actionable error |
| 10 | Loading state for OTP verification | Skill A | COMP:loading-spinner-1, Doherty Threshold | Unverifiable | Không có artboard loading state khi verify Soft OTP. Cần spinner trên "Xác nhận" button khi processing |
| 11 | OTP security warning visibility | Skill C | UXG-165 | Pass | Từ ảnh 1505: "Lưu ý: Soft OTP sẽ bị khóa nếu Quý khách nhập sai PIN 5 lần liên tiếp" hiển thị rõ ở cuối bottom-sheet |
| 12 | Overlay dismiss affordance | Skill C | UXG-165 | Pass | Từ ảnh 1505: Close icon (×) top-right sheet. Từ ảnh 1502-2..4: blur background làm rõ popup area |

---

### 3. Xác thực khuôn mặt — Chụp › Form nhập thông tin

> `SCR-TK4-003` · form · 1 artboard

**Score: 50% | Pass: 3 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Camera framing instruction | Skill C | UXG-165 | Pass | Từ ảnh 1503: "Hãy điều chỉnh sao cho khuôn mặt nằm trong khung hình" + "Vui lòng nhìn thẳng" — instructions rõ ràng, concise |
| 2 | Voice guidance accessibility | Skill C | UXG-184 (Accessibility) | Pass | Từ ảnh 1503: Voice on icon (48×48px) top-right camera area. Hỗ trợ người dùng khiếm thị điều chỉnh khuôn mặt |
| 3 | Processing loading indicator | Skill A+C | COMP:loading-spinner-1, Doherty Threshold | Gap | Từ ảnh 1503: Không có progress indicator khi auto-capture. User không biết hệ thống đang xử lý hay chờ. Thiếu loading-spinner-1 overlay khi processing |
| 4 | Cancel/exit affordance | Skill B | UXG-184 (User Control and Freedom) | Gap | Từ ảnh 1503: Back arrow ở header nhỏ là cách thoát duy nhất. Thiếu explicit "Huỷ" button. User bị trapped khi không muốn tiếp tục face scan |
| 5 | Camera oval frame visual | Skill C | UXG-165 | Pass | Từ ảnh 1503: Khung oval rõ ràng trên camera live. Face image (người dùng) trong khung |
| 6 | Auto-capture feedback | Skill C | Hick's Law | Unverifiable | Không thể verify từ ảnh tĩnh: countdown / detection progress / real-time feedback khi khuôn mặt vào đúng khung |

---

### 4. Xác thực khuôn mặt — Kết quả › Kết quả giao dịch

> `SCR-TK4-004` · result · 1 artboard

**Score: 20% | Pass: 1 | Gap: 3**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Error visual indicator | Skill C | UXG-183 | Pass | Từ ảnh 1504: Viền đỏ oval trên khuôn mặt — visual indicator rõ ràng thể hiện lỗi. Color coding nhất quán (đỏ = lỗi) |
| 2 | Error message specificity | Skill B+C | UXG-183, Product Context: Trust paramount | Gap | Từ ảnh 1504: "Ảnh xác thực khuôn mặt không hợp lệ. Quý khách vui lòng thử lại" — generic message. Thiếu: lý do cụ thể (ánh sáng / góc / cử động), retry count (lần X/3) |
| 3 | Retry CTA prominence | Skill C | Fitts's Law | Gap | Từ ảnh 1504: "Thoát" và "Thử lại" cùng style button side-by-side. Primary action "Thử lại" không được phân biệt rõ ràng (should be filled/primary) |
| 4 | Retry attempt tracking | Skill B | Product Context: Security-first | Gap | Không có retry counter. User không biết còn bao nhiêu lần thử. Banking security yêu cầu giới hạn retry để chống brute force |
| 5 | Back button behavior | Skill C | UXG-184 | Unverifiable | Tap Back button → về màn hình nào? SCR-TK4-003 hay thoát hoàn toàn? Không verify được từ ảnh tĩnh |

---

## DDL References

| Ref | Type | Used in |
|:---|:---|:---|
| COMP:otp-input-1 | Component | SCR-TK4-002 (cell design, resend, error, activeIndex, countdown) |
| COMP:app-header-1 | Component | SCR-TK4-001 (header check) |
| COMP:loading-spinner-1 | Component | SCR-TK4-002, SCR-TK4-003 (loading state) |
| COMP:countdown-timer-1 | Component | SCR-TK4-002 (OTP resend countdown) |
| COMP:receipt-preview-1 | Component | SCR-TK4-001 (success popup details) |
| UXG-165 | Guideline | Multiple screens (labels, hierarchy, confirmation, feedback) |
| UXG-183 | Guideline | SCR-TK4-003, SCR-TK4-004 (error recovery, ARIA labels) |
| UXG-184 | Guideline | SCR-TK4-003, SCR-TK4-004 (user control and freedom, keyboard nav) |
| Fitts's Law | UX Law | SCR-TK4-001, SCR-TK4-002, SCR-TK4-004 (touch targets, CTAs) |
| Hick's Law | UX Law | SCR-TK4-001, SCR-TK4-002 (info overload, decision fatigue) |
| Doherty Threshold | UX Law | SCR-TK4-002, SCR-TK4-003 (loading feedback < 400ms) |
| Peak-End Rule | UX Law | SCR-TK4-001 (success popup positive ending) |
| Product: Security-first | Context | SCR-TK4-001, SCR-TK4-004 (PII, retry limits) |
| Product: Trust paramount | Context | SCR-TK4-002 (transaction summary), SCR-TK4-004 (error specificity) |
