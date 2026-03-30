#!/usr/bin/env python3
"""
enrich_inline.py — Deterministic + Agent-ready enrichment for report-data.json.

Generates template-required fields that convert.py cannot derive:
  1. user_impact   — from evidence text of related checks (UXP) / evidence + heuristic (Gap)
  2. heuristic     — from references[].name + ddl_ref (UXP only, Gap already has it)
  3. ref_count     — count of matched references for gap cards
  4. narrative     — (optional, agent mode) richer problem description

Architecture position:
    Index → Convert → Validate → Template Check → **Enrich Inline** → Render

Two modes:
  --auto    Deterministic enrichment from existing data (fast, reproducible)
  --agent   Outputs manifest of fields needing AI generation (for agent review)

Usage:
    python3 enrich_inline.py --module /path/to/module/
    python3 enrich_inline.py --base /path/to/final/
    python3 enrich_inline.py --module /path/to/module/ --dry-run
    python3 enrich_inline.py --module /path/to/module/ --agent
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# Heuristic reference database (shared with convert.py)
_HEURISTIC_DB_PATH = Path(__file__).parent.parent / 'references' / 'heuristic-db.json'
_HEURISTIC_DB: dict[str, Any] = {}


def _load_heuristic_db() -> dict[str, Any]:
    """Load heuristic-db.json once (lazy singleton)."""
    global _HEURISTIC_DB
    if _HEURISTIC_DB:
        return _HEURISTIC_DB
    if _HEURISTIC_DB_PATH.exists():
        _HEURISTIC_DB = json.loads(
            _HEURISTIC_DB_PATH.read_text(encoding='utf-8'))
    return _HEURISTIC_DB

# ═══════════════════════════════════════════════════════════════════════
# SEVERITY → IMPACT TEMPLATES
# ═══════════════════════════════════════════════════════════════════════

IMPACT_TEMPLATES = {
    'Critical': [
        'Người dùng không thể hoàn thành thao tác {action} do {reason}.',
        'Lỗi nghiêm trọng gây gián đoạn luồng {flow}: {reason}.',
        'Trải nghiệm bị phá vỡ tại {screen}: {reason}, buộc user phải thoát và thử lại.',
    ],
    'Major': [
        'Người dùng gặp khó khăn khi {action} do {reason}, làm tăng thời gian thao tác.',
        '{reason} — gây nhầm lẫn và giảm tin tưởng vào giao diện tại bước {screen}.',
        'Trải nghiệm bị suy giảm đáng kể: {reason}, ảnh hưởng đến hiệu suất sử dụng.',
    ],
    'Minor': [
        '{reason} — không chặn luồng nhưng giảm tính chuyên nghiệp của giao diện.',
        'Chi tiết thiết kế chưa tối ưu tại {screen}: {reason}.',
        '{reason}, có thể cải thiện để nâng cao trải nghiệm tổng thể.',
    ],
}

# Verbs by context for natural language
ACTION_VERBS = {
    'otp': 'nhập mã xác thực OTP',
    'form': 'nhập thông tin',
    'cta': 'tìm và nhấn nút hành động',
    'confirm': 'xác nhận giao dịch',
    'result': 'xem kết quả giao dịch',
    'search': 'tìm kiếm',
    'navigate': 'điều hướng',
    'select': 'chọn lựa',
    'input': 'nhập dữ liệu',
    'verify': 'kiểm tra thông tin',
}


def _detect_action(problem: str, screen_tag: str) -> str:
    """Detect action context from problem + screen_tag for natural impact text."""
    combined = (problem + ' ' + screen_tag).lower()
    for keyword, action in ACTION_VERBS.items():
        if keyword in combined:
            return action
    return 'thao tác'


def _extract_flow(screen_tag: str) -> str:
    """Extract flow name from screen tag."""
    if '›' in screen_tag:
        return screen_tag.split('›')[0].strip()
    return screen_tag.strip()


def _extract_screen(screen_tag: str) -> str:
    """Extract specific screen from screen tag."""
    if '›' in screen_tag:
        return screen_tag.split('›')[-1].strip()
    return screen_tag.strip()


def _generate_user_impact(problem: str, severity: str, screen_tag: str) -> str:
    """Generate user_impact from problem + severity + screen context."""
    import hashlib
    action = _detect_action(problem, screen_tag)
    flow = _extract_flow(screen_tag)
    screen = _extract_screen(screen_tag)

    # Truncate problem to first sentence/clause for reason
    reason = problem.strip()
    if len(reason) > 80:
        # Find natural break point
        for sep in ['—', '.', ',', ';']:
            idx = reason.find(sep)
            if 10 < idx < 80:
                reason = reason[:idx].strip()
                break
        else:
            reason = reason[:80].strip()

    reason = reason.rstrip('.')
    # Don't lowercase if first word is an acronym (e.g., OTP, CTA)
    first_word = reason.split()[0] if reason else ''
    if reason and not first_word.isupper():
        reason = reason[0].lower() + reason[1:]

    templates = IMPACT_TEMPLATES.get(severity, IMPACT_TEMPLATES['Minor'])
    # Deterministic template selection based on content hash
    idx = int(hashlib.md5(problem.encode()).hexdigest(), 16) % len(templates)
    template = templates[idx]

    result = template.format(
        action=action,
        reason=reason,
        flow=flow,
        screen=screen,
    )
    # Ensure sentence starts with capital letter
    if result and result[0].islower():
        result = result[0].upper() + result[1:]
    return result


def _generate_heuristic_text(references: list, ddl_ref: str) -> str:
    """Generate heuristic violation text from references + ddl_ref."""
    parts = []

    # From matched references
    if references:
        ref_names = [r.get('name', '') for r in references if isinstance(r, dict)]
        if ref_names:
            parts.extend(ref_names[:2])  # Max 2 heuristic names

    # From ddl_ref — extract UXG codes and component refs
    if ddl_ref:
        # Extract UXG references
        uxg_refs = re.findall(r'(UXG-\d+)', ddl_ref)
        comp_refs = re.findall(r'(COMP:\S+)', ddl_ref)
        law_refs = re.findall(r'(Law:\w+)', ddl_ref)

        if uxg_refs and not any('UXG' in p for p in parts):
            parts.append(' · '.join(uxg_refs))
        if comp_refs and not any('COMP' in p for p in parts):
            parts.append(' · '.join(comp_refs))
        if law_refs:
            # Map Law:fitts → Fitts's Law
            for lr in law_refs:
                law_name = lr.replace('Law:', '').capitalize()
                parts.append(f"{law_name}'s Law")

    if not parts:
        return ddl_ref if ddl_ref else ''

    return ' · '.join(parts)


def _count_refs(item: dict) -> int:
    """Count reference sources for an item."""
    refs = item.get('references', [])
    count = len(refs) if isinstance(refs, list) else 0
    # Also count ddl_evidence as a source
    if item.get('ddl_evidence') or item.get('ddl_ref'):
        count += 1
    return max(count, 0)


# ═══════════════════════════════════════════════════════════════════════
# GAP REFERENCE RESOLVER — 3-tier deterministic
# ═══════════════════════════════════════════════════════════════════════

# Category → default heuristic ref IDs (Tier 3 fallback)
CATEGORY_DEFAULT_REFS = {
    'Visual Design': ['nielsen.8'],           # Aesthetic & Minimalist
    'Flow & Navigation': ['nielsen.2'],       # Match Real World
    'Component & DDL': ['nielsen.4'],         # Consistency & Standards
    'Content & Copy': ['nielsen.6'],          # Recognition > Recall
    'Accessibility': ['wcag.1.4.3'],          # Contrast
    'Trust & Security': ['nielsen.5'],        # Error Prevention
}


def _resolve_gap_references(data: dict, heuristic_db: dict,
                            dry_run: bool = False) -> int:
    """Resolve references for gaps using 3-tier deterministic strategy.

    Tier 1: Cross-link Gap ↔ UXP (inherit UXP's matched references)
    Tier 2: Context map keyword matching from heuristic-db.json
    Tier 3: Category-based default heuristic fallback

    Returns number of gaps enriched.
    """
    count = 0

    # ── Build UXP lookup: gap_check_num → UXP references ──
    uxp_refs_by_check: dict[int, list[dict]] = {}
    for uxp in data.get('uxps', []):
        gap_ref = uxp.get('gap_ref', '')
        refs = uxp.get('references', [])
        if refs and isinstance(refs, list):
            for num_str in re.findall(r'#(\d+)', gap_ref):
                num = int(num_str)
                if num not in uxp_refs_by_check:
                    uxp_refs_by_check[num] = []
                # Avoid duplicates by name
                existing_names = {r.get('name', '') for r in uxp_refs_by_check[num]}
                for r in refs:
                    if r.get('name', '') not in existing_names:
                        uxp_refs_by_check[num].append(r)
                        existing_names.add(r.get('name', ''))

    context_map = heuristic_db.get('context_map', {})

    for sg in data.get('gaps_by_screen', []):
        for gap in sg.get('gaps', []):
            # Skip if already has real references
            existing_refs = gap.get('references', [])
            if existing_refs and isinstance(existing_refs, list) and len(existing_refs) > 0:
                continue

            num = gap.get('num', 0)
            resolved: list[dict] = []
            tier_used = 0

            # ── Tier 1: Cross-link UXP ──
            if num in uxp_refs_by_check:
                resolved = list(uxp_refs_by_check[num])  # copy
                tier_used = 1

            # ── Tier 2: Context map matching ──
            if not resolved:
                evidence = gap.get('evidence', '')
                title = gap.get('title', '')
                ddl_evidence = gap.get('ddl_evidence', '') or gap.get('ref', '')
                combined = f'{title} {evidence} {ddl_evidence}'.lower()

                seen_ref_ids: set[str] = set()
                for pattern, ref_ids in context_map.items():
                    if pattern.startswith('_'):
                        continue
                    keywords = pattern.replace('_', ' ').split()
                    match_count = sum(1 for kw in keywords if kw in combined)
                    if match_count >= max(1, len(keywords) * 0.6):
                        for ref_id in ref_ids:
                            if ref_id in seen_ref_ids:
                                continue
                            parts = ref_id.split('.')
                            if len(parts) == 2:
                                entry = heuristic_db.get(parts[0], {}).get(parts[1])
                                if entry and isinstance(entry, dict):
                                    resolved.append({
                                        'name': entry.get('name', ''),
                                        'url': entry.get('url', ''),
                                        'quote': entry.get('quote', ''),
                                        'source': entry.get('source', ''),
                                    })
                                    seen_ref_ids.add(ref_id)
                if resolved:
                    tier_used = 2

            # ── Tier 3: Category-based default ──
            if not resolved:
                heuristic_cat = gap.get('heuristic', '')
                # Extract English category name: "Visual Design (Thiết kế trực quan)" → "Visual Design"
                cat_name = heuristic_cat.split('(')[0].strip() if '(' in heuristic_cat else heuristic_cat
                default_ref_ids = CATEGORY_DEFAULT_REFS.get(cat_name, [])
                for ref_id in default_ref_ids:
                    parts = ref_id.split('.')
                    if len(parts) == 2:
                        entry = heuristic_db.get(parts[0], {}).get(parts[1])
                        if entry and isinstance(entry, dict):
                            resolved.append({
                                'name': entry.get('name', ''),
                                'url': entry.get('url', ''),
                                'quote': entry.get('quote', ''),
                                'source': entry.get('source', ''),
                            })
                if resolved:
                    tier_used = 3

            # ── Deduplicate by name + write ──
            if resolved:
                seen_names: set[str] = set()
                unique_refs: list[dict] = []
                for r in resolved:
                    name = r.get('name', '')
                    if name and name not in seen_names:
                        unique_refs.append(r)
                        seen_names.add(name)

                if not dry_run:
                    gap['references'] = unique_refs
                    gap['ref_count'] = len(unique_refs) + (1 if gap.get('ddl_evidence') else 0)
                    gap['_ref_tier'] = tier_used
                count += 1

    return count


# ═══════════════════════════════════════════════════════════════════════
# ENRICHMENT ENGINE
# ═══════════════════════════════════════════════════════════════════════

def enrich_module(module_dir: Path, dry_run: bool = False,
                  agent_mode: bool = False) -> dict:
    """Enrich a single module's report-data.json."""
    rd_path = module_dir / 'report-data.json'
    if not rd_path.exists():
        return {'module': module_dir.name, 'status': 'skip', 'reason': 'no report-data.json'}

    data = json.loads(rd_path.read_text(encoding='utf-8'))
    stats = {
        'module': module_dir.name,
        'status': 'ok',
        'uxp_enriched': 0,
        'gap_enriched': 0,
        'fields_added': [],
        'agent_manifest': [],  # Fields that need agent review
    }

    # ── Enrich UXPs ──
    for i, uxp in enumerate(data.get('uxps', [])):
        changed = False
        uxp_id = uxp.get('id', f'UXP-{i}')
        problem = uxp.get('problem', '')
        severity = uxp.get('severity', 'Major')
        screen_tag = uxp.get('screen_tag', '')
        ddl_ref = uxp.get('ddl_ref', '')
        references = uxp.get('references', [])

        # 1. user_impact — ALWAYS generate if missing
        if not uxp.get('user_impact'):
            impact = _generate_user_impact(problem, severity, screen_tag)
            if not dry_run:
                uxp['user_impact'] = impact
            stats['fields_added'].append(f'{uxp_id}.user_impact')
            changed = True

            if agent_mode:
                stats['agent_manifest'].append({
                    'id': uxp_id,
                    'field': 'user_impact',
                    'auto_value': impact,
                    'context': {
                        'problem': problem,
                        'severity': severity,
                        'screen': screen_tag,
                    },
                    'instruction': 'Review auto-generated impact. Rewrite if not contextual enough.',
                })

        # 2. heuristic — from references + ddl_ref
        if not uxp.get('heuristic'):
            heuristic = _generate_heuristic_text(references, ddl_ref)
            if heuristic and not dry_run:
                uxp['heuristic'] = heuristic
            if heuristic:
                stats['fields_added'].append(f'{uxp_id}.heuristic')
                changed = True

        # 3. ref_count
        ref_count = _count_refs(uxp)
        if not dry_run:
            uxp['ref_count'] = ref_count

        if changed:
            stats['uxp_enriched'] += 1

    # ── Enrich Gaps ──
    for sg in data.get('gaps_by_screen', []):
        for j, gap in enumerate(sg.get('gaps', [])):
            changed = False
            gap_title = gap.get('title', '')
            gap_num = gap.get('num', j)

            # 1. user_impact — if same as title, generate better one
            current_impact = gap.get('user_impact', '')
            if current_impact == gap_title or not current_impact:
                heuristic = gap.get('heuristic', '')
                evidence = gap.get('evidence', '')
                severity = gap.get('severity', 'Minor')

                # Build impact from evidence + heuristic context
                if evidence and heuristic:
                    # Extract core insight from evidence
                    evidence_core = evidence.replace('Từ ảnh: ', '').replace('Từ ảnh:', '').strip()
                    if len(evidence_core) > 100:
                        evidence_core = evidence_core[:100].rsplit(' ', 1)[0] + '...'
                    impact = f'{evidence_core} — vi phạm {heuristic.split("(")[0].strip()}'
                elif evidence:
                    impact = evidence.replace('Từ ảnh: ', '').replace('Từ ảnh:', '').strip()
                else:
                    impact = gap_title

                if impact != current_impact:
                    if not dry_run:
                        gap['user_impact'] = impact
                    stats['fields_added'].append(f'Gap#{gap_num}.user_impact')
                    changed = True

            # 2. ref_count (updated after gap references resolved below)
            if changed:
                stats['gap_enriched'] += 1

    # ── Resolve Gap References (3-tier) ──
    heuristic_db = _load_heuristic_db()
    gap_ref_count = _resolve_gap_references(data, heuristic_db, dry_run)
    if gap_ref_count > 0:
        stats['gap_enriched'] += gap_ref_count
        stats['fields_added'].append(f'gap_references:{gap_ref_count}')

    # ── Refresh ref_count for all gaps ──
    for sg in data.get('gaps_by_screen', []):
        for gap in sg.get('gaps', []):
            if not dry_run:
                gap['ref_count'] = _count_refs(gap)

    # ── Write back ──
    if not dry_run:
        rd_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + '\n',
            encoding='utf-8',
        )

    return stats


# ═══════════════════════════════════════════════════════════════════════
# REPORT
# ═══════════════════════════════════════════════════════════════════════

def print_report(stats: dict):
    """Print enrichment report."""
    module = stats['module']
    status = stats['status']

    if status == 'skip':
        print(f'  ⏭️  {module}: {stats.get("reason", "skipped")}')
        return

    uxp_e = stats['uxp_enriched']
    gap_e = stats['gap_enriched']
    fields = stats['fields_added']

    if not fields:
        print(f'  ✅ {module}: No enrichment needed (all fields present)')
        return

    print(f'  📝 {module}: {uxp_e} UXPs + {gap_e} Gaps enriched ({len(fields)} fields)')

    # Group by field type
    field_types: dict[str, int] = {}
    for f in fields:
        ftype = f.split('.')[-1]
        field_types[ftype] = field_types.get(ftype, 0) + 1
    for ftype, count in sorted(field_types.items()):
        print(f'      · {ftype}: {count}')

    # Agent manifest
    manifest = stats.get('agent_manifest', [])
    if manifest:
        print(f'\n  🤖 AGENT REVIEW NEEDED ({len(manifest)} items):')
        for item in manifest[:5]:
            print(f'      {item["id"]}.{item["field"]}:')
            print(f'        Auto: {item["auto_value"][:80]}...')
            print(f'        Context: {item["context"]["problem"][:60]}')
        if len(manifest) > 5:
            print(f'      ... +{len(manifest) - 5} more')


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Deterministic + agent-ready enrichment for report-data.json'
    )
    parser.add_argument('--module', type=Path,
                        help='Path to single module directory')
    parser.add_argument('--base', type=Path,
                        help='Base directory to find all modules')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing')
    parser.add_argument('--agent', action='store_true',
                        help='Output agent review manifest')
    parser.add_argument('--json', type=Path, default=None,
                        help='Output results as JSON')
    args = parser.parse_args()

    modules: list[Path] = []
    if args.module:
        modules = [args.module.resolve()]
    elif args.base:
        base = args.base.resolve()
        for d in sorted(base.iterdir()):
            if d.is_dir() and (d / 'report-data.json').exists():
                modules.append(d)
        # Also scan subdirectories
        if not modules:
            import glob
            for f in sorted(glob.glob(str(base / '**' / 'report-data.json'), recursive=True)):
                modules.append(Path(f).parent)
    else:
        parser.error('Specify either --module or --base')

    if not modules:
        print('No modules with report-data.json found.', file=sys.stderr)
        sys.exit(1)

    mode = '🤖 AGENT MODE' if args.agent else ('🔍 DRY RUN' if args.dry_run else '📝 ENRICHING')
    print(f'\n{"═" * 60}')
    print(f'  {mode} — {len(modules)} module(s)')
    print(f'{"═" * 60}\n')

    all_stats = []
    total_fields = 0

    for mod_dir in modules:
        stats = enrich_module(mod_dir, dry_run=args.dry_run, agent_mode=args.agent)
        all_stats.append(stats)
        print_report(stats)
        total_fields += len(stats.get('fields_added', []))

    # Batch summary
    if len(modules) > 1:
        enriched = sum(1 for s in all_stats
                       if s.get('uxp_enriched', 0) + s.get('gap_enriched', 0) > 0)
        print(f'\n{"─" * 60}')
        print(f'  📊 BATCH: {enriched}/{len(modules)} modules enriched, '
              f'{total_fields} fields added')
        print()

    # JSON output
    if args.json:
        import datetime
        output = {
            'enriched_at': datetime.datetime.now().isoformat(),
            'mode': 'agent' if args.agent else ('dry-run' if args.dry_run else 'auto'),
            'modules': all_stats,
            'total_fields_added': total_fields,
        }
        args.json.write_text(
            json.dumps(output, ensure_ascii=False, indent=2),
            encoding='utf-8',
        )
        print(f'📝 JSON report: {args.json}', file=sys.stderr)


if __name__ == '__main__':
    main()
