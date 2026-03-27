#!/usr/bin/env python3
"""
enrich_refs.py — Enrich report-data.json with reference citations and DDL evidence.

Merges:
  1. enriched-data.json → heuristic names, impact narratives, heuristic_sources
  2. references/official-urls.md → canonical Nielsen/WCAG/Laws URLs + quotes
  3. handoff/ddl-context.json → DDL component/guideline refs

Writes enriched fields back into report-data.json (in place, idempotent).

Usage:
  python3 enrich_refs.py --module path/to/module/
  python3 enrich_refs.py --base path/to/final/
  python3 enrich_refs.py --base path/to/final/ --dry-run
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


# ── Official References Database ────────────────────────────────────────────

_REFS_FILE = Path(__file__).parent.parent / 'references' / 'official-urls.md'


def _load_official_refs() -> dict[str, dict]:
    """Parse references/official-urls.md into lookup by heuristic pattern.

    Returns: { 'nielsen_1': { 'name': ..., 'url': ..., 'quote':... }, ... }
    """
    refs: dict[str, dict] = {}

    if not _REFS_FILE.exists():
        return refs

    content = _REFS_FILE.read_text(encoding='utf-8')

    # Parse Nielsen heuristics table
    for m in re.finditer(
        r'\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(https?://[^|]+?)\s*\|\s*"([^"]+?)"\s*\|',
        content
    ):
        num = m.group(1)
        name = m.group(2).strip()
        url = m.group(3).strip()
        quote = m.group(4).strip()
        refs[f'nielsen_{num}'] = {
            'name': f'Nielsen #{num} — {name}',
            'url': url,
            'quote': quote,
            'source': 'Nielsen Norman Group',
        }

    # Parse WCAG table
    for m in re.finditer(
        r'\|\s*([\d.]+)\s*\|\s*([^|]+?)\s*\|\s*(https?://[^|]+?)\s*\|\s*(\w+)\s*\|',
        content
    ):
        sc = m.group(1).strip()
        name = m.group(2).strip()
        url = m.group(3).strip()
        level = m.group(4).strip()
        key = f'wcag_{sc.replace(".", "_")}'
        refs[key] = {
            'name': f'WCAG {sc} — {name} (Level {level})',
            'url': url,
            'quote': '',
            'source': 'W3C',
        }

    # Parse Laws of UX table
    for m in re.finditer(
        r"\|\s*([^|]+?)'s Law\s*\|\s*(https?://[^|]+?)\s*\|\s*\"([^\"]+?)\"\s*\|",
        content
    ):
        name = m.group(1).strip()
        url = m.group(2).strip()
        quote = m.group(3).strip()
        key = f'law_{name.lower().replace(" ", "_")}'
        refs[key] = {
            'name': f"{name}'s Law",
            'url': url,
            'quote': quote,
            'source': 'Laws of UX',
        }

    # Also match other Laws patterns
    for m in re.finditer(
        r'\|\s*([^|]+?)\s*\|\s*(https://lawsofux\.com/[^|]+?)\s*\|\s*"([^"]+?)"\s*\|',
        content
    ):
        name = m.group(1).strip()
        url = m.group(2).strip()
        quote = m.group(3).strip()
        raw_key = name.lower().replace(' ', '_').replace("'", '').replace('-', '_')
        key = f'law_{raw_key}'
        refs[key] = {
            'name': name,
            'url': url,
            'quote': quote,
            'source': 'Laws of UX',
        }

    return refs


def _match_heuristic_ref(heuristic_text: str, refs_db: dict) -> dict | None:
    """Match a heuristic text to official reference entry."""
    text = heuristic_text.lower()

    # Nielsen match: "Nielsen #N" or "UXG-NNN"
    m = re.search(r'nielsen\s*#?\s*(\d+)', text)
    if m:
        key = f'nielsen_{m.group(1)}'
        return refs_db.get(key)

    # WCAG match: "WCAG X.Y.Z" or "SC X.Y.Z"
    m = re.search(r'(?:wcag|sc)\s*(\d+\.\d+\.\d+)', text)
    if m:
        key = f'wcag_{m.group(1).replace(".", "_")}'
        return refs_db.get(key)

    # Laws match: "Fitts" / "Hick" / "Miller" etc.
    for law_name in ['fitts', 'hick', 'jakob', 'miller', 'peak_end',
                      'zeigarnik', 'von_restorff', 'doherty', 'aesthetic_usability']:
        if law_name.replace('_', '') in text.replace(' ', '').replace("'", ''):
            key = f'law_{law_name}'
            if key in refs_db:
                return refs_db[key]

    return None


# ── Enrichment Engine ───────────────────────────────────────────────────────


def enrich_module(module_dir: Path, refs_db: dict, dry_run: bool = False) -> dict:
    """Enrich report-data.json references for a single module."""
    rd_path = module_dir / 'report-data.json'
    if not rd_path.exists():
        return {'module': module_dir.name, 'error': 'no report-data.json'}

    data = json.loads(rd_path.read_text(encoding='utf-8'))

    # Load enriched-data.json
    ed_path = module_dir / 'enriched-data.json'
    # Build lookup: (screen_id, check_prefix) → enriched data
    # This avoids the num collision: enriched-data uses global nums,
    # report-data uses per-screen nums (both start fresh per screen).
    enriched_gaps_by_key: dict[tuple[str, str], dict] = {}
    enriched_proposals: dict[str, dict] = {}
    if ed_path.exists():
        ed = json.loads(ed_path.read_text(encoding='utf-8'))
        for g in ed.get('gaps', []):
            screen = g.get('screen', '')
            check = g.get('check', '')
            enriched_data = g.get('enriched', {})
            if screen and check and isinstance(enriched_data, dict):
                # Use first 30 chars of check as key (handles truncation)
                key = (screen, check[:30].strip())
                enriched_gaps_by_key[key] = enriched_data
        for p in ed.get('proposals', []):
            pid = p.get('id', '')
            if pid:
                enriched_proposals[pid] = p

    gap_enriched = 0
    uxp_enriched = 0

    # ── Enrich Gaps ──
    for sg in data.get('gaps_by_screen', []):
        scr_id = sg.get('screen_id', '')
        for gap in sg.get('gaps', []):
            changed = False

            # From enriched-data.json — match by (screen_id, title_prefix)
            gap_title = gap.get('title', '')
            match_key = (scr_id, gap_title[:30].strip())
            ed_gap = enriched_gaps_by_key.get(match_key, {})
            if isinstance(ed_gap, dict):
                # Impact narrative
                impact = ed_gap.get('impact', '')
                if impact and not gap.get('_enriched_impact'):
                    if not dry_run:
                        gap['_enriched_impact'] = impact
                    changed = True

                # Heuristic sources
                sources = ed_gap.get('heuristic_sources', [])
                if sources and not gap.get('_enriched_sources'):
                    if not dry_run:
                        gap['_enriched_sources'] = sources
                    changed = True

                # Heuristic name enrichment
                h_name = ed_gap.get('heuristic_name', '')
                if h_name and (not gap.get('heuristic') or len(gap['heuristic']) < 10):
                    if not dry_run:
                        gap['heuristic'] = h_name
                    changed = True

            # From official-urls.md
            heuristic_text = gap.get('heuristic', '') + ' ' + gap.get('ref', '')
            ref_entry = _match_heuristic_ref(heuristic_text, refs_db)
            if ref_entry and not gap.get('_enriched_ref'):
                if not dry_run:
                    gap['_enriched_ref'] = ref_entry
                changed = True

            if changed:
                gap_enriched += 1

    # ── Enrich UXPs ──
    for uxp in data.get('uxps', []):
        uxp_id = uxp.get('id', uxp.get('id_original', ''))
        changed = False

        # From enriched-data proposals
        proposal = enriched_proposals.get(uxp_id, {})
        if proposal:
            # Impact narrative
            narrative = proposal.get('impact_narrative', '')
            if narrative and not uxp.get('_enriched_narrative'):
                if not dry_run:
                    uxp['_enriched_narrative'] = narrative
                changed = True

            # Best practices
            practices = proposal.get('best_practice', [])
            if practices and not uxp.get('_enriched_practices'):
                if not dry_run:
                    uxp['_enriched_practices'] = practices
                changed = True

            # Severity justification
            sev = proposal.get('severity_justification', '')
            if sev and not uxp.get('_enriched_severity'):
                if not dry_run:
                    uxp['_enriched_severity'] = sev
                changed = True

        # From official-urls.md
        heuristic_text = uxp.get('gap_ref', '') + ' ' + uxp.get('ddl_ref', '')
        ref_entry = _match_heuristic_ref(heuristic_text, refs_db)
        if ref_entry and not uxp.get('_enriched_ref'):
            if not dry_run:
                uxp['_enriched_ref'] = ref_entry
            changed = True

        if changed:
            uxp_enriched += 1

    # Write back
    if not dry_run and (gap_enriched > 0 or uxp_enriched > 0):
        data['_ref_enrichment'] = {
            'gap_enriched': gap_enriched,
            'uxp_enriched': uxp_enriched,
            'sources': ['enriched-data.json', 'official-urls.md'],
        }
        rd_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding='utf-8',
        )

    return {
        'module': module_dir.name,
        'gap_enriched': gap_enriched,
        'uxp_enriched': uxp_enriched,
    }


# ── CLI ─────────────────────────────────────────────────────────────────────


def _discover_modules(base_dir: Path) -> list[Path]:
    modules = []
    for root, dirs, files in os.walk(base_dir):
        if 'report-data.json' in files:
            modules.append(Path(root))
    return sorted(modules)


def main():
    parser = argparse.ArgumentParser(
        description='Enrich report-data.json with reference citations'
    )
    parser.add_argument('--module', type=Path, help='Single module directory')
    parser.add_argument('--base', type=Path, help='Base directory (all modules)')
    parser.add_argument('--dry-run', action='store_true', help='Audit only')
    args = parser.parse_args()

    if not args.module and not args.base:
        parser.error('Either --module or --base required')

    # Load official refs database
    refs_db = _load_official_refs()
    print(f'📚 Loaded {len(refs_db)} official references', file=sys.stderr)

    modules = [args.module] if args.module else _discover_modules(args.base)

    total_gap = 0
    total_uxp = 0
    errors = 0

    for module_dir in modules:
        try:
            result = enrich_module(module_dir, refs_db, dry_run=args.dry_run)
            if 'error' in result:
                print(f'  ⚠️  {result["module"]}: {result["error"]}', file=sys.stderr)
                errors += 1
            else:
                gc = result['gap_enriched']
                uc = result['uxp_enriched']
                total_gap += gc
                total_uxp += uc
                if gc or uc:
                    mode = '[DRY-RUN] ' if args.dry_run else ''
                    print(f'  {mode}✅ {result["module"]}: +{gc} gaps, +{uc} UXPs')
        except Exception as e:
            print(f'  ❌ {module_dir.name}: {e}', file=sys.stderr)
            errors += 1

    suffix = ' (dry-run)' if args.dry_run else ''
    print(f'\n{"=" * 60}')
    print(f'✅ Reference enrichment{suffix}: {total_gap} gaps + {total_uxp} UXPs')
    print(f'   Modules: {len(modules)} processed, {errors} errors')


if __name__ == '__main__':
    main()
