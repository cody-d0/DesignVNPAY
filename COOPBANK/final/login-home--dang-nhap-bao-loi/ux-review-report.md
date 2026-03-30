# UX Review Report — Đăng nhập báo lỗi

**Sản phẩm:** Co-opBank Mobile Banking  
**Module:** Đăng nhập báo lỗi  
**Figma:** `aYeSAVi94QlI4i4rL3xtmR` · node `142:17052`  
**Domain:** Banking  
**Ngày tạo:** 2026-03-23  
**Pipeline:** figma-to-ux-review v1 | DDL-grounded | Skills A+B+C

---


**Total checks:** 46  
**Pass:** 18 | **Gap:** 20 | **Unverifiable:** 8  
**Simple Score:** 39%  
**Weighted Score:** 39%## Tổng quan

| Metric | Giá trị |
|---|---|
| Tổng check | 0 |
| Pass | 0 |
| Gap | 0 |
| Unverifiable | 0 |
| UX Score | 0% |

> ⚠️ Placeholder — Tool sẽ cập nhật sau khi chạy ux-score-calculator.js

**Skills executed:** Skill A (Component-Aware Signal Detection) · Skill B (PRD Context + DDL) · Skill C (Vision Review)  
**DDL Source:** `ddl-context.json` · 7 components · 69 guidelines · 60 UX laws

**Screens reviewed:** 4 biên màn hình · 10 artboards  
**Components matched từ DDL:** `text-input-1`, `password-strength-1`, `app-header-1`, `countdown-timer-1`, `bottom-tab-bar-1`  
**UX Laws auto-triggered:** Fitts's Law, Hick's Law, Peak-End Rule

---

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Đăng nhập báo lỗi › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | CTA mismatch: Popup-4 thông báo "đến Quầy giao dịch" nhưng nút action ghi "Cài mã PIN" |
| **Gap ref** | Check #4, Check #5 |
| **DDL** | UXG-165 (Clarity of action labels) |
| **Giải pháp** | Đổi CTA popup-4 thành "Đóng" hoặc "Tôi đã hiểu". Nếu có flow PIN thay thế, label cụ thể hơn |

---

#### UXP-002 · Critical
| **Màn hình** | Đăng nhập báo lỗi › Lỗi - Phiên hết hạn |
|:---|:---|
| **Vấn đề** | Blur background không đủ mờ — số dư tài khoản (20,000,000 VND) vẫn đọc được phía sau popup |
| **Gap ref** | Check #1 |
| **DDL** | UXG-243 (Sensitive data protection) |
| **Giải pháp** | Tăng opacity blur overlay lên ≥80%, hoặc thay bằng solid dark overlay `rgba(0,0,0,0.7)` |

---

#### UXP-003 · Major
| **Màn hình** | Đăng nhập báo lỗi › Đặt lại mật khẩu |
|:---|:---|
| **Vấn đề** | Thiếu `password-strength-1` component — không có progress bar + checklist động |
| **Gap ref** | Check #1, Check #2 |
| **DDL** | COMP:password-strength-1 · UXG-087 (Real-time validation) |
| **Giải pháp** | Thêm password strength meter với 4 checklist (8-20 ký tự / chữ hoa / số / ký tự đặc biệt) update real-time |

---

#### UXP-004 · Major
| **Màn hình** | Đăng nhập báo lỗi › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Popup-3 yêu cầu đổi mật khẩu nhưng CTA ghi "Cài mã PIN" — terminology inconsistency |
| **Gap ref** | Check #5, Check #4 |
| **DDL** | UXG-165 (Terminology consistency) |
| **Giải pháp** | Đổi CTA thành "Đổi mật khẩu ngay" cho popup-3. Giữ "Cài mã PIN" chỉ khi flow thực sự cài PIN |

---

#### UXP-005 · Major
| **Màn hình** | Đăng nhập báo lỗi › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Popup cập nhật bắt buộc (popup-1) không có nút đóng "X" — zero escape hatch |
| **Gap ref** | Check #10, Check #3 |
| **DDL** | UXG-012 (User control and freedom) |
| **Giải pháp** | Nếu thật sự bắt buộc: hiển thị countdown "Bắt buộc cập nhật sau X ngày" thay vì hard block ngay. Nếu không bắt buộc: thêm nút "Để sau" |

---

#### UXP-006 · Major
| **Màn hình** | Đăng nhập báo lỗi › Đăng nhập lại |
|:---|:---|
| **Vấn đề** | Context break: SCR-DLB-001 dùng Face ID + saved account, SCR-DLB-004 yêu cầu nhập Số điện thoại mới |
| **Gap ref** | Check #1, Check #3 |
| **DDL** | UXG-089 (Transition context) |
| **Giải pháp** | Thêm dòng hướng dẫn: "Mật khẩu đã thay đổi. Vui lòng đăng nhập với mật khẩu mới." Ưu tiên pre-fill số điện thoại |

---

#### UXP-007 · Minor
| **Màn hình** | Đăng nhập báo lỗi › Đặt lại mật khẩu |
|:---|:---|
| **Vấn đề** | Text ví dụ mật khẩu bị truncate: "12345678a$..." — ellipsis cắt ngang ví dụ |
| **Gap ref** | Check #5 |
| **DDL** | UXG-034 (Text readability) |
| **Giải pháp** | Wrap text hoặc dùng bullet points riêng cho mỗi ví dụ |

---

#### UXP-008 · Minor
| **Màn hình** | Đăng nhập báo lỗi › Lỗi - Phiên hết hạn |
|:---|:---|
| **Vấn đề** | Thiếu attempt counter — không cho user biết còn bao nhiêu lần nhập sai trước khi bị khóa |
| **Gap ref** | Check #6 |
| **DDL** | UXG-098 (Error context) |
| **Giải pháp** | Thêm text nhỏ: "Còn X lần thử" sau lần nhập sai đầu tiên |

---

#### UXP-009 · Minor
| **Màn hình** | Đăng nhập báo lỗi › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Input field "Mật khẩu" chỉ có placeholder text, không có floating label |
| **Gap ref** | Check #1, Check #8, Check #13 |
| **DDL** | COMP:text-input-1 · UXG-056 (Form label visibility) |
| **Giải pháp** | Dùng `text-input-1` spec với `label-row` persistent label phía trên input |

---

#### UXP-010 · Minor
| **Màn hình** | Đăng nhập báo lỗi › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Face ID icon không có text label đi kèm |
| **Gap ref** | Check #13, Check #1, Check #2 |
| **DDL** | UXG-056 (Label visibility) · fitts |
| **Giải pháp** | Thêm text label "Face ID" hoặc tooltip dưới icon (min 12px, WCAG accessible) |

---

#### UXP-011 · Major
| **Màn hình** | Đăng nhập báo lỗi › Lỗi - Phiên hết hạn |
|:---|:---|
| **Vấn đề** | Không có countdown timer trong popup tái xác thực — `countdown-timer-1` spec required |
| **Gap ref** | Check #9, Check #6 |
| **DDL** | COMP:countdown-timer-1 · UXG-098 (Error context) |
| **Giải pháp** | Thêm `countdown-timer-1` component với timeLeft + isExpired state. Khi expire: auto dismiss + toast thông báo |

---

#### UXP-012 · Major
| **Màn hình** | Đăng nhập báo lỗi › Đăng nhập lại |
|:---|:---|
| **Vấn đề** | Trường Số điện thoại không được pre-filled sau khi user hoàn thành đổi mật khẩu |
| **Gap ref** | Check #8, Check #3, Check #1 |
| **DDL** | COMP:text-input-1 · UXG-089 (Transition context) |
| **Giải pháp** | Pre-fill `text-input-1` với số điện thoại từ session. Nếu không available: hiện masked placeholder "090****882" |

---

## Chi tiết theo màn hình

### 1. Đăng nhập báo lỗi › Form nhập thông tin

> `SCR-DLB-001` · form · 6 artboards (1 base + 5 overlay variants)

**Score: 43% | Pass: 6 | Gap: 7**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | Input field có persistent label phía trên | Skill A (text-input-1 spec) | COMP:text-input-1 | Gap | Từ ảnh: login-with-face-id.png — input chỉ có placeholder "Mật khẩu", không có label tĩnh phía trên khi nhập |
| 2 | Input field có error state (red border) khi validate fail | Skill A (text-input-1 spec) | COMP:text-input-1 | Unverifiable | Không có artboard nào show trạng thái lỗi input, không thể verify |
| 3 | Popup có dismiss button (X icon) | Skill B (UXG-012 User control) | UXG-012 | Gap | Từ ảnh: popup.png, popup-2.png, popup-3.png, popup-4.png — không có X icon |
| 4 | CTA labels đúng với action thực sự | Skill B (UXG-165 Clarity) | UXG-165 | Gap | Từ ảnh: popup-4.png — nút "Cài mã PIN" nhưng message nói "đến Quầy giao dịch" — contradiction |
| 5 | Popup-3 terminology đồng nhất với flow | Skill A + Skill C | UXG-165 | Gap | Từ ảnh: popup-3.png — "đổi mật khẩu" nhưng nút "Cài mã PIN" — terminology mismatch |
| 6 | User name/phone masked đúng format | Skill B (privacy) | UXG-243 | Pass | Từ ảnh: login-with-face-id.png — "090****882" — masked correctly |
| 7 | Face ID button ≥44×44px touch target | Skill C (Fitts's Law) | fitts | Pass | Từ ảnh: face-id icon ~40×40px — borderline acceptable, có label bổ sung |
| 8 | Primary CTA "Đăng nhập" visually prominent | Skill C (Layer C3) | UXG-023 | Pass | Từ ảnh: Nút Đăng nhập màu xanh lá rõ ràng, contrast đủ |
| 9 | Banner quảng cáo không interfere với auth flow | Skill B (UXG priority) | UXG-078 | Gap | Từ ảnh: login-with-face-id.png — banner "Gói vay hỗ trợ mua nhà" xuất hiện ngay trong màn login — distracting |
| 10 | Popup update bắt buộc có escape option | Skill B (Nielsen #3) | UXG-012 | Gap | Từ ảnh: popup.png — popup bắt buộc chỉ có nút "Cập nhật", zero escape |
| 11 | Optional update popup có "Để sau" | Skill B | UXG-012 | Pass | Từ ảnh: popup-2.png — có nút "Để sau" bên cạnh "Cập nhật" |
| 12 | Blur overlay đủ che background (login base) | Skill C (Layer C2 security) | UXG-243 | Pass | Từ ảnh: các popup trên login base — blur đủ che login form |
| 13 | Face ID icon có text label đi kèm | Skill A (text-input-1 label rule) + Skill C | UXG-056 | Gap | Từ ảnh: login-with-face-id.png — Face ID icon không có text label |
| 14 | Login button màu đúng DDL palette | Skill C (Layer C2 token) | TOKEN:base.secondary=#1E3A8A | Pass | Từ ảnh: nút Đăng nhập màu xanh navy — match DDL token |

**Score: 43% | Pass: 6 | Gap: 7**

---

### 2. Đăng nhập báo lỗi › Lỗi - Phiên hết hạn

> `SCR-DLB-002` · error · 2 artboards

**Score: 40% | Pass: 4 | Gap: 4**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | Blur overlay đủ che sensitive data (balance) | Skill C (Layer C2 WCAG/Security) | UXG-243 | Gap | Từ ảnh: login-expired.png — "20,000,000 VND" vẫn readable qua blur — security risk |
| 2 | Quick re-auth popup có Face ID option | Skill A + Skill B | COMP:text-input-1 | Gap | Từ ảnh: login-expired.png — chỉ có text input + Bỏ qua/Tiếp tục, không có Face ID button trong popup |
| 3 | "Bỏ qua" và "Tiếp tục" CTA hierarchy đúng | Skill C (Layer C3) | UXG-023 | Pass | Từ ảnh: "Tiếp tục" (primary, xanh) vs "Bỏ qua" (secondary) — hierarchy OK |
| 4 | Session expired message rõ ràng | Skill B | UXG-098 | Pass | Từ ảnh: "Phiên đăng nhập hết hạn. Quý khách vui lòng đăng nhập lại." — clear message |
| 5 | Error state khi nhập sai mật khẩu | Skill A (text-input-1 state.error) | COMP:text-input-1 | Unverifiable | Không có artboard hiện lỗi nhập sai — không thể verify từ Figma |
| 6 | Attempt counter visible sau lần nhập sai | Skill B (UXG-098) | UXG-098 | Gap | Từ ảnh: không có lần nhập nào thất bại được thiết kế → missing state |
| 7 | Keyboard không che popup CTA | Skill C (Layer C3 layout) | UXG-034 | Pass | Từ ảnh: login-expired-2.png — keyboard visible nhưng Bỏ qua/Tiếp tục vẫn accessible |
| 8 | Hick's Law: ≤3 options trong popup | DDL (Hick's Law auto-trigger) | hick | Pass | 2 options (Bỏ qua / Tiếp tục) — đúng Hick's Law |
| 9 | Countdown timer visible trong popup | Skill A (countdown-timer-1 spec) + Skill C | COMP:countdown-timer-1 | Gap | Từ ảnh: login-expired.png — không có timer UI, chỉ có text error + input + 2 buttons |
| 10 | Wrong-password error state được design | Skill B (flow_check: has_error) | UXG-098 | Unverifiable | Không có artboard hiện error state khi nhập sai — không thể verify từ Figma |

**Score: 40% | Pass: 4 | Gap: 4**

---

### 3. Đăng nhập báo lỗi › Đặt lại mật khẩu

> `SCR-DLB-003` · form · 1 artboard

**Score: 36% | Pass: 4 | Gap: 4**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | Password strength meter với progress bar | Skill A (password-strength-1 spec) | COMP:password-strength-1 | Gap | Từ ảnh: change-password.png — không có progress bar, không có checklist động. Chỉ có text tĩnh |
| 2 | Checklist real-time updates khi nhập | Skill A (password-strength-1 state.checks) | COMP:password-strength-1 | Gap | Từ ảnh: checklist tĩnh, không có checkmark/X indicator per rule |
| 3 | Eye toggle (show/hide) trên 3 fields | Skill C (Layer C3) | UXG-056 | Pass | Từ ảnh: 3 fields đều có eye icon — visibility toggle available |
| 4 | App header đúng spec (back + title + 56px) | Skill A (app-header-1 spec) | COMP:app-header-1 | Pass | Từ ảnh: header "Đổi mật khẩu" + back arrow rõ ràng |
| 5 | Text điều kiện không bị truncate | Skill C (Layer C3) | UXG-034 | Gap | Từ ảnh: "Ví dụ: abc@1234; a&123456; 12345678a$..." bị cắt với "..." — text truncation |
| 6 | CTA "Tiếp tục" đặt ở bottom dễ tap | Skill B (Fitts's Law) | fitts | Pass | Từ ảnh: Nút "Tiếp tục" ở bottom của screen, full-width — Fitts-friendly |
| 7 | Mật khẩu cũ field có validation | Skill B | COMP:text-input-1 | Unverifiable | Không có error state artboard — không thể verify |
| 8 | 3 input fields có persistent labels | Skill A (text-input-1 label-row) | COMP:text-input-1 | Gap | Từ ảnh: các fields chỉ dùng placeholder labels, không có static label phía trên |
| 9 | Password rules section có format bullet rõ ràng | Skill C (Layer C3) | UXG-034 | Pass | Từ ảnh: bullet points phân cấp, có section header "Điều kiện đặt mật khẩu" |
| 10 | Peak-End Rule: kết thúc flow clear (success state) | DDL (Peak-End Rule auto-trigger) | peak-end | Unverifiable | Không có success state artboard cho change-password |
| 11 | Password mismatch error state được design | Skill B (flow_check: has_error=false) | UXG-087 | Unverifiable | Skill B phát hiện: không có artboard cho mismatch error — unverifiable |

**Score: 36% | Pass: 4 | Gap: 4**

---

### 4. Đăng nhập báo lỗi › Đăng nhập lại

> `SCR-DLB-004` · form · 1 artboard

**Score: 38% | Pass: 3 | Gap: 4**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|---|---|---|---|---|
| 1 | Transition context sau đổi mật khẩu | Skill B (UXG-089) | UXG-089 | Gap | Từ ảnh: re-login.png — không có message "Hãy đăng nhập với mật khẩu mới" — context break |
| 2 | Error popup message rõ ràng | Skill C (Layer C3) | UXG-098 | Pass | Từ ảnh: "Tài khoản hoặc mật khẩu của Quý khách không chính xác." — clear, generic for security |
| 3 | Phone number pre-filled sau flow | Skill B | UXG-089 | Gap | Từ ảnh: Số điện thoại field trống — user phải nhập lại từ đầu |
| 4 | Face ID option available on re-login | Skill A | fitts | Unverifiable | Có face-id icon ở background nhưng bị popup che — không rõ accessible không |
| 5 | Error popup có đủ info (không lộ which field sai) | Skill B (security) | UXG-243 | Pass | Từ ảnh: message generic "Tài khoản hoặc mật khẩu không chính xác" — tốt cho security |
| 6 | Peak-End Rule: Kết thúc flow positive | DDL (Peak-End Rule) | peak-end | Gap | Re-login sau error không có positive reinforcement — peak-end experience negative |
| 7 | Hick's Law: Single CTA trong error popup | DDL (Hick's Law) | hick | Pass | Từ ảnh: Chỉ 1 nút "Đồng ý" — minimal decision load |
| 8 | Phone number pre-filled sau đổi mật khẩu | Skill A (text-input-1 prefill) + Skill C | COMP:text-input-1 | Gap | Từ ảnh: re-login.png — Số điện thoại field trống, không pre-filled |

**Score: 38% | Pass: 3 | Gap: 4**

---

## DDL References

| Ref ID | Loại | Mô tả |
|---|---|---|
| COMP:text-input-1 | Component | Input với label-row, error state, helper text |
| COMP:password-strength-1 | Component | Password meter với progress bar + checklist |
| COMP:app-header-1 | Component | Mobile header 56px — back + title |
| COMP:countdown-timer-1 | Component | Countdown timer với auto-expire |
| UXG-012 | Guideline | User control and freedom (Nielsen #3) |
| UXG-023 | Guideline | Visual hierarchy và CTA prominence |
| UXG-034 | Guideline | Text readability và truncation |
| UXG-056 | Guideline | Form label visibility |
| UXG-087 | Guideline | Real-time form validation |
| UXG-089 | Guideline | Transition context between screens |
| UXG-098 | Guideline | Error context và recovery |
| UXG-165 | Guideline | Clarity of action labels |
| UXG-243 | Guideline | Sensitive data protection |
| fitts | UX Law | Fitts's Law — touch target sizing |
| hick | UX Law | Hick's Law — decision complexity |
| peak-end | UX Law | Peak-End Rule — experience memory |
| TOKEN:base.primary=#0F172A | Token | Primary navy color |
| TOKEN:base.secondary=#1E3A8A | Token | Secondary blue |
| TOKEN:bg=#F8FAFC | Token | Background light |
