# 🎨 UXreview — Project Description

> **Path:** `/Users/dataism/Documents/UXtool/tool/UXreview`
> **Repo:** `cody-d0/DesignVNPAY` (branch: `tool`)
> **Size:** 1.2 MB · 87 files · 31 dirs
> **License:** ISC

---

## 1. Bản chất — Đây là gì?

**UXreview** là một **AI-native UX Review Pipeline** — hệ thống tự động hóa quy trình đánh giá UX từ thiết kế Figma đến báo cáo review chuyên sâu. Nó hoạt động không phải như một ứng dụng web hay plugin, mà như một **"bộ não" cho AI Agent** — cung cấp skills, data, và workflows để Agent thực thi pipeline end-to-end.

```
┌─────────────────────────────────────────────────────────┐
│                    UXreview Pipeline                     │
│                                                         │
│   Figma URL ──→ PRD Markdown ──→ UX Review Report       │
│                                                         │
│   Input:  Link Figma (sections, pages)                  │
│   Output: Bộ PRD .md + UX Review Report có severity     │
└─────────────────────────────────────────────────────────┘
```

**Không phải là:** Web app, CLI tool, hay Figma plugin.
**Là:** Một "skill pack" + data layer cho AI Agents (Gemini, Cursor) để tự động hóa UX review.

---

## 2. Cấu trúc thư mục — Anatomy

```
UXreview/                          (1.2 MB total)
│
├── .gemini/GEMINI.md              # Project brain cho AI (context loading)
├── .gitignore
├── README.md                      # Quick start guide
├── package.json                   # Node.js: express, marked, zod, MCP SDK
│
├── 🤖 .agents/                    # ═══ AGENT INTELLIGENCE ═══
│   │
│   ├── skills/                    # 6 specialized skills (780 KB)
│   │   ├── figma-to-prd-md/       #   ① Figma → PRD pipeline (6 phases)
│   │   ├── ux-review-pipe/        #   ② PRD → UX Review orchestrator
│   │   ├── review-ux/             #   ③ UX review execution
│   │   ├── ux-signal-inference/   #   ④ UX signal detection engine
│   │   ├── ui-ux-pro-max/         #   ⑤ Design intelligence (484 KB data!)
│   │   └── frontend-design/       #   ⑥ Frontend code generation
│   │
│   ├── workflows/                 # Pipeline orchestration
│   │   ├── figma-to-ux-review.md  #   Master workflow (20.7 KB)
│   │   └── evals/evals.json       #   Quality evaluation criteria
│   │
│   └── docs/                      # Agent reference docs
│       ├── ddl/                   #   DDL documentation (6 files)
│       └── ui-ux-pro-max-ref.md   #   Skill cross-reference
│
├── 📊 design-data-layer/          # ═══ TOKEN DATA ═══ (156 KB)
│   ├── global/                    # Cross-product tokens
│   │   ├── tailwind.json          #   T1: Foundation (60 KB!)
│   │   ├── theme-default.json     #   T2: Semantic theme (33 KB)
│   │   ├── mode-light.json        #   T3: Light mode (15 KB)
│   │   ├── mode-dark.json         #   T3: Dark mode (15 KB)
│   │   ├── custom-desktop.json    #   T4: Desktop overrides
│   │   └── custom-mobile.json     #   T4: Mobile overrides
│   └── products/
│       └── default/
│           └── theme-vnpay.json   #   Product-specific VNPAY theme
│
├── 📚 docs/                       # ═══ DOCUMENTATION ═══ (152 KB)
│   ├── QUICK-START.md             # Setup guide
│   ├── DESIGN-SYSTEM.md           # Design system docs (7 KB)
│   ├── UI-UX-BRAIN-EXTRACT.md     # Full UX brain (11.5 KB)
│   └── state-pattern/             # State management specs (11 files!)
│       ├── 00-state-map-current
│       ├── 01-state-contract
│       ├── 02-scenario-catalog
│       ├── ... through 09-output-schema
│       └── README.md
│
└── 🔧 tools/                     # ═══ MCP SERVERS ═══
    └── mcp-servers/
        └── figma-save/            # Custom MCP server (v2.2.0)
            ├── server.js          #   Save Figma sections → PNG
            └── package.json
```

---

## 3. Các thành phần chính — Deep Dive

### 3.1 🤖 Skills (6 specialized AI skills)

| # | Skill | File count | Chức năng | Data |
|:--|:------|:---:|:---|:---|
| ① | **figma-to-prd-md** | 12 files | Nhận Figma URL → tạo bộ PRD markdown (6 phases) | component-mapping, term-equivalents |
| ② | **ux-review-pipe** | 1 file | Orchestrate 3 sub-skills song song: signal inference + PRD context + vision review | — |
| ③ | **review-ux** | 2 files | Đánh giá UX: clarity, usability, accessibility, consistency | checklist.md |
| ④ | **ux-signal-inference** | 5 files | Suy luận UX signals tiềm ẩn từ text + context + icons | Banking + Generic signals JSON |
| ⑤ | **ui-ux-pro-max** | 29 files | Design intelligence engine — 484 KB pure data | 12 CSV files + 13 stack configs |
| ⑥ | **frontend-design** | 2 files | Sinh code frontend production-grade | — |

#### Skill ⑤ ui-ux-pro-max — Data Breakdown

Đây là **data layer lớn nhất** (484 KB), chứa:

| Data file | Size | Nội dung |
|:---|:---:|:---|
| `styles.csv` | 96 KB | 50 design styles (glassmorphism, brutalism, etc.) |
| `typography.csv` | 31 KB | 50 font pairings |
| `ui-reasoning.csv` | 31 KB | UI decision reasoning patterns |
| `products.csv` | 29 KB | Product design patterns |
| `ux-guidelines.csv` | 18 KB | 120+ UX guidelines |
| `ux-laws.csv` | 14 KB | 60+ UX laws |
| `react-performance.csv` | 14 KB | React optimization patterns |
| `landing.csv` | 14 KB | Landing page patterns |
| `icons.csv` | 13 KB | Icon usage catalog |
| `colors.csv` | 9 KB | 21 color palettes |
| `web-interface.csv` | 7 KB | Web interface rules |
| `charts.csv` | 7 KB | 20 chart types |
| **stacks/** (13 files) | ~160 KB | React, Next.js, Vue, Svelte, SwiftUI, Flutter, etc. |

### 3.2 📊 Design Data Layer (DDL)

4-tier token hierarchy — **source of truth** cho toàn bộ design tokens:

```
Tier 1: tailwind.json (60 KB)
    └── Base primitives: colors.blue.500, spacing.4, etc.

Tier 2: theme-default.json (33 KB)
    └── Semantic aliases: primary → colors.blue.600

Tier 3: mode-light.json + mode-dark.json (30 KB)
    └── Mode resolution: background → #ffffff (light) / #0a0a0a (dark)

Tier 4: custom-desktop.json + custom-mobile.json (7 KB)
    └── Platform overrides: padding, touch targets, etc.

Product: theme-vnpay.json
    └── VNPAY brand overrides
```

### 3.3 🔧 figma-save MCP Server

Custom MCP server (`v2.2.0`) cho phép Agent **tự động save artboards từ Figma → PNG**:

| Feature | Chi tiết |
|:---|:---|
| **Tool name** | `figma_save_section_screenshots` |
| **Input** | `file_key` + `node_id` (section hoặc page) |
| **Output** | PNG files trong `{file}/{page}/{section}/*.png` |
| **Concurrency** | 5 parallel downloads |
| **Vietnamese support** | Slugify có bảng chuyển dấu tiếng Việt đầy đủ |
| **Mode** | Section mode (1 section) hoặc Page mode (all sections) |
| **Error handling** | Retry, timeout, rate limit (429) detection |

### 3.4 📚 State Pattern Docs

Bộ 11 tài liệu chuyên sâu về **state management trong UX design**:

| Doc | Nội dung |
|:---|:---|
| `00-state-map-current` | Bản đồ trạng thái hiện tại |
| `01-state-contract` | Contract giữa states |
| `02-scenario-catalog` | Danh mục kịch bản |
| `03-persistence-policy` | Chính sách lưu trữ state |
| `04-extensibility-template` | Template mở rộng |
| `05-ux-quality-checklist` | Checklist chất lượng UX |
| `06-component-scenario-mapping` | Mapping component ↔ scenario (JSON) |
| `07-crossref-spec` | Cross-reference specification |
| `08-pipeline-update` | Cập nhật pipeline |
| `09-output-schema` | Schema output |

---

## 4. Master Workflow — Pipeline Flow

Workflow chính: **`/figma-to-ux-review`** (20.7 KB workflow file)

```
┌──────────────────────────────────────────────────────────────┐
│  Phase 0: SCAN                                               │
│  • Nhận Figma URL                                            │
│  • Dùng MCP get_metadata → lấy tree structure                │
│  • Xác định pages, sections, screens                         │
└─────────────────┬────────────────────────────────────────────┘
                  ▼
┌──────────────────────────────────────────────────────────────┐
│  Phase 1: EXTRACT                                            │
│  • get_design_context cho mỗi screen                         │
│  • get_screenshot cho visual reference                       │
│  • figma_save_section_screenshots → PNG local                │
└─────────────────┬────────────────────────────────────────────┘
                  ▼
┌──────────────────────────────────────────────────────────────┐
│  Phase 2: INVENTORY                                          │
│  • Phân loại screens (form, list, detail, etc.)              │
│  • Component inventory                                       │
│  • Flow mapping                                              │
└─────────────────┬────────────────────────────────────────────┘
                  ▼
┌──────────────────────────────────────────────────────────────┐
│  Phase 3: GENERATE PRD                                       │
│  • Sinh overview.md + feature files                          │
│  • 5 sections chuẩn per feature                              │
│  • Component mapping + state definitions                     │
└─────────────────┬────────────────────────────────────────────┘
                  ▼
┌──────────────────────────────────────────────────────────────┐
│  Phase 4: AUGMENT                                            │
│  ├── 4a: DDL token enrichment                                │
│  ├── 4b: UX guidelines cross-reference                       │
│  ├── 4c: Accessibility audit                                 │
│  ├── 4d: State pattern validation                            │
│  └── 4e: UX Signal Inference (text → signals)                │
└─────────────────┬────────────────────────────────────────────┘
                  ▼
┌──────────────────────────────────────────────────────────────┐
│  Phase 5: OUTPUT                                             │
│  ├── 📄 PRD Markdown files                                   │
│  └── 📊 UX Review Report                                     │
│       ├── Findings (severity: critical/major/minor)          │
│       ├── DDL references                                     │
│       ├── Visual evidence (screenshots)                      │
│       └── Improvement recommendations                        │
└──────────────────────────────────────────────────────────────┘
```

---

## 5. Dependencies & Tech Stack

| Component | Technology |
|:---|:---|
| **Runtime** | Node.js (CommonJS) |
| **MCP SDK** | `@modelcontextprotocol/sdk` ^1.26.0 |
| **Markdown** | `marked` ^11.1.1 |
| **Validation** | `zod` ^4.3.6 |
| **Web Server** | `express` ^4.18.2 |
| **AI Agent** | Gemini / Cursor (external, consumes skills) |
| **Design Source** | Figma (via MCP Dev Mode + REST API) |

---

## 6. Tổng kết — Identity Card

```
┌─────────────────────────────────────────────────────────────┐
│  📛 NAME:     UXreview                                       │
│  🎯 PURPOSE:  AI-native UX Review Pipeline                   │
│  📊 SIZE:     1.2 MB · 87 files                              │
│                                                              │
│  🧠 BRAIN:    6 skills + 484 KB design intelligence data     │
│  🎨 TOKENS:   DDL 4-tier hierarchy (156 KB, 7 JSON files)    │
│  🔧 TOOLS:    figma-save MCP server (screenshot automation)  │
│  📚 DOCS:     State patterns (11 files) + UX Brain (11.5 KB) │
│  🔄 WORKFLOW: /figma-to-ux-review (6-phase pipeline)         │
│                                                              │
│  🏗️ ARCHITECTURE:                                            │
│     Figma ──MCP──→ Agent ──Skills──→ PRD .md ──→ UX Report   │
│                      ↑                                       │
│                   DDL tokens                                 │
│                   UX laws (60+)                               │
│                   Guidelines (120+)                           │
│                   Styles (50)                                 │
│                   Font pairs (50)                             │
│                   Stack configs (13)                          │
│                                                              │
│  🔑 DIFFERENTIATOR:                                          │
│     Không phải tool — là "intelligence layer"                │
│     cho AI Agent thực hiện UX review tự động.                │
└─────────────────────────────────────────────────────────────┘
```
