# UX Review Report — Co-opBank KHCN · Thanh toán

## Tổng quan
- Folder: coopbank/final/thanh toán
- Số màn hình: 9 | Tổng check: 0
- Pass: 0 | Gap: 0 | Unverifiable: 0
- UX Score (Simple): 0% (0/0)
- UX Score (Weighted): 0%
- Proposals: 🔴 Critical: 3 | 🟡 Major: 5 | ⚪ Minor: 4 | Total: 12

## Đề xuất cải tiến (Priority)

#### UXP-001 · Critical
| **Màn hình** | Thanh toán vé xem phim › Xác nhận giao dịch, Thanh toán vé tàu › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | Từ ảnh 1001thanh-toan-ve-xem-phim |
| **Gap ref** | Check #7 |
| **DDL** | UXG-52 · COMP:otp-input-1 · Law:cognitive-load |
| **Giải pháp** | Áp dụng Smart Summary: chỉ hiện key fields (số tiền, TK nguồn, dịch vụ) + expandable "Xem chi tiết"; Sửa "đặt lịch" → context cụ thể: "thanh toán v... |

---


**Total checks:** 72  
**Pass:** 46 | **Gap:** 26 | **Unverifiable:** 0  
**Simple Score:** 64%  
**Weighted Score:** 64%#### UXP-002 · Critical
| **Màn hình** | Thanh toán Vietlott › Xác nhận giao dịch, Thanh toán vé xem phim › Xác nhận giao dịch, Thanh toán vé tàu › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | Từ ảnh thanh-toan-vietlot |
| **Gap ref** | Check #4, Check #4, Check #4 |
| **DDL** | COMP:otp-input-1 · Law:fitts |
| **Giải pháp** | Hiển thị countdown "Còn 02:00" bên dưới digit cells; Nút "Gửi lại mã OTP" (disabled khi timer > 0, enabled khi = 0); OTP auto-submit khi đủ 6 ký tự... |

---

#### UXP-003 · Critical
| **Màn hình** | Thanh toán vé tàu › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Từ ảnh thanh-toan-ve-tau-2 |
| **Gap ref** | Check #4 |
| **DDL** | UXG-52 · Law:cognitive-load |
| **Giải pháp** | Collapsible sections — mặc định expanded nhưng tap header thu gọn; Thêm sticky summary bar (tổng tiền + số vé) ở top khi cuộn; CTA "Tiếp tục" stick... |

---

#### UXP-004 · Major
| **Màn hình** | Thanh toán Vietlott › Xác nhận giao dịch, Thanh toán vé xem phim › Xác nhận giao dịch, Thanh toán vé tàu › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | Từ ảnh 1001thanh-toan-ve-xem-phim |
| **Gap ref** | Check #1, Check #1, Check #1 |
| **DDL** | UXG-78 |
| **Giải pháp** | Context-specific: "kiểm tra lại thông tin thanh toán vé xem phim" |

---

#### UXP-005 · Major
| **Màn hình** | Thanh toán vé xem phim › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | Từ ảnh 1001thanh-toan-ve-xem-phim |
| **Gap ref** | Check #6, Check #6, Check #6 |
| **DDL** | UXG-165 |
| **Giải pháp** | Nếu chỉ 1 option → hiện text tĩnh thay vì dropdown; Nếu lộ trình có 2+ methods → giữ dropdown |

---

#### UXP-006 · Major
| **Màn hình** | Thanh toán vé xem phim › Kết quả giao dịch, Thanh toán vé tàu › Kết quả giao dịch |
|:---|:---|
| **Vấn đề** | Từ ảnh 1003thanh-toan-ve-xem-phim |
| **Gap ref** | Check #4, Check #4 |
| **DDL** | UXG-78 |
| **Giải pháp** | Thay XXXXX bằng số tổng đài thật (1900xxxx); Số tổng đài clickable (tel: link) |

---

#### UXP-007 · Major
| **Màn hình** | Thanh toán vé xem phim › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Từ ảnh 1000thanh-toan-ve-xem-phim |
| **Gap ref** | Check #4, Check #7, Check #3, Check #3 |
| **DDL** | UXG-78 |
| **Giải pháp** | Dùng realistic sample: "Nguyễn Văn A", "098****123" |

---

#### UXP-008 · Major
| **Màn hình** | Thanh toán vé tàu › Form nhập thông tin |
|:---|:---|
| **Vấn đề** | Từ ảnh thanh-toan-ve-tau-1 |
| **Gap ref** | Check #3, Check #6 |
| **DDL** | UXG-243 |
| **Giải pháp** | Fix: Tổng tiền > Giảm. VD: Tổng 120K, Giảm 40K, TT 80K; Fix: Ga đến chiều về = Hà Nội (inverse chiều đi) |

---

#### UXP-009 · Minor
| **Màn hình** | Thanh toán vé xem phim › Kết quả, Thanh toán vé tàu › Kết quả |
|:---|:---|
| **Vấn đề** | Từ ảnh: Nút "Lưu ảnh" lưu screenshot — không phải PDF biên nhận |
| **Gap ref** | Check #5, Check #6 |
| **DDL** | COMP:receipt-preview-1 |
| **Giải pháp** | Thêm "Tải biên nhận PDF" cạnh "Lưu ảnh" |

---

#### UXP-010 · Minor
| **Màn hình** | Thanh toán Vietlott › Xác nhận giao dịch, Thanh toán vé xem phim › Xác nhận giao dịch, Thanh toán vé tàu › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | Từ ảnh: Confirm screens thiếu home icon ở header — chỉ có back arrow |
| **Gap ref** | Check #6 |
| **DDL** | COMP:app-header-1 |
| **Giải pháp** | Thêm home icon cho confirm screens |

---

#### UXP-011 · Minor
| **Màn hình** | Thanh toán Vietlott › Kết quả, Thanh toán vé xem phim › Kết quả, Thanh toán vé tàu › Kết quả |
|:---|:---|
| **Vấn đề** | Từ ảnh: Result screens chỉ có CTA "Tạo giao dịch mới" (outlined) |
| **Gap ref** | Check #6, Check #6, Check #5 |
| **DDL** | — · Law:peak-end |
| **Giải pháp** | "Về trang chủ" (filled) + "Tạo giao dịch mới" (outlined) |

---

#### UXP-012 · Minor
| **Màn hình** | Thanh toán Vietlott › Xác nhận giao dịch, Thanh toán vé xem phim › Xác nhận giao dịch, Thanh toán vé tàu › Xác nhận giao dịch |
|:---|:---|
| **Vấn đề** | Từ ảnh thanh-toan-vietlot |
| **Gap ref** | Check #7 |
| **DDL** | COMP:otp-input-1 · Law:fitts |
| **Giải pháp** | Tăng cellGap lên 12px; Thêm 24px padding giữa cells và CTA |

---

## Chi tiết theo màn hình

### 1. Thanh toán Vietlott › Form nhập thông tin
> `SCR-TT-001` · form · 1 artboard
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-vietlot.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header hiển thị title + back + home | Skill B | COMP:app-header-1 | Pass | Từ ảnh: "Thanh toán mua xổ số Vietlott" + back + home icon |
| 2 | Account card hiển thị TK + số dư | Skill C | — | Pass | Từ ảnh: TK 9099798712313123, 20,000,000 VND visible |
| 3 | Thông tin dịch vụ read-only | Skill B | — | Pass | Từ ảnh: 3 info rows (Dịch vụ, Mã TT, Số tiền) read-only |
| 4 | CTA "Tiếp tục" full-width sticky | Skill C | — | Pass | Từ ảnh: CTA navy full-width ở bottom |
| 5 | Section header có icon cảnh báo | Skill C | — | Pass | Từ ảnh: icon đỏ bên trái "Thông tin thanh toán" |
| 6 | Account chevron dropdown | Skill C | — | Pass | Từ ảnh: chevron down visible = chọn TK khác |
| 7 | Fitts's Law — CTA ≥44px | Skill A | fitts | Pass | Từ ảnh: CTA 48px height full-width |
| 8 | Hick's Law — limited actions | Skill A | hicks | Gap | Từ ảnh: chỉ 1 CTA nhưng icon cảnh báo đỏ gây confusion — không rõ cảnh báo gì |

### 2. Thanh toán Vietlott › Xác nhận giao dịch
> `SCR-TT-002` · confirm · 2 artboards
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-vietlot.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Banner cảnh báo kiểm tra thông tin | Skill B | UXG-78 | Gap | Từ ảnh: banner "đặt lịch" không khớp context "Vietlott" → UXP-004 |
| 2 | Info rows hiển thị đầy đủ | Skill C | — | Pass | Từ ảnh: TK, Dịch vụ, Mã TT, Số tiền, Phí — 5 rows visible |
| 3 | Số tiền bằng chữ đỏ | Skill C | — | Pass | Từ ảnh: "Năm mươi nghìn đồng" red text visible |
| 4 | OTP timer + resend button | Skill C | COMP:otp-input-1 | Gap | Từ ảnh: OTP overlay — 6 cells, NO timer, NO resend → UXP-002 |
| 5 | OTP close (×) button | Skill C | COMP:otp-input-1 | Pass | Từ ảnh: × close visible top-right |
| 6 | Auth dropdown single-option | Skill C | — | Gap | Từ ảnh: SMS OTP là option duy nhất → dropdown redundant → UXP-005 |
| 7 | Cognitive load — redundant confirm | Skill A | UXG-52 | Gap | Từ ảnh: 5 rows duplicate từ form → UXP-001 |
| 8 | Header consistency | Skill B | COMP:app-header-1 | Pass | Từ ảnh: "Xác nhận giao dịch" + back arrow |

### 3. Thanh toán Vietlott › Kết quả giao dịch
> `SCR-TT-003` · result · 1 artboard
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-vietlot.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Success card — checkmark + amount green | Skill C | — | Pass | Từ ảnh: CoopBank logo, checkmark, "50,000 VND" green |
| 2 | Detail rows — 4 fields | Skill C | — | Pass | Từ ảnh: Thời gian, Dịch vụ, Mã TT, Mã GD visible |
| 3 | Actions — chia sẻ + lưu ảnh | Skill C | COMP:receipt-preview-1 | Pass | Từ ảnh: share + save icons + labels |
| 4 | CTA "Tạo giao dịch mới" | Skill C | — | Pass | Từ ảnh: outlined CTA bottom |
| 5 | PDF receipt option | Skill B | COMP:receipt-preview-1 | Gap | Từ ảnh: chỉ "Lưu ảnh" — thiếu PDF → UXP-009 |
| 6 | Primary exit CTA — "Về trang chủ" | Skill C | — | Gap | Từ ảnh: chỉ "Tạo giao dịch mới" + home icon nhỏ → UXP-011 |
| 7 | Peak-End Rule — positive ending | Skill A | peak-end | Pass | Từ ảnh: success prominent, green amount |
| 8 | Header home icon visible | Skill B | COMP:app-header-1 | Pass | Từ ảnh: home icon top-left |

### 4. Thanh toán vé xem phim › Form nhập thông tin
> `SCR-TT-004` · form · 1 artboard
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: 1000thanh-toan-ve-xem-phim.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header hiển thị title + nav | Skill B | COMP:app-header-1 | Pass | Từ ảnh: "Thanh toán vé xem phim" + back + home |
| 2 | Account card | Skill C | — | Pass | Từ ảnh: TK + 20M VND + chevron |
| 3 | Thông tin thanh toán 3 rows | Skill C | — | Pass | Từ ảnh: Tổng tiền 150K, Giảm 20K, Tổng GD 100K |
| 4 | Thông tin KH placeholder raw | Skill C | UXG-78 | Gap | Từ ảnh: "[Customer name]", "[Phone number]" → placeholder raw → UXP-007 |
| 5 | CTA "Tiếp tục" sticky | Skill C | — | Pass | Từ ảnh: CTA navy bottom |
| 6 | Fitts's Law — CTA size | Skill A | fitts | Pass | Từ ảnh: CTA 48px full-width |
| 7 | Email realistic | Skill C | — | Gap | Từ ảnh: "email@examplemail.com" — placeholder → UXP-007 |
| 8 | Hick's Law — simple form | Skill A | hicks | Pass | Từ ảnh: read-only, 1 CTA |

### 5. Thanh toán vé xem phim › Xác nhận giao dịch
> `SCR-TT-005` · confirm · 2 artboards
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: 1001thanh-toan-ve-xem-phim.png, 1002thanh-toan-ve-xem-phim.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Banner contextualization | Skill B | UXG-78 | Gap | Từ ảnh: "đặt lịch" ≠ "vé xem phim" → UXP-004 |
| 2 | Info rows 7 fields complete | Skill C | — | Pass | Từ ảnh: TK, DV, NCC, MaTT, TenKH, Tiền, Phí |
| 3 | Nhà cung cấp placeholder | Skill C | UXG-78 | Gap | Từ ảnh: "[provider name]" placeholder visible → UXP-007 |
| 4 | OTP timer + resend | Skill C | COMP:otp-input-1 | Gap | Từ ảnh 1002: OTP overlay no timer → UXP-002 |
| 5 | OTP close × | Skill C | COMP:otp-input-1 | Pass | Từ ảnh: × close visible |
| 6 | Auth dropdown | Skill C | — | Gap | Từ ảnh: single-option SMS OTP dropdown → UXP-005 |
| 7 | Amount bằng chữ | Skill C | — | Pass | Từ ảnh: "Một trăm nghìn đồng" red |
| 8 | Fitts's Law — OTP cells | Skill A | fitts | Pass | Từ ảnh: 6 cells adequately sized |

### 6. Thanh toán vé xem phim › Kết quả giao dịch
> `SCR-TT-006` · result · 1 artboard
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: 1003thanh-toan-ve-xem-phim.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Success card prominent | Skill C | — | Pass | Từ ảnh: checkmark + "100,000 VND" green |
| 2 | Detail rows 6 fields | Skill C | — | Pass | Từ ảnh: Thời gian, DV, NCC(CGV), MaTT, TenKH, MaGD |
| 3 | Customer name placeholder | Skill C | UXG-78 | Gap | Từ ảnh: "[Customer name]" in result → UXP-007 |
| 4 | Hotline placeholder XXXXX | Skill C | UXG-78 | Gap | Từ ảnh: "tổng đài XXXXX" → UXP-006 |
| 5 | Actions — chia sẻ + lưu ảnh | Skill C | — | Pass | Từ ảnh: icons + labels visible |
| 6 | Primary exit CTA | Skill C | — | Gap | Từ ảnh: chỉ "Tạo giao dịch mới" outlined → UXP-011 |
| 7 | Peak-End Rule | Skill A | peak-end | Pass | Từ ảnh: success prominent = positive |
| 8 | Lưu ý mã đặt chỗ rõ ràng | Skill C | — | Pass | Từ ảnh: notice yellow box visible |

### 7. Thanh toán vé tàu › Form nhập thông tin
> `SCR-TT-007` · form · 2 artboards
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-ve-tau-1.png, thanh-toan-ve-tau-2.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Header + nav | Skill B | COMP:app-header-1 | Pass | Từ ảnh: "Thanh toán vé tàu" + back + home |
| 2 | Account card | Skill C | — | Pass | Từ ảnh: TK + 20M VND |
| 3 | Data logic — sum correct | Skill C | UXG-243 | Gap | Từ ảnh: 20K tổng < 100K giảm = impossible → UXP-008 |
| 4 | Long scroll form | Skill C | UXG-52 | Gap | Từ ảnh tau-2: artboard 1407px, 20 rows → UXP-003 |
| 5 | Chiều đi info complete | Skill C | — | Pass | Từ ảnh: 7 rows chiều đi — ga, ngày, tàu, ghế, SL |
| 6 | Chiều về data copy error | Skill C | UXG-243 | Gap | Từ ảnh tau-2: "Ga đến: Sài Gòn" = ga đi → UXP-008 |
| 7 | CTA "Tiếp tục" visible | Skill C | — | Pass | Từ ảnh: CTA bottom |
| 8 | Fitts's Law — CTA | Skill A | fitts | Pass | Từ ảnh: CTA 48px full-width |

### 8. Thanh toán vé tàu › Xác nhận giao dịch
> `SCR-TT-008` · confirm · 2 artboards
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-ve-tau-3.png, thanh-toan-ve-tau-4.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Banner text mismatch | Skill B | UXG-78 | Gap | Từ ảnh: "đặt lịch" ≠ "vé tàu" → UXP-004 |
| 2 | Info rows complete | Skill C | — | Pass | Từ ảnh: TK, DV, MaTT, TenKH, Tiền, Phí |
| 3 | Amount bằng chữ | Skill C | — | Pass | Từ ảnh: "Một trăm nghìn đồng" red |
| 4 | OTP timer + resend | Skill C | COMP:otp-input-1 | Gap | Từ ảnh tau-4: no timer, no resend → UXP-002 |
| 5 | OTP close × | Skill C | — | Pass | Từ ảnh: × visible |
| 6 | Auth single-option | Skill C | — | Gap | Từ ảnh: SMS OTP single dropdown → UXP-005 |
| 7 | OTP spacing tight | Skill C | COMP:otp-input-1 | Gap | Từ ảnh: cells compact, CTA close → UXP-012 |
| 8 | Header consistency | Skill B | COMP:app-header-1 | Pass | Từ ảnh: "Xác nhận giao dịch" + back |

### 9. Thanh toán vé tàu › Kết quả giao dịch
> `SCR-TT-009` · result · 1 artboard
>
> **Score: 0% | Pass: 0 | Gap: 0 | Unverifiable: 0 | Images: thanh-toan-ve-tau-5.png**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|-----|---------|----------|
| 1 | Success card | Skill C | — | Pass | Từ ảnh: checkmark + "100,000 VND" green |
| 2 | Detail rows 4 fields | Skill C | — | Pass | Từ ảnh: Thời gian, DV, MaTT, MaGD |
| 3 | Actions | Skill C | — | Pass | Từ ảnh: chia sẻ + lưu ảnh |
| 4 | Hotline XXXXX | Skill C | UXG-78 | Gap | Từ ảnh: "tổng đài XXXXX" → UXP-006 |
| 5 | Primary exit CTA | Skill C | — | Gap | Từ ảnh: chỉ "Tạo giao dịch mới" → UXP-011 |
| 6 | PDF receipt | Skill B | COMP:receipt-preview-1 | Gap | Từ ảnh: chỉ "Lưu ảnh" → UXP-009 |
| 7 | Peak-End Rule | Skill A | peak-end | Pass | Từ ảnh: success = positive ending |
| 8 | Header home icon | Skill B | COMP:app-header-1 | Pass | Từ ảnh: home icon visible top-left |

---

## DDL References sử dụng

| ddl_ref | Rule | UX Law | Áp dụng |
|---------|------|--------|---------|
| UXG-52 | Long List / Information Hierarchy | cognitive-load | SCR-TT-002,005,008 confirm redundancy; SCR-TT-007 long scroll |
| UXG-78 | Content Quality | — | Banner "đặt lịch", placeholder text, hotline XXXXX |
| UXG-165 | Text Legibility | — | SCR-TT-005 provider placeholder |
| UXG-243 | Error Prevention / Data Validation | — | SCR-TT-007 math + copy errors |
| COMP:otp-input-1 | OTP input with resend timer | fitts | All confirm screens — missing timer, resend |
| COMP:app-header-1 | App header consistency | — | All screens — form has home, confirm doesn't |
| COMP:receipt-preview-1 | Receipt with PDF option | — | Result screens — only screenshot, no PDF |
