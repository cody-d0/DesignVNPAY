# Component Mapping Dictionary

Core knowledge cho Phase 2: map Figma layer names → `prd_type` + `component_key`.

Reusable bởi: `figma-to-prd-md` (Phase 2b), `pdr-extract`, `comp-extraction`.

---

## Recognition Strategy (theo thứ tự ưu tiên)

1. **Slash-name match**: Figma dùng `Component/Variant/State` (vd: `Button/Primary/Default`, `Input/Text/Focused`) → tách phần đầu làm component type, phần sau làm variant/state metadata
2. **Exact match**: Figma component name (PascalCase hoặc Title Case) khớp known `prd_type`
3. **Pattern match**: layer name chứa keyword pattern (case-insensitive, wildcard)
4. **Structural inference**: auto-layout structure ngụ ý component type (xem cột Figma Clues)
5. **Fallback**: `NEW_KEY_CANDIDATE` với best-guess group từ structural analysis

**Nguồn tham chiếu mapping:** PRD output thực tế (XPOS, co-op-bank-khcn), ui-ux-pro-max (accessibility, touch target, loading/error states), frontend-design (Design Thinking, Pre-Delivery), Ant Design / Ant Design Vue component taxonomy (General, Layout, Navigation, Data Entry, Data Display, Feedback, Other).

---

## Mapping Dictionary

### Input/Form

| Figma Layer Pattern | prd_type | component_key | Figma Clues |
|---|---|---|---|
| `*input*`, `*text field*`, `*text-field*`, `Input/*` | Input Field | `input-field` | Single-line frame, placeholder text, border, auto-layout horizontal (icon + text) |
| `*phone*input*`, `*sdt*`, `*tel*` | Input Field (SĐT) | `input-field-phone` | Input with phone icon or +84 prefix; keyboard type = `tel` |
| `*password*`, `*pass*field*` | Input Field (Pass) | `input-field-password` | Input with eye/show-hide icon (toggle visibility) |
| `*otp*`, `*verification*code*`, `*pin*input*` | OTP/Pin Input | `otp-input` | Row of 4-6 equal-width boxes, auto-layout horizontal, gap equal |
| `*textarea*`, `*text*area*`, `*multiline*` | Textarea | `textarea` | Multi-line frame, height > 2x single input, scroll indicator hoặc character counter |
| `*switch*`, `*toggle*` | Switch | `switch` | Small frame (36-52px wide) with circle + track, 2 states |
| `*select*`, `*dropdown*` (in form context), `Select` | Dropdown | `select-field` | Input-like frame with chevron-down icon trailing; Ant Design Select |
| `*radio*`, `*radio*button*`, `*radio*group*` | Radio Button | `radio-button` | Circle (16-20px) with inner dot when selected; thường trong group vertical |
| `*checkbox*` | Checkbox | `checkbox` | Small square (16-20px) with check icon |
| `*upload*`, `*file*upload*`, `*drag*drop*` | Upload Area | `upload-area` | Large dashed-border frame, icon upload/cloud, text "Kéo thả" |
| `*date*picker*`, `*calendar*`, `*ngay*`, `DatePicker`, `Calendar` | Date Picker | `date-picker` | Input with calendar icon; hoặc grid 7 columns (calendar view) |
| `*read*only*`, `*disabled*input*` | Read-only Field | `read-only-field` | Input appearance nhưng không có border focus, text muted, có lock icon hoặc note "không thể chỉnh sửa" |
| `*input*number*`, `InputNumber`, `*number*input*` | Input Number | `input-number` | Input restricted to digits, optional stepper (+/-), min/max; Ant Design InputNumber |
| `*auto*complete*`, `AutoComplete` | AutoComplete | `autocomplete` | Input with dropdown suggestions below, typeahead; Ant Design AutoComplete |
| `*cascader*`, `Cascader` | Cascader | `cascader` | Multi-level select (vd: Tỉnh → Huyện → Xã); Ant Design Cascader |
| `*time*picker*`, `TimePicker` | Time Picker | `time-picker` | Input or dropdown with time selection (HH:mm); Ant Design TimePicker |
| `*slider*`, `Slider` | Slider | `slider` | Horizontal track + thumb, min/max value; Ant Design Slider |
| `*rate*`, `Rate` | Rate | `rate` | Row of star icons (1-5), clickable; Ant Design Rate |
| `*mentions*`, `Mentions` | Mentions | `mentions` | Input with @ trigger, dropdown list (user/tag mention); Ant Design Mentions |
| `*tree*select*`, `TreeSelect` | Tree Select | `tree-select` | Select with hierarchical tree (expand/collapse); Ant Design TreeSelect |
| `*transfer*`, `Transfer` | Transfer | `transfer` | Two lists with move buttons (source ↔ target); Ant Design Transfer |
| `*form*` (wrapper) | Form | `form` | Container group: label + control + helper/error per field; Ant Design Form |

### Layout

| Figma Layer Pattern | prd_type | component_key | Figma Clues |
|---|---|---|---|
| `*header*`, `*top*bar*`, `*app*bar*`, `*nav*bar*` (top) | Header | `header` | Top-positioned, full-width, auto-layout horizontal: [back icon, title, action icons] |
| `*header*view*`, `*hero*`, `*banner*` (top large) | Header View | `header-view` | Top section cao hơn header thường (>120px), có illustration/gradient, title + subtitle |
| `*footer*` (không sticky) | Footer | `footer` | Bottom-positioned, full-width, thường chứa links/info |
| `*sticky*footer*`, `*bottom*cta*`, `*fixed*bottom*` | Sticky Footer | `sticky-footer` | Fixed bottom bar chứa tổng tiền/count + CTA button, shadow top |
| `*bottom*bar*`, `*tab*bar*`, `*bottom*nav*` | Bottom Bar | `bottom-bar` | Fixed bottom, 3-5 equal columns, mỗi column: icon + label stacked |
| `*separator*`, `*divider*`, `Divider` | Separator | `separator` | 1-2px height, full-width, color muted; Ant Design Divider |
| `*modal*`, `*dialog*`, `*popup*`, `Modal` | Dialog | `dialog` | Centered frame with backdrop/overlay, border-radius, shadow; Ant Design Modal |
| `*bottom*sheet*`, `*drawer*`, `*action*sheet*` | Bottom Sheet | `bottom-sheet` | Frame từ bottom lên, top handle bar (40px wide, 4px tall), border-radius top |
| `*accordion*`, `*expand*`, `*collapse*`, `Collapse` | Accordion | `accordion` | Frame with title row (text + chevron) + collapsible content area; Ant Design Collapse |
| `*section*`, `*group*` (content grouping) | Section | `section` | Auto-layout vertical: [heading text + content group], padding, optional divider |
| `*form*section*` | Form Section | `form-section` | Section chứa group input fields, có heading bold + multiple inputs stacked |
| `*stepper*`, `*step*indicator*`, `*progress*step*`, `Steps` | Stepper | `stepper` | Horizontal row: numbered circles/dots connected by lines, active state highlighted; Ant Design Steps |
| `*flex*`, `Flex` | Flex | `flex` | Auto-layout frame (row/column), gap, wrap; Ant Design Flex |
| `*grid*`, `Grid` | Grid | `grid` | Multi-column layout, row/col span; Ant Design Grid |
| `*space*`, `Space` | Space | `space` | Wrapper with consistent gap between children; Ant Design Space |
| `*page*header*`, `PageHeader` | Page Header | `page-header` | Title + breadcrumb + extra actions row; Ant Design PageHeader |
| `*affix*`, `Affix` | Affix | `affix` | Element fixed when scroll (e.g. navbar sticks to top); Ant Design Affix |
| `*watermark*`, `Watermark` | Watermark | `watermark` | Diagonal text/image overlay (draft, confidential); Ant Design Watermark |
| `*app*shell*`, `*main*layout*` | App Shell | `app-shell` | Full-screen: header + content area + bottom-bar stacked vertically |
| `*split*view*`, `*master*detail*` | Split View | `split-view` | Horizontal: list pane left + detail pane right (tablet/desktop) |
| `*sidebar*`, `*side*nav*` | Sidebar | `sidebar` | Vertical nav, width 240-280px, left-positioned, collapsible |
| `*tab*content*`, `*tab*panel*` | Tab Panel | `tab-panel` | Content area dưới filter-tabs, thay đổi theo tab active |
| `*quick*action*`, `*action*grid*` | Quick Action Grid | `quick-action-grid` | Grid 2×2 hoặc 3×3: icon + label mỗi cell, equal-width columns |

### Navigation/Action

| Figma Layer Pattern | prd_type | component_key | Figma Clues |
|---|---|---|---|
| `*button*primary*`, `*btn*primary*`, `Button/Primary*` | Button (Primary) | `button-primary` | Filled solid background, prominent text, full-width hoặc auto, min-height 44-48px |
| `*button*outline*`, `*btn*secondary*`, `*btn*ghost*` | Button (Outline) | `button-outline` | Border only, transparent/light fill, same size as primary |
| `*button*destruct*`, `*btn*danger*`, `*logout*`, `*delete*btn*` | Button (Destructive) | `button-destructive` | Red/danger fill hoặc red text, cùng structure với primary/outline |
| `*fab*`, `*float*action*`, `*add*button*` (circular) | FAB Button | `fab-button` | Circle 48-56px, single icon (thường "+"), shadow, fixed position bottom-right |
| `*icon*btn*`, `*icon*button*` (icon-only) | Icon Button | `icon-button` | Square/circle frame 32-48px chỉ chứa 1 icon, không có text label |
| `*button*`, `*btn*`, `*cta*` (generic) | Button | `button` | Interactive frame with text + optional icon, padding horizontal, min-height 44px |
| `*link*`, `*text*link*`, `Typography*Link*` | Link | `link` | Underlined or colored text, inline within paragraph; Ant Design Typography.Link |
| `*action*link*` | Action Link | `action-link` | Text + arrow/chevron trailing, standalone (không inline), thường dẫn sang màn khác |
| `*breadcrumb*`, `Breadcrumb` | Breadcrumbs | `breadcrumbs` | Horizontal row: text items separated by "/" hoặc ">"; Ant Design Breadcrumb |
| `*menu*`, `Menu` (vertical/horizontal nav) | Menu | `menu` | List of nav items (vertical or horizontal), active item highlighted, optional submenu; Ant Design Menu |
| `*dropdown*`, `Dropdown` (nav/action) | Dropdown Menu | `dropdown-menu` | Trigger (button/text) + overlay menu list; Ant Design Dropdown |
| `*anchor*`, `Anchor` | Anchor | `anchor` | In-page links to sections (sidebar or inline); Ant Design Anchor |
| `*pagination*`, `Pagination` | Pagination | `pagination` | Prev/Next + page numbers (1,2,3…), optional page size; Ant Design Pagination |
| `*icon*`, `Icon` (standalone) | Icon | `icon` | Single SVG/symbol, 16-24px; Ant Design Icon — dùng cho aria-label khi icon-only (ui-ux-pro-max) |

### Search/Filter

| Figma Layer Pattern | prd_type | component_key | Figma Clues |
|---|---|---|---|
| `*search*` | Search Bar | `search-bar` | Input with magnifying glass icon leading, pill/rounded border, placeholder text |
| `*filter*`, `*dropdown*filter*` | Dropdown Filter | `dropdown-filter` | Button/select with filter icon, thường nằm cạnh search bar |
| `*tab*`, `*tabs*`, `Tabs` (horizontal row, content area) | Filter Tabs | `filter-tabs` | Horizontal row items, active item có underline/background highlight; Ant Design Tabs |
| `*chip*`, `*tag*`, `*pill*`, `Tag` (selectable) | Chip/Tag | `chip` | Small rounded frame (24-32px height), text + optional close icon, border; Ant Design Tag |
| `*segmented*`, `Segmented` | Segmented Control | `segmented` | Horizontal group of options, one selected (pill/tab style); Ant Design Segmented |

### Cards/Lists

| Figma Layer Pattern | prd_type | component_key | Figma Clues |
|---|---|---|---|
| `*card*` (generic), `Card` | Card Item | `card-item` | Rounded frame, shadow/elevation, auto-layout vertical, padding, content group; Ant Design Card |
| `*product*card*` | Product Card | `product-card` | Card: image top + name + price text, optional badge/label |
| `*order*card*` | Order Card | `order-card` | Card: order ID (monospace) + status badge + amount + timestamp |
| `*stat*card*`, `*statistic*`, `*metric*`, `Statistic` | Statistic Cards | `statistic-cards` | Card: large number (heading size) + label small + optional trend arrow; Ant Design Statistic |
| `*contact*item*`, `*beneficiary*` | Contact Item | `contact-item` | Horizontal: avatar circle + name (bold) + subtitle (account number), divider |
| `*list*item*`, `*row*`, `*menu*item*` | List Item | `list-item` | Horizontal auto-layout: [left icon/avatar, text group, right chevron/action], full-width |
| `*list*`, `List` (container) | List | `list` | Vertical stack of list items, optional header/footer; Ant Design List |
| `*table*`, `Table` | Table | `table` | Grid: header row + data rows, sortable/filterable columns; Ant Design Table — cần data-table a11y (ui-ux-pro-max) |
| `*descriptions*`, `Descriptions` | Descriptions | `descriptions` | Label-value pairs in grid (2-col layout), multi-row; Ant Design Descriptions |
| `*avatar*`, `Avatar` | Avatar | `avatar` | Circle 32-48px, chứa image hoặc initials text, optional status dot; Ant Design Avatar |
| `*badge*`, `*notification*badge*`, `*count*`, `Badge` | Badge | `badge` | Small circle/pill (16-24px), number hoặc dot, position absolute trên icon/avatar; Ant Design Badge |
| `*carousel*`, `Carousel` | Carousel | `carousel` | Horizontal scroll/swipe, multiple slides, dots or arrows; Ant Design Carousel |
| `*image*`, `Image` (component) | Image | `image` | Image with placeholder/fallback, optional preview; Ant Design Image — cần alt text (ui-ux-pro-max) |
| `*tree*`, `Tree` (hierarchical list) | Tree | `tree` | Nested nodes, expand/collapse, checkbox optional; Ant Design Tree |
| `*comment*`, `Comment` | Comment | `comment` | Avatar + author + content + datetime, nested replies; Ant Design Comment |
| `*timeline*`, `Timeline` | Timeline | `timeline` | Vertical/horizontal steps with dot + line, date + content; Ant Design Timeline |
| `*calendar*`, `Calendar` (full view) | Calendar | `calendar` | Month grid, date cells, events; Ant Design Calendar |

### Info/Feedback

| Figma Layer Pattern | prd_type | component_key | Figma Clues |
|---|---|---|---|
| `*infobox*`, `*alert*`, `*notice*`, `*callout*`, `Alert` | Infobox | `infobox` | Colored background frame (blue/yellow/red tint) + icon left + text, border-radius, padding; Ant Design Alert |
| `*helper*text*` | Helper Text | `helper-text` | Small text (12-14px) trực tiếp dưới input field, color muted |
| `*error*text*`, `*error*helper*`, `*error*message*` | Error Helper Text | `error-helper-text` | Small text dưới input, color red/danger, thường kèm error icon |
| `*requirement*`, `*validation*rule*`, `*password*rule*` | Requirement Box | `requirement-box` | List check/cross items (vd: "Tối thiểu 6 ký tự ✓"), each row: icon + text |
| `*growth*label*`, `*trend*` | Growth Label | `growth-label` | Small text with arrow icon (↑/↓) + percentage, color green (up) / red (down) |
| `*success*header*`, `*success*banner*` | Success Header | `success-header` | Large area: green/blue background + checkmark icon + "Thành công" text |
| `*success*popup*` | Success Popup | `success-popup` | Dialog variant: icon tick lớn + congratulation text + CTA buttons |
| `*toast*`, `*snackbar*` | Toast | `toast` | Small frame bottom/top, auto-dismiss, text + optional action link |
| `*toast*banner*` | Toast Banner | `toast-banner` | Full-width card dưới header, shadow, instructional text (không auto-dismiss) |
| `*loading*`, `*spinner*`, `*skeleton*`, `Skeleton`, `Spin` (inline) | Loading State | `loading-state` | Skeleton placeholder (shimmer) hoặc spinner; Ant Design Skeleton/Spin — content-jumping reserve space (ui-ux-pro-max) |
| `*empty*state*`, `*no*data*`, `*no*result*`, `Empty` | Empty State | `empty-state` | Centered: illustration/icon + message text + optional CTA button; Ant Design Empty |
| `*progress*bar*`, `*progress*indicator*`, `Progress` | Progress Bar | `progress-bar` | Horizontal bar: track (gray) + fill (colored), height 4-8px, optional percentage; Ant Design Progress |
| `*tooltip*`, `Tooltip` | Tooltip | `tooltip` | Small floating frame with arrow/pointer, text only; Ant Design Tooltip |
| `*message*`, `Message` | Message | `message` | Global lightweight feedback (top center), auto-close; Ant Design Message |
| `*notification*`, `Notification` | Notification | `notification` | Corner card with title + description + icon; Ant Design Notification |
| `*popconfirm*`, `Popconfirm` | Popconfirm | `popconfirm` | Trigger + small popover "Bạn có chắc?" + Confirm/Cancel; Ant Design Popconfirm |
| `*result*`, `Result` | Result | `result` | Full-page: icon (success/error/info) + title + subTitle + extra buttons; Ant Design Result |
| `*spin*`, `Spin` | Spin | `spin` | Loading spinner overlay or inline; Ant Design Spin — dùng khi async (ui-ux-pro-max loading-buttons) |
| `*popover*`, `Popover` | Popover | `popover` | Trigger + floating panel (rich content); Ant Design Popover |
| `*drawer*`, `Drawer` | Drawer | `drawer` | Panel slide from left/right/top/bottom, overlay; Ant Design Drawer (alias bottom-sheet khi từ bottom) |
| `*tour*`, `Tour` | Tour | `tour` | Step-by-step spotlight overlay (onboarding); Ant Design Tour |

### Special (Domain-specific)

| Figma Layer Pattern | prd_type | component_key | Figma Clues |
|---|---|---|---|
| `*qr*code*`, `*qr*`, `QRCode` | QR Code Container | `qr-code-container` | Square frame (200-280px), QR pattern inside; Ant Design QRCode |
| `*payment*option*` | Payment Options | `payment-options` | Row/grid: radio + icon + label per option (vd: "Tiền mặt", "VNPAY QR") |
| `*bill*detail*`, `*receipt*`, `*order*summary*` | Bill Detail | `bill-detail` | Structured rows: label left (muted) + value right (bold), divider between groups |
| `*timer*`, `*countdown*` | Timer | `timer` | Time display (MM:SS hoặc countdown), monospace/tabular font, often near OTP or QR |
| `*keyboard*`, `*numpad*` | Keyboard | `keyboard` | Grid 3-4 columns of number/action buttons, fixed bottom, height ~240px |
| `*typography*`, `Typography` (block) | Typography | `typography` | Text block: title/paragraph/code/editable/copyable; Ant Design Typography — font pairing (frontend-design) |
| `*float*button*`, `FloatButton` | FAB Button | `fab-button` | Ant Design FloatButton — alias FAB |
| `*illustration*`, `*decoration*`, `*shape*` (standalone), Fallback: bất kỳ node chưa map | Design element | `design-element` | Phần tử trang trí, minh họa, shape không match component khác; Phase 2b-bis dùng khi node visible nhưng không match pattern trên |

**Aliases (tùy chọn):** Mỗi dòng pattern có thể kèm cột **Aliases** — danh sách chuỗi đa ngôn ngữ cùng nghĩa (vd. cho input-field-phone: `phone`, `sdt`, `số điện thoại`). Khi 2b-pre dùng term-equivalents, canonical_term đã đưa về form match pattern; bổ sung Aliases trong mapping cho pattern cụ thể nếu cần match trực tiếp mà không qua file term-equivalents.

---

## Fallback Rules (khi không match)

1. Tách slash-name: nếu layer dùng `Parent/Child/Variant` → lấy Parent làm component type candidate
2. Phân nhóm theo structural analysis (auto-layout direction, children count, size ratio)
3. Sinh kebab-case component_key từ Figma layer name (bỏ dấu tiếng Việt, lowercase); **prd_type** = "Design element", **component_key** = `design-element-{kebab-name}` (Phase 2b-bis sẽ thêm row tương ứng)
4. Đánh dấu `NEW_KEY_CANDIDATE`

---

## States, Description Hints, A11y & Touch

Dùng khi sinh Mô tả (Phase 3) và Phase 4 kiểm tra coverage. `states[]` → bổ sung AC/NFR; `description_hint` → cột Mô tả; `a11y_hint` → Phase 4 COMPextend proposal; `min_touch` → flag khi touch target thiếu.

| component_key | states[] | description_hint | a11y_hint | min_touch |
|---|---|---|---|---|
| input-field | default, focus, filled, error, disabled, read-only | "[Label]: placeholder '[text]', [N]/[max] ký tự" | `label` hoặc `aria-label`; error dùng `aria-describedby` | — |
| input-field-password | default, focus, visible, hidden, error, disabled | — | — | — |
| button-primary | default, hover, active, disabled, loading | "Nút '[label]' full-width, min-height 48px" | — | 44×48px |
| button-outline | default, hover, active, disabled | — | — | 44×48px |
| icon-button | default, hover, active, disabled | — | Bắt buộc `aria-label` (không có visible text) | 44×44px |
| select-field | default, focus, open, error, disabled | — | — | — |
| otp-input | default, focus, filled, error, expired | "[N] ô, [W]px mỗi ô, auto-focus, countdown [T]s" | Không block paste | — |
| dialog | closed, open, loading | "Modal '[title]': [desc], nút [CTA1] + [CTA2]" | `role="dialog"` + `aria-modal` + focus trap | — |
| infobox | info, warning, error, success | — | Không chỉ dùng màu; kèm icon/text | — |
| loading-state | loading | "[type: skeleton/spinner], [N] placeholder items" | — | — |
| empty-state | empty | "Illustration + '[message]' + nút [CTA]" | — | — |
| list-item | default, selected, swipe-delete | "[icon/avatar] + [title] + [subtitle], chevron phải" | — | full-width × 48px |
| card-item | default, hover, selected, skeleton | "[image] + [title] + [desc] + [badge], shadow, radius [N]px" | — | — |
| search-bar | default, focus, has-value, no-result | — | — | — |
| switch | off, on, disabled | — | `role="switch"` + `aria-checked` | 44×36px (48px tap area) |
| checkbox | unchecked, checked, indeterminate, disabled | — | — | 44×44px tap area |
| radio-button | unselected, selected, disabled | — | — | 44×44px tap area |
| toast | info, success, warning, error | — | `role="alert"` hoặc `aria-live="polite"` | — |
| bottom-sheet | closed, open, expanded | — | Focus trap khi open; `Escape` để close | — |
| stepper | active-step, completed-step, error-step | — | `aria-current="step"` cho active step | — |
| header | default, scrolled, transparent | "Back icon + '[title]' + [action icons], height [H]px" | — | — |
| bill-detail | — | "[N] dòng label-value, tổng tiền in đậm cuối" | — | — |
| fab-button | default, hover, active, disabled | — | — | 48×48px |

---

## Minimum Granularity (bắt buộc khi dùng trong Phase 2b)

- Mỗi **Figma section grouping** (nhóm có tiêu đề, vd: "Thông tin người hưởng", "Thông tin chuyển tiền") → 1 component row riêng với `prd_type` = "Section — {tên nhóm}".
- Mỗi **interactive element** (button, toggle, input, dropdown, radio, checkbox) → 1 component row riêng; không gộp nhiều nút vào 1 row.
- Mỗi **feedback element** (modal, infobox, toast, success header, dialog, loading, empty state) → 1 component row riêng.
- **Tối thiểu per screen:** Màn form → ít nhất 5 rows (header + N form sections + N inputs + buttons + errors/modals nếu có). Màn confirm → ít nhất 4 rows (header, helper text, bill detail/summary, button). Màn result → ít nhất 5 rows (header, success header, bill detail, action icons, CTA button). Màn list → ít nhất 4 rows (header, search bar, list items, empty state/loading).
- Cột **description_vi** (Mô tả) phải **cụ thể**: có sample data từ Figma text nodes (vd: "số dư 20,000,000 VND", "39/50 ký tự", "3 item skeleton shimmer") — không dùng mô tả chung chung.
- **State trong mô tả**: Nếu Figma có variant/state khác nhau (vd: artboard "chế độ xóa"), ghi rõ state trong description (vd: "Chế độ xóa — checkbox xuất hiện, tick xanh khi chọn").
