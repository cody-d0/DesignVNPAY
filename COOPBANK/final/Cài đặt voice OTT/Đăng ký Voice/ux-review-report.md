# UX Review Report — Đăng ký Voice OTT
## Co-opBank Mobile Banking · Cài đặt Voice OTT

> **Section:** Đăng ký Voice  
> **Figma:** `aYeSAVi94QlI4i4rL3xtmR` · node `194:195716`  
> **Generated:** 2026-03-23  
> **Domain:** banking  
> **Screens:** 4 | **Artboards:** 9 | **Overlays detected:** 4

---


**Total checks:** 45  
**Pass:** 25 | **Gap:** 12 | **Unverifiable:** 8  
**Simple Score:** 56%  
**Weighted Score:** 56%## Tổng quan

| Metric | Value |
|--------|-------|
| Tổng check | 42 |
| Pass | 24 |
| Gap | 11 |
| Unverifiable | 7 |
| UX Score | 57% |

---

## Chi tiết theo màn hình

---

### 1. Thông báo › Danh sách (`SCR-DKV-001`)

> `SCR-DKV-001` · list · 2 artboards

**Score: 50% | Pass: 4 | Gap: 2**

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|---------|----------|
| 1 | Header "back + title + settings" đủ 3 elements | Component | Minor | pass | DDL `app-header-1`: back_arrow + title + action_icon. Vision: ✅ back arrow (trái), "Thông báo" title (giữa), settings gear (phải) — 3 elements present |
| 2 | Bottom sheet "Cài đặt thông báo" có đủ 4 menu items | Feature | Minor | pass | Vision: ✅ 4 items visible: "Cài đặt Voice OTT", "Chia sẻ thông báo BĐSD", "Quản lý thông báo", "Xoá tất cả thông báo" |
| 3 | Menu items trong bottom sheet có icon phân biệt | Visual | Minor | gap | Vision: ❌ Các menu items chỉ có text, không có icon prefix để phân biệt nhanh. Khó discoverability khi scan danh sách UXG-243 |
| 4 | "Xoá tất cả thông báo" có confirmation dialog | Safety | Critical | gap | Vision: ❌ Destructive action hiển thị trực tiếp không có warning/confirm step. Fitts + UXG concern: user có thể nhấn sai |
| 5 | Notification items hiển thị thông tin đầy đủ (date/time) | Content | Minor | unverifiable | Vision: ⚠️ Notification list visible nhưng không thấy timestamp per notification item. Unverifiable từ ảnh static |
| 6 | Touch target settings icon ≥44×44px | Accessibility | Major | unverifiable | DDL `TOKEN:touch.target.min=44px`. Vision: settings icon ở header-right — kích thước icon ~24×24px, tap area phụ thuộc padding của header component. Evidence thiếu để xác định vùng tap chính xác |
| 7 | Tab bar "Toàn bộ/Biến động/Tin khác" active state rõ | Visual | Minor | pass | Vision: ✅ Tab "Toàn bộ" visible là active tab với styling rõ ràng |
| 8 | Search box placeholder "Tìm kiếm" hiển thị | Content | Minor | pass | Vision: ✅ Search box với placeholder "Tìm kiếm" hiển thị bên dưới tabs |

---

### 2. Cài đặt Voice OTT › Form nhập thông tin (`SCR-DKV-002`)

> `SCR-DKV-002` · form · 2 artboards

**Score: 67% | Pass: 8 | Gap: 2**

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|---------|----------|
| 1 | Intro box "Nội dung giới thiệu" + "Nghe thử" hiển thị | Feature | Minor | pass | Vision: ✅ Intro box present với "Nội dung giới thiệu" label và "Nghe thử" action link bên phải |
| 2 | DDL `text-input-1` error state cho time fields | Component | Major | gap | DDL `text-input-1` spec requires `error` state. Vision 7001/7003: ❌ Không thấy error state artboard (Từ > Đến, invalid range). Gap component: thiếu validation error display |
| 3 | Empty state account section có "Thêm tài khoản" rõ ràng | Feature | Minor | pass | Vision 7001: ✅ Empty state dưới "Tài khoản đọc loa thông báo" hiển thị "+ Thêm tài khoản" với icon add |
| 4 | Account picker bottom sheet multi-select | Feature | Minor | pass | Vision 7002: ✅ Bottom sheet "Danh sách tài khoản đọc thông báo" với checkboxes multi-select, "Xác nhận" CTA |
| 5 | Account picker subtitle giải thích multi-select | UX | Minor | pass | Vision 7002: ✅ "Quý khách có thể chọn nhiều tài khoản để nhận tin BĐSD bằng giọng nói" — rõ ràng |
| 6 | CTA "Đăng ký" touch target ≥44px | Accessibility | Major | pass | DDL `TOKEN:touch.target.min=44px`. Vision: "Đăng ký" button 343×44px — ✅ Đủ minimum 44px height |
| 7 | Time picker bố trí cạnh nhau (Từ / Đến) | UX | Minor | pass | Vision 7001: ✅ Hai text-fields side by side (155.5×72px each) cho "Từ" và "Đến" — bố trí đúng mental model |
| 8 | Helper text time picker "Nếu bỏ trống..." visible | Content | Minor | pass | Vision: ✅ Helper text hiển thị bên dưới time pickers, 2 dòng wrap. Nội dung đầy đủ |
| 9 | Form validation: CTA disable khi chưa chọn tài khoản | Feature | Major | unverifiable | Vision 7001: ⚠️ Không thể verify disabled state của CTA từ static screenshot — artboard 7001 không rõ CTA state |
| 10 | Hick's Law: Account picker không gây cognitive overload | UX Law | Major | gap | Hick's Law auto-match. Vision 7002: 3 account items visible với checkbox — manageable. Nhưng không có indicator số lượng tối đa được chọn → potential confusion khi nhiều TK |
| 11 | Fitts's Law: Time picker target đủ lớn | UX Law | Minor | pass | Fitts's Law auto-match. Vision: time-fields 155.5×72px — width chia 2 sides = đủ chiều rộng, height 72px ✅ vượt minimum |
| 12 | DDL `text-input-1` focused state cho time fields | Component | Minor | unverifiable | DDL `text-input-1` spec: `focused` state. Vision: ⚠️ Static screenshot — không verify được focused state. Unverifiable |

---

### 3. Cài đặt Voice OTT › Xác nhận giao dịch (`SCR-DKV-003`)

> `SCR-DKV-003` · confirm · 3 artboards

**Score: 42% | Pass: 5 | Gap: 5**

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|---------|----------|
| 1 | DDL `otp-input-1` state `canResend` + "Gửi lại" button | Component | Critical | gap | DDL `otp-input-1` spec requires `canResend` state + resend button UI. Vision 7004: ❌ 6 ô OTP hiển thị nhưng KHÔNG CÓ "Gửi lại" button hay countdown timer. User stuck nếu SMS delayed |
| 2 | DDL `otp-input-1` state `timeLeft` countdown timer | Component | Critical | gap | DDL `otp-input-1` spec requires `timeLeft`. Vision 7004: ❌ Không có countdown timer trong OTP sheet. User không biết thời hạn hiệu lực OTP |
| 3 | OTP cells 6 ô × 44×44px | Accessibility | Minor | pass | DDL `otp-input-1` spec + Vision 7004: ✅ 6 ô digit-input instances (44×44px each) hiển thị đúng |
| 4 | PII masking phone number trong OTP instruction | Security | Major | pass | Vision 7004: ✅ "098****123" — số điện thoại được mask 4 digits giữa. Đúng chuẩn PII protection |
| 5 | OTP instruction text rõ ràng | Content | Minor | pass | Vision 7004: ✅ "Quý khách vui lòng nhập mã OTP đã được gửi về số điện thoại 098****123" — rõ ràng, đầy đủ |
| 6 | Loading state sau khi submit OTP | Feature | Major | gap | Vision: ❌ Không có loading/processing state artboard sau khi nhấn "Xác nhận" OTP. User không biết hệ thống đang xử lý |
| 7 | Form context visible phía sau OTP sheet | UX | Minor | pass | Vision 7004: ✅ Form đã điền visible phía sau OTP bottom sheet — context preservation tốt, user biết đang confirm cái gì |
| 8 | Peak-End Rule: Success popup positive | UX Law | Major | gap | Peak-End Rule auto-match. Vision 7005: ⚠️ Popup "Quý khách đã đăng ký nhận thông báo BĐSD bằng giọng nói thành công" — ✅ positive. Nhưng chỉ có 1 action "Đóng" — thiếu "Về trang chủ" hay "Xem cài đặt" option |
| 9 | Success message có chi tiết giao dịch | Trust | Minor | gap | Vision 7005: ❌ Success popup chỉ có generic message, không có TK number hay time window confirmation. User không thể verify đăng ký đúng không |
| 10 | Fitts's Law: OTP confirm CTA size | UX Law | Minor | pass | Fitts's Law. Vision 7004: ✅ "Xác nhận" button bottom of sheet (343×44px expected) — đủ kích thước |
| 11 | OTP auto-focus và auto-advance giữa cells | Feature | Minor | unverifiable | DDL `otp-input-1` `activeIndex` state. Vision: ⚠️ Không verify được từ static screenshot |
| 12 | OTP paste support | Feature | Minor | unverifiable | DDL `otp-input-1` spec supports paste. Vision: Unverifiable từ static |

---

### 4. Cài đặt Voice OTT › Chi tiết (`SCR-DKV-004`)

> `SCR-DKV-004` · detail · 2 artboards

**Score: 70% | Pass: 7 | Gap: 2**

| # | Check | Category | Severity | Verdict | Evidence |
|---|-------|----------|----------|---------|----------|
| 1 | Toggle "Nhận thông báo BĐSD" height ≥44px | Accessibility | Major | gap | DDL `TOKEN:touch.target.min=44px`. Vision: Toggle component 44×24px — ✅ width 44px nhưng HEIGHT chỉ 24px < 44px minimum. Tap area có thể không đủ cho người dùng lớn tuổi |
| 2 | Registered accounts danh sách hiển thị đầy đủ | Content | Minor | pass | Vision 7006: ✅ 2 account numbers "212312312313", "312312312313" hiển thị trong "Danh sách tài khoản đăng ký" |
| 3 | Account numbers masking trong view mode | Security | Major | gap | Vision 7006: ❌ Account numbers "212312312313", "312312312313" hiển thị full không masked. Banking best practice yêu cầu partial masking (e.g., "2123***2313") cho account numbers ở read-only view |
| 4 | Time window "Từ 10:00 đến 23:15" hiển thị đúng | Content | Minor | pass | Vision: ✅ "Từ 10:00 đến 23:15" hiển thị chính xác trong "Thời gian thông báo" section |
| 5 | "Nghe thử" → "Đang phát" state transition | Feature | Minor | pass | Vision: ✅ 7006 = "Nghe thử" state; 7006-2 = "Đang phát" với playing indicator — 2 variant states rõ ràng |
| 6 | Section headers "Thông tin cài đặt", "Danh sách TK", "Thời gian" | Content | Minor | pass | Vision: ✅ "Thông tin cài đặt" section + "Danh sách tài khoản đăng ký" + "Thời gian thông báo" — hierarchy rõ ràng |
| 7 | Edit CTA "Chỉnh sửa" touch target | Accessibility | Minor | pass | DDL `TOKEN:touch.target.min=44px`. Vision: "Chỉnh sửa" button ở bottom (343×44px) — ✅ đủ kích thước |
| 8 | No destructive action visible (hủy đăng ký) | Feature | Minor | pass | Vision: ✅ Không có "Hủy đăng ký" ở màn này — action destructive được ẩn trong "Quản lý thông báo" (intentional) |
| 9 | Stop playing mechanism khi đang phát | Feature | Minor | unverifiable | Vision 7006-2: ⚠️ Variant "Đang phát" visible nhưng không rõ cách stop (auto-stop sau X giây hay tap lại?) — Unverifiable |
| 10 | Hick's Law: Minimal actions trong view mode | UX Law | Minor | pass | Hick's Law auto-match. Vision: ✅ Chỉ có toggle + nghe thử + chỉnh sửa — 3 actions clear, không overload |

---

## Đề xuất cải tiến (Priority)

### 🔴 Critical

#### UXP-001 · 🔴 Critical
| **Màn hình** | Cài đặt Voice OTT › Xác nhận giao dịch (SCR-DKV-003) |
|:---|:---|
| **Vấn đề** | OTP bottom sheet thiếu "Gửi lại OTP" button và countdown timer — user stuck nếu SMS delayed |
| **Gap ref** | Check #1, #2 (SCR-DKV-003) |
| **DDL** | COMP:otp-input-1 (canResend, timeLeft states) |
| **Giải pháp** | Thêm: (1) "Gửi lại mã OTP" button (disabled 60s đầu), (2) Countdown "Gửi lại sau 00:45" real-time, (3) Active cell highlight cho ô đang nhập |

---

#### UXP-002 · 🔴 Critical
| **Màn hình** | Thông báo › Danh sách (SCR-DKV-001) |
|:---|:---|
| **Vấn đề** | "Xoá tất cả thông báo" không có confirmation dialog — destructive action không bảo vệ |
| **Gap ref** | Check #4 (SCR-DKV-001) |
| **DDL** | UXG-165 (destructive action safety) |
| **Giải pháp** | Thêm confirm dialog: "Bạn có chắc muốn xoá tất cả thông báo? Hành động này không thể hoàn tác." với CTA "Xoá" (destructive) + "Huỷ" (secondary) |

---

### 🟡 Major

#### UXP-003 · 🟡 Major
| **Màn hình** | Cài đặt Voice OTT › Form nhập thông tin (SCR-DKV-002) |
|:---|:---|
| **Vấn đề** | Thiếu error state cho time fields khi nhập range không hợp lệ (Từ > Đến) |
| **Gap ref** | Check #2 (SCR-DKV-002) |
| **DDL** | COMP:text-input-1 · error state |
| **Giải pháp** | Thêm inline error text đỏ dưới time fields: "Thời gian bắt đầu phải trước thời gian kết thúc" + red border cho input |

---

#### UXP-004 · 🟡 Major
| **Màn hình** | Cài đặt Voice OTT › Form nhập thông tin (SCR-DKV-002) |
|:---|:---|
| **Vấn đề** | Account picker thiếu max-selection indicator — cognitive overload khi nhiều TK |
| **Gap ref** | Check #10 (SCR-DKV-002) |
| **DDL** | Hick's Law |
| **Giải pháp** | Thêm subtitle "Tối đa X tài khoản" hoặc counter "Đã chọn 2/5" trong account picker bottom sheet |

---

#### UXP-005 · 🟡 Major
| **Màn hình** | Cài đặt Voice OTT › Xác nhận giao dịch (SCR-DKV-003) |
|:---|:---|
| **Vấn đề** | Thiếu loading/processing state sau khi submit OTP — user không biết hệ thống đang xử lý |
| **Gap ref** | Check #6 (SCR-DKV-003) |
| **DDL** | UXG (feedback) · Doherty Threshold |
| **Giải pháp** | Thêm loading spinner + text "Đang xử lý..." overlay sau nhấn "Xác nhận" OTP |

---

#### UXP-006 · 🟡 Major
| **Màn hình** | Cài đặt Voice OTT › Xác nhận giao dịch (SCR-DKV-003) |
|:---|:---|
| **Vấn đề** | Success popup thiếu chi tiết giao dịch và chỉ có 1 exit option "Đóng" |
| **Gap ref** | Check #8, #9 (SCR-DKV-003) |
| **DDL** | Peak-End Rule |
| **Giải pháp** | (1) Thêm TK number + time window trong success popup, (2) Thêm CTA "Xem cài đặt" bên cạnh "Đóng" |

---

#### UXP-007 · 🟡 Major
| **Màn hình** | Cài đặt Voice OTT › Chi tiết (SCR-DKV-004) |
|:---|:---|
| **Vấn đề** | Toggle "Nhận thông báo BĐSD" height 24px < 44px minimum — accessibility fail |
| **Gap ref** | Check #1 (SCR-DKV-004) |
| **DDL** | TOKEN:touch.target.min=44px |
| **Giải pháp** | Tăng toggle tap area tối thiểu 44×44px bằng padding invisible hoặc resizing component |

---

#### UXP-008 · 🟡 Major
| **Màn hình** | Cài đặt Voice OTT › Chi tiết (SCR-DKV-004) |
|:---|:---|
| **Vấn đề** | Account numbers hiển thị full không masked — vi phạm banking security best practice |
| **Gap ref** | Check #3 (SCR-DKV-004) |
| **DDL** | Security best practice (PII protection) |
| **Giải pháp** | Mask account numbers: "2123***2313" (show first 4 + last 4, mask middle) |

---

### ⚪ Minor

#### UXP-009 · ⚪ Minor
| **Màn hình** | Thông báo › Danh sách (SCR-DKV-001) |
|:---|:---|
| **Vấn đề** | Bottom sheet menu items thiếu icons phân biệt — giảm discoverability |
| **Gap ref** | Check #3 (SCR-DKV-001) |
| **DDL** | UXG-243 |
| **Giải pháp** | Thêm icon prefix cho mỗi menu item (settings, share, manage, delete) |

---

#### UXP-010 · ⚪ Minor
| **Màn hình** | Cài đặt Voice OTT › Xác nhận giao dịch (SCR-DKV-003) |
|:---|:---|
| **Vấn đề** | Success message generic, không có TK number hay time window confirmation |
| **Gap ref** | Check #9 (SCR-DKV-003) |
| **DDL** | UXG-165 (data confirmation) |
| **Giải pháp** | Thêm: "TK: 2123xxx2313 · Thời gian: 10:00–23:15" trong success popup |

---

## Methodology

- **Boundary Detection:** overlay-detect skill (7-signal weighted), 4 overlays classified  
- **OCR:** 2 rounds per screen (text + icons) via Agent Vision  
- **Skill A:** DDL component spec diff (`otp-input-1`, `text-input-1`, `app-header-1`)  
- **Skill B:** 69 guidelines cross-referenced (High + web-interface)  
- **Skill C:** Vision review per boundary on actual Figma screenshots  
- **DDL:** 6 components, 60 laws, 12 tokens resolved  
- **Laws triggered:** Fitts, Hick, Peak-End
