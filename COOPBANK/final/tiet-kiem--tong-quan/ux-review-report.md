# UX Review Report — Tài khoản Tiết kiệm
**Sản phẩm:** Co-opBank Mobile Banking  
**Module:** Tài khoản Tiết kiệm  
**Figma:** `aYeSAVi94QlI4i4rL3xtmR` · node `154:188175`  
**Ngày:** 2026-03-23  
**Domain:** Banking  

---


**Total checks:** 41  
**Pass:** 18 | **Gap:** 20 | **Unverifiable:** 3  
**Simple Score:** 44%  
**Weighted Score:** 44%## Tổng quan

| Metric | Giá trị |
|--------|---------|
| **Tổng màn hình** | 4 |
| **Tổng check** | 0 |
| **Pass** | 0 |
| **Gap** | 0 |
| **Unverifiable** | 0 |
| **Simple Score** | 0% |
| **Weighted Score** | 0% |

---

## Danh sách màn hình

| # | Screen ID | Tên màn hình | Pass | Gap | Score |
|---|-----------|-------------|------|-----|-------|
| 1 | SCR-TKTK-001 | Danh sách tài khoản | 0 | 0 | 0% |
| 2 | SCR-TKTK-002 | Chi tiết tài khoản | 0 | 0 | 0% |
| 3 | SCR-TKTK-003 | Lịch sử giao dịch | 0 | 0 | 0% |
| 4 | SCR-TKTK-004 | Chi tiết giao dịch | 0 | 0 | 0% |

---

## Chi tiết đánh giá per màn hình

---

### 1. Tài khoản Tiết kiệm › Danh sách

> `SCR-TKTK-001` · list · 1 artboard

| **Màn hình** | Tài khoản Tiết kiệm › Danh sách |
|---|---|
| **Screen ID** | SCR-TKTK-001 |
| **Artboards** | 1400 Tài khoản Tiết kiệm |
| **Wireframes** | 1400-tai-khoan-tiet-kiem.png |

**Score: 50% | Pass: 4 | Gap: 2**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Tiêu đề trang rõ ràng và mô tả đúng nội dung màn hình | Skill B | UXG-001 | Pass | Từ ảnh: Header "Tài khoản" hiển thị rõ ở top navigation bar, căn giữa |
| 2 | Phân cấp thông tin rõ ràng giữa section headers và account cards | Skill B | UXG-003 | Pass | Từ ảnh: Section "Tài khoản tiết kiệm (2)" có Tổng số dư ở trên, từng card con bên dưới — hierarchy rõ ràng |
| 3 | Account cards có affordance tap để xem chi tiết (chevron hoặc active indicator) | Skill C | UXG-045 | Gap | Từ ảnh: Các card tài khoản tiết kiệm (12300123123000) không có chevron > hay indicator gì cho thấy tappable |
| 4 | Touch targets ≥ 44px (Fitts's Law) cho từng account row | Skill A | fitts | Unverifiable | Không thể đo pixel chính xác từ ảnh tĩnh ở kích thước này |
| 5 | Số tài khoản dễ đọc — có dấu phân cách hoặc format chuẩn | Skill B | UXG-022 | Gap | Từ ảnh: "12300123123000" (13 ký tự) không có dấu phân cách, khó đọc nhanh |
| 6 | Label text contrast đạt WCAG AA (≥4.5:1) | Skill C | UXG-089 | Unverifiable | Màu label xám nhạt, cần đo chính xác — không thể verify từ ảnh tĩnh |
| 7 | Ngày đến hạn được highlight rõ ràng trong card tiết kiệm | Skill B | UXG-031 | Pass | Từ ảnh: "Ngày đến hạn: 20/09/2021" hiển thị trong mỗi card với font rõ ràng |
| 8 | Layout sạch, không có thông tin noise gây rối người dùng | Skill C | UXG-012 | Pass | Từ ảnh: Layout sạch, mỗi section hiển thị đúng thông tin cần thiết, không có element thừa |

---

### 2. Tài khoản Tiết kiệm › Chi tiết tài khoản

> `SCR-TKTK-002` · detail · 3 artboards

| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết tài khoản |
|---|---|
| **Screen ID** | SCR-TKTK-002 |
| **Artboards** | 1401, 1402, 1403 Tài khoản Tiết kiệm - TTTK |
| **Wireframes** | 1401-tai-khoan-tiet-kiem-tttk.png, 1402-tai-khoan-tiet-kiem-tttk.png, 1403-tai-khoan-tiet-kiem-tttk.png |

**Score: 50% | Pass: 6 | Gap: 5**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Header navigation đúng spec app-header-1 (back + title + action) | Skill A | app-header-1 | Pass | Từ ảnh: caret-arrow-left (back), "Thông tin tài khoản" (title), home icon (action) — đủ 3 thành phần |
| 2 | Bottom action bar tối đa 4 actions để giảm Hick's Law cognitive load | Skill A | hick | Gap | Từ ảnh: Bottom bar 4 icons nhưng label bị viết tắt ("Thay đổi t.tin tích lũy định kỳ") — vi phạm Hick's Law về clarity |
| 3 | CTA labels đầy đủ, không viết tắt trong bottom bar | Skill C | UXG-022 | Gap | Từ ảnh: "Thay đổi t.tin tích lũy định kỳ" bị truncate/viết tắt trong bottom bar label — thiếu rõ ràng |
| 4 | Màu CTA Primary đúng DDL (#CA8A04 Gold hoặc Trust Blue) | Skill B | TOKEN:cta=#CA8A04 | Gap | Từ ảnh: Bottom bar icons dùng Blue, không có Gold #CA8A04. DDL banking CTA Gold không được áp dụng |
| 5 | Thông tin nhạy cảm (số TK, tên chủ TK) có masking/privacy protection | Skill B | UXG-089 | Gap | Từ ảnh: "HA NGUYEN QUANG" và "012547288" hiển thị full — không có option hide/mask. Banking security standard vi phạm |
| 6 | Touch targets bottom bar icons ≥ 44px (Fitts's Law) | Skill A | fitts | Unverifiable | Icons bottom bar khoảng 40-44px ước tính — cần đo đạc chính xác |
| 7 | Danh sách trường thông tin theo thứ tự logic (nhóm theo chủ đề) | Skill B | UXG-003 | Pass | Từ ảnh: Nhóm "Thông tin cơ bản" → "Thông tin tích lũy" → "Thông tin tất toán" → CTA — logic tốt |
| 8 | Label-Value pairs căn lề nhất quán (label trái, value phải) | Skill C | UXG-031 | Pass | Từ ảnh: Tất cả label-value pairs căn lề trái/phải đồng nhất trong toàn màn hình |
| 9 | Lãi suất hiển thị nổi bật để user dễ tham khảo | Skill C | UXG-045 | Gap | Từ ảnh: "Lãi suất: 0.1%" nằm lẫn trong danh sách dài — không được highlight hay emphasized |
| 10 | Variants CTA thay đổi đúng theo loại sản phẩm | Skill C | UXG-031 | Pass | Từ ảnh 1401/1402/1403: CTA bottom bar thay đổi phù hợp theo từng loại SP |
| 11 | Màn hình scroll được tự nhiên (nội dung dài 1300px) | Skill B | UXG-012 | Pass | Từ ảnh 1401 (375×1300): Content flow rõ ràng, scroll naturally |
| 12 | Không có empty content sections | Skill A | empty-state-1 | Pass | Từ ảnh: Không có empty section — tất cả fields có giá trị data |

---

### 3. Tài khoản Tiết kiệm › Lịch sử Giao dịch

> `SCR-TKTK-003` · list · 4 artboards

| **Màn hình** | Tài khoản Tiết kiệm › Lịch sử Giao dịch |
|---|---|
| **Screen ID** | SCR-TKTK-003 |
| **Artboards** | 1410, 1411, 1412, 1413 Tài khoản Tiết kiệm - LSGD |
| **Wireframes** | 1410-tai-khoan-tiet-kiem-lsgd.png, 1411-tai-khoan-tiet-kiem-lsgd.png, 1412-tai-khoan-tiet-kiem-lsgd.png, 1413-tai-khoan-tiet-kiem-lsgd.png |

**Score: 45% | Pass: 5 | Gap: 6**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Filter buttons phân biệt selected/unselected rõ ràng | Skill C | UXG-045 | Pass | Từ ảnh 1410: "1 tuần" nền xanh đậm/chữ trắng (selected), còn lại nền xám — visual contrast rõ ràng |
| 2 | Touch targets filter buttons ≥ 44px height (Fitts's Law) | Skill A | fitts | Gap | Từ ảnh: Filter buttons nhìn khoảng ~36-40px height — dưới ngưỡng 44px tiêu chuẩn Fitts's Law |
| 3 | Bottom sheet date picker (1411) có backdrop dimming và close affordance | Skill C | UXG-031 | Pass | Từ ảnh 1411: Nền bị dimmed rõ ràng, close-X icon ở góc trên phải overlay — đúng pattern |
| 4 | Date picker fields tách biệt rõ ràng và usable | Skill C | UXG-022 | Pass | Từ ảnh 1411: Hai fields riêng biệt với calendar icon, label "Từ ngày"/"Đến ngày" rõ ràng |
| 5 | Empty state (1412) có icon + title + description + CTA retry (DDL empty-state-1 spec) | Skill A | empty-state-1 | Gap | Từ ảnh 1412: Chỉ có text "Không có kết quả tìm kiếm" — thiếu illustrative icon, description helpful, và CTA "Thử tìm lại" |
| 6 | Peak-End Rule: Empty state tạo trải nghiệm kết thúc tích cực (gợi ý thử lại) | Skill A | peak-end | Gap | Từ ảnh 1412: Màn hình empty state minimalistic — không có guidance hoặc suggestion giúp user recover |
| 7 | Transaction items phân biệt tiền vào/ra qua màu sắc | Skill C | UXG-045 | Pass | Từ ảnh 1413: "+2,000,000 VND" màu xanh (tiền vào), "-2,000,000 VND" màu đỏ (tiền ra) |
| 8 | Disclaimer text dễ đọc (font ≥12px, contrast tốt) | Skill C | UXG-089 | Gap | Từ ảnh 1410: Disclaimer text rất nhỏ (~10px ước tính), nằm ở khu vực ít chú ý |
| 9 | Transaction description không bị truncate quá mức | Skill C | UXG-022 | Gap | Từ ảnh 1410/1413: "HA chuyen..." bị truncate — thiếu đủ thông tin nhận diện giao dịch |
| 10 | Tab bar active indicator (Toàn bộ/Tiền vào/Tiền ra) rõ ràng | Skill C | UXG-045 | Pass | Từ ảnh 1413: "Toàn bộ" tab có đường kẻ đỏ underline active indicator — visible và rõ ràng |
| 11 | Số tài khoản 16 ký tự có format dễ đọc | Skill B | UXG-022 | Gap | Từ ảnh: "9099798712313123" không có dấu phân cách — cần format nhóm 4 ký tự |

---

### 4. Tài khoản Tiết kiệm › Chi tiết Giao dịch

> `SCR-TKTK-004` · detail · 1 artboard

| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết Giao dịch |
|---|---|
| **Screen ID** | SCR-TKTK-004 |
| **Artboards** | 1414 Tài khoản Tiết kiệm - Chi tiết GD |
| **Wireframes** | 1414-tai-khoan-tiet-kiem-chi-tiet-gd.png |

**Score: 25% | Pass: 2 | Gap: 6**

| # | Check | Source | DDL Ref | Verdict | Evidence |
|---|-------|--------|---------|---------|----------|
| 1 | Header navigation đúng spec (back + title + home) | Skill A | app-header-1 | Pass | Từ ảnh: caret-arrow-left (back), "Chi tiết giao dịch" (title), home icon (right) — đúng spec |
| 2 | DDL receipt-preview-1 spec: có Share/Print action buttons | Skill A | receipt-preview-1 | Gap | Từ ảnh: Màn hình không có nút Share, Print hay "Tải biên lai" — thiếu hoàn toàn receipt action |
| 3 | Trạng thái giao dịch (Thành công/Thất bại) được hiển thị rõ ràng | Skill B | UXG-031 | Gap | Từ ảnh: Không có status indicator, badge hay icon phân biệt trạng thái giao dịch |
| 4 | Icon/màu sắc phân biệt chiều giao dịch (vào/ra tiền) | Skill C | UXG-045 | Gap | Từ ảnh: "2,000,000 VND" không có màu xanh/đỏ hay icon +/- phân biệt chiều giao dịch |
| 5 | Visual hierarchy nhấn mạnh số tiền giao dịch | Skill C | UXG-003 | Gap | Từ ảnh: "2,000,000 VND" cùng font size với các labels khác — không được emphasized theo banking standard |
| 6 | Nội dung giao dịch có dấu tiếng Việt (không phải raw text) | Skill C | UXG-012 | Gap | Từ ảnh: "Tien tiet kiem" — không có dấu tiếng Việt, thiếu chuyên nghiệp |
| 7 | Content density phù hợp, không có dead whitespace quá nhiều | Skill C | UXG-003 | Gap | Từ ảnh: ~70% màn hình bên dưới là khoảng trống — gây cảm giác chưa hoàn thiện |
| 8 | Text contrast số giao dịch và giá trị đạt WCAG AA | Skill C | UXG-089 | Pass | Từ ảnh: Dark text trên white background — contrast ước tính đạt WCAG AA (≥4.5:1) |

---

## Đề xuất cải thiện (Priority)

### Critical

#### UXP-003 · Critical
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết tài khoản |
|---|---|
| **Vấn đề** | Tên chủ TK và số TK hiển thị full — security risk |
| **Gap ref** | Check #5, Check #8 |
| **Giải pháp** | Thêm toggle "Ẩn thông tin" (mặc định ẩn) với icon mắt; mask thành `HA N. Q***G` và `012-5***-288` |
| **DDL** | UXG-089 |

---

#### UXP-007 · Critical
| **Màn hình** | Tài khoản Tiết kiệm › Lịch sử Giao dịch |
|---|---|
| **Vấn đề** | Empty state thiếu icon + description + CTA — vi phạm DDL empty-state-1 spec |
| **Gap ref** | Check #5 |
| **Giải pháp** | Thêm: illustration + "Không tìm thấy giao dịch trong khoảng thời gian này" + CTA "Mở rộng bộ lọc" |
| **DDL** | empty-state-1 |

---

#### UXP-011 · Critical
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết Giao dịch |
|---|---|
| **Vấn đề** | Thiếu Share/Print biên lai — vi phạm DDL receipt-preview-1 spec |
| **Gap ref** | Check #2 |
| **Giải pháp** | Thêm bottom action bar: "Chia sẻ biên lai" + "Lưu PDF" + "Báo lỗi giao dịch" |
| **DDL** | receipt-preview-1 |

---

### Major

#### UXP-004 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết tài khoản |
|---|---|
| **Vấn đề** | Label bottom bar bị viết tắt, khó hiểu |
| **Gap ref** | Check #3, Check #5, Check #9 |
| **Giải pháp** | Rút ngắn labels: "Thay đổi TT" hoặc dùng icon+tooltip on longpress |
| **DDL** | UXG-022 |

---

#### UXP-006 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Lịch sử Giao dịch |
|---|---|
| **Vấn đề** | Filter buttons <44px touch target — vi phạm Fitts's Law |
| **Gap ref** | Check #2 |
| **Giải pháp** | Tăng chiều cao filter buttons lên tối thiểu 44px với đủ padding |
| **DDL** | fitts |

---

#### UXP-008 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Lịch sử Giao dịch |
|---|---|
| **Vấn đề** | Disclaimer text quá nhỏ (~10px), khó đọc |
| **Gap ref** | Check #8, Check #5 |
| **Giải pháp** | Tăng font size lên ≥12px; đặt trong styled callout box (info card) thay vì plain text |
| **DDL** | UXG-089 |

---

#### UXP-009 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Lịch sử Giao dịch |
|---|---|
| **Vấn đề** | Transaction description bị truncate — "HA chuyen..." thiếu thông tin |
| **Gap ref** | Check #9, Check #5, Check #3 |
| **Giải pháp** | Hiển thị 2 dòng mô tả; hoặc tap-to-expand tooltip |
| **DDL** | UXG-022 |

---

#### UXP-012 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết Giao dịch |
|---|---|
| **Vấn đề** | Thiếu trạng thái giao dịch (Thành công/Đang xử lý) |
| **Gap ref** | Check #3 |
| **Giải pháp** | Thêm status badge ("✅ Thành công") với màu semantic ngay dưới header |
| **DDL** | UXG-031 |

---

#### UXP-013 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết Giao dịch |
|---|---|
| **Vấn đề** | Số tiền không có visual hierarchy — không được emphasized |
| **Gap ref** | Check #5, Check #7 |
| **Giải pháp** | Font-size 24px bold, màu semantic (xanh/đỏ tùy chiều GD) cho số tiền |
| **DDL** | UXG-003 |

---

### Minor

#### UXP-001 · Minor
| **Màn hình** | Tài khoản Tiết kiệm › Danh sách |
|---|---|
| **Vấn đề** | Account cards thiếu tap affordance |
| **Gap ref** | Check #3, Check #9, Check #4 |
| **Giải pháp** | Thêm chevron `>` hoặc caret ở phải mỗi account row để chỉ ra tính tappable |
| **DDL** | UXG-045 |

---

#### UXP-002 · Minor
| **Màn hình** | Tài khoản Tiết kiệm › Danh sách |
|---|---|
| **Vấn đề** | Số TK không có dấu phân cách — khó đọc |
| **Gap ref** | Check #5, Check #11, Check #3 |
| **Giải pháp** | Format số tài khoản nhóm 4 ký tự: `1230-0123-1230-00` |
| **DDL** | UXG-022 |

---

#### UXP-003 · Critical
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết tài khoản |
|---|---|
| **Vấn đề** | Tên chủ TK và số TK hiển thị full — security risk |
| **Gap ref** | Check #5, Check #8 |
| **Giải pháp** | Thêm toggle "Ẩn thông tin" (mặc định ẩn) với icon mắt; mask thành `HA N. Q***G` và `012-5***-288` |
| **DDL** | UXG-089 |

---

#### UXP-004 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết tài khoản |
|---|---|
| **Vấn đề** | Label bottom bar bị viết tắt, khó hiểu |
| **Gap ref** | Check #3, Check #5, Check #9 |
| **Giải pháp** | Rút ngắn labels: "Thay đổi TT" hoặc dùng icon+tooltip on longpress |
| **DDL** | UXG-022 |

---

#### UXP-005 · Minor
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết tài khoản |
|---|---|
| **Vấn đề** | Lãi suất không được emphasized trong danh sách fields dài |
| **Gap ref** | Check #9, Check #3, Check #4 |
| **Giải pháp** | Highlight "Lãi suất: 0.1%" bằng badge màu xanh hoặc font bold/larger |
| **DDL** | UXG-045 |

---

#### UXP-006 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Lịch sử Giao dịch |
|---|---|
| **Vấn đề** | Filter buttons <44px touch target — vi phạm Fitts's Law |
| **Gap ref** | Check #2 |
| **Giải pháp** | Tăng chiều cao filter buttons lên tối thiểu 44px với đủ padding |
| **DDL** | fitts |

---

#### UXP-007 · Critical
| **Màn hình** | Tài khoản Tiết kiệm › Lịch sử Giao dịch |
|---|---|
| **Vấn đề** | Empty state thiếu icon + description + CTA — vi phạm DDL empty-state-1 spec |
| **Gap ref** | Check #5 |
| **Giải pháp** | Thêm: illustration + "Không tìm thấy giao dịch trong khoảng thời gian này" + CTA "Mở rộng bộ lọc" |
| **DDL** | empty-state-1 |

---

#### UXP-008 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Lịch sử Giao dịch |
|---|---|
| **Vấn đề** | Disclaimer text quá nhỏ (~10px), khó đọc |
| **Gap ref** | Check #8, Check #5 |
| **Giải pháp** | Tăng font size lên ≥12px; đặt trong styled callout box (info card) thay vì plain text |
| **DDL** | UXG-089 |

---

#### UXP-009 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Lịch sử Giao dịch |
|---|---|
| **Vấn đề** | Transaction description bị truncate — "HA chuyen..." thiếu thông tin |
| **Gap ref** | Check #9, Check #5, Check #3 |
| **Giải pháp** | Hiển thị 2 dòng mô tả; hoặc tap-to-expand tooltip |
| **DDL** | UXG-022 |

---

#### UXP-010 · Minor
| **Màn hình** | Tài khoản Tiết kiệm › Lịch sử Giao dịch |
|---|---|
| **Vấn đề** | Số tài khoản 16 ký tự không formatted |
| **Gap ref** | Check #5, Check #11, Check #3 |
| **Giải pháp** | Format: `9099-7987-1231-3123` với dấu gạch |
| **DDL** | UXG-022 |

---

#### UXP-011 · Critical
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết Giao dịch |
|---|---|
| **Vấn đề** | Thiếu Share/Print biên lai — vi phạm DDL receipt-preview-1 spec |
| **Gap ref** | Check #2 |
| **Giải pháp** | Thêm bottom action bar: "Chia sẻ biên lai" + "Lưu PDF" + "Báo lỗi giao dịch" |
| **DDL** | receipt-preview-1 |

---

#### UXP-012 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết Giao dịch |
|---|---|
| **Vấn đề** | Thiếu trạng thái giao dịch (Thành công/Đang xử lý) |
| **Gap ref** | Check #3 |
| **Giải pháp** | Thêm status badge ("✅ Thành công") với màu semantic ngay dưới header |
| **DDL** | UXG-031 |

---

#### UXP-013 · Major
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết Giao dịch |
|---|---|
| **Vấn đề** | Số tiền không có visual hierarchy — không được emphasized |
| **Gap ref** | Check #5, Check #7 |
| **Giải pháp** | Font-size 24px bold, màu semantic (xanh/đỏ tùy chiều GD) cho số tiền |
| **DDL** | UXG-003 |

---

#### UXP-014 · Minor
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết Giao dịch |
|---|---|
| **Vấn đề** | Nội dung giao dịch thiếu dấu tiếng Việt |
| **Gap ref** | Check #6 |
| **Giải pháp** | Normalize encoding: "Tien tiet kiem" → "Tiền tiết kiệm" |
| **DDL** | UXG-012 |

---

#### UXP-015 · Minor
| **Màn hình** | Tài khoản Tiết kiệm › Chi tiết Giao dịch |
|---|---|
| **Vấn đề** | Dead whitespace ~70% màn hình |
| **Gap ref** | Check #7, Check #5 |
| **Giải pháp** | Thêm section "Giao dịch liên quan" hoặc "Thao tác nhanh" (Liên hệ hỗ trợ, Đặt câu hỏi) |
| **DDL** | UXG-003 |
