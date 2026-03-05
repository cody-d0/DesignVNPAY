# Co-op Bank KHCN — Chuyển tiền nội bộ khác chủ

## Thông tin chung

| Thuộc tính | Giá trị |
|---|---|
| Sản phẩm | Co-op Bank KHCN (Mobile Banking) |
| Module | Chuyển tiền |
| Tính năng | Chuyển tiền nội bộ khác chủ tài khoản |
| Platform | iOS / Android (Mobile-first, 375×812pt) |
| Figma Source | [Co-op Bank KHCN — Chuyển tiền nội bộ khác chủ](https://www.figma.com/design/kPft93N2A3gYOC3YwuXpQR/Co-op-Bank-KHCN?node-id=5199-5930&m=dev) |
| Ngôn ngữ | Tiếng Việt |
| Font | Nunito Sans (Bold 700, Regular 400) |
| Design System | Co-op Bank Design System (gradient primary #285598 → #002a69, neutrals, semantic colors) |

## Mô tả tổng quan

Tính năng **Chuyển tiền nội bộ khác chủ** cho phép khách hàng cá nhân (KHCN) thực hiện giao dịch chuyển tiền đến tài khoản khác chủ sở hữu trong hệ thống Co-op Bank. Tính năng hỗ trợ:

- Chuyển tiền ngay (one-time transfer)
- Đặt lịch chuyển tiền định kỳ (scheduled/recurring transfer)
- Xác thực giao dịch qua SMS OTP
- Lưu danh bạ thụ hưởng để tái sử dụng

## Danh sách màn hình (Screen Inventory)

| # | Màn hình | File | Số artboard | Mô tả |
|---|---|---|---|---|
| 1 | Nhập thông tin chuyển tiền | [nhap-thong-tin-chuyen-tien.md](./package-2/chuyen-tien-noi-bo-khac-chu/nhap-thong-tin-chuyen-tien.md) | 4 | Form nhập: tài khoản nguồn, người hưởng, số tiền, nội dung, đặt lịch. Bao gồm 2 state chính (toggle đặt lịch off/on) và 2 popup xác nhận. |
| 2 | Xác nhận giao dịch | [xac-nhan-giao-dich.md](./package-2/chuyen-tien-noi-bo-khac-chu/xac-nhan-giao-dich.md) | 2 | Review thông tin + xác thực OTP. Bao gồm state base (review) và state OTP bottom sheet. |
| 3 | Kết quả giao dịch | [ket-qua-giao-dich.md](./package-2/chuyen-tien-noi-bo-khac-chu/ket-qua-giao-dich.md) | 1 | Hiển thị kết quả đặt lịch thành công, chi tiết giao dịch, hành động chia sẻ/lưu ảnh. |

## User Flow tổng quan

```
[Nhập thông tin chuyển tiền]
    ├── Toggle đặt lịch OFF → Chuyển tiền ngay
    │       └── Nhấn "Tiếp tục"
    │               └── [Xác nhận giao dịch]
    │                       └── Nhập OTP → Xác nhận
    │                               └── [Kết quả giao dịch]
    │
    └── Toggle đặt lịch ON → Chuyển tiền định kỳ
            ├── Chọn tần suất (Hàng tháng)
            ├── Nhập số lần giao dịch
            ├── Chọn ngày bắt đầu / kết thúc
            └── Nhấn "Tiếp tục"
                    └── [Popup xác nhận thông tin]
                            └── Đồng ý
                                    └── [Xác nhận giao dịch]
                                            └── Nhập OTP → Xác nhận
                                                    └── [Kết quả giao dịch]
```

## Design Tokens (tham khảo)

| Token | Giá trị | Mô tả |
|---|---|---|
| `--primary/1000` | `#002a69` | Màu chính đậm (header, CTA gradient end) |
| `--neutrals/0` | `#FFFFFF` | Trắng (text trên header, button label) |
| `--neutrals/900` | `#828190` | Text muted (label, placeholder) |
| `--neutrals/1000` | `#050421` | Text chính (value, content) |
| `--neutrals/800` | `#acaeba` | Placeholder text |
| `--secondary/rojo` | `#e50019` | Đỏ (số tiền bằng chữ, ngày kết thúc, amount highlight) |
| `--background/basement` | `#FFFFFF` | Nền card/section |
| `--background/card` | `#f5f5f5` | Nền page |
| `--background/text-field` | `#f6f7f9` | Nền OTP input |
| `--border` | `rgba(162,165,184,0.2)` | Viền divider |
| `--blur` | `rgba(5,4,33,0.7)` | Overlay mờ (popup, bottom sheet) |
| Button gradient | `#285598 → #002a69` | Gradient nút chính |
| `--radius/8*4` | `8px` | Border-radius button |
| `--radius/12*4` | `12px` | Border-radius card, balance-card |
| `--radius/16*4` | `16px` | Border-radius bottom sheet, result card |

## Typography

| Style | Font | Weight | Size | Line Height |
|---|---|---|---|---|
| Heading | Nunito Sans | Bold 700 | 18px | 26px |
| Title | Nunito Sans | Bold 700 | 16px | 22px |
| Nunito Sans/LG | Nunito Sans | Bold 700 | 17px | 24px |
| Nunito Sans/MD | Nunito Sans | Bold 700 | 15px | 20px |
| Body | Nunito Sans | Regular 400 | 15px | 20px |
| Label text/LT1 | Nunito Sans | Bold 700 | 13px | 18px |
| Label text/LT2 | Nunito Sans | Regular 400 | 13px | 18px |
| Heading/Bold 21 | Nunito Sans | Bold 700 | 21px | auto |

---

## Kết quả chạy pipeline (Phase Report)

| Phase | Status | Chi tiết |
|---|---|---|
| **Phase 0: Scan & Scope** | ⏭️ SKIPPED | Node-id = section-level (5199:5930), không cần scan page. |
| **Phase 1: Figma MCP Extract** | ✅ DONE | `get_metadata` → 7 frames (all "internal-transaction", 375px mobile). `get_design_context` × 5 screens (key states). `get_screenshot` → section overview. Screenshots saved via `save-figma-section-screenshots.js` → 7 artboards. Post-step: moved to `ui/`. |
| **Phase 2: Screen Inventory** | ✅ DONE | `screen_boundaries`: 3 distinct screens (nhập thông tin, xác nhận, kết quả) mapped from 7 frames. `component_registry`: header, balance-card, section, list-item, input-field, select-field, switch, button-primary, dialog, bottom-sheet, otp-input, success-header, bill-detail, separator. `flow_graph`: 3 edges (nhập → xác nhận → kết quả → nhập). OCR: agent vision 2 rounds per screen (text + icon). |
| **Phase 3: PRD Structure Gen** | ✅ DONE | 1 overview + 3 feature .md files. 5 sections per file (Chân dung KH, User Story, Wireframe, Database, NFR). Screen parity: 3 screens = 3 files ✓. |
| **Phase 4: Augment** | ✅ DONE | COMPextend proposals: US-012 (Gửi lại OTP), US-013 (Quay lại chỉnh sửa), US-023 (Về trang chủ). Persona mở rộng. AI badge applied with citation + confidence. |
| **Phase 5: Output** | ✅ DONE | .md pack written. `.handoff/handoff-manifest.json` written. Image paths verified (7 .png in `ui/`). |

### UNSPECIFIED Summary

Các thông tin chưa rõ từ Figma cần confirm với stakeholder:

| # | Item | Lý do | Gợi ý |
|---|---|---|---|
| 1 | Field labels trong State 2 (schedule form) | Figma dùng placeholder "Label" cho tần suất, số lần, ngày bắt đầu | Confirm label text thực tế với BA/Designer |
| 2 | Nội dung popup thông báo (State 3, 4) | Figma chỉ có layout, text trong popup không rõ | Cần spec cụ thể: "Bạn có chắc chắn muốn đặt lịch?" vs "Số tiền vượt hạn mức" |
| 3 | Số tiền trên màn kết quả | Figma hiển thị "50,000 VND" khác với form input "20,000,000 VND" | Có thể là 2 test case khác nhau — confirm |
| 4 | Phương thức xác thực khác SMS OTP | Figma chỉ show SMS OTP trong dropdown | Hỏi có hỗ trợ Smart OTP, Face ID, etc. |
| 5 | Trạng thái giao dịch thất bại | Figma chỉ có artboard success | Cần thiết kế màn failure/error |
| 6 | Tài khoản nguồn "12300123123000" vs "9099798712313123" | Figma dùng sample data khác nhau giữa các frame | Chỉ là mockup data, không ảnh hưởng logic |

---

*Generated from Figma: Co-op Bank KHCN — Section "Chuyển tiền nội bộ khác chủ" (node 5199:5930)*
*Pipeline: figma-to-prd-md v3 | Date: 2026-02-26*
