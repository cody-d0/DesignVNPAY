#!/usr/bin/env python3
"""
audit_images.py — Audit image quality and diversity in report-data.json.

Reports:
  - Coverage: % of UXPs/gaps with screenshot_path
  - Diversity: % of screen groups with multi-image assignment
  - Breakdown: reasons for single-image groups
  - Delta: improvement from enrichment (if _image_enrichment exists)

Usage:
  python3 audit_images.py --base path/to/final/
  python3 audit_images.py --module path/to/module/
  python3 audit_images.py --base path/to/final/ --json  # machine-readable output
"""

import argparse
import json
import os
import sys
from pathlib import Path


def audit_module(module_dir: Path) -> dict:
    """Audit a single module's image quality."""
    rd_path = module_dir / 'report-data.json'
    if not rd_path.exists():
        return {'module': module_dir.name, 'error': 'no report-data.json'}

    data = json.loads(rd_path.read_text(encoding='utf-8'))

    # Load inventory for comparison
    inv_path = module_dir / 'handoff' / 'screen_inventory.json'
    inv_by_scr: dict[str, int] = {}
    if inv_path.exists():
        inv = json.loads(inv_path.read_text(encoding='utf-8'))
        for scr in inv.get('screens', []):
            sid = scr.get('id', '')
            imgs = scr.get('wireframe_images', [])
            inv_by_scr[sid] = len(imgs)

    # Load artboard-index for comparison
    ai_path = module_dir / 'artboard-index.json'
    ai_by_scr: dict[str, int] = {}
    if ai_path.exists():
        ai = json.loads(ai_path.read_text(encoding='utf-8'))
        import re
        for scr_key, scr_data in ai.items():
            m = re.match(r'(SCR-\w+-\d+)', scr_key)
            if m and isinstance(scr_data, dict):
                sid = m.group(1)
                ab_count = len(scr_data.get('artboards', {}))
                ai_by_scr[sid] = max(ai_by_scr.get(sid, 0), ab_count)

    # UXP coverage
    uxps = data.get('uxps', [])
    uxp_total = len(uxps)
    uxp_with_img = sum(1 for u in uxps if u.get('screenshot_path'))
    uxp_enriched = sum(1 for u in uxps if u.get('_img_enriched_from'))

    # Gap coverage & diversity
    gap_total = 0
    gap_with_img = 0
    gap_enriched = 0
    screen_groups = []

    for sg in data.get('gaps_by_screen', []):
        sid = sg.get('screen_id', '')
        gaps = sg.get('gaps', [])
        imgs_set = set()

        for g in gaps:
            gap_total += 1
            if g.get('screenshot_path'):
                gap_with_img += 1
                imgs_set.add(g['screenshot_path'])
            if g.get('_img_enriched_from'):
                gap_enriched += 1

        n_gaps = len(gaps)
        n_unique = len(imgs_set)
        inv_count = inv_by_scr.get(sid, 0)
        ai_count = ai_by_scr.get(sid, 0)

        reason = 'multi' if n_unique > 1 else (
            '1_gap' if n_gaps == 1 else (
            '1_artboard' if max(inv_count, ai_count) <= 1 else
            'scoring_limit'))

        screen_groups.append({
            'screen_id': sid,
            'gaps': n_gaps,
            'unique_imgs': n_unique,
            'inv_artboards': inv_count,
            'ai_artboards': ai_count,
            'diversity': reason,
        })

    multi = sum(1 for sg in screen_groups if sg['diversity'] == 'multi')
    total_sg = len(screen_groups)

    return {
        'module': module_dir.name,
        'uxp_total': uxp_total,
        'uxp_with_img': uxp_with_img,
        'uxp_enriched': uxp_enriched,
        'gap_total': gap_total,
        'gap_with_img': gap_with_img,
        'gap_enriched': gap_enriched,
        'screen_groups': total_sg,
        'multi_image': multi,
        'diversity_pct': round(100 * multi / max(1, total_sg)),
        'screen_breakdown': screen_groups,
        'enrichment': data.get('_image_enrichment'),
    }


def _discover_modules(base_dir: Path) -> list[Path]:
    modules = []
    for root, dirs, files in os.walk(base_dir):
        if 'report-data.json' in files:
            modules.append(Path(root))
    return sorted(modules)


def main():
    parser = argparse.ArgumentParser(description='Audit image quality in report-data.json')
    parser.add_argument('--module', type=Path, help='Single module directory')
    parser.add_argument('--base', type=Path, help='Base directory (all modules)')
    parser.add_argument('--json', action='store_true', help='JSON output')
    args = parser.parse_args()

    if not args.module and not args.base:
        parser.error('Either --module or --base required')

    modules = [args.module] if args.module else _discover_modules(args.base)

    all_results = []
    t_uxp = t_uxi = t_gap = t_gi = t_sg = t_mm = 0
    reasons: dict[str, int] = {}

    for module_dir in modules:
        result = audit_module(module_dir)
        all_results.append(result)

        if 'error' not in result:
            t_uxp += result['uxp_total']
            t_uxi += result['uxp_with_img']
            t_gap += result['gap_total']
            t_gi += result['gap_with_img']
            t_sg += result['screen_groups']
            t_mm += result['multi_image']

            for sg in result['screen_breakdown']:
                r = sg['diversity']
                reasons[r] = reasons.get(r, 0) + 1

    if args.json:
        print(json.dumps({
            'modules': all_results,
            'summary': {
                'uxp_coverage': f'{t_uxi}/{t_uxp}',
                'gap_coverage': f'{t_gi}/{t_gap}',
                'multi_image': f'{t_mm}/{t_sg}',
                'diversity_pct': round(100 * t_mm / max(1, t_sg)),
                'breakdown': reasons,
            }
        }, ensure_ascii=False, indent=2))
    else:
        print('=' * 60)
        print('📊 IMAGE QUALITY AUDIT')
        print('=' * 60)
        print(f'UXP coverage: {t_uxi}/{t_uxp} ({100 * t_uxi // max(1, t_uxp)}%)')
        print(f'Gap coverage: {t_gi}/{t_gap} ({100 * t_gi // max(1, t_gap)}%)')
        print()
        print('Gap image diversity:')
        print(f'  Multi-image: {t_mm}/{t_sg} ({100 * t_mm // max(1, t_sg)}%)')
        print(f'  Single-image: {t_sg - t_mm}/{t_sg}')
        print()
        print('Single-image breakdown:')
        for r, c in sorted(reasons.items(), key=lambda x: -x[1]):
            if r != 'multi':
                print(f'  {r:20s}: {c}')


if __name__ == '__main__':
    main()
