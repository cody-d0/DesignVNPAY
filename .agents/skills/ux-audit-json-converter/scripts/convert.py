#!/usr/bin/env python3
"""
convert.py — Module Index → report-data.json converter.

Reads module-index.json (Lớp 2: canonical, single source of truth)
and assembles report-data.json (Lớp 3: consumer-ready for render_report.py).

This script ONLY reads module-index.json. It never touches raw markdown
or handoff files directly. All format normalization happens in index_module.py.

Usage:
    python3 convert.py --module /path/to/module/
    python3 convert.py --module /path/to/module/ --dry
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# ═══════════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════════

HEURISTIC_CATEGORIES = [
    {"key": "flow",      "name_vi": "Luồng người dùng",     "name_en": "Flow & Navigation"},
    {"key": "component", "name_vi": "Thành phần",            "name_en": "Component & DDL"},
    {"key": "visual",    "name_vi": "Thiết kế trực quan",    "name_en": "Visual Design"},
    {"key": "content",   "name_vi": "Nội dung",              "name_en": "Content & Copy"},
    {"key": "a11y",      "name_vi": "Tiếp cận",              "name_en": "Accessibility"},
    {"key": "trust",     "name_vi": "Tin cậy & Bảo mật",     "name_en": "Trust & Security"},
]

CATEGORY_MAP = {
    'component': 'component', 'feature': 'flow', 'visual': 'visual',
    'content': 'content', 'accessibility': 'a11y', 'safety': 'trust',
    'security': 'trust', 'trust': 'trust', 'ux': 'flow', 'ux law': 'flow',
    'skill a': 'component', 'skill b': 'flow', 'skill c': 'visual',
    'ddl law': 'flow',
}


# ═══════════════════════════════════════════════════════════════════════
# HELPERS
# ═══════════════════════════════════════════════════════════════════════

def _score_color(score: int) -> str:
    if score < 50:
        return '#b91c1c'
    if score < 70:
        return '#c2410c'
    return '#15803d'


def _score_offset(score: int) -> int:
    return round(314 * (1 - score / 100))


def _screen_score_offset(score: int) -> int:
    """For per-screen SVG rings: r=25, circumference=157."""
    return round(157 * (1 - score / 100))


_OVERLAY_KEYWORDS = [
    'bottom sheet', 'dialog', 'confirm', 'popup', 'modal', 'overlay',
    'menu', 'picker', 'otp', 'xác nhận', 'hủy', 'huỷ', 'xoá tất cả',
    'dropdown', 'action sheet', 'toast', 'snackbar', 'alert',
]


def _resolve_screenshot(screen_id: str, image_map: dict,
                        check_nums: list = None,
                        evidence_text: str = '',
                        context_text: str = '') -> str:
    """Resolve best screenshot for a UXP or Gap.

    Resolution chain (7 steps):
    1. Evidence direct image ref
    2. Evidence artboard ID → fuzzy match disk
    3. Context-aware overlay match (if problem text mentions overlay patterns)
    4. Inventory base image for screen
    5. SCR-MD base image for screen
    6. First disk image matching artboard pattern
    7. Fallback: empty

    Args:
        context_text: UXP problem/solution text for overlay keyword detection
    """
    # Step 1: Evidence direct image ref
    if check_nums:
        for ref in image_map.get('evidence_refs', []):
            if ref.get('check_num') in check_nums and ref.get('image_ref'):
                filename = ref['image_ref']
                if filename in image_map.get('disk_files', []):
                    return f'ui/{filename}'

    # Step 2: Evidence artboard ID from text
    artboard_ids = re.findall(r'\b(\d{4})\b', evidence_text)
    if artboard_ids:
        for aid in artboard_ids:
            for df in image_map.get('disk_files', []):
                if df.startswith(aid):
                    return f'ui/{df}'

    # Step 3: Context-aware overlay match
    # If UXP/gap text mentions overlay patterns, prefer overlay images
    combined_text = (context_text + ' ' + evidence_text).lower()
    prefer_overlay = any(kw in combined_text for kw in _OVERLAY_KEYWORDS)

    if prefer_overlay:
        for inv_img in image_map.get('inventory_images', []):
            if (inv_img.get('screen_id') == screen_id
                    and inv_img.get('role', '').startswith('overlay')):
                fn = inv_img['filename']
                if fn in image_map.get('disk_files', []):
                    return f'ui/{fn}'

    # Step 4: Inventory base image
    for inv_img in image_map.get('inventory_images', []):
        if inv_img.get('screen_id') == screen_id and inv_img.get('role') == 'base':
            fn = inv_img['filename']
            if fn in image_map.get('disk_files', []):
                return f'ui/{fn}'

    # Step 5: SCR-MD image
    for scr_img in image_map.get('scr_md_images', []):
        if scr_img.get('screen_id') == screen_id:
            fn = scr_img['filename']
            if fn in image_map.get('disk_files', []):
                return f'ui/{fn}'

    # Step 6: Any inventory image for screen
    for inv_img in image_map.get('inventory_images', []):
        if inv_img.get('screen_id') == screen_id:
            fn = inv_img['filename']
            if fn in image_map.get('disk_files', []):
                return f'ui/{fn}'

    # Step 7: Fallback
    return ''


# ═══════════════════════════════════════════════════════════════════════
# ASSEMBLERS
# ═══════════════════════════════════════════════════════════════════════

def assemble_meta(index: dict) -> dict:
    """Build meta section from module-index report_meta."""
    rm = index['report_meta']
    return {
        'client_name': rm.get('client_name', 'Co-opBank'),
        'product_name': rm.get('product_name', 'Co-opBank Mobile Banking'),
        'module_name': rm.get('module_name', ''),
        'domain': rm.get('domain', 'Banking'),
        'section': rm.get('section', ''),
        'module_dir': index['_meta'].get('module_dir', ''),
    }


def assemble_stats(index: dict) -> dict:
    """Build stats section from score_block + screens + uxps."""
    sb = index['score_block']
    screens = index['screens']
    uxps = index['uxp_blocks']

    # Calculate from screen data if score_block incomplete
    total_pass = sb.get('pass', 0) or sum(s.get('pass_count', 0) for s in screens)
    total_gap = sb.get('gap', 0) or sum(s.get('gap_count', 0) for s in screens)
    total_checks = sb.get('total_checks', 0) or sum(s.get('check_count', 0) for s in screens)
    score = sb.get('score', 0)
    if not score and (total_pass + total_gap) > 0:
        score = round(total_pass / (total_pass + total_gap) * 100)

    # Severity counts from UXPs
    sev_counts = {'critical': 0, 'major': 0, 'minor': 0}
    for u in uxps:
        sev = u.get('severity', 'Major').lower()
        if sev in sev_counts:
            sev_counts[sev] += 1

    return {
        'screen_count': len(screens),
        'check_count': total_checks,
        'gap_count': total_gap,
        'pass_count': total_pass,
        'proposal_count': len(uxps),
        'overall_score': score,
        'overall_score_color': _score_color(score),
        'overall_score_offset': _score_offset(score),
        'severity_counts': sev_counts,
    }


def assemble_screens(index: dict) -> list[dict]:
    """Build screens array from module-index screens data."""
    result = []
    for s in index['screens']:
        score = s.get('score', 0)
        screen_id = s.get('screen_id', '')
        screen_name = s.get('screen_name', '')

        result.append({
            'id': screen_id,
            'name': f'{screen_name} (`{screen_id}`)' if screen_id else screen_name,
            'type': s.get('screen_type', ''),
            'score': score,
            'score_color': _score_color(score),
            'score_offset': _screen_score_offset(score),
            'gap_count': s.get('gap_count', 0),
            'artboard_count': s.get('artboard_count', 0),
        })
    return result


def assemble_uxps(index: dict) -> list[dict]:
    """Build uxps array from module-index uxp_blocks."""
    image_map = index.get('image_map', {})
    result = []

    for u in index['uxp_blocks']:
        fields = u.get('fields', {})
        screen_tag = fields.get('Màn hình', u.get('screen_tag', ''))
        screen_id = u.get('screen_id', '')
        gap_ref = fields.get('Gap ref', '')

        # Parse check numbers from gap_ref
        check_nums = [int(n) for n in re.findall(r'#(\d+)', gap_ref)]

        # Collect evidence text from related checks
        evidence_text = ''
        for screen_data in index['screens']:
            if screen_data.get('screen_id') == screen_id:
                for check in screen_data.get('checks', []):
                    if check.get('num') in check_nums:
                        evidence_text += ' ' + check.get('evidence', '')

        # Build context for overlay keyword detection
        problem_text = fields.get('Vấn đề', '')
        solution_text = fields.get('Giải pháp', '')
        context_text = f'{problem_text} {solution_text}'

        screenshot = _resolve_screenshot(screen_id, image_map,
                                           check_nums, evidence_text,
                                           context_text)

        result.append({
            'id': u['id'],
            'severity': u.get('severity', 'Major'),
            'screen_tag': screen_tag,
            'problem': fields.get('Vấn đề', ''),
            'gap_ref': gap_ref,
            'ddl_ref': fields.get('DDL', ''),
            'solution': fields.get('Giải pháp', ''),
            'screenshot_path': screenshot,
        })
    return result


def assemble_gaps_by_screen(index: dict) -> list[dict]:
    """Build gaps_by_screen from check tables (verdict=gap)."""
    image_map = index.get('image_map', {})
    result = []

    for screen_data in index['screens']:
        screen_id = screen_data.get('screen_id', '')
        screen_name = screen_data.get('screen_name', '')
        screen_type = screen_data.get('screen_type', '')

        gaps = []
        for check in screen_data.get('checks', []):
            verdict = check.get('verdict', '').lower().strip()
            if verdict != 'gap':
                continue

            num = check.get('num', 0)
            evidence = check.get('evidence', '')

            # Resolve heuristic from category
            category = check.get('category', '').lower()
            heuristic_key = CATEGORY_MAP.get(category, 'flow')
            # Find heuristic name
            heuristic_name = ''
            for h in HEURISTIC_CATEGORIES:
                if h['key'] == heuristic_key:
                    heuristic_name = f"{h['name_en']} ({h['name_vi']})"
                    break

            # Extract DDL/UXG ref from evidence or ddl_ref column
            ref = check.get('ddl_ref', '')
            if not ref:
                # Try to extract from evidence
                ref_match = re.search(r'(UXG-\d+|COMP:\w+|TOKEN:\w+)', evidence)
                if ref_match:
                    ref = ref_match.group(1)

            # Extract severity
            severity = check.get('severity', 'Minor')

            # Screenshot resolution
            check_title = check.get('check', '')
            context_text = f'{check_title} {evidence}'
            screenshot = _resolve_screenshot(
                screen_id, image_map, [num], evidence, context_text
            )
            screenshot_filename = screenshot.replace('ui/', '') if screenshot else ''

            # Derive user_impact from check description
            user_impact = check.get('check', '')

            gaps.append({
                'num': num,
                'title': check.get('check', ''),
                'ref': ref,
                'severity': severity,
                'user_impact': user_impact,
                'heuristic': heuristic_name,
                'evidence': evidence,
                'screenshot': screenshot_filename,
                'screen_id': screen_id,
                'screen_name': screen_name,
                'screen_type': screen_type,
                'screenshot_path': screenshot,
            })

        if gaps:
            result.append({
                'screen_id': screen_id,
                'screen_name': f'{screen_name} (`{screen_id}`)' if screen_id else screen_name,
                'screen_type': screen_type,
                'gaps': gaps,
            })

    return result


def assemble_heuristics(index: dict) -> list[dict]:
    """Build heuristic scorecard from check tables."""
    # Count pass/gap per heuristic category
    cat_stats = {h['key']: {'pass': 0, 'gap': 0} for h in HEURISTIC_CATEGORIES}

    for screen_data in index['screens']:
        for check in screen_data.get('checks', []):
            verdict = check.get('verdict', '').lower().strip()
            if verdict not in ('pass', 'gap'):
                continue

            category = check.get('category', '').lower()
            heuristic_key = CATEGORY_MAP.get(category, 'flow')

            if heuristic_key in cat_stats:
                if verdict == 'pass':
                    cat_stats[heuristic_key]['pass'] += 1
                else:
                    cat_stats[heuristic_key]['gap'] += 1

    result = []
    for h in HEURISTIC_CATEGORIES:
        stats = cat_stats[h['key']]
        total = stats['pass'] + stats['gap']
        score = round(stats['pass'] / total * 100) if total > 0 else 100

        result.append({
            'key': h['key'],
            'name_vi': h['name_vi'],
            'name_en': h['name_en'],
            'score': score,
            'gap_count': stats['gap'],
        })

    return result


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════

def convert(index: dict) -> dict:
    """Assemble report-data.json from module-index.json."""
    return {
        'meta': assemble_meta(index),
        'stats': assemble_stats(index),
        'screens': assemble_screens(index),
        'uxps': assemble_uxps(index),
        'gaps_by_screen': assemble_gaps_by_screen(index),
        'heuristics': assemble_heuristics(index),
    }


def main():
    parser = argparse.ArgumentParser(
        description='module-index.json → report-data.json converter'
    )
    parser.add_argument('--module', type=Path, required=True,
                        help='Path to module directory')
    parser.add_argument('--dry', action='store_true',
                        help='Print to stdout instead of writing file')
    args = parser.parse_args()

    module_dir = args.module.resolve()
    index_path = module_dir / 'module-index.json'

    if not index_path.exists():
        print(f'❌ {module_dir.name}: module-index.json not found. '
              f'Run index_module.py first.', file=sys.stderr)
        sys.exit(1)

    index = json.loads(index_path.read_text(encoding='utf-8'))
    report_data = convert(index)

    output_json = json.dumps(report_data, ensure_ascii=False, indent=2)

    if args.dry:
        print(output_json)
    else:
        out_path = module_dir / 'report-data.json'
        out_path.write_text(output_json, encoding='utf-8')

        stats = report_data['stats']
        n_uxps = stats['proposal_count']
        n_gaps = stats['gap_count']
        score = stats['overall_score']
        n_screens = stats['screen_count']
        n_imgs = sum(1 for u in report_data['uxps'] if u.get('screenshot_path'))
        n_gap_imgs = sum(
            1 for sg in report_data['gaps_by_screen']
            for g in sg['gaps']
            if g.get('screenshot_path')
        )

        print(f'✅ Converted: {module_dir.name}', file=sys.stderr)
        print(f'   Score: {score}% | Screens: {n_screens}', file=sys.stderr)
        print(f'   UXPs: {n_uxps} ({n_imgs} with screenshots)', file=sys.stderr)
        print(f'   Gaps: {n_gaps} ({n_gap_imgs} with screenshots)', file=sys.stderr)
        print(f'   Output: {out_path}', file=sys.stderr)


if __name__ == '__main__':
    main()
