# SCR-TRK-005 — Kết quả giao dịch › Kết quả tra soát

**Screen ID:** SCR-TRK-005  
**Figma node:** 142:29606  
**Screen type:** result  
**Flow:** Tạo yêu cầu tra soát khác  
**Wireframe:** `ui/tra-soat-khac-6.png`

---

## 1. Flow & Navigation

- **Entry:** SCR-TRK-004 (OTP confirm)
- **Actions:**
  - "Chia sẻ" → share receipt
  - "Lưu ảnh" → save screenshot
  - "Tạo yêu cầu mới" → SCR-TRK-001 hoặc SCR-TRK-002 (reset flow)
- **Home:** Thoát về màn hình chính

### User Story

> Là người dùng Co-opBank, sau khi xác thực OTP, tôi muốn xem kết quả lập yêu cầu tra soát thành công, bao gồm mã tra soát và thời gian thụ lý.

---

## 2. UX Signal Inference (Phase 4e · scope=screen)

**Signals detected:**
- "✓" → success state icon
- "Quý khách đã lập yêu cầu tra soát thành công!" → success confirmation message
- "Mã tra soát: UT123123" → transaction reference ID → copyable?
- "29/09/2025 12:30" → timestamp of request submission
- "Co-opBank sẽ xử lý yêu cầu và cập nhật kết quả xử lý tới Quý khách trong thời gian tra soát quy định." → next-step guidance (thời gian xử lý không rõ)
- "Chia sẻ / Lưu ảnh" → secondary social actions
- "Tạo yêu cầu mới" → loop-back action

**Inferred UX:**
- **Pattern:** Transaction receipt / success state
- **Component:** Success card (logo + icon + message + data rows), Action row (share + save), Secondary CTA
- **State:** Success terminal state
- **DDL ref:** ux-guidelines.csv#58 (Success State), ux-guidelines.csv#63 (Transaction Receipt), ux-laws.csv#doherty (Acknowledged completion)

---

## 3. Mô tả màn hình

| Element | Nội dung | Ghi chú |
|---------|---------|---------|
| Header | "Kết quả giao dịch" | Home icon trái (không có back) |
| Card | White card trung tâm | Bo góc, shadow |
| Logo | Co-opBank logo | Top of card |
| Success icon | ✓ (checkmark circle) | Màu success green/blue |
| Success message | "Quý khách đã lập yêu cầu tra soát thành công!" | Bold, center |
| Mã tra soát | UT123123 | Row label-value |
| Lý do tra soát | Chưa nhận được tiền | Row label-value |
| Thời gian tra soát | 29/09/2025 12:30 | Row label-value |
| Info note | "Co-opBank sẽ xử lý yêu cầu…" | Gray italic text |
| Divider kẻ ngang | — | Phân cách khỏi actions |
| Chia sẻ | Icon share + label | Action phụ |
| Lưu ảnh | Icon camera + label | Action phụ |
| CTA "Tạo yêu cầu mới" | Bottom full-width | Ghost/outline button |
| Background | Dark navy (#0a2d6e) | Contrast với white card |

### NFR

- "Mã tra soát" phải copyable (tap to copy)
- Card phải có shadow/elevation để nổi trên background
- "Tạo yêu cầu mới" không được là primary button (tránh accidental tap)
- Action "Chia sẻ" share native OS sheet

---

## 4. UX Improvements (từ signal inference)

- **[Major] Thời gian xử lý không cụ thể:** "trong thời gian tra soát quy định" rất mơ hồ — không cho user biết cụ thể bao nhiêu ngày. Nên thêm SLA cụ thể (VD: "trong vòng 5-7 ngày làm việc"). DDL ref: ux-guidelines.csv#63 (Expectation Setting), ux-laws.csv#doherty
- **[Minor] "Mã tra soát" không có tap-to-copy:** UT123123 là mã tham chiếu quan trọng — user cần copy để follow up. Nên thêm icon copy và feedback "Đã sao chép". DDL ref: ux-guidelines.csv#65 (Copyable Data)
- **[Minor] Action "Chia sẻ" và "Lưu ảnh" không có icon rõ ràng trong thiết kế:** Từ ảnh, 2 actions này thiếu visual cue đủ mạnh — nên dùng icon + label với nền nhạt. DDL ref: ux-guidelines.csv#23 (Secondary Action Visibility)
- **[Minor] "Tạo yêu cầu mới" nên ra danh sách, không về form ngay:** Nên về SCR-TRK-001 (chọn loại tra soát) thay vì trực tiếp vào form — để user chọn đúng loại tra soát cần tạo. DDL ref: ux-guidelines.csv#28 (Navigation Clarity)
