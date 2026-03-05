# Nghiên cứu: Đóng gói và chia sẻ workflow qua Git

Tài liệu tổng hợp phương án đóng gói skills + workflow (agent pipeline) để version bằng Git và chia sẻ (nội bộ hoặc công khai).

---

## 1. Hiện trạng trong project

| Thành phần | Vị trí | Ghi chú |
|------------|--------|---------|
| **Skills** | `.cursor/skills/<tên-skill>/` | Mỗi skill: SKILL.md + scripts/, references/, assets/ |
| **Skills (Agents)** | `.agents/skills/<tên-skill>/` | Cùng format, dùng bởi agent CLI / find-skills |
| **Workflow (Agent)** | `.cursor/agents/prd-full-pipeline.md` | Subagent chạy tuần tự nhiều skill, có input/output contract |
| **Rules** | `.cursor/rules/*.mdc` | Rule tham chiếu bởi pipeline (pdr-component-pipeline, comp-extraction) |
| **Package script** | `.agents/skills/skill-creator/scripts/package_skill.py` | Tạo file `.skill` (zip) từ 1 folder skill |
| **Validate** | `quick_validate.py` (cùng thư mục) | Kiểm tra SKILL.md frontmatter, naming |

---

## 2. Ba mức đóng gói

### 2.1 Mức 1: Một skill — repo Git + (tùy chọn) file .skill

**Mục tiêu:** Chia sẻ một skill đơn lẻ, version bằng Git, có thể cài qua `npx skills add` hoặc copy folder.

**Cấu trúc repo gợi ý:**

```
repo-prd-crossfile-mapping/
├── SKILL.md
├── scripts/
├── references/
├── assets/
├── README.md          # Mô tả ngắn, link docs, cách cài
├── .gitignore         # __pycache__, .env, *.skill (nếu không commit artifact)
├── LICENSE
└── package.json       # Tùy chọn: dùng nếu publish npm / agents field
```

**Chia sẻ:**

- **Qua Git:** clone repo → copy folder vào `.cursor/skills/` hoặc `.agents/skills/`.
- **Qua .skill:** chạy `package_skill.py` → đính kèm file `.skill` trong Release GitHub (hoặc nội bộ); người dùng giải nén vào `skills/`.
- **Qua npx skills:** nếu repo tuân thủ cấu trúc multi-skill (xem 2.2), người khác có thể dùng `npx skills add <owner/repo> --skill <tên-skill>`.

**Lưu ý:** `package_skill.py` import `quick_validate`; khi chạy từ repo của skill cần đảm bảo `quick_validate.py` nằm cùng thư mục với `package_skill.py` hoặc trong `PYTHONPATH` (hoặc copy từ skill-creator).

---

### 2.2 Mức 2: Nhiều skill — multi-skill repo (monorepo)

**Mục tiêu:** Một repo chứa nhiều skill, cài một hoặc tất cả qua `npx skills add <owner/repo> [--skill <name>] [--all]`.

**Cấu trúc repo (theo kiểu vercel-labs/agent-skills):**

```
repo-workflow-skills/
├── design-system-gen/
│   ├── SKILL.md
│   ├── scripts/
│   └── references/
├── prd-crossfile-mapping/
│   ├── SKILL.md
│   └── ...
├── pdr-extract/
│   └── SKILL.md
├── pdr-analyze/
│   └── SKILL.md
├── comp-extraction/
│   └── SKILL.md
├── visual-spec-gen/
│   └── SKILL.md
├── README.md
├── .gitignore
└── LICENSE
```

**Cách dùng (người nhận):**

```bash
# Xem danh sách skill
npx skills add <owner/repo-workflow-skills> --list

# Cài một skill
npx skills add <owner/repo-workflow-skills> --skill prd-crossfile-mapping

# Cài toàn bộ
npx skills add <owner/repo-workflow-skills> --all
```

**Lưu ý:** Tên thư mục thường trùng với `name` trong SKILL.md (kebab-case). Công cụ `npx skills` sẽ tìm các folder có SKILL.md và coi mỗi folder là một skill.

---

### 2.3 Mức 3: Workflow (pipeline) — agent + skills + rules

**Mục tiêu:** Chia sẻ cả “quy trình” (subagent + danh sách skill + rule) để người khác chạy cùng một pipeline (ví dụ prd-full-pipeline) mà không phải tự lắp ghép.

**Thành phần cần đóng gói:**

| Thành phần | Nội dung |
|------------|----------|
| **Agent definition** | File mô tả pipeline (ví dụ `prd-full-pipeline.md`): thứ tự skill, input/output, gate. |
| **Skills** | Toàn bộ skill được pipeline gọi (design-system-gen, prd-crossfile-mapping, pdr-extract, pdr-analyze, comp-extraction, visual-spec-gen, v.v.). |
| **Rules** | Các rule được tham chiếu (ví dụ `pdr-component-pipeline.mdc`, `comp-extraction.mdc`). |
| **Docs/DDL** | Tùy chọn: `.cursor/docs/ddl/`, contract, governance — nếu pipeline phụ thuộc. |

**Hai cách tổ chức:**

**Cách A — Repo “workflow pack” (all-in-one):**

```
repo-prd-full-pipeline/
├── agents/
│   ├── README.md
│   └── prd-full-pipeline.md
├── skills/
│   ├── design-system-gen/
│   ├── prd-crossfile-mapping/
│   ├── pdr-extract/
│   ├── pdr-analyze/
│   ├── comp-extraction/
│   └── visual-spec-gen/
├── rules/
│   ├── pdr-component-pipeline.mdc
│   └── comp-extraction.mdc
├── docs/                    # Tùy chọn
│   └── ddl/
├── install.sh               # Copy agents/ → .cursor/agents, skills/ → .cursor/skills, rules/ → .cursor/rules
├── README.md
├── .gitignore
└── LICENSE
```

- **install.sh:** copy (hoặc symlink) `agents/` → `.cursor/agents/`, `skills/` → `.cursor/skills/`, `rules/` → `.cursor/rules/` (có thể hỏi đường dẫn workspace).
- Người dùng: clone → chạy `./install.sh` trong workspace Cursor.

**Ví dụ install.sh (mẫu):**

```bash
#!/usr/bin/env bash
# Chạy từ repo workflow pack, trong thư mục workspace Cursor.
set -e
ROOT="${1:-.}"
CURSOR="${ROOT}/.cursor"
mkdir -p "$CURSOR/agents" "$CURSOR/skills" "$CURSOR/rules"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cp -r "${SCRIPT_DIR}/agents/"* "$CURSOR/agents/"
cp -r "${SCRIPT_DIR}/skills/"* "$CURSOR/skills/"
cp -r "${SCRIPT_DIR}/rules/"* "$CURSOR/rules/" 2>/dev/null || true
echo "Installed agents + skills + rules into ${CURSOR}"
```

**Cách B — Repo skills + hướng dẫn workflow:**

- Một repo chỉ chứa **skills** (như 2.2).
- Một file **WORKFLOW.md** (hoặc doc trong repo hoặc wiki) mô tả:
  - Workflow prd-full-pipeline: thứ tự skill, input (`prd_folder`, v.v.), output.
  - Cách “lắp” workflow trong Cursor: tạo file agent (ví dụ `.cursor/agents/prd-full-pipeline.md`) và copy nội dung từ WORKFLOW.md; cài skills bằng `npx skills add <owner/repo> --all` hoặc copy folder vào `.cursor/skills/`.
- Rules và docs DDL: link đến repo khác hoặc nội bộ, hoặc copy vào `.cursor/rules` / `.cursor/docs` theo hướng dẫn.

**So sánh nhanh:**

| Tiêu chí | Cách A (workflow pack) | Cách B (skills + doc) |
|----------|------------------------|------------------------|
| Cài một lần chạy script | Có (install.sh) | Không, phải tự copy agent + rules |
| Dùng lại skill cho workflow khác | Vẫn được (skills tách folder) | Rất thuận (repo chỉ skills) |
| Cập nhật từng skill | Có thể submodule hoặc copy từ repo skills | Cập nhật repo skills là xong |
| Phù hợp | Team dùng đúng một pipeline | Ai muốn mix nhiều workflow / chỉ dùng vài skill |

---

## 3. Gợi ý kỹ thuật Git

### 3.1 .gitignore (repo skill / workflow)

```gitignore
# Python
__pycache__/
*.py[cod]
venv/
.env
.env.*

# Artifacts (nếu không commit)
*.skill
dist/

# IDE / OS
.idea/
.vscode/
.DS_Store
```

### 3.2 Release / tag

- **Skill đơn:** tag version ví dụ `v1.0.0`, đính kèm file `.skill` trong Release (build bằng `package_skill.py`).
- **Multi-skill / workflow:** tag theo bộ (ví dụ `pipeline-v3.0.0`); Release note liệt kê thay đổi skill + agent + rules.

### 3.3 Submodule (nếu tách repo)

- Repo workflow (Cách A) có thể dùng **git submodule** trỏ tới từng repo skill, để cập nhật skill độc lập:
  - `git submodule add <url-skill-design-system> skills/design-system-gen`
  - Người clone: `git clone --recurse-submodules <repo-workflow>` hoặc `git submodule update --init`.

### 3.4 package.json (tùy chọn)

Nếu muốn tích hợp với ecosystem `npx skills` / npm:

```json
{
  "name": "@org/workflow-skills",
  "version": "1.0.0",
  "private": true,
  "agents": {
    "skills": [
      { "name": "design-system-gen", "path": "./skills/design-system-gen" },
      { "name": "prd-crossfile-mapping", "path": "./skills/prd-crossfile-mapping" }
    ]
  }
}
```

Cần kiểm tra lại spec của `npx skills` / npm-agentskills (path tương đối so với repo root).

---

## 4. Checklist đóng gói workflow

- [ ] **Skills:** Mỗi skill có SKILL.md đúng frontmatter (name, description), chạy `quick_validate.py` (hoặc package_skill.py) cho từng skill.
- [ ] **Agent:** File pipeline (ví dụ `prd-full-pipeline.md`) có mô tả input/output, thứ tự skill, và đường dẫn skill/rule đúng (tương đối so với `.cursor/` sau khi cài).
- [ ] **Rules:** Các file .mdc được tham chiếu tồn tại trong pack hoặc có hướng dẫn copy từ nguồn khác.
- [ ] **Install:** Script hoặc README rõ: clone → chạy gì, copy vào đâu (.cursor/agents, .cursor/skills, .cursor/rules).
- [ ] **Docs:** README giải thích workflow là gì, khi nào dùng, input mẫu (ví dụ `prd_folder`), output (mockup-spec.json, v.v.).
- [ ] **Version:** Tag + Release (và đính kèm .skill nếu dùng artifact).

---

## 5. Tóm tắt lựa chọn

| Nhu cầu | Phương án |
|---------|-----------|
| Chia sẻ **1 skill** | Repo 1 skill + (tùy chọn) Release đính kèm .skill |
| Chia sẻ **nhiều skill** (cùng bộ) | Multi-skill repo (monorepo) + `npx skills add <owner/repo> [--skill name \| --all]` |
| Chia sẻ **cả pipeline** (agent + skills + rules) | Repo “workflow pack” (agents + skills + rules + install.sh) hoặc repo skills + WORKFLOW.md hướng dẫn lắp agent/rules |
| Version + release | Git tag + GitHub Release; tùy chọn đính kèm .skill cho từng skill |

Nếu bạn cho biết ưu tiên (chỉ skills / hay cả pipeline / dùng npx skills hay chỉ copy thủ công), có thể đi sâu bước thiết kế repo cụ thể và nội dung `install.sh` / WORKFLOW.md cho project hiện tại.
