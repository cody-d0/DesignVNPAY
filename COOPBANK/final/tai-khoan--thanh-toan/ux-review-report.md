# UX Review Report — Tài khoản thanh toán | Co-opBank Mobile Banking

**Product:** Co-opBank Mobile Banking  
**Section:** tài khoản thanh toán  
**Figma:** `aYeSAVi94QlI4i4rL3xtmR` node `142:17452`  
**Generated:** 2026-03-23  
**Domain:** Banking  
**Screens reviewed:** 4  
**Total checks:** 34  
**Pass:** 14 | **Gap:** 20 | **Unverifiable:** 0  
**Simple Score:** 41%  
**Weighted Score:** 41%**Pass:** 0 | **Gap:** 0 | **Unverifiable:** 0  
**Simple Score:** 0%  
**Weighted Score:** 0%

> ⚠️ Overview counters replaced by ux-score-calculator.js after scoring.

---

## Methodology

Pipeline: Figma → OCR (2 rounds) → Boundary Detection (overlay-detect 7-signal) → DDL Prefetch → Skills A+B+C.

| Layer | Source | Coverage |
|:---|:---|:---|
| Skill A | DDL component specs (`accordion-1`, `card-1`, `bottom-sheet-1`, `calendar-1`) | 4 screens |
| Skill B | 69 guidelines + banking product context | All screens |
| Skill C | Agent Vision (14 screenshots reviewed) | All screens |
| DDL Laws | Fitts, Hick, Miller, Zeigarnik, Peak-End (auto-triggered) | All screens |

---

## Chi tiết theo màn hình

### 1. Tài khoản › Danh sách (`SCR-TAT-001`)

> `SCR-TAT-001` · list · 3 artboards

**Score: 56% | Pass: 5 | Gap: 4**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:-------:|:---------|
| 1 | Accordion label count badge rõ ràng và accurate | Skill A · C1 | COMP:accordion-1 | Pass | Từ ảnh account.png: "Tài khoản thanh toán (2)" — count badge chính xác, rõ ràng |
| 2 | Copy action có visual feedback (toast) ngay lập tức | Skill B · C2 | UXG-165 | Pass | Từ ảnh account-2.png: Toast "Đã chép số tài khoản thành công" xuất hiện ngay sau copy — đúng pattern |
| 3 | Copy icon touch target ≥44pt (Fitts's Law) | DDL Law | fitts | Gap | Từ ảnh account.png: Copy icon cạnh số TK nhỏ (~24pt) — ước tính touch target <44pt, vi phạm Fitts's Law |
| 4 | Loading state khi refresh data có indicator rõ ràng | Skill B | UXG-165 | Gap | Từ ảnh account.png: Không thấy loading indicator khi tap refresh icon — user không biết data đang load |
| 5 | TK mặc định được phân biệt rõ về visual (badge + color) | Skill C · C2 | — | Pass | Từ ảnh account.png: TK 12300123123000 có badge "Tài khoản mặc định" — phân biệt được với TK phụ |
| 6 | Section accordion mặc định expand TK thanh toán (primary) | Skill B | UXG-165 | Pass | Từ ảnh account.png: TK thanh toán expanded by default — đúng priority cho user |
| 7 | TK tiết kiệm và vay collapsed — có visual hint để expand | Skill B | — | Gap | Từ ảnh account.png: Chỉ có caret icon nhỏ, không có text gợi ý "Nhấn để xem" — discoverability thấp |
| 8 | Tổng số dư section header hiển thị đúng aggregate | Skill C | — | Gap | Từ ảnh account.png: Tổng 15,000,000 VND cho 2 TK (mỗi TK 5Mtr... tổng phải là 10Mtr) — có thể dữ liệu test inconsistent |
| 9 | Swipe-to-refresh hoặc pull-to-refresh pattern available | Skill B | — | Pass | Từ ảnh account.png: Refresh icon ở header top-right — acceptable alternative dù swipe là pattern chuẩn hơn |

---

### 2. Thông tin tài khoản › Chi tiết (`SCR-TAT-002`)

> `SCR-TAT-002` · detail · 4 artboards

**Score: 20% | Pass: 2 | Gap: 8**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:-------:|:---------|
| 10 | Thông tin fields được grouping theo nhóm logic (Hick's Law) | DDL Law | hick | Gap | Từ ảnh account-3.png + account-4.png: 12 fields flat list không có section header phân nhóm — cognitive overload vi phạm Hick's Law |
| 11 | Số dư thực tế và số dư khả dụng được explain bằng tooltip | Skill B | UXG-165 | Gap | Từ ảnh account-3.png: 2 fields balance kề nhau (cùng 12Mtr) không có giải thích khác biệt — user không hiểu tại sao giống nhau |
| 12 | "Lãi cộng dồn", "Số tiền phong tòa" có help text hoặc icon ⓘ | Skill B | UXG-165 | Gap | Từ ảnh account-3.png: Không có bất kỳ help icon hay tooltip cho thuật ngữ tài chính — user không self-service được |
| 13 | Modal confirm đặt TK mặc định: title cụ thể (không generic) | Skill B · C3 | — | Gap | Từ ảnh account-5.png: Modal title "Thông báo" — quá generic, không describe action. DDL: confirm dialog cần title context-aware |
| 14 | Sau set default: có badge success và undo/change option | Skill B | UXG-165 | Gap | Từ ảnh account-3.png: Badge "Tài khoản thanh toán mặc định" OK, nhưng không có cách undo từ cùng màn hình — thiếu user control |
| 15 | Loading spinner visible và ở position hợp lý | Skill C · C1 | — | Gap | Từ ảnh account-9.png: Spinner xuất hiện giữa header và content (bên dưới title) — vị trí không chuẩn, thường spinner overlay hoặc trong content area |
| 16 | Bottom nav badge hiển thị count có nghĩa | Skill C · C2 | — | Gap | Từ ảnh account-3.png: Bottom nav tabs có badge đỏ nhưng không có số — không rõ là notification, pending action, hay decoration |
| 17 | CTA button "Xác nhận" trong modal màu primary | Skill C · C2 | TOKEN:base.primary=#1E3A8A | Pass | Từ ảnh account-5.png: Nút "Xác nhận" màu navy blue — match brand token |
| 18 | Modal body text rõ ràng, súc tích, tên TK visible | Skill B · C3 | — | Pass | Từ ảnh account-5.png: Body "Quý khách có muốn đặt tài khoản 12332300011 làm tài khoản thanh toán mặc định?" — số TK visible, ý nghĩa rõ ràng |
| 19 | Scrollable content có visual hint (scroll indicator) | Skill B | — | Gap | Từ ảnh account-3.png: Screen bị cắt tại "Ngày mở tài khoản" — không có scroll indicator, user không biết còn nội dung |

---

### 3. My QR › Chi tiết (`SCR-TAT-003`)

> `SCR-TAT-003` · detail · 2 artboards

**Score: 60% | Pass: 3 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:-------:|:---------|
| 20 | QR code hiển thị rõ ràng, owner info đầy đủ | Skill C · C2 | — | Pass | Từ ảnh account-6.png: QR lớn, rõ nét; tên "NGUYEN HOANG KHAI", số TK, chi nhánh đầy đủ phía dưới |
| 21 | "Lưu ảnh" và "Chia sẻ" CTA rõ ràng, accessible | Skill C · C2 | — | Pass | Từ ảnh account-6.png: 2 buttons bottom — outlined (Lưu ảnh) và filled (Chia sẻ) — tap-friendly, accessible |
| 22 | QR có expiry/rotate mechanism để chống lạm dụng | Skill B | — | Gap | Từ ảnh account-6.png: QR static, không có expiry timer, không có bất kỳ security indicator nào — rủi ro bảo mật cho banking app |
| 23 | Tên feature "My QR" nhất quán với ngôn ngữ app (tiếng Việt) | Skill B | UXG-165 | Gap | Từ ảnh account-6.png: Label "My QR" tiếng Anh trong khi toàn bộ app sử dụng tiếng Việt — thiếu nhất quán localization |
| 24 | Save toast tự dismiss có visual check icon | Skill C · C1 | — | Pass | Từ ảnh account-7.png: Toast "Đã lưu ảnh mã QR thành công" có checkmark icon, dark bg — đúng success toast pattern |

---

### 4. Lịch sử giao dịch › Danh sách (`SCR-TAT-004`)

> `SCR-TAT-004` · list · 5 artboards

**Score: 40% | Pass: 4 | Gap: 6**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:-------:|:---------|
| 25 | Balance card ở top hiển thị context TK đang xem | Skill C · C2 | — | Pass | Từ ảnh transaction-history.png: Card "Tài khoản thanh toán mặc định" + số TK + số dư khả dụng — user biết đang xem TK nào |
| 26 | Quick filter chips (1 tuần/2 tuần/1 tháng) visible và tappable | Skill C · C1 | — | Pass | Từ ảnh transaction-history.png: Chips hiển thị rõ ràng, "1 tuần" active (dark bg) — discoverability và usability tốt |
| 27 | Transaction amount color coding (+ xanh / - đỏ) | Skill C · C2 | — | Pass | Từ ảnh transaction-history.png: +2,000,000 VND màu xanh, -2,000,000 VND màu đỏ — đúng banking convention |
| 28 | Transaction description đầy đủ hoặc expandable | Skill B · C3 | UXG-165 | Gap | Từ ảnh transaction-history.png: "MB (270832) (HA chuyen..." bị truncate ellipsis — không có tap-to-expand, user mất thông tin quan trọng |
| 29 | Clear filter button khi custom filter active | Skill B | UXG-165 | Gap | Từ ảnh transaction-historyfilter.png: Khi filter active, không có nút clear filter nhanh trên màn hình chính — UX friction cao |
| 30 | Tab "Toàn bộ/Tiền vào/Tiền ra" có count badge | Skill B | — | Gap | Từ ảnh transaction-history.png: Tabs không có count — user không biết có bao nhiêu tx mỗi loại trước khi tap |
| 31 | Empty state có illustration và CTA gợi ý action | Skill B | UXG-165 | Gap | Từ ảnh transaction-history-2.png: Chỉ có text "Không có kết quả tìm kiếm" — thiếu illustration, thiếu CTA, thiếu context message |
| 32 | Disclaimer giới hạn tra cứu ngắn gọn, dễ đọc | Skill B | UXG-165 | Gap | Từ ảnh transaction-history.png: Disclaimer dài 2 dòng, font nhỏ gray — user phải đọc toàn bộ. Cần rút gọn or tooltip |
| 33 | Calendar picker có way để cancel (không chỉ "Xong") | Skill B · C3 | — | Gap | Từ ảnh timepicker.png: Chỉ có nút "Xong" — không có "Hủy" / back gesture rõ ràng — user không biết cách thoát calendar bỏ qua |
| 34 | Filter bottom-sheet: date input labels và calendar icon rõ | Skill C · C1 | COMP:bottom-sheet-1 | Pass | Từ ảnh transaction-historyfilter.png: "Từ ngày" + calendar icon, "Đến ngày" + calendar icon — rõ ràng, nhất quán |

---

## Đề xuất cải tiến (Priority)

#### UXP-TAT-001 · Critical
| **Màn hình** | Thông tin tài khoản |
|:---|:---|
| **Vấn đề** | 12 fields flat list — cognitive overload, vi phạm Hick's Law và Miller's Law |
| **Gap ref** | Check #10 |
| **DDL** | Law:hick, Law:miller |
| **Giải pháp** | Nhóm fields thành 3 section có header: (1) Thông tin cơ bản, (2) Số dư & Lãi suất, (3) Thấu chi. Cân nhắc collapse (3) nếu giá trị toàn 0. |

---

#### UXP-TAT-002 · Critical
| **Màn hình** | Thông tin tài khoản |
|:---|:---|
| **Vấn đề** | Không có help text/tooltip cho thuật ngữ tài chính phức tạp |
| **Gap ref** | Check #11, #12 |
| **DDL** | UXG-165 (helpfulness) |
| **Giải pháp** | Thêm icon ⓘ bên cạnh fields "Lãi cộng dồn", "Số tiền phong tòa", "Hạn mức thấu chi", "Lãi thấu chi". Tap icon → bottom sheet giải thích ngôn ngữ đơn giản. |

---

#### UXP-TAT-003 · Critical
| **Màn hình** | My QR |
|:---|:---|
| **Vấn đề** | QR static — không có expiry/rotate, rủi ro bảo mật |
| **Gap ref** | Check #22 |
| **DDL** | DDL Banking: Security-first |
| **Giải pháp** | Thêm QR expiry countdown timer (ví dụ "Mã hết hạn sau 5:00"). QR rotate sau khi expire. Thêm disclaimer "Không chia sẻ mã QR với người khác". |

---

#### UXP-TAT-004 · Major
| **Màn hình** | Lịch sử giao dịch |
|:---|:---|
| **Vấn đề** | Transaction description bị truncate, không xem được full text |
| **Gap ref** | Check #28 |
| **DDL** | UXG-165 |
| **Giải pháp** | Cho phép 2-line wrap trong list item, hoặc thêm transaction detail screen khi tap vào tx item. |

---

#### UXP-TAT-005 · Major
| **Màn hình** | Thông tin tài khoản |
|:---|:---|
| **Vấn đề** | Không có undo sau khi đặt TK mặc định |
| **Gap ref** | Check #14 |
| **DDL** | UXG-165 (user control) |
| **Giải pháp** | Badge "TK mặc định" có thể tap → "Hủy đặt làm mặc định?" hoặc: trong SCR-TAT-001 cho phép đổi TK mặc định trực tiếp. |

---

#### UXP-TAT-006 · Major
| **Màn hình** | Lịch sử giao dịch |
|:---|:---|
| **Vấn đề** | Không có clear filter nhanh khi custom filter active |
| **Gap ref** | Check #29 |
| **DDL** | UXG-165 |
| **Giải pháp** | Khi custom filter active: chip "Khác" đổi thành "22/10 – 22/11 ✕" — tap ✕ để clear filter. |

---

#### UXP-TAT-007 · Minor
| **Màn hình** | Lịch sử giao dịch |
|:---|:---|
| **Vấn đề** | Empty state thiếu illustration và CTA |
| **Gap ref** | Check #31 |
| **DDL** | UXG-165 |
| **Giải pháp** | Thêm illustration (empty box icon), context message "Không có giao dịch trong khoảng thời gian này", CTA button "Xem 1 tháng gần nhất". |

---

#### UXP-TAT-008 · Minor
| **Màn hình** | My QR |
|:---|:---|
| **Vấn đề** | "My QR" label tiếng Anh — thiếu nhất quán localization |
| **Gap ref** | Check #23 |
| **DDL** | UXG-165 (consistency) |
| **Giải pháp** | Đổi thành "Mã QR của tôi" hoặc "QR thanh toán" — hoặc nhất quán hóa trong toàn app nếu "My QR" là brand name. |

---

*Report generated by figma-to-ux-review pipeline v1 · Co-opBank 2026 · VNPAY Design Intelligence*
