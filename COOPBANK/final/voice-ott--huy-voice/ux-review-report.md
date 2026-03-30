# UX Audit — Huỷ Voice OTT · Co-opBank Mobile Banking

**Sản phẩm:** Co-opBank Mobile Banking  
**Section:** Cài đặt Voice OTT / Huỷ Voice OTT  
**Figma:** `aYeSAVi94QlI4i4rL3xtmR` · node `194:195718`  
**Ngày audit:** 2026-03-23  
**Pipeline:** figma-to-ux-review v1 · DDL-grounded · overlay-detect enabled  

---


**Total checks:** 35  
**Pass:** 19 | **Gap:** 11 | **Unverifiable:** 5  
**Simple Score:** 54%  
**Weighted Score:** 54%## Tổng quan

| Metric | Giá trị |
|--------|---------|
| Tổng check | 0 |
| Pass | 0 |
| Gap | 0 |
| Unverifiable | 0 |
| UX Score | 0% |
| Proposals (Critical / Major / Minor) | 0 / 0 / 0 |
| Màn hình reviewed | 2 |
| Overlays detected | 4 (popup ×3 + OTP bottom-sheet) |

---

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Huỷ Voice OTT › Chi tiết & Xác nhận |
|:---|:---|
| **Vấn đề** | OTP flow thiếu countdown timer và resend button |
| **Gap ref** | Check #3, Check #4 |
| **DDL** | COMP:otp-input-1 — `canResend`, `timeLeft`, `resendTimeout=60`; COMP:countdown-timer-1 |
| **Giải pháp** | Thêm countdown timer (DDL `countdown-timer-1`: `timeLeft` state, `isExpired`) bên dưới ô OTP. Thêm "Gửi lại OTP" button, disable cho đến khi hết 60... |

---

#### UXP-002 · Critical
| **Màn hình** | Huỷ Voice OTT › Chi tiết & Xác nhận |
|:---|:---|
| **Vấn đề** | Nội dung popup prerequisite (7100) có lỗi copy — câu lặp và thiếu rõ ràng |
| **Gap ref** | Check #12, Check #1 |
| **DDL** | UXG-243 — CTA label phải phản ánh đúng hành động; Banking product: Trust paramount |
| **Giải pháp** | Rewrite: "Quý khách cần đăng ký nhận thông báo BĐSD trước khi sử dụng tính năng Voice OTT. Vui lòng đăng ký tại mục Thông báo và Cảnh báo." Thêm CT... |

---

#### UXP-003 · Major
| **Màn hình** | Huỷ Voice OTT › Form cài đặt |
|:---|:---|
| **Vấn đề** | CTA label "Đăng ký" sai ngữ cảnh khi màn hình là chỉnh sửa |
| **Gap ref** | Check #1, Check #12 |
| **DDL** | UXG-243 — CTA clarity; COMP:app-header-1 — title context |
| **Giải pháp** | Thay "Đăng ký" bằng "Lưu thay đổi" khi màn hình được mở từ context chỉnh sửa. Hoặc: "Xác nhận" nếu đơn giản hơn. |

---

#### UXP-004 · Major
| **Màn hình** | Huỷ Voice OTT › Form cài đặt |
|:---|:---|
| **Vấn đề** | Time-picker fields thiếu error state và placeholder |
| **Gap ref** | Check #2, Check #3, Check #6 |
| **DDL** | COMP:text-input-1 — `error` state, `helper text`; UXG-165 |
| **Giải pháp** | Thêm placeholder "HH:mm" cho cả 2 fields. Thêm inline error: "Giờ bắt đầu phải nhỏ hơn giờ kết thúc" khi Từ ≥ Đến. DDL `text-input-1` spec: `error`... |

---

#### UXP-005 · Major
| **Màn hình** | Huỷ Voice OTT › Chi tiết & Xác nhận |
|:---|:---|
| **Vấn đề** | Destructive action (huỷ dịch vụ) thiếu visual distinction — "Đồng ý" không có màu destructive |
| **Gap ref** | Check #6 |
| **DDL** | TOKEN:base.destructive; Banking: "Trust paramount" — destructive actions cần visual warning |
| **Giải pháp** | Đổi màu button "Đồng ý" trong confirm dialog thành destructive color (DDL `base.destructive`). Hoặc đổi label thành "Huỷ dịch vụ" để rõ hơn ý định. |

---

#### UXP-006 · Minor
| **Màn hình** | Huỷ Voice OTT › Chi tiết & Xác nhận |
|:---|:---|
| **Vấn đề** | "Nghe thử" thiếu play state indicator |
| **Gap ref** | Check #16, Check #8, Check #10 |
| **DDL** | UXG-165 — System status visibility for media |
| **Giải pháp** | Thêm playing state: icon đổi sang pause, text đổi sang "Đang phát..." với animated indicator. Stop state khi hoàn thành. |

---

#### UXP-007 · Minor
| **Màn hình** | Huỷ Voice OTT › Chi tiết & Xác nhận; Huỷ Voice OTT › Form cài đặt |
|:---|:---|
| **Vấn đề** | Intro box "Nội dung giới thiệu" lặp lại trên cả 2 màn hình |
| **Gap ref** | Check #6, Check #16, Check #8 |
| **DDL** | UXG-165 — Content density optimization |
| **Giải pháp** | SCR-VOT-002 rút ngắn intro box: chỉ giữ warning "Lưu ý: KHÔNG để thiết bị im lặng" và "Nghe thử". Remove duplicated description text. |

---

#### UXP-008 · Minor
| **Màn hình** | Huỷ Voice OTT › Form cài đặt |
|:---|:---|
| **Vấn đề** | Empty account section thiếu visual guidance |
| **Gap ref** | Check #8, Check #6, Check #16 |
| **DDL** | COMP:empty-state-1; UXG-165 — Empty state clarity |
| **Giải pháp** | Thêm placeholder text: "Chưa có tài khoản nào. Nhấn + để thêm tài khoản nhận đọc loa." Validation: require ≥1 tài khoản trước khi enable CTA. |

---

## Chi tiết theo màn hình

### 1. Huỷ Voice OTT › Chi tiết & Xác nhận

> `SCR-VOT-001` · detail · 5 artboards (7101 main + 7100/7102/7103/7104 overlays)

**Score: 60% | Pass: 12 | Gap: 5**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|---------|
| 1 | Toggle ON/OFF visual state rõ ràng | Skill C (vision) | COMP:toggle | Pass | Từ ảnh 7101: toggle màu blue active, visually distinct với OFF state |
| 2 | OTP cell count = 6 (spec default) | Skill A (component) | COMP:otp-input-1 digitCount=6 | Pass | Từ ảnh 7103: đúng 6 ô digit-input trong soft-otp container |
| 3 | OTP countdown timer visible | Skill A (component) | COMP:otp-input-1 timeLeft; COMP:countdown-timer-1 | Gap | Từ ảnh 7103: KHÔNG có countdown timer — chỉ có 6 cells + "Xác nhận" button. DDL spec yêu cầu timeLeft state |
| 4 | OTP resend button visible | Skill A (component) | COMP:otp-input-1 canResend | Gap | Từ ảnh 7103: KHÔNG có resend button. DDL `canResend` state không được implement trong Figma |
| 5 | Confirm dialog có 2 actions Huỷ / Đồng ý | Skill C (vision) | UXG-165 | Pass | Từ ảnh 7102: Huỷ (secondary) và Đồng ý (primary) rõ ràng |
| 6 | Destructive action color differentiation | Skill B (guideline) | TOKEN:base.destructive; UXG-165 | Gap | Từ ảnh 7102: "Đồng ý" button dùng màu blue giống non-destructive action — không phân biệt với destructive intent |
| 7 | SĐT masking (OTP screen) | Skill B (banking) | Banking: Trust paramount | Pass | Từ ảnh 7103: "098****123" — đúng masking format banking |
| 8 | Back navigation available | Skill C (vision) | COMP:app-header-1 | Pass | Từ ảnh 7101: back arrow top-left visible |
| 9 | Home navigation available | Skill C (vision) | COMP:app-header-1 actions | Pass | Từ ảnh 7101: home icon top-right visible |
| 10 | Section header hierarchy | Skill C (vision) | UXG-165 | Pass | Từ ảnh 7101: "Nội dung giới thiệu" và "Thông tin cài đặt" phân cấp rõ bằng section-icon màu đỏ |
| 11 | Warning text KHÔNG im lặng visible | Skill C (vision) | UXG-243 | Pass | Từ ảnh 7101: "Lưu ý: KHÔNG để thiết bị ở chế độ im lặng" hiển thị trong intro box |
| 12 | Prerequisite popup có hướng dẫn action | Skill B (guideline) | UXG-243; Banking: Trust | Gap | Từ ảnh 7100: text lặp phrase "đăng ký nhận thông báo BĐSD" 2 lần. CTA "Đồng ý" không rõ user cần làm gì tiếp theo |
| 13 | Account numbers display (không masking) | Skill C (vision) | Banking policy | Pass | Từ ảnh 7101: 212312312313 và 312312312313 hiển thị đầy đủ — OK cho số TK |
| 14 | Thời gian thông báo hiển thị đúng format | Skill C (vision) | UXG-243 | Pass | Từ ảnh 7101: "Từ 10:00 đến 23:15" — format HH:mm rõ ràng |
| 15 | OTP close affordance (bottom-sheet) | Skill C (vision) | COMP:otp-input-1; UXG-165 | Unverifiable | Từ ảnh 7103: bottom-sheet có title "Xác thực giao dịch" — close X từ vision metadata có nhưng không rõ kích thước/vị trí trong ảnh static |
| 16 | "Nghe thử" play state indicator | Skill B (guideline) | UXG-165 | Gap | Từ ảnh 7101: chỉ có icon play_circle tĩnh, không có playing/stopped state indication |
| 17 | Fitts's Law — OTP cell touch target | Skill A (law: fitts) | COMP:otp-input-1 cellSize=48 | Unverifiable | DDL spec: cellSize=48px. Từ ảnh 7103: 6 cells trong ~343px width → est. ~57px per cell. Borderline OK nhưng không đo được chính xác từ screenshot |
| 18 | Peak-End Rule — success message quality | Skill A (law: peak-end) | UXG-243 | Pass | Từ ảnh 7104: "Quý khách đã huỷ đăng ký...thành công" — clear positive completion message |
| 19 | Hick's Law — dialog không quá nhiều options | Skill A (law: hick) | UXG-165 | Pass | Từ ảnh 7102: dialog chỉ có 2 options (Huỷ / Đồng ý) — cognitive load thấp |
| 20 | Loading state cho OTP submit | Skill B (banking: security) | COMP:app-header-1 | Unverifiable | Static artboard không thể xác nhận button loading state khi submit OTP |

---

### 2. Huỷ Voice OTT › Form cài đặt

> `SCR-VOT-002` · form · 1 artboard (7105)

**Score: 50% | Pass: 6 | Gap: 5**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|---------|
| 1 | CTA label phù hợp với context | Skill B (guideline) | UXG-243; COMP:app-header-1 | Gap | Từ ảnh 7105: CTA "Đăng ký" khi màn hình được trigger từ "Chỉnh sửa". Label không phản ánh đúng action (nên là "Lưu cài đặt" hoặc "Xác nhận") |
| 2 | Time-picker fields có placeholder | Skill C (vision) | COMP:text-input-1 | Gap | Từ ảnh 7105: fields "Từ" và "Đến" rỗng không có placeholder HH:mm — user không biết format nhập |
| 3 | Time-picker error validation state | Skill A (component) | COMP:text-input-1 error state | Gap | DDL `text-input-1` có `error` state. Artboard 7105 không show error state khi Từ ≥ Đến. Figma thiếu validation error screen |
| 4 | Back navigation available | Skill C (vision) | COMP:app-header-1 | Pass | Từ ảnh 7105: back arrow top-left visible |
| 5 | Home navigation available | Skill C (vision) | COMP:app-header-1 actions | Pass | Từ ảnh 7105: home icon top-right visible |
| 6 | Section icons visual hierarchy | Skill C (vision) | UXG-165 | Pass | Từ ảnh 7105: section icons màu đỏ phân cấp rõ (person icon + timer icon) |
| 7 | "Thêm tài khoản" action discoverable | Skill C (vision) | UXG-165 | Pass | Từ ảnh 7105: "+" icon + text "Thêm tài khoản" inline, rõ ràng và discoverable |
| 8 | Empty account state visual guidance | Skill B (guideline) | COMP:empty-state-1; UXG-165 | Gap | Từ ảnh 7105: account section trống chỉ có "+Thêm tài khoản" — không có hint/empty state text mô tả cần thêm gì |
| 9 | Calendar icon touch target (Fitts's Law) | Skill A (law: fitts) | COMP:text-input-1; UXG-165 | Unverifiable | DDL yêu cầu ≥44px. Từ ảnh 7105 calendar icons trông nhỏ (~24px icon trong 72px field) — field có vẻ đủ target nhưng icon hit area không verify được |
| 10 | Intro box length trên form screen | Skill B (guideline) | UXG-165 (aesthetic minimalism) | Gap | Từ ảnh 7105: full intro box (description + warning + Nghe thử) lặp lại identically từ SCR-VOT-001. Redundant content tốn viewport |
| 11 | Hick's Law — form sections không quá nhiều | Skill A (law: hick) | UXG-165 | Pass | Từ ảnh 7105: 2 sections (Tài khoản + Khung giờ) — cognitive load hợp lý |
| 12 | Warning text cảnh báo im lặng | Skill C (vision) | UXG-243 | Pass | Từ ảnh 7105: "Lưu ý: KHÔNG để thiết bị ở chế độ im lặng" visible trong intro box |

---

## DDL References

| Ref ID | Type | Value | Dùng ở |
|--------|------|-------|--------|
| COMP:otp-input-1 | Component | OTP/PIN input — `digitCount=6`, `canResend`, `timeLeft`, `resendTimeout=60` | SCR-VOT-001 Skill A |
| COMP:countdown-timer-1 | Component | Countdown timer — `timeLeft`, `isExpired` | SCR-VOT-001 UXP-001 |
| COMP:text-input-1 | Component | Text input — `value`, `error`, `focused` states | SCR-VOT-002 Skill A |
| COMP:app-header-1 | Component | Mobile header — back, title, actions | Both screens |
| COMP:empty-state-1 | Component | Empty state — icon + title + description + CTA | SCR-VOT-002 UXP-008 |
| TOKEN:base.destructive | Token | Destructive action color | SCR-VOT-001 UXP-005 |
| UXG-165 | Guideline | Visibility / Empty state / Content clarity | Multiple checks |
| UXG-243 | Guideline | CTA clarity / Currency/format display | Multiple checks |
| fitts | UX Law | Touch target ≥44px | SCR-VOT-001 #17, SCR-VOT-002 #9 |
| peak-end | UX Law | Success message quality | SCR-VOT-001 #18 |
| hick | UX Law | Options count / Cognitive load | SCR-VOT-001 #19, SCR-VOT-002 #11 |
