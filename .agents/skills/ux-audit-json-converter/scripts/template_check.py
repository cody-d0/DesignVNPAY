#!/usr/bin/env python3
"""
template_check.py — Consumer-backward validation gate.

Compares report-data.json against template-contract.json to find
all mismatches before pitch deck rendering. Generates human-readable
checkpoint report for self-learning review.

Pipeline position:
    Index → Convert → Validate (schema) → **Template Check** (consumer) → Enrich → Render
                                                    ↑
                                          HUMAN CHECKPOINT HERE

Usage:
    python3 template_check.py --module /path/to/module/
    python3 template_check.py --base /path/to/final/
    python3 template_check.py --module /path/to/module/ --json /tmp/report.json
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

# ═══════════════════════════════════════════════════════════════════════
# LOCATE CONTRACT
# ═══════════════════════════════════════════════════════════════════════

SCRIPT_DIR = Path(__file__).resolve().parent
CONTRACT_PATH = SCRIPT_DIR.parent / 'references' / 'template-contract.json'


def load_contract() -> dict:
    """Load template-contract.json."""
    if not CONTRACT_PATH.exists():
        print(f'❌ template-contract.json not found at {CONTRACT_PATH}',
              file=sys.stderr)
        sys.exit(1)
    return json.loads(CONTRACT_PATH.read_text(encoding='utf-8'))


# ═══════════════════════════════════════════════════════════════════════
# CHECKER CORE
# ═══════════════════════════════════════════════════════════════════════

class Issue:
    """Single validation issue."""
    def __init__(self, level: str, path: str, message: str,
                 template_ref: str = '', got: Any = None):
        self.level = level        # error | warning | info
        self.path = path          # JSON path: meta.client_name
        self.message = message
        self.template_ref = template_ref  # L189 {{CLIENT_NAME}}
        self.got = got            # actual value

    def to_dict(self) -> dict:
        d = {'level': self.level, 'path': self.path, 'message': self.message}
        if self.template_ref:
            d['template_ref'] = self.template_ref
        if self.got is not None:
            d['got'] = str(self.got)[:200]
        return d


def check_field(data: dict, path: str, spec: dict) -> list[Issue]:
    """Check a single field against its spec."""
    issues = []
    keys = path.split('.')
    obj = data
    for k in keys[:-1]:
        obj = obj.get(k, {})
    field = keys[-1]
    value = obj.get(field)
    tref = spec.get('template_ref', '')

    # Required check
    if spec.get('required') and (value is None or value == ''):
        issues.append(Issue('error', path,
                            f'Missing required field',
                            template_ref=tref))
        return issues

    if value is None:
        return issues  # optional, absent → OK

    # Type check
    expected_type = spec.get('type')
    if expected_type == 'int' and not isinstance(value, int):
        issues.append(Issue('error', path,
                            f'Expected int, got {type(value).__name__}',
                            template_ref=tref, got=value))
    elif expected_type == 'string' and not isinstance(value, str):
        issues.append(Issue('error', path,
                            f'Expected string, got {type(value).__name__}',
                            template_ref=tref, got=value))

    # Min/max
    if isinstance(value, int):
        if 'min' in spec and value < spec['min']:
            issues.append(Issue('warning', path,
                                f'Value {value} < min {spec["min"]}',
                                template_ref=tref, got=value))
        if 'max' in spec and value > spec['max']:
            issues.append(Issue('warning', path,
                                f'Value {value} > max {spec["max"]}',
                                template_ref=tref, got=value))

    # Min length
    if isinstance(value, str) and 'min_len' in spec:
        if len(value.strip()) < spec['min_len']:
            issues.append(Issue('warning', path,
                                f'Too short: {len(value)} chars < min_len {spec["min_len"]}',
                                template_ref=tref, got=value))

    # Pattern
    if isinstance(value, str) and 'pattern' in spec:
        if not re.search(spec['pattern'], value):
            issues.append(Issue('warning', path,
                                f'Does not match pattern: {spec["pattern"]}',
                                template_ref=tref, got=value))

    # Enum
    if 'enum' in spec and value not in spec['enum']:
        issues.append(Issue('error', path,
                            f'Invalid value, expected one of {spec["enum"]}',
                            template_ref=tref, got=value))

    return issues


def check_formula(data: dict) -> list[Issue]:
    """Validate computed fields (score offsets)."""
    issues = []
    stats = data.get('stats', {})

    # Hero ring: circumference = 320
    score = stats.get('overall_score', 0)
    expected_offset = round(320 * (1 - score / 100))
    actual_offset = stats.get('overall_score_offset')
    if actual_offset is not None and actual_offset != expected_offset:
        issues.append(Issue('error', 'stats.overall_score_offset',
                            f'Formula mismatch: expected 320*(1-{score}/100)={expected_offset}, '
                            f'got {actual_offset}',
                            template_ref='L198 hero ring r=51 C=320',
                            got=actual_offset))

    # Screen rings: circumference = 157
    for i, scr in enumerate(data.get('screens', [])):
        s_score = scr.get('score', 0)
        expected = round(157 * (1 - s_score / 100))
        actual = scr.get('score_offset')
        if actual is not None and actual != expected:
            issues.append(Issue('warning', f'screens[{i}].score_offset',
                                f'Formula mismatch: expected 157*(1-{s_score}/100)={expected}, '
                                f'got {actual}',
                                template_ref='L214 screen ring r=25 C=157',
                                got=actual))

    # Score color consistency
    color = stats.get('overall_score_color', '')
    if score < 50 and color != '#b91c1c':
        issues.append(Issue('warning', 'stats.overall_score_color',
                            f'Score {score} < 50 should be #b91c1c (red)',
                            got=color))
    elif 50 <= score < 70 and color != '#c2410c':
        issues.append(Issue('warning', 'stats.overall_score_color',
                            f'Score {score} 50-69 should be #c2410c (orange)',
                            got=color))
    elif score >= 70 and color != '#15803d':
        issues.append(Issue('warning', 'stats.overall_score_color',
                            f'Score {score} >= 70 should be #15803d (green)',
                            got=color))

    return issues


def check_cross_validation(data: dict) -> list[Issue]:
    """Cross-field consistency checks."""
    issues = []
    stats = data.get('stats', {})
    sev = stats.get('severity_counts', {})

    # UXP count vs severity sum
    uxps = data.get('uxps', [])
    sev_sum = sev.get('critical', 0) + sev.get('major', 0) + sev.get('minor', 0)
    if len(uxps) != sev_sum:
        issues.append(Issue('warning', 'stats.severity_counts',
                            f'severity_counts sum ({sev_sum}) != uxps count ({len(uxps)})'))

    # UXP severity distribution
    actual_sev = {'Critical': 0, 'Major': 0, 'Minor': 0}
    for u in uxps:
        s = u.get('severity', '')
        if s in actual_sev:
            actual_sev[s] += 1
    for key, count in actual_sev.items():
        stat_key = key.lower()
        stat_val = sev.get(stat_key, 0)
        if count != stat_val:
            issues.append(Issue('warning', f'stats.severity_counts.{stat_key}',
                                f'Declared {stat_val}, actual UXPs with severity={key}: {count}'))

    # Gap count vs actual gaps
    total_gaps = sum(len(sg.get('gaps', []))
                     for sg in data.get('gaps_by_screen', []))
    if stats.get('gap_count', 0) != total_gaps:
        issues.append(Issue('warning', 'stats.gap_count',
                            f'Declared {stats.get("gap_count")}, '
                            f'actual gaps in gaps_by_screen: {total_gaps}'))

    # Screen count vs actual screens
    if stats.get('screen_count', 0) != len(data.get('screens', [])):
        issues.append(Issue('warning', 'stats.screen_count',
                            f'Declared {stats.get("screen_count")}, '
                            f'actual screens: {len(data.get("screens", []))}'))

    # proposal_count vs UXPs with solution
    solutions = sum(1 for u in uxps if u.get('solution'))
    if stats.get('proposal_count', 0) != solutions and solutions > 0:
        issues.append(Issue('info', 'stats.proposal_count',
                            f'Declared {stats.get("proposal_count")}, '
                            f'UXPs with solution: {solutions}'))

    return issues


def check_images(data: dict, module_dir: Path) -> dict:
    """Image coverage analysis."""
    ui_dir = module_dir / 'ui'
    disk_files = set()
    if ui_dir.exists():
        disk_files = {
            f.name for f in ui_dir.iterdir()
            if f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.webp')
            and not f.name.startswith('.')
        }

    used_images = set()
    issues = []

    # UXP screenshots
    uxps = data.get('uxps', [])
    uxp_with_img = 0
    uxp_without_img = 0
    for i, u in enumerate(uxps):
        ss = u.get('screenshot_path', '')
        if ss:
            uxp_with_img += 1
            fn = ss.split('/')[-1] if '/' in ss else ss
            used_images.add(fn)
            if fn not in disk_files:
                issues.append(Issue('error', f'uxps[{i}].screenshot_path',
                                    f'Referenced image not on disk: {fn}',
                                    template_ref='L266 phone-frame img',
                                    got=ss))
        else:
            uxp_without_img += 1
            issues.append(Issue('warning', f'uxps[{i}].screenshot_path',
                                f'UXP {u.get("id", "?")} has no screenshot',
                                template_ref='L266 phone-frame img'))

    # Gap screenshots
    gap_with_img = 0
    gap_without_img = 0
    for sg in data.get('gaps_by_screen', []):
        for j, gap in enumerate(sg.get('gaps', [])):
            ss = gap.get('screenshot_path', '')
            if ss:
                gap_with_img += 1
                fn = ss.split('/')[-1] if '/' in ss else ss
                used_images.add(fn)
                if fn not in disk_files:
                    issues.append(Issue('warning',
                                        f'gaps_by_screen.gaps[{j}].screenshot_path',
                                        f'Referenced image not on disk: {fn}',
                                        got=ss))
            else:
                gap_without_img += 1

    unused_images = disk_files - used_images

    return {
        'disk_total': len(disk_files),
        'used_total': len(used_images),
        'unused_total': len(unused_images),
        'unused_list': sorted(unused_images),
        'uxp_with_img': uxp_with_img,
        'uxp_without_img': uxp_without_img,
        'gap_with_img': gap_with_img,
        'gap_without_img': gap_without_img,
        'issues': issues,
    }


def check_references(data: dict) -> dict:
    """Reference citation coverage analysis."""
    uxps = data.get('uxps', [])
    uxp_with_ref = 0
    uxp_without_ref = 0
    ref_sources: dict[str, int] = {}  # count by source name

    for u in uxps:
        refs = u.get('references', [])
        if refs and isinstance(refs, list) and len(refs) > 0:
            uxp_with_ref += 1
            for r in refs:
                src = r.get('source', 'Unknown') if isinstance(r, dict) else 'Unknown'
                ref_sources[src] = ref_sources.get(src, 0) + 1
        else:
            uxp_without_ref += 1

    gap_with_ref = 0
    gap_without_ref = 0
    for sg in data.get('gaps_by_screen', []):
        for gap in sg.get('gaps', []):
            refs = gap.get('references', [])
            if refs and isinstance(refs, list) and len(refs) > 0:
                gap_with_ref += 1
                for r in refs:
                    src = r.get('source', 'Unknown') if isinstance(r, dict) else 'Unknown'
                    ref_sources[src] = ref_sources.get(src, 0) + 1
            else:
                gap_without_ref += 1

    total_items = uxp_with_ref + uxp_without_ref + gap_with_ref + gap_without_ref
    total_with_ref = uxp_with_ref + gap_with_ref
    coverage_pct = round(total_with_ref / total_items * 100) if total_items > 0 else 0

    return {
        'uxp_with_ref': uxp_with_ref,
        'uxp_without_ref': uxp_without_ref,
        'gap_with_ref': gap_with_ref,
        'gap_without_ref': gap_without_ref,
        'total_with_ref': total_with_ref,
        'total_items': total_items,
        'coverage_pct': coverage_pct,
        'sources_breakdown': ref_sources,
    }


# ═══════════════════════════════════════════════════════════════════════
# MAIN CHECK RUNNER
# ═══════════════════════════════════════════════════════════════════════

def check_enrichment_preview(data: dict, contract: dict) -> dict:
    """Check which enrichment fields are already populated vs pending.

    Scans contract for fields with "source": "enrich_inline" and reports
    their current status. Used for human review BEFORE enrichment runs.
    """
    result: dict[str, dict] = {}

    # UXP enrichment fields
    uxps_spec = contract.get('uxps', {}).get('item', {})
    uxps = data.get('uxps', [])
    for field, spec in uxps_spec.items():
        if isinstance(spec, dict) and spec.get('source') == 'enrich_inline':
            filled = sum(1 for u in uxps if u.get(field))
            result[f'uxp.{field}'] = {
                'total': len(uxps),
                'filled': filled,
                'empty': len(uxps) - filled,
                'label': spec.get('label_vi', field),
            }

    # Gap enrichment fields
    gap_spec = contract.get('gaps_by_screen', {}).get('gap_item', {})
    all_gaps = [g for sg in data.get('gaps_by_screen', []) for g in sg.get('gaps', [])]
    for field, spec in gap_spec.items():
        if isinstance(spec, dict) and spec.get('source') == 'enrich_inline':
            filled = sum(1 for g in all_gaps if g.get(field))
            result[f'gap.{field}'] = {
                'total': len(all_gaps),
                'filled': filled,
                'empty': len(all_gaps) - filled,
                'label': spec.get('label_vi', field),
            }

    return result


def template_check(data: dict, module_dir: Path,
                   contract: dict) -> dict:
    """Full template check against contract."""
    all_issues: list[Issue] = []

    # 1. Meta fields
    for field, spec in contract.get('meta', {}).items():
        if isinstance(spec, dict) and 'type' in spec:
            all_issues.extend(check_field(data, f'meta.{field}', spec))

    # 2. Stats fields
    for field, spec in contract.get('stats', {}).items():
        if field == 'severity_counts':
            for sf, ss in spec.items():
                if isinstance(ss, dict) and 'type' in ss:
                    all_issues.extend(check_field(
                        data, f'stats.severity_counts.{sf}', ss))
        elif isinstance(spec, dict) and 'type' in spec:
            all_issues.extend(check_field(data, f'stats.{field}', spec))

    # 3. Screens array
    screens_spec = contract.get('screens', {}).get('item', {})
    for i, scr in enumerate(data.get('screens', [])):
        for field, spec in screens_spec.items():
            if isinstance(spec, dict) and 'type' in spec:
                path = f'screens[{i}].{field}'
                # Inline check for array items
                value = scr.get(field)
                tref = spec.get('template_ref', '')
                if spec.get('required') and (value is None or value == ''):
                    all_issues.append(Issue('error', path,
                                            'Missing required field',
                                            template_ref=tref))
                elif value is not None:
                    if spec.get('type') == 'int' and not isinstance(value, int):
                        all_issues.append(Issue('error', path,
                                                f'Expected int, got {type(value).__name__}',
                                                template_ref=tref, got=value))
                    if isinstance(value, str) and 'pattern' in spec:
                        if not re.search(spec['pattern'], value):
                            all_issues.append(Issue('warning', path,
                                                    f'Pattern mismatch: {spec["pattern"]}',
                                                    template_ref=tref, got=value))

    # 4. UXPs array
    uxps_spec = contract.get('uxps', {}).get('item', {})
    for i, uxp in enumerate(data.get('uxps', [])):
        for field, spec in uxps_spec.items():
            if isinstance(spec, dict) and 'type' in spec:
                path = f'uxps[{i}].{field}'
                value = uxp.get(field)
                tref = spec.get('template_ref', '')
                if spec.get('required') and (value is None or value == ''):
                    all_issues.append(Issue('error', path,
                                            'Missing required field',
                                            template_ref=tref))
                elif value is not None:
                    if 'min_len' in spec and isinstance(value, str):
                        if len(value.strip()) < spec['min_len']:
                            all_issues.append(Issue('warning', path,
                                                    f'Too short: {len(value)} < {spec["min_len"]}',
                                                    template_ref=tref, got=value))
                    if 'enum' in spec and value not in spec['enum']:
                        all_issues.append(Issue('error', path,
                                                f'Invalid: expected {spec["enum"]}',
                                                template_ref=tref, got=value))

    # 5. Gaps array
    gbs_screen_spec = contract.get('gaps_by_screen', {}).get('screen_item', {})
    gap_spec = contract.get('gaps_by_screen', {}).get('gap_item', {})
    for i, sg in enumerate(data.get('gaps_by_screen', [])):
        for field, spec in gbs_screen_spec.items():
            if isinstance(spec, dict) and 'type' in spec:
                path = f'gaps_by_screen[{i}].{field}'
                value = sg.get(field)
                tref = spec.get('template_ref', '')
                if spec.get('required') and (value is None or value == ''):
                    all_issues.append(Issue('error', path,
                                            'Missing required field',
                                            template_ref=tref))
        for j, gap in enumerate(sg.get('gaps', [])):
            for field, spec in gap_spec.items():
                if isinstance(spec, dict) and 'type' in spec:
                    path = f'gaps_by_screen[{i}].gaps[{j}].{field}'
                    value = gap.get(field)
                    tref = spec.get('template_ref', '')
                    if spec.get('required') and (value is None or value == ''):
                        all_issues.append(Issue('error', path,
                                                'Missing required field',
                                                template_ref=tref))
                    elif value is not None and 'min_len' in spec:
                        if isinstance(value, str) and len(value.strip()) < spec['min_len']:
                            all_issues.append(Issue('warning', path,
                                                    f'Too short: {len(value)} < {spec["min_len"]}',
                                                    template_ref=tref, got=value))

    # 6. Formula checks
    all_issues.extend(check_formula(data))

    # 7. Cross-validation
    all_issues.extend(check_cross_validation(data))

    # 8. Image coverage
    img_report = check_images(data, module_dir)
    all_issues.extend(img_report.pop('issues'))

    # 9. Reference coverage
    ref_report = check_references(data)

    # Classify
    errors = [i for i in all_issues if i.level == 'error']
    warnings = [i for i in all_issues if i.level == 'warning']
    infos = [i for i in all_issues if i.level == 'info']

    return {
        'module': module_dir.name,
        'passed': len(errors) == 0,
        'errors': len(errors),
        'warnings': len(warnings),
        'infos': len(infos),
        'issues': [i.to_dict() for i in all_issues],
        'images': img_report,
        'references': ref_report,
        'summary': {
            'uxps': len(data.get('uxps', [])),
            'gaps': sum(len(sg.get('gaps', []))
                        for sg in data.get('gaps_by_screen', [])),
            'screens': len(data.get('screens', [])),
            'score': data.get('stats', {}).get('overall_score', 0),
        },
        'enrichment_preview': check_enrichment_preview(data, contract),
    }


# ═══════════════════════════════════════════════════════════════════════
# HUMAN CHECKPOINT REPORT
# ═══════════════════════════════════════════════════════════════════════

def print_checkpoint(result: dict, verbose: bool = False):
    """Print human-readable checkpoint report for review."""
    module = result['module']
    passed = result['passed']
    summary = result['summary']
    images = result['images']
    refs = result.get('references', {})

    # ── Header ──
    status = '✅ PASS' if passed else '❌ FAIL'
    print(f'\n{"═" * 60}')
    print(f'🔍 TEMPLATE CHECK — {module}')
    print(f'{"═" * 60}')
    print(f'Status: {status}')
    print(f'Score: {summary["score"]}% | '
          f'Screens: {summary["screens"]} | '
          f'UXPs: {summary["uxps"]} | '
          f'Gaps: {summary["gaps"]}')
    print(f'Issues: {result["errors"]} errors, '
          f'{result["warnings"]} warnings, '
          f'{result["infos"]} info')

    # ── Image Coverage ──
    print(f'\n📸 IMAGE COVERAGE')
    print(f'   Disk:   {images["disk_total"]} images in ui/')
    print(f'   Used:   {images["used_total"]} referenced in JSON')
    print(f'   Unused: {images["unused_total"]} not referenced')
    print(f'   UXP:    {images["uxp_with_img"]} with screenshot, '
          f'{images["uxp_without_img"]} without')
    print(f'   Gap:    {images["gap_with_img"]} with screenshot, '
          f'{images["gap_without_img"]} without')

    if images['unused_list']:
        print(f'   📂 Unused images:')
        for fn in images['unused_list'][:10]:
            print(f'      · {fn}')
        if len(images['unused_list']) > 10:
            print(f'      ... +{len(images["unused_list"]) - 10} more')

    # ── Reference Coverage ──
    if refs:
        print(f'\n📚 REFERENCE COVERAGE')
        print(f'   Total:  {refs.get("total_with_ref", 0)}/{refs.get("total_items", 0)} '
              f'items with citations ({refs.get("coverage_pct", 0)}%)')
        print(f'   UXP:    {refs.get("uxp_with_ref", 0)} with ref, '
              f'{refs.get("uxp_without_ref", 0)} without')
        print(f'   Gap:    {refs.get("gap_with_ref", 0)} with ref, '
              f'{refs.get("gap_without_ref", 0)} without')
        sources = refs.get('sources_breakdown', {})
        if sources:
            print(f'   Sources:')
            for src, count in sorted(sources.items(), key=lambda x: -x[1]):
                print(f'      · {src}: {count}')

    # ── Enrichment Preview ──
    enrich = result.get('enrichment_preview', {})
    if enrich:
        print(f'\n🔮 ENRICHMENT PREVIEW (enrich_inline.py)')
        all_filled = True
        for field_key, info in enrich.items():
            total = info['total']
            filled = info['filled']
            empty = info['empty']
            label = info.get('label', field_key)
            if total == 0:
                status = '➖'
            elif filled == total:
                status = '✅'
            elif filled > 0:
                status = '⚠️'
                all_filled = False
            else:
                status = '⭕'
                all_filled = False
            print(f'   {status} {field_key} ({label}): {filled}/{total}')
        if all_filled:
            print(f'   → All enrichment fields already populated')
        else:
            print(f'   → Run: python3 enrich_inline.py --module <path>')

    # ── Issues ──
    if result['errors'] > 0:
        print(f'\n🔴 ERRORS ({result["errors"]})')
        for iss in result['issues']:
            if iss['level'] == 'error':
                ref = f' ← {iss["template_ref"]}' if iss.get('template_ref') else ''
                got = f' (got: {iss["got"]})' if iss.get('got') else ''
                print(f'   {iss["path"]}: {iss["message"]}{got}{ref}')

    if result['warnings'] > 0 and (verbose or result['errors'] > 0):
        print(f'\n🟡 WARNINGS ({result["warnings"]})')
        for iss in result['issues']:
            if iss['level'] == 'warning':
                ref = f' ← {iss["template_ref"]}' if iss.get('template_ref') else ''
                got = f' (got: {iss["got"]})' if iss.get('got') else ''
                print(f'   {iss["path"]}: {iss["message"]}{got}{ref}')

    if result['infos'] > 0 and verbose:
        print(f'\n💬 INFO ({result["infos"]})')
        for iss in result['issues']:
            if iss['level'] == 'info':
                print(f'   {iss["path"]}: {iss["message"]}')

    # ── Human Checkpoint ──
    print(f'\n{"─" * 60}')
    if not passed:
        print(f'🛑 HUMAN CHECKPOINT REQUIRED')
        print(f'   {result["errors"]} error(s) must be resolved before rendering.')
        print(f'   Review errors above and decide:')
        print(f'     → Fix source (ux-review-report.md) and re-run pipeline')
        print(f'     → Update template-contract.json if contract needs revision')
        print(f'     → Override with --force to render despite errors')
    elif result['warnings'] > 0:
        print(f'⚠️  HUMAN REVIEW RECOMMENDED')
        print(f'   {result["warnings"]} warning(s) found. Rendering will proceed.')
        print(f'   Review warnings to improve output quality.')
    else:
        print(f'✅ All checks passed. Ready to render.')
    print()


# ═══════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='Consumer-backward template validation gate'
    )
    parser.add_argument('--module', type=Path,
                        help='Path to single module directory')
    parser.add_argument('--base', type=Path,
                        help='Base directory to find all modules')
    parser.add_argument('--json', type=Path, default=None,
                        help='Output results as JSON')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Show all issue levels including info')
    args = parser.parse_args()

    contract = load_contract()

    modules: list[Path] = []
    if args.module:
        modules = [args.module.resolve()]
    elif args.base:
        base = args.base.resolve()
        for d in sorted(base.iterdir()):
            if d.is_dir() and (d / 'report-data.json').exists():
                modules.append(d)
    else:
        parser.error('Specify either --module or --base')

    if not modules:
        print('No modules with report-data.json found.', file=sys.stderr)
        sys.exit(1)

    all_results = []
    total_errors = 0
    total_warnings = 0

    for mod_dir in modules:
        data_path = mod_dir / 'report-data.json'
        if not data_path.exists():
            print(f'⏭️  Skip {mod_dir.name}: no report-data.json',
                  file=sys.stderr)
            continue

        data = json.loads(data_path.read_text(encoding='utf-8'))
        result = template_check(data, mod_dir, contract)
        all_results.append(result)
        print_checkpoint(result, verbose=args.verbose)
        total_errors += result['errors']
        total_warnings += result['warnings']

    # ── Batch summary ──
    if len(modules) > 1:
        print(f'\n{"═" * 60}')
        print(f'📊 BATCH SUMMARY — {len(all_results)} modules')
        print(f'{"═" * 60}')
        passed = sum(1 for r in all_results if r['passed'])
        failed = len(all_results) - passed
        print(f'   ✅ Passed: {passed}')
        print(f'   ❌ Failed: {failed}')
        print(f'   Errors: {total_errors} | Warnings: {total_warnings}')

        total_disk = sum(r['images']['disk_total'] for r in all_results)
        total_used = sum(r['images']['used_total'] for r in all_results)
        total_unused = sum(r['images']['unused_total'] for r in all_results)
        print(f'   📸 Images: {total_used}/{total_disk} used, '
              f'{total_unused} unused')
        print()

    if args.json:
        output = {
            'checked_at': __import__('datetime').datetime.now().isoformat(),
            'contract_version': contract.get('_contract_version', ''),
            'modules': all_results,
            'batch_summary': {
                'total': len(all_results),
                'passed': sum(1 for r in all_results if r['passed']),
                'total_errors': total_errors,
                'total_warnings': total_warnings,
            },
        }
        args.json.write_text(
            json.dumps(output, ensure_ascii=False, indent=2),
            encoding='utf-8')
        print(f'📝 JSON report: {args.json}', file=sys.stderr)

    sys.exit(1 if total_errors > 0 else 0)


if __name__ == '__main__':
    main()
