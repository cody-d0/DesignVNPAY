#!/usr/bin/env python3
"""
score_engine.py — UX Score Calculator Engine (ported from ux-score-calculator.js).

Pure Python scoring engine with two score models:
  1. Simple Score  = pass / total_checks × 100
  2. Weighted Score = (1 - weighted_penalty / max_penalty) × 100
     Critical = 3.0, Major = 2.0, Minor = 1.0

Standalone usage:
    python3 score_engine.py --module /path/to/module/ [--json] [--verbose]

Library usage:
    from score_engine import calculate_scores, ScoreResult
    result = calculate_scores(screens, uxps)
"""

import argparse
import json
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any


# ═══════════════════════════════════════════════════════════════════════
# SEVERITY WEIGHTS (from ux-score-calculator.js)
# ═══════════════════════════════════════════════════════════════════════

SEVERITY_WEIGHTS = {
    'critical': 3.0,
    'major':    2.0,
    'minor':    1.0,
}


# ═══════════════════════════════════════════════════════════════════════
# DATA CLASSES
# ═══════════════════════════════════════════════════════════════════════

@dataclass
class ScreenScore:
    """Score result for a single screen."""
    screen_id: str
    screen_name: str
    total_checks: int = 0
    pass_count: int = 0
    gap_count: int = 0
    unverifiable_count: int = 0
    simple_score: int = 0
    weighted_score: int = 0
    weighted_penalty: float = 0.0
    max_penalty: float = 0.0
    proposals_count: int = 0
    proposals_by_severity: dict = field(default_factory=lambda: {
        'critical': 0, 'major': 0, 'minor': 0
    })


@dataclass
class Discrepancy:
    """A discrepancy between claimed and actual values."""
    screen_id: str
    field_name: str
    claimed: Any
    actual: Any


@dataclass
class ScoreResult:
    """Complete scoring result."""
    simple_score: int = 0
    weighted_score: int = 0
    total_checks: int = 0
    total_pass: int = 0
    total_gap: int = 0
    total_unverifiable: int = 0
    screens: list = field(default_factory=list)
    discrepancies: list = field(default_factory=list)


# ═══════════════════════════════════════════════════════════════════════
# CORE SCORING
# ═══════════════════════════════════════════════════════════════════════

def calculate_scores(
    screens: list[dict],
    uxps: list[dict],
) -> ScoreResult:
    """Calculate accurate simple + weighted scores from module-index data.

    This is the canonical scoring engine ported from ux-score-calculator.js.
    It re-counts pass/gap from raw check data rather than trusting claimed values.

    Args:
        screens: module-index.json 'screens' array. Each has 'checks' array
                 with 'verdict' and optionally 'severity'.
        uxps:    module-index.json 'uxp_blocks' array. Each has 'severity'
                 and 'screen_id'.

    Returns:
        ScoreResult with per-screen breakdown and discrepancies.
    """
    result = ScoreResult()

    # Map UXPs to screens for weighted calculation
    uxp_by_screen: dict[str, list[dict]] = {}
    for u in uxps:
        sid = u.get('screen_id', '')
        uxp_by_screen.setdefault(sid, []).append(u)

    total_weighted_penalty = 0.0
    total_max_penalty = 0.0

    for screen in screens:
        screen_id = screen.get('screen_id', '')
        screen_name = screen.get('screen_name', '')

        # Re-count from raw checks
        counts = {'pass': 0, 'gap': 0, 'unverifiable': 0}
        for check in screen.get('checks', []):
            verdict = (check.get('verdict', '') or '').lower().strip()
            if 'pass' in verdict:
                counts['pass'] += 1
            elif 'gap' in verdict:
                counts['gap'] += 1
            elif 'unverif' in verdict:
                counts['unverifiable'] += 1

        total_checks = counts['pass'] + counts['gap'] + counts['unverifiable']
        verifiable_checks = counts['pass'] + counts['gap']

        # Simple score: pass / total_checks
        simple_score = (
            round(counts['pass'] / total_checks * 100)
            if total_checks > 0 else 0
        )

        # Weighted score: penalty from proposals for this screen
        screen_uxps = uxp_by_screen.get(screen_id, [])
        screen_weighted_penalty = 0.0
        sev_counts = {'critical': 0, 'major': 0, 'minor': 0}

        for u in screen_uxps:
            sev = (u.get('severity', 'Major') or 'Major').lower()
            weight = SEVERITY_WEIGHTS.get(sev, 1.0)
            screen_weighted_penalty += weight
            if sev in sev_counts:
                sev_counts[sev] += 1

        screen_max_penalty = (
            verifiable_checks * SEVERITY_WEIGHTS['critical']
            if verifiable_checks > 0 else 0.0
        )

        weighted_score = (
            max(0, round(
                (1 - screen_weighted_penalty / screen_max_penalty) * 100
            ))
            if screen_max_penalty > 0 else 100
        )

        total_weighted_penalty += screen_weighted_penalty
        total_max_penalty += screen_max_penalty

        # Discrepancy checking against claimed values
        claimed_score = screen.get('score')
        claimed_pass = screen.get('pass_count')
        claimed_gap = screen.get('gap_count')

        if claimed_pass is not None and claimed_pass != counts['pass']:
            result.discrepancies.append(Discrepancy(
                screen_id=screen_id,
                field_name='pass_count',
                claimed=claimed_pass,
                actual=counts['pass'],
            ))

        if claimed_gap is not None and claimed_gap != counts['gap']:
            result.discrepancies.append(Discrepancy(
                screen_id=screen_id,
                field_name='gap_count',
                claimed=claimed_gap,
                actual=counts['gap'],
            ))

        if claimed_score is not None and claimed_score != simple_score:
            result.discrepancies.append(Discrepancy(
                screen_id=screen_id,
                field_name='score',
                claimed=f'{claimed_score}%',
                actual=f'{simple_score}%',
            ))

        # Build screen score record
        ss = ScreenScore(
            screen_id=screen_id,
            screen_name=screen_name,
            total_checks=total_checks,
            pass_count=counts['pass'],
            gap_count=counts['gap'],
            unverifiable_count=counts['unverifiable'],
            simple_score=simple_score,
            weighted_score=weighted_score,
            weighted_penalty=screen_weighted_penalty,
            max_penalty=screen_max_penalty,
            proposals_count=len(screen_uxps),
            proposals_by_severity=sev_counts,
        )

        result.screens.append(ss)
        result.total_checks += total_checks
        result.total_pass += counts['pass']
        result.total_gap += counts['gap']
        result.total_unverifiable += counts['unverifiable']

    # Overall scores
    result.simple_score = (
        round(result.total_pass / result.total_checks * 100)
        if result.total_checks > 0 else 0
    )
    result.weighted_score = (
        max(0, round(
            (1 - total_weighted_penalty / total_max_penalty) * 100
        ))
        if total_max_penalty > 0 else 100
    )

    return result


# ═══════════════════════════════════════════════════════════════════════
# STANDALONE CLI
# ═══════════════════════════════════════════════════════════════════════

def _format_table(result: ScoreResult) -> str:
    """Format score results as a readable table."""
    lines = []
    header = (
        f'{"Screen":<35} {"Checks":>6} {"Pass":>5} {"Gap":>5} '
        f'{"Unv.":>5} {"Simple":>7} {"Weighted":>9}'
    )
    sep = f'{"─"*35} {"─"*6} {"─"*5} {"─"*5} {"─"*5} {"─"*7} {"─"*9}'

    lines.append(header)
    lines.append(sep)

    for s in result.screens:
        lines.append(
            f'{s.screen_id:<35} {s.total_checks:>6} {s.pass_count:>5} '
            f'{s.gap_count:>5} {s.unverifiable_count:>5} '
            f'{s.simple_score:>6}% {s.weighted_score:>8}%'
        )

    lines.append(sep)
    lines.append(
        f'{"TOTAL":<35} {result.total_checks:>6} {result.total_pass:>5} '
        f'{result.total_gap:>5} {result.total_unverifiable:>5} '
        f'{result.simple_score:>6}% {result.weighted_score:>8}%'
    )

    if result.discrepancies:
        lines.append('')
        lines.append(f'⚠️  DISCREPANCIES ({len(result.discrepancies)}):')
        for d in result.discrepancies:
            lines.append(
                f'  {d.screen_id} → {d.field_name}: '
                f'claimed {d.claimed} vs actual {d.actual}'
            )
    else:
        lines.append('✅ No discrepancies — all counts match.')

    return '\n'.join(lines)


def _to_json(result: ScoreResult) -> dict:
    """Convert ScoreResult to JSON-serializable dict."""
    return {
        'simple_score': result.simple_score,
        'weighted_score': result.weighted_score,
        'total_checks': result.total_checks,
        'total_pass': result.total_pass,
        'total_gap': result.total_gap,
        'total_unverifiable': result.total_unverifiable,
        'screens': [asdict(s) for s in result.screens],
        'discrepancies': [asdict(d) for d in result.discrepancies],
    }


def main():
    parser = argparse.ArgumentParser(
        description='UX Score Calculator Engine (Python port)'
    )
    parser.add_argument('--module', type=Path, required=True,
                        help='Module directory containing module-index.json')
    parser.add_argument('--json', action='store_true',
                        help='Output as JSON')
    parser.add_argument('--verbose', action='store_true',
                        help='Verbose per-check breakdown')
    args = parser.parse_args()

    module_dir = args.module.resolve()
    index_path = module_dir / 'module-index.json'

    if not index_path.exists():
        print(f'❌ module-index.json not found in {module_dir}',
              file=sys.stderr)
        sys.exit(1)

    index = json.loads(index_path.read_text(encoding='utf-8'))
    result = calculate_scores(index['screens'], index.get('uxp_blocks', []))

    if args.json:
        print(json.dumps(_to_json(result), ensure_ascii=False, indent=2))
    else:
        print(_format_table(result), file=sys.stderr)
        print(f'\n  Simple Score:   {result.simple_score}%', file=sys.stderr)
        print(f'  Weighted Score: {result.weighted_score}%', file=sys.stderr)


if __name__ == '__main__':
    main()
