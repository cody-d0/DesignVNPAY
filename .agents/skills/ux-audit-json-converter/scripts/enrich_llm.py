#!/usr/bin/env python3
"""
enrich_llm.py — LLM-ready enrichment manifest generator.

Assembles full context per UXP/Gap from all available data sources and
outputs a structured manifest (llm-manifest.json) for an LLM agent to
generate enriched content.

Architecture position:
    Index → Convert → Validate → TplCheck → Enrich Inline → **Enrich LLM** → Render
                                              (deterministic)   (LLM-powered)

The manifest bundles:
  • Finding data (problem, evidence, ddl_ref, solution draft)
  • Artboard context (overlay type, UI elements, parent screen)
  • Domain context (banking → high sensitivity)
  • Related checks (aggregated evidence)
  • Heuristic candidates (pre-filtered from heuristic-db.json)

The agent reads the manifest, generates enriched fields, and writes
llm-enriched.json. Then merge_llm.py merges results back.

Modes:
  --json     Output llm-manifest.json (default, for agent consumption)
  --prompt   Output human-readable prompt markdown (for copy-paste)
  --stats    Print stats only (no file output)

Usage:
    python3 enrich_llm.py --module /path/to/module/
    python3 enrich_llm.py --base /path/to/final/
    python3 enrich_llm.py --module /path/to/module/ --prompt
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

# ═══════════════════════════════════════════════════════════════════════
# PATHS
# ═══════════════════════════════════════════════════════════════════════

SKILL_DIR = Path(__file__).parent.parent  # ux-audit-json-converter/
HEURISTIC_DB_PATH = SKILL_DIR / 'references' / 'heuristic-db.json'


# ═══════════════════════════════════════════════════════════════════════
# DATA LOADERS
# ═══════════════════════════════════════════════════════════════════════

def _load_json(path: Path) -> dict | list | None:
    """Load JSON file, return None if not found."""
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding='utf-8'))


def _load_heuristic_db() -> dict:
    """Load shared heuristic-db.json."""
    return _load_json(HEURISTIC_DB_PATH) or {}


# ═══════════════════════════════════════════════════════════════════════
# ARTBOARD CONTEXT EXTRACTION
# ═══════════════════════════════════════════════════════════════════════

def _extract_artboard_ids(text: str) -> list[str]:
    """Extract 4-digit artboard IDs from text."""
    ids = []
    for m in re.finditer(r'\b(\d{4})\b', text):
        aid = m.group(1)
        if aid not in ids:
            ids.append(aid)
    return ids


def _find_overlay_context(screen_inventory: dict | None,
                          screen_id: str,
                          artboard_ids: list[str]) -> dict:
    """Find overlay context from screen_inventory.json."""
    result = {
        'artboard_id': artboard_ids[0] if artboard_ids else None,
        'overlay_type': None,
        'overlay_label': None,
        'parent_screen_id': None,
        'parent_screen_name': None,
        'boundary_type': None,
    }

    if not screen_inventory:
        return result

    for screen in screen_inventory.get('screens', []):
        if screen.get('id') != screen_id and screen.get('screen_id') != screen_id:
            continue

        result['parent_screen_id'] = screen.get('id', '')
        result['parent_screen_name'] = screen.get('display_name_vi', screen.get('screen_name', ''))
        ba = screen.get('boundary_annotations', {})
        result['boundary_type'] = ba.get('boundary_type', '')

        # Search overlays for matching artboard ID
        for overlay in ba.get('overlays', []):
            artboard_name = overlay.get('artboard', '')
            # Check if any of our artboard IDs match
            for aid in artboard_ids:
                if aid in artboard_name:
                    result['overlay_type'] = overlay.get('type', '')
                    result['overlay_label'] = overlay.get('label', '')
                    result['artboard_id'] = aid
                    return result

    return result


# ═══════════════════════════════════════════════════════════════════════
# HEURISTIC CANDIDATE SELECTION
# ═══════════════════════════════════════════════════════════════════════

def _select_heuristic_candidates(evidence: str, problem: str,
                                 ddl_ref: str,
                                 heuristic_db: dict) -> list[dict]:
    """Pre-select likely heuristic candidates from the DB.

    Uses context_map keyword matching + direct text matching.
    Returns full entries for the LLM to choose from.
    """
    combined = f'{problem} {evidence} {ddl_ref}'.lower()
    candidates: list[dict] = []
    seen: set[str] = set()

    # 1. Context map matching (semantic patterns)
    context_map = heuristic_db.get('context_map', {})
    for pattern, ref_ids in context_map.items():
        keywords = pattern.replace('_', ' ').split()
        # Match if >= 60% of keywords present
        match_count = sum(1 for kw in keywords if kw in combined)
        if match_count >= max(1, len(keywords) * 0.6):
            for ref_id in ref_ids:
                if ref_id in seen:
                    continue
                parts = ref_id.split('.')
                if len(parts) == 2:
                    category, key = parts
                    entry = heuristic_db.get(category, {}).get(key)
                    if entry:
                        candidates.append({
                            **entry,
                            '_match_source': f'context_map:{pattern}',
                            '_ref_id': ref_id,
                        })
                        seen.add(ref_id)

    # 2. Direct text matching (explicit mentions)
    # Nielsen
    for m in re.finditer(r'(?:nielsen|heuristic|h)\s*#?\s*(\d+)', combined):
        ref_id = f'nielsen.{m.group(1)}'
        if ref_id not in seen:
            entry = heuristic_db.get('nielsen', {}).get(m.group(1))
            if entry:
                candidates.append({**entry, '_match_source': 'direct', '_ref_id': ref_id})
                seen.add(ref_id)

    # WCAG
    for m in re.finditer(r'(?:wcag|sc)\s*([\d.]+)', combined):
        ref_id = f'wcag.{m.group(1)}'
        if ref_id not in seen:
            entry = heuristic_db.get('wcag', {}).get(m.group(1))
            if entry:
                candidates.append({**entry, '_match_source': 'direct', '_ref_id': ref_id})
                seen.add(ref_id)

    # Laws
    law_keywords = {
        'fitts': 'fitts', 'hick': 'hick', 'jakob': 'jakob',
        'miller': 'miller', 'peak': 'peak_end', 'zeigarnik': 'zeigarnik',
        'von restorff': 'von_restorff', 'doherty': 'doherty',
        'aesthetic': 'aesthetic_usability',
        'countdown': 'zeigarnik',  # implicit: countdown → incomplete task feeling
        'timer': 'zeigarnik',
        'resend': 'zeigarnik',
        'feedback': 'doherty',
        'status': 'doherty',
    }
    for keyword, law_key in law_keywords.items():
        ref_id = f'laws.{law_key}'
        if keyword in combined and ref_id not in seen:
            entry = heuristic_db.get('laws', {}).get(law_key)
            if entry:
                candidates.append({
                    **entry,
                    '_match_source': f'keyword:{keyword}',
                    '_ref_id': ref_id,
                })
                seen.add(ref_id)

    # 3. Always include Nielsen #1 if evidence mentions missing status/feedback
    visibility_kw = ['thiếu', 'không có', 'missing', 'absent', 'no feedback',
                     'countdown', 'timer', 'indicator', 'progress', 'loading',
                     'status', 'trạng thái']
    if any(kw in combined for kw in visibility_kw):
        ref_id = 'nielsen.1'
        if ref_id not in seen:
            entry = heuristic_db.get('nielsen', {}).get('1')
            if entry:
                candidates.append({
                    **entry,
                    '_match_source': 'visibility_heuristic',
                    '_ref_id': ref_id,
                })
                seen.add(ref_id)

    return candidates


# ═══════════════════════════════════════════════════════════════════════
# RELATED CHECKS AGGREGATION
# ═══════════════════════════════════════════════════════════════════════

def _aggregate_related_checks(screen_id: str, gap_ref: str,
                              module_index: dict) -> list[dict]:
    """Aggregate evidence from related checks referenced by gap_ref."""
    check_nums = [int(n) for n in re.findall(r'#(\d+)', gap_ref)]
    if not check_nums:
        return []

    related = []
    for screen in module_index.get('screens', []):
        if screen.get('screen_id') != screen_id:
            continue
        for check in screen.get('checks', []):
            if check.get('num') in check_nums:
                related.append({
                    'num': check.get('num'),
                    'title': check.get('check', ''),
                    'verdict': check.get('verdict', ''),
                    'evidence': check.get('evidence', ''),
                    'ddl_ref': check.get('ddl_ref', ''),
                    'category': check.get('category', ''),
                    'severity': check.get('severity', ''),
                    'artboard_ids': check.get('_evidence_artboard_ids', []),
                })

    return related


# ═══════════════════════════════════════════════════════════════════════
# CONTEXT ASSEMBLER
# ═══════════════════════════════════════════════════════════════════════

def assemble_uxp_context(uxp: dict, module_index: dict,
                         screen_inventory: dict | None,
                         heuristic_db: dict,
                         meta: dict) -> dict:
    """Assemble full context bundle for a single UXP."""
    screen_id = uxp.get('screen_id', '')
    # For UXPs, screen_id might not be in report-data; try to find from index
    if not screen_id:
        # Find screen_id from gap_ref check numbers
        gap_ref = uxp.get('gap_ref', '')
        check_nums = [int(n) for n in re.findall(r'#(\d+)', gap_ref)]
        for screen in module_index.get('screens', []):
            for check in screen.get('checks', []):
                if check.get('num') in check_nums:
                    screen_id = screen.get('screen_id', '')
                    break
            if screen_id:
                break

    # Aggregate evidence from related checks
    gap_ref = uxp.get('gap_ref', '')
    related_checks = _aggregate_related_checks(screen_id, gap_ref, module_index)

    # Extract artboard IDs from all evidence
    all_evidence = uxp.get('problem', '') + ' '
    for rc in related_checks:
        all_evidence += rc.get('evidence', '') + ' '
        all_evidence += ' '.join(rc.get('artboard_ids', [])) + ' '
    artboard_ids = _extract_artboard_ids(all_evidence)

    # Overlay context
    overlay_ctx = _find_overlay_context(screen_inventory, screen_id, artboard_ids)

    # Heuristic candidates
    evidence_text = ' '.join(rc.get('evidence', '') for rc in related_checks)
    candidates = _select_heuristic_candidates(
        evidence_text, uxp.get('problem', ''),
        uxp.get('ddl_ref', ''), heuristic_db
    )

    return {
        'id': uxp.get('id', ''),
        'type': 'uxp',
        'finding': {
            'severity': uxp.get('severity', ''),
            'screen_tag': uxp.get('screen_tag', ''),
            'screen_id': screen_id,
            'problem': uxp.get('problem', ''),
            'ddl_ref': uxp.get('ddl_ref', ''),
            'solution_draft': uxp.get('solution', ''),
            'gap_ref': gap_ref,
            'current_user_impact': uxp.get('user_impact', ''),
            'current_heuristic': uxp.get('heuristic', ''),
        },
        'artboard': overlay_ctx,
        'related_checks': related_checks,
        'domain': {
            'name': meta.get('domain', 'Banking'),
            'product': meta.get('product_name', ''),
            'module': meta.get('module_name', ''),
            'sensitivity': 'high' if 'bank' in meta.get('domain', '').lower() else 'medium',
        },
        'heuristic_candidates': candidates,
        'fields_to_generate': [
            'hiện_trạng',
            'tác_động',
            'nguyên_tắc',
            'đề_xuất_steps',
            'references',
        ],
    }


def assemble_gap_context(gap: dict, screen_group: dict,
                         module_index: dict,
                         screen_inventory: dict | None,
                         heuristic_db: dict,
                         meta: dict) -> dict:
    """Assemble full context bundle for a single Gap."""
    screen_id = gap.get('screen_id', screen_group.get('screen_id', ''))
    evidence = gap.get('evidence', '')
    title = gap.get('title', '')

    artboard_ids = _extract_artboard_ids(evidence)
    overlay_ctx = _find_overlay_context(screen_inventory, screen_id, artboard_ids)

    candidates = _select_heuristic_candidates(
        evidence, title, gap.get('ref', ''), heuristic_db
    )

    return {
        'id': f"Gap#{gap.get('num', '?')}@{screen_id}",
        'type': 'gap',
        'finding': {
            'num': gap.get('num'),
            'title': title,
            'severity': gap.get('severity', ''),
            'screen_id': screen_id,
            'screen_name': gap.get('screen_name', screen_group.get('screen_name', '')),
            'screen_type': gap.get('screen_type', screen_group.get('screen_type', '')),
            'evidence': evidence,
            'ddl_ref': gap.get('ref', ''),
            'ddl_evidence': gap.get('ddl_evidence', ''),
            'current_user_impact': gap.get('user_impact', ''),
            'current_heuristic': gap.get('heuristic', ''),
        },
        'artboard': overlay_ctx,
        'related_checks': [],  # Gaps are individual checks already
        'domain': {
            'name': meta.get('domain', 'Banking'),
            'product': meta.get('product_name', ''),
            'module': meta.get('module_name', ''),
            'sensitivity': 'high' if 'bank' in meta.get('domain', '').lower() else 'medium',
        },
        'heuristic_candidates': candidates,
        'fields_to_generate': [
            'hiện_trạng',
            'tác_động',
            'nguyên_tắc',
            'references',
        ],
    }


# ═══════════════════════════════════════════════════════════════════════
# MANIFEST GENERATOR
# ═══════════════════════════════════════════════════════════════════════

def generate_manifest(module_dir: Path) -> dict:
    """Generate LLM enrichment manifest for a module."""
    report_data = _load_json(module_dir / 'report-data.json')
    if not report_data:
        return {'error': f'No report-data.json in {module_dir}'}

    module_index = _load_json(module_dir / 'module-index.json') or {}
    screen_inventory = _load_json(module_dir / 'handoff' / 'screen_inventory.json')
    heuristic_db = _load_heuristic_db()
    meta = report_data.get('meta', {})

    manifest = {
        '_generator': 'enrich_llm.py',
        '_version': '1.0',
        'module': {
            'name': meta.get('module_name', module_dir.name),
            'domain': meta.get('domain', ''),
            'product': meta.get('product_name', ''),
            'dir': str(module_dir),
        },
        'system_prompt': _build_system_prompt(meta, heuristic_db),
        'items': [],
        'stats': {
            'uxp_count': 0,
            'gap_count': 0,
            'total_items': 0,
            'fields_to_generate': 0,
        },
    }

    # UXPs
    for uxp in report_data.get('uxps', []):
        ctx = assemble_uxp_context(
            uxp, module_index, screen_inventory, heuristic_db, meta
        )
        manifest['items'].append(ctx)
        manifest['stats']['uxp_count'] += 1

    # Gaps
    for sg in report_data.get('gaps_by_screen', []):
        for gap in sg.get('gaps', []):
            ctx = assemble_gap_context(
                gap, sg, module_index, screen_inventory, heuristic_db, meta
            )
            manifest['items'].append(ctx)
            manifest['stats']['gap_count'] += 1

    manifest['stats']['total_items'] = len(manifest['items'])
    manifest['stats']['fields_to_generate'] = sum(
        len(item.get('fields_to_generate', [])) for item in manifest['items']
    )

    return manifest


# ═══════════════════════════════════════════════════════════════════════
# SYSTEM PROMPT BUILDER
# ═══════════════════════════════════════════════════════════════════════

def _build_system_prompt(meta: dict, heuristic_db: dict) -> str:
    """Build system prompt for LLM agent."""
    domain = meta.get('domain', 'Banking')
    product = meta.get('product_name', '')

    # Build heuristic reference table
    ref_table = []
    for num, entry in sorted(heuristic_db.get('nielsen', {}).items()):
        ref_table.append(f"  Nielsen #{num}: {entry.get('name', '')} — \"{entry.get('quote', '')}\"")
    for key, entry in heuristic_db.get('laws', {}).items():
        ref_table.append(f"  {entry.get('name', '')}: \"{entry.get('quote', '')}\"")
    for sc, entry in sorted(heuristic_db.get('wcag', {}).items()):
        ref_table.append(f"  {entry.get('name', '')}")
    ref_text = '\n'.join(ref_table)

    return f"""Bạn là UX Auditor chuyên nghiệp cho {domain} app ({product}).

Nhiệm vụ: Enrich các finding từ UX audit report. Mỗi finding cần 4-5 fields:

1. **hiện_trạng**: Mô tả chính xác UI hiện tại
   - PHẢI có artboard ID (vd: "Trên artboard 7103")
   - PHẢI có overlay type nếu có (vd: "overlay: OTP bottom-sheet")
   - PHẢI liệt kê UI elements thực tế có mặt
   - KHÔNG suy diễn elements không có trong evidence

2. **tác_động**: Hậu quả cụ thể cho người dùng
   - PHẢI mô tả consequence cho user (bị chặn, mất khả năng, nhầm lẫn...)
   - PHẢI có domain context ({domain}: giao dịch nhạy cảm, trust, compliance...)
   - KHÔNG dùng severity label ("nghiêm trọng", "critical", "major")
   - KHÔNG lặp lại problem title

3. **nguyên_tắc**: Heuristic vi phạm + quote + giải thích
   - PHẢI cite heuristic bằng tên chính xác (Nielsen #N, WCAG X.Y.Z, Laws of UX)
   - PHẢI có quote gốc tiếng Anh
   - PHẢI giải thích TẠI SAO design vi phạm nguyên tắc này
   - Ưu tiên chọn từ heuristic_candidates đã pre-select

4. **đề_xuất_steps**: (chỉ UXP) Array các bước cải thiện
   - Ít nhất 2 bước
   - Mỗi bước actionable, có DDL ref nếu liên quan
   - Spec cụ thể (timeout=60s, color token, component name)

5. **references**: Array các tham chiếu chính thức
   - Mỗi ref: {{name, url, quote, source}}
   - Dữ liệu từ REFERENCE DATABASE bên dưới
   - KHÔNG bịa URL — chỉ dùng URL từ database

OUTPUT FORMAT: JSON array of objects, mỗi object có id + các fields trên.

REFERENCE DATABASE:
{ref_text}"""


# ═══════════════════════════════════════════════════════════════════════
# PROMPT FORMAT OUTPUT
# ═══════════════════════════════════════════════════════════════════════

def manifest_to_prompt(manifest: dict) -> str:
    """Convert manifest to human-readable prompt markdown."""
    lines = []
    lines.append('# LLM Enrichment Prompt\n')
    lines.append(f'## System Prompt\n')
    lines.append(manifest.get('system_prompt', ''))
    lines.append('\n---\n')
    lines.append(f'## Items to Enrich ({manifest["stats"]["total_items"]} total)\n')

    for i, item in enumerate(manifest.get('items', [])):
        finding = item.get('finding', {})
        artboard = item.get('artboard', {})
        lines.append(f'### Item {i+1}: {item["id"]} ({item["type"].upper()})\n')
        lines.append(f'**Severity:** {finding.get("severity", "")}')
        lines.append(f'**Screen:** {finding.get("screen_tag", finding.get("screen_name", ""))}')
        lines.append(f'**Problem:** {finding.get("problem", finding.get("title", ""))}')

        evidence = finding.get('evidence', '')
        if not evidence and item.get('related_checks'):
            evidence = ' | '.join(
                rc.get('evidence', '') for rc in item['related_checks']
            )
        lines.append(f'**Evidence:** {evidence}')
        lines.append(f'**DDL Ref:** {finding.get("ddl_ref", finding.get("ref", ""))}')

        if finding.get('solution_draft'):
            lines.append(f'**Solution draft:** {finding["solution_draft"]}')

        if artboard.get('overlay_type'):
            lines.append(f'**Artboard:** {artboard.get("artboard_id", "?")} '
                         f'(type: {artboard["overlay_type"]}, '
                         f'label: {artboard.get("overlay_label", "")})')

        if item.get('heuristic_candidates'):
            cands = ', '.join(
                c.get('name', '') for c in item['heuristic_candidates'][:3]
            )
            lines.append(f'**Heuristic candidates:** {cands}')

        lines.append(f'**Fields to generate:** {", ".join(item.get("fields_to_generate", []))}')
        lines.append('')

    lines.append('\n---\n')
    lines.append('## Expected Output Format\n')
    lines.append('```json')
    lines.append('[')
    lines.append('  {')
    lines.append('    "id": "UXP-001",')
    lines.append('    "hiện_trạng": "Trên artboard 7103 (overlay: OTP bottom-sheet), ...",')
    lines.append('    "tác_động": "Người dùng bị chặn hoặc ...",')
    lines.append('    "nguyên_tắc": "Nielsen #1 — Visibility of System Status — ...",')
    lines.append('    "đề_xuất_steps": ["Bước 1...", "Bước 2..."],')
    lines.append('    "references": [{"name": "...", "url": "...", "quote": "...", "source": "..."}]')
    lines.append('  }')
    lines.append(']')
    lines.append('```')

    return '\n'.join(lines)


# ═══════════════════════════════════════════════════════════════════════
# MODULE PROCESSOR
# ═══════════════════════════════════════════════════════════════════════

def process_module(module_dir: Path, output_format: str = 'json') -> dict:
    """Process a single module: generate manifest and/or prompt."""
    module_dir = module_dir.resolve()

    if not (module_dir / 'report-data.json').exists():
        return {'module': module_dir.name, 'status': 'skip',
                'reason': 'no report-data.json'}

    # Check cache
    cache_path = module_dir / 'llm-enriched.json'
    manifest_path = module_dir / 'llm-manifest.json'

    manifest = generate_manifest(module_dir)
    if 'error' in manifest:
        return {'module': module_dir.name, 'status': 'error',
                'reason': manifest['error']}

    stats = manifest['stats']

    if output_format == 'json':
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
            encoding='utf-8',
        )

    if output_format == 'prompt':
        prompt_path = module_dir / 'llm-prompt.md'
        prompt_text = manifest_to_prompt(manifest)
        prompt_path.write_text(prompt_text, encoding='utf-8')
        # Also write manifest for merge_llm to use
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + '\n',
            encoding='utf-8',
        )

    has_cache = cache_path.exists()

    return {
        'module': module_dir.name,
        'status': 'ok',
        'uxp_count': stats['uxp_count'],
        'gap_count': stats['gap_count'],
        'total_items': stats['total_items'],
        'fields_to_generate': stats['fields_to_generate'],
        'has_cache': has_cache,
        'manifest_path': str(manifest_path),
    }


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Generate LLM enrichment manifest for UX audit modules'
    )
    parser.add_argument('--module', type=Path,
                        help='Path to single module directory')
    parser.add_argument('--base', type=Path,
                        help='Base directory to find all modules')
    parser.add_argument('--prompt', action='store_true',
                        help='Output human-readable prompt (also writes JSON)')
    parser.add_argument('--stats', action='store_true',
                        help='Print stats only (no file output)')
    args = parser.parse_args()

    output_format = 'prompt' if args.prompt else ('stats' if args.stats else 'json')

    modules: list[Path] = []
    if args.module:
        modules = [args.module.resolve()]
    elif args.base:
        base = args.base.resolve()
        for root, dirs, files in os.walk(base):
            if 'report-data.json' in files:
                modules.append(Path(root))
        modules.sort()
    else:
        parser.error('Specify either --module or --base')

    if not modules:
        print('No modules with report-data.json found.', file=sys.stderr)
        sys.exit(1)

    fmt_label = {'json': '📋 MANIFEST', 'prompt': '📝 PROMPT', 'stats': '📊 STATS'}
    print(f'\n{"═" * 60}')
    print(f'  {fmt_label[output_format]} — {len(modules)} module(s)')
    print(f'{"═" * 60}\n')

    total_items = 0
    total_fields = 0

    for mod_dir in modules:
        result = process_module(mod_dir, output_format)

        if result['status'] == 'skip':
            print(f'  ⏭️  {result["module"]}: {result.get("reason", "skipped")}')
        elif result['status'] == 'error':
            print(f'  ❌ {result["module"]}: {result.get("reason", "error")}')
        else:
            cached = ' (cached ✅)' if result.get('has_cache') else ''
            print(f'  📋 {result["module"]}: '
                  f'{result["uxp_count"]} UXPs + {result["gap_count"]} Gaps '
                  f'= {result["total_items"]} items, '
                  f'{result["fields_to_generate"]} fields{cached}')
            total_items += result['total_items']
            total_fields += result['fields_to_generate']

            if output_format != 'stats':
                print(f'      → {result.get("manifest_path", "")}')

    if len(modules) > 1:
        print(f'\n{"─" * 60}')
        print(f'  📊 BATCH: {total_items} items, {total_fields} fields to generate')
    print()


if __name__ == '__main__':
    main()
