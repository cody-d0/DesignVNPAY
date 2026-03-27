# UX Review Report — Chỉnh sửa cài đặt Voice OTT | Co-opBank Mobile Banking

**Product:** Co-opBank Mobile Banking  
**Section:** Cài đặt voice OTT › Chỉnh sửa cài đặt Voice  
**Figma:** `aYeSAVi94QlI4i4rL3xtmR` node `194:195719`  
**Generated:** 2026-03-23  
**Domain:** Banking  
**Screens reviewed:** 2  
**Total checks:** 24  
**Pass:** 12 | **Gap:** 11 | **Unverifiable:** 1  
**Simple Score:** 50%  
**Weighted Score:** 50%**Pass:** 0 | **Gap:** 0 | **Unverifiable:** 0  
**Simple Score:** 0%  
**Weighted Score:** 0%

> ⚠️ Overview counters replaced by ux-score-calculator.js after scoring.

---

## Methodology

Pipeline: Figma → OCR (2 rounds) → Boundary Detection (overlay-detect 7-signal, scores 11/12 × 2 overlays) → DDL Prefetch → Skills A+B+C.

| Layer | Source | Coverage |
|:---|:---|:---|
| Skill A | DDL component specs (`otp-input-1`, `text-input-1`, `app-header-1`, `empty-state-1`) | 2 screens |
| Skill B | 69 guidelines + banking product context (Security-first, Trust paramount) | All screens |
| Skill C | Agent Vision (4 screenshots: 7201, 7202, 7203, 7204) | All screens |
| DDL Laws | Fitts, Hick, Peak-End (auto-triggered per screen) | All screens |

---

## Chi tiết theo màn hình

### 1. Cài đặt Voice OTT › Form nhập thông tin (`SCR-VCE-001`)

> `SCR-VCE-001` · form · 2 artboards (7201 main + 7204 overlay success popup)

**Score: 70% | Pass: 7 | Gap: 3**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:-------:|:---------|
| 1 | Toggle switch hiển thị trạng thái ON/OFF không chỉ qua màu sắc | Skill C · C1 | UXG-180 | Pass | Từ ảnh 7201-chinh-sua-voice.png: Toggle ON có màu xanh navy + dấu tích trắng bên trong — affordance vượt qua color-only. Đúng UXG-180 |
| 2 | Toggle có label rõ ràng đi kèm (không chỉ icon) | Skill B · C1 | UXG-186 | Pass | Từ ảnh 7201-chinh-sua-voice.png: Label "Nhận thông báo BĐSD bằng giọng nói" cạnh toggle — đúng form label convention |
| 3 | Warning text "Lưu ý: KHÔNG" đủ nổi bật, không chỉ dựa vào chữ in hoa | Skill C · C3 | UXG-219 | Gap | Từ ảnh 7201-chinh-sua-voice.png: Text "Lưu ý: KHÔNG..." cùng màu body text, không có màu cảnh báo (amber/đỏ). Chỉ caps không đủ để phân biệt — rủi ro bị bỏ qua |
| 4 | Số tài khoản trong danh sách được masking (PII protection) | Skill B | UXG-180 | Gap | Từ ảnh 7201-chinh-sua-voice.png: "212312312313" / "312312312313" hiển thị đầy đủ. Banking: account numbers phải masked (e.g., ****2313). Inconsistent với OTP screen (mask phone) |
| 5 | CTA chính "Chỉnh sửa" có touch target ≥ 44px height | Skill C · C1 | UXG-165 | Pass | Từ ảnh 7201-chinh-sua-voice.png: "Chỉnh sửa" full-width, height ≈ 44px theo metadata 142:22886 — đạt Fitts's Law |
| 6 | Success popup "Thông báo" (7204): nút "Đóng" có affordance rõ dạng button | Skill C · C2 | UXG-204 | Gap | Từ ảnh 7204-chinh-sua-voice.png: "Đóng" được render dạng text-link màu xanh, không có border/background. Giảm affordance — user có thể không nhận ra là bấm được |
| 7 | Success popup body text đủ contrast trên nền popup | Skill C · C2 | UXG-219 | Pass | Từ ảnh 7204-chinh-sua-voice.png: Text tối trên nền trắng popup — contrast đạt WCAG AA (est. ≥4.5:1) |
| 8 | Nút "Nghe thử" — play icon + label đủ rõ để tương tác | Skill C · C3 | UXG-165 | Pass | Từ ảnh 7201-chinh-sua-voice.png: Icon play xanh tròn + text "Nghe thử" rõ, vị trí sau intro text hợp lý |
| 9 | Peak-End Rule: Success message "...thành công" đủ rõ và tích cực | DDL Law | peak-end | Pass | Từ ảnh 7204-chinh-sua-voice.png: "Quý khách đã cập nhật cài đặt...thành công" — nội dung rõ ràng, kết thúc flow tích cực |
| 10 | Hick's Law: 1 CTA duy nhất trên màn hình view — action hierarchy rõ ràng | DDL Law | hick | Pass | Từ ảnh 7201-chinh-sua-voice.png: 1 primary CTA "Chỉnh sửa" ở bottom, không có competing actions |

---

### 2. Chỉnh sửa cài đặt Voice › Form nhập thông tin (`SCR-VCE-002`)

> `SCR-VCE-002` · form · 2 artboards (7202 edit form + 7203 overlay OTP bottom sheet)

**Score: 36% | Pass: 5 | Gap: 8**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:-------:|:---------|
| 11 | Time picker fields dùng Clock icon (không phải Calendar) | Skill C · C1 | UXG-197 | Gap | Từ ảnh 7202-chinh-sua-voice.png: Các field "Từ"/"Đến" kèm **Calendar icon (📅)** — semantic mismatch. Time selection phải dùng Clock icon 🕐, không phải date picker icon |
| 12 | `otp-input-1` DDL spec: có "Gửi lại OTP" (canResend) trong bottom sheet | Skill A · C1 | COMP:otp-input-1 | Gap | Từ ảnh 7203-chinh-sua-voice.png: Bottom sheet OTP chỉ có 6 ô + "Xác nhận". **Thiếu hoàn toàn** "Gửi lại" trigger. DDL `otp-input-1` spec: `canResend` state là mandatory |
| 13 | `otp-input-1` DDL spec: có countdown timer (timeLeft) | Skill A · C1 | COMP:otp-input-1 | Gap | Từ ảnh 7203-chinh-sua-voice.png: Không có countdown "Gửi lại sau Xs". DDL `otp-input-1` spec: `timeLeft` state là mandatory. User không biết khi nào resend |
| 14 | OTP input cells — 6 ô, size đủ touch target (≥ 44px) | Skill C · C1 | UXG-165 | Pass | Từ ảnh 7203-chinh-sua-voice.png: 6 digit-input cells ≈ 44×44px per metadata (142:22828..142:22833) — đạt touch target |
| 15 | OTP: Số điện thoại được masking (bảo mật) | Skill C · C2 | UXG-180 | Pass | Từ ảnh 7203-chinh-sua-voice.png: "098****123" — masking đúng chuẩn Banking, chỉ lộ 3 số cuối |
| 16 | OTP paste support không bị block (UXG-254) | Skill B | UXG-254 | ⚠️ unverifiable | Không verify được từ static Figma. Cần kiểm tra tại implementation: UXG-254 (Never Block Paste) — các trường OTP không được dùng onPaste=preventDefault |
| 17 | Time picker: error state khi "Từ" > "Đến" invalid range | Skill A · C1 | UXG-257 | Gap | Từ ảnh 7202-chinh-sua-voice.png: Không có error state visible cho invalid time range. DDL `text-input-1` spec có `error` state — thiếu trong Figma variants |
| 18 | Số tài khoản trong edit form được masking | Skill C · C3 | UXG-180 | Gap | Từ ảnh 7202-chinh-sua-voice.png: "12312312313123" hiển thị đầy đủ trong list. Inconsistent: phone masked ở 7203 nhưng account không masked ở 7202 |
| 19 | Xóa tài khoản (−) có confirmation dialog trước khi xóa | Skill B | UXG-265 | Gap | Từ ảnh 7202-chinh-sua-voice.png: Icon (−) per account row, không rõ có confirm step. UXG-265 (Confirm Destructive Actions) — xóa tài khoản là destructive action |
| 20 | Dual CTA "Huỷ"/"Lưu chỉnh sửa" — touch target đủ (≥44px) | Skill C · C1 | UXG-165 | Pass | Từ ảnh 7202-chinh-sua-voice.png: CTA pair ≈ 167.5×48px — đạt Fitts's Law và touch target |
| 21 | Dual CTA — phân biệt rõ primary vs secondary | Skill C · C3 | UXG-204 | Pass | Từ ảnh 7202-chinh-sua-voice.png: "Huỷ" (outline/secondary) vs "Lưu chỉnh sửa" (filled/primary) — visual hierarchy rõ |
| 22 | "Lưu chỉnh sửa" có loading state sau submit (tránh double-submit) | Skill B | UXG-175 | Gap | Không thấy loading button state trong Figma 7202. Banking: submit → OTP trigger cần loading indicator. DDL `text-input-1`: missing loading/submitting state |
| 23 | OTP X close button — vị trí và close affordance rõ ràng | Skill C · C3 | UXG-178 | Pass | Từ ảnh 7203-chinh-sua-voice.png: Nút X top-right của bottom sheet — chuẩn close affordance |
| 24 | Hick's Law: form có nhiều interactive zones — cognitive load có thể cao | DDL Law | hick | Gap | Từ ảnh 7202-chinh-sua-voice.png: 5-6 interactive zones (add/remove accounts + time pickers + dual CTA). Hick's Law: cân nhắc visual grouping rõ hơn giữa sections để giảm cognitive load |

---

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Chỉnh sửa cài đặt Voice › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | OTP bottom sheet (7203) thiếu hoàn toàn "Gửi lại OTP" button và countdown timer |
| **Gap ref** | Check #12, #13 |
| **DDL** | COMP:otp-input-1 (canResend, timeLeft states) |
| **Giải pháp** | Thêm: (1) Countdown "Gửi lại sau 01:30" và (2) Link "Gửi lại" sau khi hết timeout. Đặt ngay dưới instruction text trong bottom sheet |

---

#### UXP-002 · Major
| **Màn hình** | Chỉnh sửa cài đặt Voice › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Time picker fields "Từ"/"Đến" dùng Calendar icon thay vì Clock icon — semantic mismatch |
| **Gap ref** | Check #11 |
| **DDL** | UXG-197 (Input Labels) |
| **Giải pháp** | Thay Calendar icon (📅) bằng Clock icon (🕐) cho 2 time-picker fields "Từ" và "Đến" trong màn hình 7202 |

---

#### UXP-003 · Major
| **Màn hình** | SCR-VCE-001 + SCR-VCE-002 |
|:---|:---|
| **Vấn đề** | Số tài khoản hiển thị đầy đủ trên cả view (7201) và edit (7202) — không mask PII |
| **Gap ref** | Check #4, #18 |
| **DDL** | UXG-180 (Color Only) — security principle Banking |
| **Giải pháp** | Mask account numbers: "212312312313" → "****2313". Nhất quán với phone masking tại OTP screen |

---

#### UXP-004 · Major
| **Màn hình** | Chỉnh sửa cài đặt Voice › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Thiếu inline error cho time picker khi "Từ" > "Đến" (invalid range) |
| **Gap ref** | Check #17 |
| **DDL** | UXG-257 (Inline Errors) · COMP:text-input-1 (error state) |
| **Giải pháp** | Thêm error state dưới time picker: "Thời gian bắt đầu phải nhỏ hơn thời gian kết thúc". Dùng red border + error text pattern |

---

#### UXP-005 · Major
| **Màn hình** | Chỉnh sửa cài đặt Voice › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Xóa tài khoản khỏi danh sách không có confirmation dialog — destructive action không được bảo vệ |
| **Gap ref** | Check #19 |
| **DDL** | UXG-265 (Confirm Destructive Actions) |
| **Giải pháp** | Khi tap (−): hiện confirmation bottom sheet "Xóa tài khoản ****2313 khỏi danh sách Voice OTT?" với CTA "Xóa" (destructive) + "Huỷ" |

---

#### UXP-006 · Major
| **Màn hình** | Chỉnh sửa cài đặt Voice › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | "Lưu chỉnh sửa" thiếu loading state sau khi submit — nguy cơ double-submit |
| **Gap ref** | Check #22 |
| **DDL** | UXG-175 (Loading Buttons) |
| **Giải pháp** | Sau tap "Lưu chỉnh sửa": button chuyển sang loading state (spinner + disabled) trong khi OTP bottom sheet loading |

---

#### UXP-007 · Minor
| **Màn hình** | Cài đặt Voice OTT › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Nút "Đóng" trong success popup (7204) là text-link, thiếu button affordance |
| **Gap ref** | Check #6 |
| **DDL** | UXG-204 (Submit Feedback) |
| **Giải pháp** | Style "Đóng" dưới dạng outlined button (border + padding) để rõ ràng là tappable element |

---

#### UXP-008 · Minor
| **Màn hình** | Cài đặt Voice OTT › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Warning "Lưu ý: KHÔNG để thiết bị ở chế độ im lặng" không đủ nổi bật |
| **Gap ref** | Check #3 |
| **DDL** | UXG-219 (Contrast Readability) |
| **Giải pháp** | Thêm icon cảnh báo (⚠️ amber) trước text, hoặc dùng warning text color (#D97706 amber) để phân biệt với body text |
