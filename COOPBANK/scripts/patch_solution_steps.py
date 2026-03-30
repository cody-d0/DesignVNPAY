#!/usr/bin/env python3
"""
Patch đề_xuất_steps for UXPs missing it in llm-enriched.json.

Strategy:
- Parse the existing `solution` field from report-data.json
- Split into actionable steps using common delimiters
- Patch into llm-enriched.json
- Re-run merge_llm.py + render_report.py

Usage:
    python3 patch_solution_steps.py --base /path/to/final/
    python3 patch_solution_steps.py --base /path/to/final/ --dry-run
"""
import json
import os
import re
import glob
import argparse


def split_solution_to_steps(solution: str) -> list[str]:
    """Split a solution string into actionable steps."""
    if not solution or not solution.strip():
        return []

    text = solution.strip()

    # Strategy 1: Explicit numbered items (1) ... (2) ... or 1. ... 2. ...
    numbered = re.split(r'\s*\(\d+\)\s*|\s*\d+\.\s+', text)
    numbered = [s.strip() for s in numbered if s.strip()]
    if len(numbered) >= 2:
        return numbered

    # Strategy 2: Semicolons
    if ';' in text:
        parts = [s.strip() for s in text.split(';') if s.strip()]
        if len(parts) >= 2:
            return parts

    # Strategy 3: Vietnamese conjunctions/delimiters
    # "và" as separator when between distinct clauses
    if ' và ' in text and len(text) > 80:
        parts = [s.strip() for s in text.split(' và ') if s.strip()]
        if len(parts) >= 2:
            return parts

    # Strategy 4: Comma-separated with action verbs
    if ', ' in text and len(text) > 60:
        parts = [s.strip() for s in text.split(', ') if s.strip()]
        # Only split on commas if each part is substantial
        if len(parts) >= 2 and all(len(p) > 15 for p in parts):
            return parts

    # Fallback: return as single-item list
    return [text]


def patch_module(module_dir: str, dry_run: bool = False) -> dict:
    """Patch a single module's llm-enriched.json with missing đề_xuất_steps."""
    enriched_path = os.path.join(module_dir, 'llm-enriched.json')
    report_path = os.path.join(module_dir, 'report-data.json')

    if not os.path.exists(enriched_path) or not os.path.exists(report_path):
        return {'module': os.path.basename(module_dir), 'status': 'skip', 'patched': 0}

    enriched = json.load(open(enriched_path))
    report = json.load(open(report_path))

    # Build UXP lookup from report-data
    uxp_lookup = {u['id']: u for u in report.get('uxps', [])}

    patched = 0
    for item in enriched:
        item_id = item.get('id', '')
        if 'UXP' not in item_id:
            continue
        if item.get('đề_xuất_steps'):
            continue

        # Get solution from report-data
        rd_uxp = uxp_lookup.get(item_id, {})
        solution = rd_uxp.get('solution', '')

        steps = split_solution_to_steps(solution)
        if steps:
            item['đề_xuất_steps'] = steps
            patched += 1

    mod_name = os.path.basename(module_dir)

    if patched > 0 and not dry_run:
        with open(enriched_path, 'w', encoding='utf-8') as f:
            json.dump(enriched, f, ensure_ascii=False, indent=2)

    return {'module': mod_name, 'status': 'patched' if patched > 0 else 'ok', 'patched': patched}


def main():
    parser = argparse.ArgumentParser(description='Patch missing đề_xuất_steps')
    parser.add_argument('--base', required=True, help='Path to final/ directory')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    args = parser.parse_args()

    modules = sorted(glob.glob(os.path.join(args.base, '*/report-data.json')))
    print(f"📂 Found {len(modules)} modules")

    total_patched = 0
    for rp in modules:
        mod_dir = os.path.dirname(rp)
        result = patch_module(mod_dir, dry_run=args.dry_run)
        if result['patched'] > 0:
            flag = '🔧' if not args.dry_run else '👁️'
            print(f"  {flag} {result['module']}: patched {result['patched']} UXPs")
            total_patched += result['patched']

    mode = 'DRY RUN' if args.dry_run else 'PATCHED'
    print(f"\n{'👁️' if args.dry_run else '✅'} {mode}: {total_patched} UXPs across {len(modules)} modules")


if __name__ == '__main__':
    main()
