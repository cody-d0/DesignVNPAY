#!/usr/bin/env python3
"""
pipeline.py — Full end-to-end pipeline orchestrator.

Runs: Index → Convert → Validate → Enrich Images → Enrich Refs → Render

Usage:
  python3 pipeline.py --module /path/to/module/
  python3 pipeline.py --base /path/to/final/
  python3 pipeline.py --module /path/to/module/ --skip-render
  python3 pipeline.py --module /path/to/module/ --from enrich
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent  # ux-audit-json-converter/
SCRIPTS_DIR = SKILL_DIR / 'scripts'

# External skill script paths
EVIDENCE_IMG_SCRIPT = SKILL_DIR.parent / 'evidence-img' / 'scripts' / 'enrich_images.py'
EVIDENCE_INFO_SCRIPT = SKILL_DIR.parent / 'evidence-info' / 'scripts' / 'enrich_refs.py'
RENDER_SCRIPT = SKILL_DIR.parent / 'ux-audit-pitch-deck' / 'scripts' / 'render_report.py'


STEPS = ['index', 'convert', 'validate', 'enrich-img', 'enrich-ref', 'render']


def _run_step(name: str, cmd: list[str], module_dir: Path, critical: bool = True) -> bool:
    """Run a pipeline step. Returns True if successful."""
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=60
        )
        # Print stderr (most scripts output to stderr)
        if result.stderr:
            for line in result.stderr.strip().split('\n'):
                print(f'  {line}')
        if result.stdout:
            for line in result.stdout.strip().split('\n'):
                print(f'  {line}')

        if result.returncode != 0 and critical:
            print(f'  ❌ {name} FAILED (exit {result.returncode})')
            return False
        return True
    except subprocess.TimeoutExpired:
        print(f'  ❌ {name} TIMEOUT (60s)')
        return False
    except FileNotFoundError as e:
        print(f'  ⚠️  {name} SKIPPED — script not found: {e.filename}')
        return not critical  # Non-critical skip is OK


def run_pipeline(module_dir: Path, skip_render: bool = False,
                 from_step: str = 'index', dry_run: bool = False) -> dict:
    """Run full pipeline on a single module.

    Returns: { 'module': str, 'steps': { step: status }, 'success': bool }
    """
    module_dir = module_dir.resolve()
    result = {'module': module_dir.name, 'steps': {}, 'success': True}

    python = sys.executable
    steps_to_run = STEPS[STEPS.index(from_step):]

    for step in steps_to_run:
        if step == 'render' and skip_render:
            result['steps'][step] = 'skipped'
            continue

        if step == 'index':
            cmd = [python, str(SCRIPTS_DIR / 'index_module.py'),
                   '--module', str(module_dir)]
        elif step == 'convert':
            cmd = [python, str(SCRIPTS_DIR / 'convert.py'),
                   '--module', str(module_dir)]
        elif step == 'validate':
            cmd = [python, str(SCRIPTS_DIR / 'validate.py'),
                   '--module', str(module_dir)]
        elif step == 'enrich-img':
            if not EVIDENCE_IMG_SCRIPT.exists():
                result['steps'][step] = 'not-installed'
                continue
            cmd = [python, str(EVIDENCE_IMG_SCRIPT),
                   '--module', str(module_dir)]
            if dry_run:
                cmd.append('--dry-run')
        elif step == 'enrich-ref':
            if not EVIDENCE_INFO_SCRIPT.exists():
                result['steps'][step] = 'not-installed'
                continue
            cmd = [python, str(EVIDENCE_INFO_SCRIPT),
                   '--module', str(module_dir)]
            if dry_run:
                cmd.append('--dry-run')
        elif step == 'render':
            if not RENDER_SCRIPT.exists():
                result['steps'][step] = 'not-installed'
                continue
            cmd = [python, str(RENDER_SCRIPT),
                   '--module', str(module_dir)]
        else:
            continue

        # Index/Convert/Validate are critical; enrichment is non-critical
        critical = step in ('index', 'convert', 'validate')
        ok = _run_step(step, cmd, module_dir, critical=critical)

        if ok:
            result['steps'][step] = 'ok'
        else:
            result['steps'][step] = 'failed'
            if critical:
                result['success'] = False
                print(f'  ⛔ Pipeline stopped at {step}')
                break

    return result


def _discover_modules(base_dir: Path) -> list[Path]:
    """Find all module directories containing ux-review-report.md."""
    modules = []
    for root, dirs, files in os.walk(base_dir):
        if 'ux-review-report.md' in files:
            modules.append(Path(root))
    return sorted(modules)


def main():
    parser = argparse.ArgumentParser(
        description='Full UX Audit pipeline orchestrator'
    )
    parser.add_argument('--module', type=Path, help='Single module directory')
    parser.add_argument('--base', type=Path, help='Base directory (all modules)')
    parser.add_argument('--skip-render', action='store_true',
                        help='Skip pitch deck rendering')
    parser.add_argument('--from', dest='from_step', default='index',
                        choices=STEPS,
                        help='Start from specific step (default: index)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Enrichment dry-run (no writes)')
    args = parser.parse_args()

    if not args.module and not args.base:
        parser.error('Either --module or --base required')

    modules = [args.module] if args.module else _discover_modules(args.base)

    print(f'🚀 Pipeline: {len(modules)} modules | Steps: {args.from_step} → '
          f'{"render" if not args.skip_render else "enrich-ref"}')
    print(f'{"=" * 60}')

    results = []
    for i, module_dir in enumerate(modules):
        print(f'\n[{i+1}/{len(modules)}] {module_dir.name}')
        print(f'{"-" * 50}')
        r = run_pipeline(module_dir, skip_render=args.skip_render,
                        from_step=args.from_step, dry_run=args.dry_run)
        results.append(r)

    # Summary
    print(f'\n{"=" * 60}')
    print(f'📊 Pipeline Summary')
    print(f'{"=" * 60}')

    success_count = sum(1 for r in results if r['success'])
    fail_count = len(results) - success_count

    for r in results:
        status = '✅' if r['success'] else '❌'
        steps_str = ' → '.join(
            f'{s}:{v[:2]}' for s, v in r['steps'].items()
        )
        print(f'  {status} {r["module"]}: {steps_str}')

    print(f'\n  Total: {success_count} success, {fail_count} failed')

    if fail_count > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
