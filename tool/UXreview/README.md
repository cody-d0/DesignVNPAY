# 🎨 UXreview

AI-powered UX Review pipeline — Figma → PRD → UX Review Report.

## 📰 News

| Ngày | Update |
|---|---|
| 06/03 | Refine workflow |
| 05/03 | Đơn giản hoá README, deploy GitHub Pages, refactor project structure |

## Quick Start

```bash
git clone -b tool https://github.com/cody-d0/DesignVNPAY.git
cd DesignVNPAY/tool/UXreview
```

Tạo `.env` (optional):

```
FIGMA_PAT=your_figma_personal_access_token
```

Mở folder `tool/UXreview` trong **Cursor** hoặc **Gemini** — skills & workflows tự động detect.

## Cấu trúc

```
UXreview/
├── .agents/skills/          # Agent skills (figma-to-prd, ux-review, ui-ux-pro-max...)
├── .agents/workflows/       # Pipeline orchestration
├── design-data-layer/       # Tokens, themes, component registry
├── docs/                    # Quick start, design system, UX brain
├── tools/mcp-servers/       # Figma MCP integration
└── package.json
```

## Pipeline

`/figma-to-ux-review` — end-to-end:

1. **Figma → PRD** — extract screens, generate markdown specs
2. **PRD → UX Review** — analyse against UX laws, accessibility, design patterns
3. **Output** — UX Review Report (findings, recommendations, severity)

## License

ISC — Made by **cody-d0**
