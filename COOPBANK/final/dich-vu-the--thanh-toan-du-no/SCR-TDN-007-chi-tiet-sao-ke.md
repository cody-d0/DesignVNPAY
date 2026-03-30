# SCR-TDN-007 — Chi tiết sao kê - Hệ thống

**Display Name:** Chi tiết sao kê - Hệ thống › Chi tiết  
**Screen ID:** SCR-TDN-007  
**Screen Type:** detail  
**Flow Stage:** detail_view  
**Wireframe:** `ui/chi-tiet-sao-ke-he-thong.png`

---

## 1. User Flow & Context

**Vị trí trong flow:** Leaf node — Chi tiết một tháng sao kê thẻ, hiển thị bởi system file viewer (không phải native UI component).

**Flow từ màn hình này:**
- ← Back: Về SCR-TDN-006 (system back button)

**Note kiến trúc:** Màn hình này là system-rendered content — placeholder "Xem file sao kê thẻ" cho thấy đây là in-app webview hoặc native document viewer được nhúng. Không có custom UI components. Design team nên xem xét thay thế bằng in-app PDF viewer.

**User Story:**
> Với tư cách là chủ thẻ tín dụng, tôi muốn xem chi tiết sao kê tháng dưới dạng file PDF để kiểm tra các giao dịch và số tiền trong kỳ thanh toán.

**🤖 AI UX Inferences (by ux-signal-inference — scope=screen):**
- `embedded_file_viewer`: Screen là system PDF viewer placeholder — minimal design intent từ thiết kế. UX risk: user mất context app (navigation, header), không có back button native của app. DDL ref: UXG in-app browser/viewer patterns
- `system_screen_limited_control`: Chỉ có "Xem file sao kê thẻ" — không có search, bookmark, zoom controls visible trong wireframe. Có thể được provided by OS-level viewer.

---

## 2. Non-Functional Requirements

| # | Yêu cầu | Mức độ |
|---|---------|--------|
| NFR-001 | PDF load: progress indicator, không blank screen | Critical |
| NFR-002 | PDF render: text selectable, pinch-to-zoom | High |
| NFR-003 | Navigation: app back button visible (không mất trong system viewer) | Critical |
| NFR-004 | Print/share PDF: functionality available | Medium |
| NFR-005 | Security: PDF download requires authentication | High |

---

## 3. Mô tả màn hình

![Chi tiết sao kê hệ thống](ui/chi-tiet-sao-ke-he-thong.png)

| # | Element | Loại | Nội dung / Hành vi | DDL Ref |
|---|---------|------|---------------------|---------|
| 1 | System viewer | Container | Full-screen document viewer | `embedded_file_viewer` |
| 2 | Placeholder text | Display | "Xem file sao kê thẻ" | — |
| 3 | System controls | System UI | OS-native PDF controls (zoom, share, print) | — |

**Note:** Wireframe này chỉ là placeholder. Thiết kế thực tế khi có file PDF sẽ do system viewer render (iOS: QuickLook, Android: PdfRenderer hoặc third-party).

**OCR UX Gaps:**
- Không có app-level navigation bar (back button)
- Không có loading state
- Không có error state (nếu PDF fail to load)
- Placeholder text không informative

---

## 4. Đề xuất cải thiện UX

| Ưu tiên | Vấn đề | Đề xuất |
|---------|--------|---------|
| Critical | Mất navigation context khi vào system viewer | Dùng in-app PDF viewer wrapper với Co-opBank header + back button |
| Critical | Không có loading/error state | Thêm: skeleton loader → PDF content; error state với "Thử lại" |
| High | System viewer không có branding | Wrap PDF viewer với Co-opBank app chrome |
| High | User không biết mình đang xem tháng nào | Thêm breadcrumb: "Sao kê tháng 11/2025" trong header |
| Medium | PDF chỉ view, không thể download | Thêm Download button với authentication |
| Medium | Không thể tìm kiếm trong sao kê | Nếu dùng in-app viewer, enable native PDF search |

---

## 5. PRD References

- **Figma node:** 142:173923
- **Domain:** banking
- **Architecture note:** System-rendered screen — requires native PDF viewer integration or in-app WebView PDF solution
- **Recommendation:** Replace system placeholder với `PSPDFKit`, `PDFTron`, hoặc iOS QuickLook wrapped với custom chrome
