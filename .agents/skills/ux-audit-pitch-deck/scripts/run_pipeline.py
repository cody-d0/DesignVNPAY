#!/usr/bin/env python3
"""
run_pipeline.py — Full UXP Reasoning + HTML Generation Pipeline

Single command to execute the complete pipeline for one or all modules:
  Step 1: reason_uxps.py → enriched-data.json (5-block reasoning + citations)
  Step 2: generate.py    → pitch-deck.html (with reasoned content)
  Step 3: audit.py       → quality checks (structural + content)

Usage:
  # Single module (by report path)
  python3 run_pipeline.py --report path/to/ux-review-report.md

  # Batch (all modules under a base directory)
  python3 run_pipeline.py --base path/to/project/final/

  # With options
  python3 run_pipeline.py --base path/to/project/final/ --force --verify
"""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent


def run_step(name: str, cmd: list[str]) -> tuple[bool, str]:
    """Run a pipeline step and capture output."""
    print(f'  ⏳ {name}...', file=sys.stderr, end=' ', flush=True)
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    ok = result.returncode == 0
    print('✅' if ok else '❌', file=sys.stderr)
    if not ok:
        print(f'    stderr: {result.stderr[:200]}', file=sys.stderr)
    return ok, result.stdout


def process_module(report_path: Path, force: bool = False, verify: bool = False) -> dict:
    """Run full pipeline for one module."""
    module_name = report_path.parent.name
    print(f'\n📂 {module_name}', file=sys.stderr)

    results: dict = {
        'module': module_name,
        'report': str(report_path),
        'steps': {},
        'success': True,
    }

    # Step 1: Reason UXPs
    reason_cmd = [
        sys.executable,
        str(SCRIPT_DIR / 'reason_uxps.py'),
        '--report', str(report_path),
    ]
    if force:
        reason_cmd.append('--force')
    if verify:
        reason_cmd.append('--verify')

    ok, stdout = run_step('Reasoning UXPs', reason_cmd)
    try:
        reason_result = json.loads(stdout) if stdout.strip() else {}
    except json.JSONDecodeError:
        reason_result = {'error': stdout[:200]}
    results['steps']['reason_uxps'] = reason_result
    if not ok:
        results['success'] = False

    # Step 2: Reason Gaps (heuristic resolution + source links)
    gap_cmd = [
        sys.executable,
        str(SCRIPT_DIR / 'reason_gaps.py'),
        '--report', str(report_path),
    ]
    if force:
        gap_cmd.append('--force')
    if verify:
        gap_cmd.append('--verify')

    ok, stdout = run_step('Reasoning Gaps', gap_cmd)
    try:
        gap_result = json.loads(stdout) if stdout.strip() else {}
    except json.JSONDecodeError:
        gap_result = {'error': stdout[:200]}
    results['steps']['reason_gaps'] = gap_result
    if not ok:
        results['success'] = False

    # Step 3: Generate HTML
    gen_cmd = [
        sys.executable,
        str(SCRIPT_DIR / 'generate.py'),
        '--report', str(report_path),
    ]
    ok, stdout = run_step('Generating HTML', gen_cmd)
    try:
        gen_result = json.loads(stdout) if stdout.strip() else {}
    except json.JSONDecodeError:
        gen_result = {'error': stdout[:200]}
    results['steps']['generate'] = gen_result
    if not ok:
        results['success'] = False

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description='UXP Full Pipeline Runner')
    parser.add_argument('--report', help='Single report path')
    parser.add_argument('--base', help='Base directory for batch processing')
    parser.add_argument('--force', action='store_true', help='Force re-reasoning')
    parser.add_argument('--verify', action='store_true', help='Quality check')
    args = parser.parse_args()

    if not args.report and not args.base:
        parser.error('Must specify --report or --base')

    all_results = []

    if args.report:
        report = Path(args.report)
        if not report.exists():
            print(f'❌ Report not found: {report}', file=sys.stderr)
            sys.exit(1)
        all_results.append(process_module(report, args.force, args.verify))
    else:
        base = Path(args.base)
        reports = sorted(base.rglob('ux-review-report.md'))
        print(f'🔍 Found {len(reports)} modules under {base}', file=sys.stderr)
        for r in reports:
            all_results.append(process_module(r, args.force, args.verify))

    # Summary
    total = len(all_results)
    ok = sum(1 for r in all_results if r['success'])
    failed = total - ok

    print(f'\n{"="*50}', file=sys.stderr)
    print(f'Pipeline complete: {ok}/{total} modules OK', file=sys.stderr)
    if failed:
        print(f'⚠️  {failed} modules had issues', file=sys.stderr)
        for r in all_results:
            if not r['success']:
                print(f'  ❌ {r["module"]}', file=sys.stderr)

    # Run audit if batch
    if args.base:
        print(f'\n🔍 Running audit...', file=sys.stderr)
        audit_cmd = [
            sys.executable,
            str(SCRIPT_DIR / 'audit.py'),
            '--base', args.base,
        ]
        subprocess.run(audit_cmd)

    # Output JSON summary
    print(json.dumps({
        'total': total,
        'ok': ok,
        'failed': failed,
        'modules': all_results,
    }, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
