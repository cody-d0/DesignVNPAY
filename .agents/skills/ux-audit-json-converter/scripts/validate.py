#!/usr/bin/env python3
"""
validate.py — Schema validator for report-data.json.

Validates that report-data.json matches the consumer contract required
by render_report.py. Functions as a gate between convert.py and the renderer.

Usage:
    python3 validate.py --module /path/to/module/
    python3 validate.py --module /path/to/module/ --json /tmp/validation.json
"""

import argparse
import json
import sys
from pathlib import Path

# ═══════════════════════════════════════════════════════════════════════
# SCHEMA: Required fields per consumer function
# ═══════════════════════════════════════════════════════════════════════

SCHEMA = {
    'meta': {
        'required': ['client_name', 'product_name', 'module_name'],
        'types': {'client_name': str, 'product_name': str, 'module_name': str},
    },
    'stats': {
        'required': ['screen_count', 'check_count', 'gap_count',
                     'proposal_count', 'overall_score',
                     'overall_score_color', 'overall_score_offset',
                     'severity_counts'],
        'types': {
            'screen_count': int, 'check_count': int, 'gap_count': int,
            'proposal_count': int, 'overall_score': int,
            'overall_score_color': str, 'overall_score_offset': int,
        },
    },
    'screens[]': {
        'required': ['id', 'name', 'type', 'score', 'score_color',
                     'score_offset', 'gap_count'],
        'types': {
            'score': int, 'gap_count': int, 'score_offset': int,
        },
    },
    'uxps[]': {
        'required': ['id', 'severity', 'problem'],
        'types': {
            'severity': str,
        },
        'enum': {
            'severity': ['Critical', 'Major', 'Minor'],
        },
    },
    'gaps_by_screen[]': {
        'required': ['screen_id', 'screen_name', 'screen_type', 'gaps'],
    },
    'gaps_by_screen[].gaps[]': {
        'required': ['num', 'title', 'evidence'],
        'types': {'num': int},
    },
    'heuristics[]': {
        'required': ['name_vi', 'name_en', 'score'],
        'types': {'score': int},
    },
}


def validate(data: dict) -> list[dict]:
    """Validate report-data.json against consumer contract.

    Returns list of issues. Empty = passed.
    """
    issues = []

    def _check(path: str, obj: dict, rules: dict, context: str = ''):
        for field in rules.get('required', []):
            if field not in obj:
                issues.append({
                    'level': 'error',
                    'path': f'{path}.{field}',
                    'message': f'Missing required field',
                    'context': context,
                })
            elif obj[field] is None or obj[field] == '':
                # Empty string for optional display is OK, but log as warning
                if field not in ('type', 'screen_type', 'ddl_ref', 'solution',
                                 'screenshot_path', 'screenshot', 'ref',
                                 'user_impact', 'heuristic'):
                    issues.append({
                        'level': 'warning',
                        'path': f'{path}.{field}',
                        'message': f'Empty value',
                        'context': context,
                    })

        for field, expected_type in rules.get('types', {}).items():
            if field in obj and obj[field] is not None:
                if not isinstance(obj[field], expected_type):
                    issues.append({
                        'level': 'error',
                        'path': f'{path}.{field}',
                        'message': f'Type mismatch: expected {expected_type.__name__}, '
                                   f'got {type(obj[field]).__name__}',
                        'context': context,
                    })

        for field, valid_values in rules.get('enum', {}).items():
            if field in obj and obj[field] not in valid_values:
                issues.append({
                    'level': 'warning',
                    'path': f'{path}.{field}',
                    'message': f'Unexpected value "{obj[field]}", '
                               f'expected one of {valid_values}',
                    'context': context,
                })

    # Top-level sections
    for section in ['meta', 'stats', 'screens', 'uxps',
                    'gaps_by_screen', 'heuristics']:
        if section not in data:
            issues.append({
                'level': 'error',
                'path': section,
                'message': f'Missing top-level section',
                'context': '',
            })

    if 'meta' in data:
        _check('meta', data['meta'], SCHEMA['meta'])

    if 'stats' in data:
        _check('stats', data['stats'], SCHEMA['stats'])
        # Validate severity_counts sub-object
        sev = data['stats'].get('severity_counts', {})
        for key in ['critical', 'major', 'minor']:
            if key not in sev:
                issues.append({
                    'level': 'error',
                    'path': f'stats.severity_counts.{key}',
                    'message': 'Missing severity count',
                    'context': '',
                })

    if 'screens' in data:
        for i, s in enumerate(data['screens']):
            _check(f'screens[{i}]', s, SCHEMA['screens[]'],
                   context=s.get('id', f'index-{i}'))

    if 'uxps' in data:
        for i, u in enumerate(data['uxps']):
            _check(f'uxps[{i}]', u, SCHEMA['uxps[]'],
                   context=u.get('id', f'index-{i}'))

    if 'gaps_by_screen' in data:
        total_gaps = 0
        for i, sg in enumerate(data['gaps_by_screen']):
            _check(f'gaps_by_screen[{i}]', sg, SCHEMA['gaps_by_screen[]'],
                   context=sg.get('screen_id', f'index-{i}'))
            for j, gap in enumerate(sg.get('gaps', [])):
                _check(f'gaps_by_screen[{i}].gaps[{j}]', gap,
                       SCHEMA['gaps_by_screen[].gaps[]'],
                       context=f'{sg.get("screen_id", "")} gap#{j}')
                total_gaps += 1

        # Cross-validate gap count
        stats_gaps = data.get('stats', {}).get('gap_count', 0)
        if stats_gaps != total_gaps:
            issues.append({
                'level': 'warning',
                'path': 'stats.gap_count',
                'message': f'Gap count mismatch: stats says {stats_gaps}, '
                           f'actual gaps = {total_gaps}',
                'context': 'cross-validation',
            })

    if 'heuristics' in data:
        for i, h in enumerate(data['heuristics']):
            _check(f'heuristics[{i}]', h, SCHEMA['heuristics[]'],
                   context=h.get('key', f'index-{i}'))

    # Cross-validate score color format
    color = data.get('stats', {}).get('overall_score_color', '')
    if color and not color.startswith('#'):
        issues.append({
            'level': 'error',
            'path': 'stats.overall_score_color',
            'message': f'Color must be hex format (#rrggbb), got: {color}',
            'context': '',
        })

    return issues


def main():
    parser = argparse.ArgumentParser(
        description='Schema validator for report-data.json'
    )
    parser.add_argument('--module', type=Path, required=True,
                        help='Path to module directory')
    parser.add_argument('--json', type=Path, default=None,
                        help='Output validation results as JSON')
    args = parser.parse_args()

    module_dir = args.module.resolve()
    data_path = module_dir / 'report-data.json'

    if not data_path.exists():
        print(f'❌ {module_dir.name}: report-data.json not found. '
              f'Run convert.py first.', file=sys.stderr)
        sys.exit(1)

    data = json.loads(data_path.read_text(encoding='utf-8'))
    issues = validate(data)

    errors = [i for i in issues if i['level'] == 'error']
    warnings = [i for i in issues if i['level'] == 'warning']

    if args.json:
        result = {
            'module': module_dir.name,
            'valid': len(errors) == 0,
            'errors': len(errors),
            'warnings': len(warnings),
            'issues': issues,
        }
        args.json.write_text(json.dumps(result, ensure_ascii=False, indent=2),
                             encoding='utf-8')

    # Print report
    if errors:
        print(f'❌ FAILED: {module_dir.name} ({len(errors)} errors, '
              f'{len(warnings)} warnings)', file=sys.stderr)
        for e in errors:
            print(f'  🔴 {e["path"]}: {e["message"]}', file=sys.stderr)
        for w in warnings:
            print(f'  🟡 {w["path"]}: {w["message"]}', file=sys.stderr)
        sys.exit(1)
    elif warnings:
        print(f'✅ PASSED with {len(warnings)} warnings: {module_dir.name}',
              file=sys.stderr)
        for w in warnings:
            print(f'  🟡 {w["path"]}: {w["message"]}', file=sys.stderr)
    else:
        print(f'✅ PASSED: {module_dir.name} — schema 100% valid',
              file=sys.stderr)


if __name__ == '__main__':
    main()
