---
description: Health check toàn hệ thống VNPAY Design Automation — kiểm tra Runtime, DDL, Skills, MCP, Git, Knowledge, Figma
---

# 🏥 Health Check Workflow

Workflow kiểm tra sức khoẻ toàn bộ hệ thống VNPAY Design Automation ecosystem. Chạy khi cần xác nhận trạng thái sẵn sàng trước khi thực hiện pipeline hoặc sau khi cài đặt/update.

---

## Bước 1: Runtime & Dependencies

// turbo
Kiểm tra Node.js, npm, Python3, và node_modules:

```bash
echo "=== RUNTIME ===" && \
node -v && npm -v && python3 --version && \
echo "" && \
echo "=== NODE_MODULES ===" && \
test -d node_modules && echo "✅ node_modules exists ($(ls node_modules | wc -l | tr -d ' ') packages)" || echo "❌ MISSING — run: npm install"
```

**Pass criteria:**
- Node.js ≥ v20
- npm ≥ v10
- Python3 có sẵn
- `node_modules/` tồn tại và có packages

**Fix nếu fail:**
```bash
npm install
```

---

## Bước 2: Environment & Credentials

// turbo
Kiểm tra `.env` và Figma PAT token:

```bash
echo "=== ENV FILE ===" && \
test -f .env && echo "✅ .env exists" || echo "⚠️ .env MISSING — Figma MCP sẽ không hoạt động" && \
echo "" && \
echo "=== FIGMA CREDENTIALS ===" && \
grep -q "FIGMA_PAT" .env 2>/dev/null && echo "✅ FIGMA_PAT configured" || echo "⚠️ FIGMA_PAT not found in .env"
```

**Pass criteria:**
- `.env` tồn tại
- `FIGMA_PAT` được set trong `.env`

**Fix nếu fail:**
```bash
echo 'FIGMA_PAT=figd_xxx...' > .env
# Lấy token từ: https://www.figma.com/developers/api#access-tokens
```

---

## Bước 3: DDL Token Layer

// turbo
Kiểm tra tất cả DDL JSON files parse được không lỗi:

```bash
echo "=== DDL GLOBAL TOKEN FILES ===" && \
for f in design-data-layer/global/*.json; do \
  echo -n "  $f: "; \
  python3 -c "import json; d=json.load(open('$f')); print(f'✅ Valid ({len(str(d))} chars)')" 2>/dev/null || echo "❌ INVALID JSON"; \
done && \
echo "" && \
echo "=== PRO BLOCKS CATALOG ===" && \
python3 -c "import json; d=json.load(open('design-data-layer/global/pro-blocks/block-catalog.json')); print(f'✅ {len(d)} catalog entries')" && \
echo "" && \
echo "=== SCHEMA FILES ===" && \
for dir in primitives patterns compositions; do \
  count=$(ls design-data-layer/global/pro-blocks/$dir/ 2>/dev/null | wc -l | tr -d ' '); \
  echo "  $dir: $count schemas"; \
done
```

**Pass criteria:**
- 6 global token JSON files all valid
- `block-catalog.json` parseable
- Schema dirs (primitives/patterns/compositions) have files

**Known issues (from DDL Health Check 2026-03-06):**
- Typography Sets: 0 — needs `npm run ddl:import-context`
- 64 missing token references (overridable/state placeholders)
- 161/350 color contrast failures (WCAG AA) — mostly alpha tokens

---

## Bước 4: MCP Servers

// turbo
Kiểm tra MCP config:

```bash
echo "=== MCP CONFIG ===" && \
python3 -c "
import json
with open('mcp.json') as f:
    d = json.load(f)
servers = d.get('servers', {})
for name, cfg in servers.items():
    endpoint = cfg.get('url', cfg.get('command', '?'))
    print(f'  {name}: {endpoint}')
print(f'\n✅ {len(servers)} MCP server(s) configured')
"
```

**Pass criteria:**
- `figma` server: `https://mcp.figma.com/mcp`
- `figma-save` server: `node` command

---

## Bước 5: Skills Inventory

// turbo
Kiểm tra skill directories:

```bash
echo "=== CURSOR SKILLS ($(ls .cursor/skills/ | wc -l | tr -d ' ') total) ===" && \
ls .cursor/skills/ | while read d; do \
  test -f ".cursor/skills/$d/SKILL.md" && echo "  ✅ $d" || echo "  ⚠️ $d (no SKILL.md!)"; \
done && \
echo "" && \
echo "=== AGENTS SKILLS ($(ls .agents/skills/ | wc -l | tr -d ' ') total) ===" && \
ls .agents/skills/ | while read d; do \
  test -f ".agents/skills/$d/SKILL.md" && echo "  ✅ $d" || echo "  ⚠️ $d (no SKILL.md!)"; \
done && \
echo "" && \
echo "=== WORKFLOWS ===" && \
ls .agents/workflows/ | while read f; do echo "  📋 $f"; done
```

**Pass criteria:**
- Tất cả skill dirs có `SKILL.md`
- Key skills present: `figma-to-prd-md`, `ux-review-pipe`, `ui-ux-pro-max`, `visual-spec-gen`

---

## Bước 6: Git & Repo

// turbo
Kiểm tra Git status:

```bash
echo "=== GIT ===" && \
git branch --show-current && \
echo "" && \
echo "=== REMOTE ===" && \
git remote -v && \
echo "" && \
echo "=== LAST 5 COMMITS ===" && \
git log --oneline -5 && \
echo "" && \
echo "=== UNCOMMITTED CHANGES ===" && \
git status --short | head -10 && \
count=$(git status --short | wc -l | tr -d ' ') && \
echo "" && echo "Total uncommitted: $count files"
```

**Pass criteria:**
- Branch: `main`
- Remote: `origin` → `github.com/cody-d0/DesignVNPAY.git`
- Uncommitted changes < 20 files

---

## Bước 7: Knowledge Base

// turbo
Kiểm tra Knowledge Items:

```bash
echo "=== KNOWLEDGE ITEMS ===" && \
ls ~/.gemini/antigravity/knowledge/ 2>/dev/null | grep -v ".lock" | while read d; do \
  echo "  📚 $d"; \
done && \
echo "" && \
total=$(ls ~/.gemini/antigravity/knowledge/ 2>/dev/null | grep -v ".lock" | wc -l | tr -d ' ') && \
echo "Total KIs: $total" && \
echo "" && \
echo "=== BP REGISTRY ===" && \
test -f ~/.gemini/bp-knowledge/bp-registry.md && echo "✅ bp-registry.md exists" || echo "⚠️ bp-registry.md MISSING"
```

**Pass criteria:**
- ≥ 10 Knowledge Items
- `bp-registry.md` tồn tại
- Key KIs present: `figma_bridge_system`, `design_data_layer_system`, `ba_design_pipeline_architecture`

---

## Bước 8: Disk & Performance

// turbo
Kiểm tra disk usage:

```bash
echo "=== DISK USAGE ===" && \
du -sh . 2>/dev/null && \
echo "" && \
echo "=== TOP DIRECTORIES ===" && \
du -sh */ .cursor/ .agents/ .gemini/ 2>/dev/null | sort -hr | head -10
```

**Pass criteria:**
- Total workspace < 500MB
- Không có thư mục outgrown bất thường

---

## Bước 9: Tổng hợp Report

Agent tổng hợp kết quả các bước trên thành **Health Check Report** dạng bảng, ghi vào artifact. Mỗi check có 3 trạng thái:
- ✅ **Healthy** — hoạt động bình thường
- ⚠️ **Warning** — vẫn chạy nhưng cần chú ý
- ❌ **Critical** — phải fix trước khi chạy pipeline

Format output:

```markdown
# 🏥 Health Check Report — {YYYY-MM-DD HH:mm}

| # | Subsystem          | Status | Detail |
|---|:-------------------|:------:|:-------|
| 1 | Runtime            | ✅/⚠️/❌ | ...    |
| 2 | Environment        | ✅/⚠️/❌ | ...    |
| 3 | DDL Token Layer    | ✅/⚠️/❌ | ...    |
| 4 | MCP Servers        | ✅/⚠️/❌ | ...    |
| 5 | Skills             | ✅/⚠️/❌ | ...    |
| 6 | Git & Repo         | ✅/⚠️/❌ | ...    |
| 7 | Knowledge Base     | ✅/⚠️/❌ | ...    |
| 8 | Disk & Performance | ✅/⚠️/❌ | ...    |

## Action Items
- [ ] Fix item 1...
- [ ] Fix item 2...
```
