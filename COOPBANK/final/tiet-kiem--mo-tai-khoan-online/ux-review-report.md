# UX Review Report — Mở tài khoản tiền gửi online

> **Product:** Mở tài khoản tiền gửi online (Co-opBank)
> **Domain:** Banking
> **Generated:** 2026-03-23
> **Pipeline:** figma-to-ux-review v1
> **Figma:** [Source](https://www.figma.com/design/aYeSAVi94QlI4i4rL3xtmR/Untitled?node-id=164-195027)

---


**Total checks:** 47  
**Pass:** 29 | **Gap:** 18 | **Unverifiable:** 0  
**Simple Score:** 62%  
**Weighted Score:** 62%## Tổng quan

| Metric | Value |
|:---|:---|
| Tổng screens | 7 |
| Tổng check | 47 |
| Pass: 29 \| Gap: 18 \| Unverifiable: 0 | |
| UX Score (Simple) | 62% |
| UX Score (Weighted) | 100% |
| Proposals | Critical: 3 \| Major: 4 \| Minor: 3 |

---

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Mở tiền gửi trực tuyến - Tích luỹ linh động |
|:---|:---|
| **Vấn đề** | DDL spec `otp-input-1` yêu cầu states: `activeIndex`, `canResend`, `timeLeft`, `digits`, `errorCount`. Ảnh Figma chỉ hiển thị 6 ô tĩnh, KHÔNG có UI resend timer, KHÔNG có error state, KHÔNG có countdown. Thiếu hoàn toàn UX cho trường hợp nhập sai, hết thời gian OTP. |
| **Gap ref** | Check #1, Check #1 |
| **DDL** | COMP:otp-input-1 |
| **Giải pháp** | Bổ sung: (1) Countdown timer "Gửi lại mã sau 60s", (2) Nút "Gửi lại" khi hết thời gian, (3) Error state khi nhập sai (viền đỏ + thông báo lần nhập ... |

---

#### UXP-002 · Critical
| **Màn hình** | Xác nhận giao dịch - Tích luỹ linh động |
|:---|:---|
| **Vấn đề** | Sau khi user nhập OTP và tap "Xác nhận", không có loading indicator hay processing state. Banking transaction cần feedback tức thì để user biết giao dịch đang xử lý (Doherty Threshold: response < 400ms hoặc show progress). |
| **Gap ref** | Check #6, Check #5, Check #5 |
| **DDL** | UXG-165 |
| **Giải pháp** | Thêm màn hình/overlay loading "Đang xử lý giao dịch..." với spinner hoặc progress bar. Disable button "Xác nhận" sau khi tap để tránh double-submit. |

---

#### UXP-003 · Critical
| **Màn hình** | Mở tiền gửi trực tuyến - Tích luỹ linh động |
|:---|:---|
| **Vấn đề** | Form có nhiều trường nhập liệu nhưng không có variant nào hiển thị error state (viền đỏ, thông báo lỗi dưới field). Chỉ có helper text "Số tiền gửi tối thiểu là 1,000,000 VND" nhưng không có UI khi vi phạm rule này. |
| **Gap ref** | Check #1 |
| **DDL** | UXG-243 |
| **Giải pháp** | Bổ sung error state cho text-input: viền đỏ, helper text chuyển đỏ, icon error. Cần artboard riêng cho validation failed state. |

---

#### UXP-004 · Major
| **Màn hình** | Tiền gửi tiết kiệm |
|:---|:---|
| **Vấn đề** | Các icon menu (40×40px) gần sát nhau trong grid 3×2. Khoảng cách giữa các touch target có thể không đủ 8px spacing theo WCAG. Trên screenshot, icon row 2 chỉ có 2 items nên alignment không cân đối. |
| **Gap ref** | Check #1, Check #3 |
| **DDL** | UXG-042 |
| **Giải pháp** | Tăng touch target tối thiểu 44×44px, đảm bảo spacing ≥ 8px giữa các items. Cân nhắc layout 2 cột cho row 2 để cân đối hơn. |

---

#### UXP-005 · Major
| **Màn hình** | Kết quả giao dịch - Tích luỹ linh động |
|:---|:---|
| **Vấn đề** | DDL `receipt-preview-1` spec yêu cầu fields: `transactionId`, `timestamp`, `amount`, `status`, `recipientInfo`, `senderInfo`. Ảnh thiếu `senderInfo` (tài khoản nguồn) — user không thấy tiền trích từ tài khoản nào. Cũng thiếu "Lãi suất" và "Kỳ hạn" trong receipt. |
| **Gap ref** | Check #1, Check #1 |
| **DDL** | COMP:receipt-preview-1 |
| **Giải pháp** | Bổ sung: Tài khoản nguồn, Lãi suất, Kỳ hạn, Hình thức tích luỹ vào receipt card. |

---

#### UXP-006 · Major
| **Màn hình** | Xác nhận giao dịch - Tích luỹ linh động |
|:---|:---|
| **Vấn đề** | Form hiển thị lãi suất 3,98%/năm nhưng màn hình xác nhận hiển thị 5%. Tài khoản nguồn ở form là "9099798712313123" nhưng confirm là "98712313123" (thiếu prefix). Gây mất tin tưởng user. |
| **Gap ref** | Check #5, Check #4, Check #5 |
| **DDL** | UXG-165 |
| **Giải pháp** | Đảm bảo data consistency giữa form và confirm screen. Hiển thị đầy đủ số tài khoản. |

---

#### UXP-007 · Major
| **Màn hình** | Mở tiền gửi trực tuyến - Tích luỹ định kỳ tự động |
|:---|:---|
| **Vấn đề** | Form TLTÐ có ~15 fields, artboard cao 1593px (gấp đôi viewport 812px). User phải scroll nhiều lần. Quá nhiều lựa chọn cùng lúc vi phạm Hick's Law — thời gian quyết định tăng theo số lựa chọn. |
| **Gap ref** | Check #2 |
| **DDL** | Hick's Law |
| **Giải pháp** | Chia form thành 2-3 bước (wizard/stepper): Bước 1 thông tin cơ bản, Bước 2 tích luỹ định kỳ, Bước 3 tài khoản nhận. Progressive disclosure giảm cog... |

---

#### UXP-008 · Minor
| **Màn hình** | Xác nhận giao dịch - Tích luỹ linh động |
|:---|:---|
| **Vấn đề** | Artboard 1305 hiển thị "Qúy khách vui lòng kiểm tra lại thông tin đã khởi tạo" — sai chính tả "Qúy" (đúng: "Quý"). Cũng có trong artboard 1313. Lỗi nhỏ nhưng ảnh hưởng perceived quality. |
| **Gap ref** | Check #6, Check #8 |
| **DDL** | UXG-101 |
| **Giải pháp** | Sửa "Qúy" → "Quý" trên tất cả artboards. |

---

#### UXP-009 · Minor
| **Màn hình** | Mở tiền gửi trực tuyến - Tích luỹ linh động |
|:---|:---|
| **Vấn đề** | Form có dropdown "Phương thức đáo hạn" nhưng KHÔNG có artboard popup tương ứng (chỉ có popup cho "Chu kỳ tích luỹ" và "Phương thức rút gốc"). User không biết options nào available. |
| **Gap ref** | Check #9 |
| **DDL** | — |
| **Giải pháp** | Bổ sung artboard popup cho "Phương thức đáo hạn" với danh sách options. |

---

#### UXP-010 · Minor
| **Màn hình** | Kết quả giao dịch - Tích luỹ linh động |
|:---|:---|
| **Vấn đề** | Button "Giấy xác nhận" không rõ sẽ mở PDF, download, hay navigate screen mới. Thiếu icon indicator. Fitts's Law: 2 buttons cùng size nhưng "Tạo giao dịch mới" (primary) và "Giấy xác nhận" (secondary) không phân biệt rõ hierarchy. |
| **Gap ref** | Check #4, Check #3 |
| **DDL** | UXG-080 |
| **Giải pháp** | Dùng visual hierarchy rõ ràng: primary button (filled) cho action chính, outline button cho secondary. Thêm icon download/PDF bên cạnh "Giấy xác nh... |

---

## Chi tiết theo màn hình

### 1. Tiền gửi tiết kiệm › Danh mục

> `SCR-TK-001` · menu · 1 artboard

**Score: 60% | Pass: 3 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Touch target ≥ 44×44px | Vision | UXG-042 | Gap | Từ ảnh: Icon menu ~40×40px, dưới chuẩn 44px. Spacing hẹp giữa các items |
| 2 | Header back navigation | Vision | UXG-080 | Pass | Từ ảnh: Back arrow icon ở header-left, rõ ràng |
| 3 | Grid layout alignment | Vision | UXG-165 | Gap | Từ ảnh: Row 2 chỉ có 2 items trên grid 3 cột, gây bất cân đối |
| 4 | Text truncation | Vision | UXG-101 | Pass | Từ ảnh: Tất cả text labels hiển thị đầy đủ, không truncation |
| 5 | Color contrast header | Vision | WCAG AA | Pass | Từ ảnh: Text trắng (#FFFFFF) trên nền xanh đậm (~#1E3A8A), contrast ≥ 7:1 |

### 2. Mở tiền gửi trực tuyến - Tích luỹ linh động › Form nhập thông tin

> `SCR-TK-002` · form · 5 artboards (incl. 2 overlays)

**Score: 80% | Pass: 8 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Text-input error state | Skill A | COMP:text-input-1 | Gap | DDL `text-input-1` spec: `error`, `errorMessage` states. Screenshot: chỉ có default + filled states, KHÔNG có error variant |
| 2 | Form field labels | Vision | UXG-243 | Pass | Từ ảnh: Tất cả fields có label rõ ràng (Loại sản phẩm, Kỳ hạn, Lãi suất...) |
| 3 | CTA visibility | Vision | Fitts's Law | Pass | Từ ảnh: Button "Tiếp tục" full-width 343px, height 44px, đạt chuẩn touch target |
| 4 | Terms checkbox | Vision | UXG-165 | Pass | Từ ảnh: Checkbox kèm link "Điều khoản, điều kiện sử dụng" — đầy đủ |
| 5 | Dropdown bottom-sheet | Vision | Hick's Law | Pass | Từ ảnh: Popup "Chu kỳ tích luỹ" có 5 options rõ ràng, selected item có checkmark |
| 6 | Min amount helper | Vision | UXG-101 | Pass | Từ ảnh: "Số tiền gửi tối thiểu là 1,000,000 VND" hiển thị rõ dưới field |
| 7 | Popup close affordance | Vision | UXG-080 | Pass | Từ ảnh: Icon X (clear) ở góc phải popup, kích thước đủ |
| 8 | Interest info expand/collapse | Vision | — | Pass | Từ ảnh: "Xem thêm" / "Thu gọn" toggle hoạt động, content expand rõ |
| 9 | Missing popup "Phương thức đáo hạn" | Vision | — | Gap | Từ ảnh: Dropdown "Phương thức đáo hạn" có caret nhưng KHÔNG có artboard popup |
| 10 | Account source card | Vision | UXG-165 | Pass | Từ ảnh: Card tài khoản nguồn hiển thị số TK + số dư rõ ràng |

### 3. Xác nhận giao dịch - Tích luỹ linh động › Xác nhận giao dịch

> `SCR-TK-003` · confirm · 2 artboards (incl. OTP overlay)

**Score: 50% | Pass: 4 | Gap: 4**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | OTP states completeness | Skill A | COMP:otp-input-1 | Gap | DDL `otp-input-1`: `activeIndex`, `canResend`, `timeLeft`, `digits`, `errorCount`. Screenshot: 6 ô tĩnh only |
| 2 | Transaction summary completeness | Vision | UXG-165 | Pass | Từ ảnh: 11 fields hiển thị đầy đủ thông tin giao dịch |
| 3 | Amount in words | Vision | — | Pass | Từ ảnh: "20,000,000 VND" + "Hai mươi triệu đồng" — confirmation bằng chữ |
| 4 | Auth method selector | Vision | UXG-080 | Pass | Từ ảnh: Dropdown "Chọn phương thức xác thực" → "Soft OTP" |
| 5 | Data consistency form→confirm | Vision | UXG-165 | Gap | Từ ảnh: Form lãi suất 3,98%/năm vs Confirm 5%. TK nguồn bị cắt prefix |
| 6 | Loading/processing state | Vision | UXG-165 | Gap | Từ ảnh: KHÔNG có loading state sau tap "Xác nhận" — thiếu feedback |
| 7 | OTP warning text | Vision | UXG-101 | Pass | Từ ảnh: "Soft OTP sẽ bị khóa nếu Qúy khách nhập sai PIN 5 lần liên tiếp" hiển thị |
| 8 | Typo "Qúy khách" | Vision | UXG-101 | Gap | Từ ảnh: "Qúy khách" thay vì "Quý khách" — lỗi chính tả |

### 4. Kết quả giao dịch - Tích luỹ linh động › Kết quả giao dịch

> `SCR-TK-004` · result · 1 artboard

**Score: 60% | Pass: 3 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Receipt fields completeness | Skill A | COMP:receipt-preview-1 | Gap | DDL `receipt-preview-1`: cần `senderInfo`. Screenshot: thiếu tài khoản nguồn, lãi suất, kỳ hạn |
| 2 | Success indicator | Vision | Peak-End Rule | Pass | Từ ảnh: Checkmark xanh + text "thành công" + amount nổi bật — peak positive |
| 3 | Share/Save actions | Vision | UXG-080 | Pass | Từ ảnh: 2 action icons (Chia sẻ, Lưu ảnh) rõ ràng với labels |
| 4 | Primary/Secondary CTA hierarchy | Vision | Fitts's Law | Gap | Từ ảnh: "Tạo giao dịch mới" và "Giấy xác nhận" cùng style — thiếu visual hierarchy |
| 5 | Home navigation | Vision | UXG-080 | Pass | Từ ảnh: Home icon ở header-left thay vì back arrow — đúng cho result screen |

### 5. Mở tiền gửi trực tuyến - Tích luỹ định kỳ tự động › Form nhập thông tin

> `SCR-TK-005` · form · 2 artboards

**Score: 75% | Pass: 6 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Text-input error state | Skill A | COMP:text-input-1 | Gap | DDL `text-input-1`: `error` state. Screenshot: NO error variant |
| 2 | Form length / cognitive load | Vision | Hick's Law | Gap | Từ ảnh: ~15 fields, artboard 1593px (2× viewport). Quá dài, cần stepper |
| 3 | Field labels clarity | Vision | UXG-243 | Pass | Từ ảnh: Tất cả fields có label rõ ràng |
| 4 | CTA "Tiếp tục" visibility | Vision | Fitts's Law | Pass | Từ ảnh: Button full-width ở bottom, height 44px |
| 5 | Min amount helpers | Vision | UXG-101 | Pass | Từ ảnh: 2 helper texts cho 2 amount fields |
| 6 | Terms checkbox | Vision | UXG-165 | Pass | Từ ảnh: Checkbox + link điều khoản hiện đầy đủ |
| 7 | Interest note expandable | Vision | — | Pass | Từ ảnh: "Lưu ý" section có "Xem thêm" toggle |
| 8 | Periodic deposit fields | Vision | — | Pass | Từ ảnh: Chu kỳ, số tiền định kỳ, TK trích tiền — đủ fields cho TLTÐ |

### 6. Xác nhận giao dịch - Tích luỹ định kỳ tự động › Xác nhận giao dịch

> `SCR-TK-006` · confirm · 2 artboards (incl. OTP overlay)

**Score: 33% | Pass: 2 | Gap: 4**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | OTP states completeness | Skill A | COMP:otp-input-1 | Gap | DDL `otp-input-1`: states thiếu tương tự SCR-TK-003 |
| 2 | Transaction summary | Vision | UXG-165 | Pass | Từ ảnh: Hiển thị đầy đủ hơn linh động (có chu kỳ, tài khoản trích tiền) |
| 3 | Amount in words | Vision | — | Pass | Từ ảnh: "Hai mươi triệu đồng" xác nhận bằng chữ |
| 4 | Data consistency | Vision | UXG-165 | Gap | Từ ảnh: Tương tự SCR-TK-003, lãi suất form vs confirm không nhất quán |
| 5 | Loading state | Vision | UXG-165 | Gap | Từ ảnh: Thiếu loading state sau OTP confirm |
| 6 | Typo "Qúy khách" | Vision | UXG-101 | Gap | Từ ảnh: Artboard 1313 có "Qúy khách" — cùng lỗi chính tả |

### 7. Kết quả giao dịch - Tích luỹ định kỳ tự động › Kết quả giao dịch

> `SCR-TK-007` · result · 1 artboard

**Score: 60% | Pass: 3 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|:--|:------|:-------|:--------|:--------|:---------|
| 1 | Receipt fields completeness | Skill A | COMP:receipt-preview-1 | Gap | DDL: thiếu tài khoản nguồn, lãi suất, kỳ hạn. Có thêm chu kỳ + số tiền định kỳ (tốt) |
| 2 | Success indicator | Vision | Peak-End Rule | Pass | Từ ảnh: Checkmark + "thành công" + amount — tốt |
| 3 | CTA hierarchy | Vision | Fitts's Law | Gap | Từ ảnh: 2 buttons cùng style, thiếu visual hierarchy |
| 4 | TLTÐ-specific receipt fields | Vision | — | Pass | Từ ảnh: Chu kỳ tích luỹ "Hàng tháng" + Số tiền "1,000,000 VND" hiển thị |
| 5 | Home navigation | Vision | UXG-080 | Pass | Từ ảnh: Home icon header-left |

---

## DDL References

| Ref Type | ID | Mô tả |
|:---------|:---|:------|
| Component | COMP:otp-input-1 | OTP input component — states: activeIndex, canResend, timeLeft, digits, errorCount |
| Component | COMP:text-input-1 | Text input — states: error, errorMessage, disabled, focused |
| Component | COMP:receipt-preview-1 | Receipt preview — fields: transactionId, timestamp, amount, status, recipientInfo, senderInfo |
| Guideline | UXG-042 | Touch target minimum 44×44px (WCAG) |
| Guideline | UXG-080 | Navigation clarity and affordance |
| Guideline | UXG-101 | Content quality and typography |
| Guideline | UXG-165 | Data consistency and completeness |
| Guideline | UXG-243 | Form usability and validation |
| Law | Fitts's Law | Touch target size and distance affect interaction speed |
| Law | Hick's Law | Decision time increases with number of choices |
| Law | Peak-End Rule | People judge experience by peak and end moments |
