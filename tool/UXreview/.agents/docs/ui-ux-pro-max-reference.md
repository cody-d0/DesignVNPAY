# ui-ux-pro-max — Tham chiếu thống nhất

Tài liệu này là **vị trí tham chiếu đầy đủ duy nhất** cho skill ui-ux-pro-max. Chỉ có **một** đường dẫn canonical; mọi tham chiếu trong repo dùng path bên dưới (không dùng `.agents/skills/ui-ux-pro-max/`). Các skill khác (figma-to-prd-md, design-system-gen, pdr-analyze, comp-extraction, v.v.) link tới file này hoặc dùng path canonical trực tiếp.

---

## Canonical paths (duy nhất)

| Loại | Đường dẫn |
|------|-----------|
| **Skill** | `.agents/skills/ui-ux-pro-max/SKILL.md` |
| **Data (CSV)** | `.agents/skills/ui-ux-pro-max/data/` |
| **Script search** | `.agents/skills/ui-ux-pro-max/scripts/search.py` |

---

## CSV trong data/ (dùng chung)

- `ux-guidelines.csv` — UX rules (accessibility, touch, error feedback, …); dùng cho §2 AC, §5 NFR, COMPextend.
- `web-interface.csv` — Web UI patterns; §2 Business Rule, AC; form/validation/keyboard.
- `colors.csv` — Palettes, HEX; design system, token.
- `typography.csv` — Font pairings, sizes; design system, NFR.
- `styles.csv` — Style recommendations; design system.
- `icons.csv` — Icon usage; §3 Mô tả, aria-label.
- `ux-laws.csv` — UX laws (Fitts, Hick, …); citation khi dùng ux-guidelines.
- `ui-reasoning.csv` — Reasoning rules; COMPextend, pdr-analyze.

Các file khác trong `data/` (charts, stacks, products, landing, react-performance, …) dùng theo nhu cầu từng skill.

---

## Khi nào skill khác cần dùng

- **Augment PRD:** figma-to-prd-md Phase 4 — CSV + search.py cho persona, AC, NFR, §3 Mô tả.
- **Design system:** design-system-gen — search.py `--design-system`, colors/typography/styles.
- **COMPextend / token:** comp-extraction, pdr-analyze — ux-guidelines, web-interface, ui-reasoning.
- **Citation:** Mọi đề xuất từ ui-ux-pro-max cần citation dạng `ux-guidelines.csv#22`, `web-interface.csv#1`, v.v.

---

## Ví dụ lệnh search.py

```bash
# Design system cho sản phẩm
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "<product_type> <industry>" --design-system -p "Project Name"

# Domain ux / web
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "error feedback loading empty" --domain ux
python3 .agents/skills/ui-ux-pro-max/scripts/search.py "form validation keyboard aria" --domain web
```

Tham khảo đầy đủ tham số và use case trong [.agents/skills/ui-ux-pro-max/SKILL.md](.agents/skills/ui-ux-pro-max/SKILL.md).
