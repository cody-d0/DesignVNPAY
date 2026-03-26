#!/usr/bin/env python3
"""
reason_gaps.py — Gap Card Enrichment Pipeline

Enriches gap cards in enriched-data.json with:
  1. Heuristic resolution — maps Unknown tags to official Nielsen/WCAG/Laws
  2. Official citations — clickable source links (nngroup.com, WCAG, etc.)
  3. DDL evidence improvement — contextual DDL component descriptions

Usage:
  python3 reason_gaps.py --report path/to/ux-review-report.md [--force] [--verify]

Reads:
  - enriched-data.json      → existing gap enriched data
  - heuristics_db.json      → offline citation database

Writes:
  - enriched-data.json      → updates gap.enriched with heuristic + sources

Design:
  - No API calls needed (deterministic heuristic matching)
  - Preserves existing impact/hiện_trạng (from enrich.py)
  - Only adds: resolved heuristic_name, heuristic_sources, heuristic_category
  - Graceful: skips gaps that already have resolved heuristics unless --force
"""

import json
import re
import sys
import argparse
from datetime import datetime
from pathlib import Path
from typing import Optional

SCRIPT_DIR = Path(__file__).parent
HEURISTICS_DB_PATH = SCRIPT_DIR / 'heuristics_db.json'

# ── Expanded UXG → Nielsen/WCAG mapping ──
# Maps DDL guideline codes to the most relevant Nielsen heuristic
UXG_TO_NIELSEN = {
    # Visibility of System Status (#1)
    'UXG-12': '1',    # Loading/processing state
    'UXG-165': '1',   # System status visibility
    'UXG-175': '1',   # Loading state / feedback
    'UXG-176': '1',   # Progress indicator
    # Match system & real world (#2)
    'UXG-181': '2',   # Auto-fill labels
    'UXG-183': '2',   # Label naming
    'UXG-197': '2',   # Input labels semantic
    # User control & freedom (#3)
    'UXG-4': '3',     # Cancel option
    'UXG-10': '3',    # Toast guidance / dismissible
    'UXG-044': '3',   # Back/undo support
    'UXG-178': '3',   # Close affordance
    # Consistency & standards (#4)
    'UXG-78': '4',    # Consistency pattern
    'UXG-088': '4',   # Terminology consistency
    'UXG-180': '4',   # Color usage consistency
    'UXG-204': '4',   # Visual hierarchy
    'UXG-243': '4',   # CTA clarity / accessibility
    # Error prevention (#5)
    'UXG-074': '5',   # Form validation
    'UXG-087': '5',   # Real-time validation
    'UXG-112': '5',   # Error prevention
    # Recognition not recall (#6)
    'UXG-061': '6',   # Placeholder/hint text
    'UXG-88': '6',    # Label missing
    # Flexibility & efficiency (#7)
    # Aesthetic & minimalist (#8)
    'UXG-32': '8',    # FAB placement / layout
    'UXG-52': '8',    # Sticky headers / content density
    # Error recovery (#9)
    'UXG-257': '9',   # Inline errors
    # Help & documentation (#10)
}

# Source classification → Nielsen mapping
SOURCE_TO_NIELSEN = {
    'Skill A': '4',         # Component spec → Consistency
    'Skill B': '1',         # Heuristic evaluation → various, default to visibility
    'Skill C': '8',         # Visual inspection → Aesthetic
    'Vision': '8',          # Visual check → Aesthetic
    'Content': '2',         # Content → Match real world
    'DDL comp': '4',        # DDL component → Consistency
    'DDL Law': None,        # UX Law → handled separately
    'Accessibility': None,  # WCAG → handled separately
    'Layout': '8',          # Layout → Aesthetic
    'Interaction': '1',     # Interaction → Visibility
    'Component': '4',       # Component → Consistency
}

# COMP: prefix → typical heuristic
COMP_TO_NIELSEN = {
    'otp-input': '1',       # OTP → System status (countdown, resend)
    'text-input': '9',      # Text input → Error recovery (validation)
    'empty-state': '6',     # Empty state → Recognition
    'countdown-timer': '1', # Timer → System status
    'receipt-preview': '6', # Receipt → Recognition
    'app-header': '4',      # Header → Consistency
    'bottom-sheet': '3',    # Bottom sheet → User control (dismiss)
    'toast': '1',           # Toast → System status
    'button': '4',          # Button → Consistency
}


def load_heuristics_db() -> dict:
    """Load offline heuristic reference database."""
    if not HEURISTICS_DB_PATH.exists():
        print(f'⚠️  heuristics_db.json not found at {HEURISTICS_DB_PATH}', file=sys.stderr)
        return {}
    return json.loads(HEURISTICS_DB_PATH.read_text('utf-8'))


def resolve_gap_heuristic(gap: dict, db: dict) -> Optional[dict]:
    """Resolve a gap's heuristic from source/ref/check fields.
    
    Returns dict with: name, number, sources, category
    """
    ref = gap.get('ref', '')
    source = gap.get('source', '')
    check = gap.get('check', '')
    combined = f'{ref} {source} {check}'.lower()

    nielsen_db = db.get('nielsen', {})
    wcag_db = db.get('wcag', {})
    laws_db = db.get('laws', {})

    # ── Strategy 1: Direct UXG code match ──
    for uxg_code, nielsen_num in UXG_TO_NIELSEN.items():
        if uxg_code.lower() in combined:
            entry = nielsen_db.get(nielsen_num)
            if entry:
                return entry

    # ── Strategy 2: COMP: prefix match ──
    comp_m = re.search(r'COMP:(\w[\w-]+)', ref)
    if comp_m:
        comp_name = comp_m.group(1).lower()
        for comp_prefix, nielsen_num in COMP_TO_NIELSEN.items():
            if comp_prefix in comp_name:
                entry = nielsen_db.get(nielsen_num)
                if entry:
                    return entry

    # ── Strategy 3: Source classification ──
    for src_prefix, nielsen_num in SOURCE_TO_NIELSEN.items():
        if src_prefix.lower() in source.lower() and nielsen_num:
            entry = nielsen_db.get(nielsen_num)
            if entry:
                return entry

    # ── Strategy 4: Laws of UX ──
    for law_key, law_entry in laws_db.items():
        if law_key.lower() in combined or law_entry.get('name', '').lower() in combined:
            return {
                'name': law_entry['name'],
                'desc_en': law_entry['desc'],
                'desc_vi': law_entry['desc'],
                'sources': [{'name': law_entry['name'], 'url': law_entry['url'], 'quote': law_entry['quote']}],
                'id': f'law_{law_key}',
            }

    # ── Strategy 5: Keyword scoring ──
    best_score = 0
    best_entry = None
    for _num, entry in nielsen_db.items():
        keywords = entry.get('keywords', []) + entry.get('keywords_vi', [])
        score = sum(1 for kw in keywords if kw.lower() in combined)
        if score > best_score:
            best_score = score
            best_entry = entry

    if best_entry and best_score >= 2:
        return best_entry

    # ── Strategy 6: Accessibility checks ──
    if any(kw in combined for kw in ['wcag', 'contrast', 'accessibility', 'trợ năng', 'a11y']):
        return {
            'name': 'WCAG 2.2 AA — Accessibility',
            'desc_en': 'Content must meet WCAG 2.2 Level AA success criteria.',
            'desc_vi': 'Nội dung phải đáp ứng tiêu chí WCAG 2.2 Level AA.',
            'sources': [
                {'name': 'W3C WCAG 2.2', 'url': 'https://www.w3.org/TR/WCAG22/', 'quote': 'Web Content Accessibility Guidelines (WCAG) 2.2 covers a wide range of recommendations for making Web content more accessible.'}
            ],
            'id': 'wcag_aa',
        }

    return None


def build_gap_sources(gap: dict, matched: Optional[dict], db: dict) -> list[dict]:
    """Build source links for a gap card."""
    sources = []
    
    if matched:
        sources = list(matched.get('sources', []))

    # Add contextual WCAG sources
    ref = gap.get('ref', '').lower()
    check = gap.get('check', '').lower()
    combined = f'{ref} {check}'
    
    wcag_db = db.get('wcag', {})
    if any(kw in combined for kw in ['error', 'validation', 'inline error']):
        for sc_id in ['3.3.1', '3.3.3']:
            sc = wcag_db.get(sc_id)
            if sc and sc not in sources:
                sources.append({'name': sc['name'], 'url': sc['url'], 'quote': sc['quote']})
    
    if any(kw in combined for kw in ['touch', 'target', 'fitts', '44px', '48px']):
        sc = wcag_db.get('2.5.8')
        if sc:
            sources.append({'name': sc['name'], 'url': sc['url'], 'quote': sc['quote']})

    return sources


def build_heuristic_tag(matched: Optional[dict], gap: dict) -> str:
    """Build a clean, readable heuristic tag label."""
    if matched:
        name = matched.get('name', '')
        if name:
            return name
    
    # Fallback: source-based label
    source = gap.get('source', '')
    ref = gap.get('ref', '')
    
    if 'COMP:' in ref:
        comp_name = ref.split('COMP:')[-1].strip().split(';')[0].strip()
        return f'Thông số DDL — {comp_name}'
    if 'TOKEN:' in ref:
        return 'Tuân thủ Design Token'
    if 'Skill A' in source:
        return 'Đối chiếu thông số thiết kế'
    if 'Skill B' in source:
        return 'Đánh giá Heuristic'
    if 'Skill C' in source:
        return 'Kiểm tra trực quan'
    
    return 'Nguyên tắc UX'


def reason_gap(gap: dict, db: dict) -> dict:
    """Enrich a single gap with heuristic resolution + sources."""
    matched = resolve_gap_heuristic(gap, db)
    sources = build_gap_sources(gap, matched, db)
    tag = build_heuristic_tag(matched, gap)
    
    result = {
        'heuristic_tag': tag,
        'heuristic_name': matched['name'] if matched else '',
        'heuristic_sources': sources,
        'heuristic_category': matched.get('id', 'unknown') if matched else 'unknown',
    }
    
    return result


def verify_gap(gap: dict, idx: int) -> list[str]:
    """Quality check for a gap's enriched data."""
    issues = []
    enr = gap.get('enriched', {})
    
    tag = enr.get('heuristic_tag', '')
    if 'Unknown' in tag or 'Chưa' in tag:
        issues.append(f'Gap #{idx}: heuristic_tag still Unknown: {tag[:50]}')
    
    sources = enr.get('heuristic_sources', [])
    if not sources:
        issues.append(f'Gap #{idx}: no official sources')
    
    if not enr.get('impact'):
        issues.append(f'Gap #{idx}: missing impact text')
    
    return issues


def main():
    parser = argparse.ArgumentParser(description='Gap Card Enrichment Pipeline')
    parser.add_argument('--report', required=True, help='Path to ux-review-report.md')
    parser.add_argument('--force', action='store_true', help='Re-reason all gaps')
    parser.add_argument('--verify', action='store_true', help='Quality check')
    args = parser.parse_args()

    report_path = Path(args.report)
    report_dir = report_path.parent
    enriched_path = report_dir / 'enriched-data.json'

    if not enriched_path.exists():
        print(f'❌ enriched-data.json not found. Run enrich.py first.', file=sys.stderr)
        sys.exit(1)

    # Load data
    db = load_heuristics_db()
    enriched = json.loads(enriched_path.read_text('utf-8'))
    gaps = enriched.get('gaps', [])

    print(f'📚 Heuristics DB: {len(db.get("nielsen", {}))} Nielsen, '
          f'{len(db.get("wcag", {}))} WCAG, '
          f'{len(db.get("laws", {}))} Laws', file=sys.stderr)
    print(f'📋 Gaps to process: {len(gaps)}', file=sys.stderr)

    # Process each gap
    reasoned_count = 0
    skipped_count = 0
    all_issues: list[str] = []

    for i, gap in enumerate(gaps, 1):
        enr = gap.setdefault('enriched', {})

        # Skip if already has resolved heuristic (unless --force)
        existing_tag = enr.get('heuristic_tag', '')
        has_sources = bool(enr.get('heuristic_sources'))
        if not args.force and existing_tag and 'Unknown' not in existing_tag and 'Chưa' not in existing_tag and has_sources:
            skipped_count += 1
            if args.verify:
                all_issues.extend(verify_gap(gap, i))
            continue

        # Reason this gap
        result = reason_gap(gap, db)
        
        # Merge with existing enriched data (preserve impact, hiện_trạng)
        enr.update(result)
        reasoned_count += 1

        if args.verify:
            all_issues.extend(verify_gap(gap, i))

        n_src = len(result.get('heuristic_sources', []))
        tag_short = result['heuristic_tag'][:50]
        status = '✅' if 'Unknown' not in tag_short and n_src > 0 else '⚠️'
        print(f'  {status} Gap #{i}: {tag_short} · {n_src} sources', file=sys.stderr)

    # Save
    enriched['gaps'] = gaps
    enriched['_gap_reasoning_engine'] = 'reason_gaps.py/deterministic'
    enriched['_gap_reasoning_timestamp'] = datetime.now().isoformat()
    enriched_path.write_text(json.dumps(enriched, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f'\n✅ Reasoned: {reasoned_count} gaps, Skipped: {skipped_count}', file=sys.stderr)
    print(f'📁 Saved to: {enriched_path}', file=sys.stderr)

    if args.verify:
        if all_issues:
            print(f'\n⚠️  Quality issues ({len(all_issues)}):', file=sys.stderr)
            for issue in all_issues:
                print(f'  • {issue}', file=sys.stderr)
        else:
            print(f'\n✅ All {len(gaps)} gaps pass quality checks', file=sys.stderr)

    # JSON summary
    summary = {
        'gaps_total': len(gaps),
        'reasoned': reasoned_count,
        'skipped': skipped_count,
        'issues': len(all_issues),
    }
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
