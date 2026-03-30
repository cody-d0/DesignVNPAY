# SCR-TRK-001 — Tra soát khiếu nại › Danh sách

**Screen ID:** SCR-TRK-001  
**Figma node:** 142:29627  
**Screen type:** list  
**Flow:** Tạo yêu cầu tra soát khác  
**Wireframe:** `ui/tra-soat-khac-0.png`

---

## 1. Flow & Navigation

- **Entry point:** Menu chính → Tra soát khiếu nại
- **Tab navigation:** "Tạo yêu cầu" (active) | "Tra cứu yêu cầu" (inactive)
- **Menu items:**
  1. Tra soát giao dịch qua Mobilebanking → [flow khác]
  2. Tra soát khác → SCR-TRK-002
- **Back:** Quay về màn hình trước

### User Story

> Là người dùng Co-opBank, tôi muốn chọn loại tra soát để bắt đầu tạo yêu cầu tra soát phù hợp với giao dịch của tôi.

---

## 2. UX Signal Inference (Phase 4e · scope=screen)

**Signals detected:**
- Tab navigation → user cần chuyển đổi giữa "Tạo yêu cầu" và "Tra cứu yêu cầu" (2 modes)
- Chevron-right per menu item → disclosure navigation pattern
- 2 loại tra soát → phân loại rõ ràng (Mobilebanking vs Khác)

**Inferred UX:**
- **Pattern:** Tab + menu list → giảm cognitive load bằng phân cấp 2 tầng
- **Component:** Tab bar (2 tabs), Menu list (2 items với icon + label + chevron)
- **State:** Tab active underline, menu item normal/pressed
- **DDL ref:** ux-guidelines.csv#22 (Tab Navigation), ux-guidelines.csv#45 (Menu List Disclosure)

---

## 3. Mô tả màn hình

| Element | Mô tả | Ghi chú |
|---------|-------|---------|
| Header | "Tra soát khiếu nại" | Back arrow trái, title center |
| Tab bar | "Tạo yêu cầu" (active), "Tra cứu yêu cầu" | Active underline màu primary |
| Menu item 1 | Icon mobile + "Tra soát giao dịch qua Mobilebanking" + chevron | Row full-width |
| Menu item 2 | Icon calendar + "Tra soát khác" + chevron | Row full-width |
| Background | Light gray (#f5f5f5) | Empty state bên dưới 2 items |

### NFR

- Touch target mỗi menu row ≥ 44px height
- Tab switching phải < 300ms
- Separator giữa 2 menu items rõ ràng

---

## 4. UX Improvements (từ signal inference)

- **[Improvement 1]** Thiếu empty state guidance: Bên dưới 2 menu items là vùng trắng rỗng — nên có micro-copy giải thích "Chọn loại tra soát để bắt đầu tạo yêu cầu". DDL ref: ux-guidelines.csv#67 (Empty State Guidance)
- **[Improvement 2]** Tab "Tra cứu yêu cầu" không có badge count — người dùng không biết có bao nhiêu yêu cầu đang xử lý. Cân nhắc thêm badge số. DDL ref: ux-laws.csv#hick (Hick's Law — reduce decision time)
