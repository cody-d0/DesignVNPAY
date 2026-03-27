#!/usr/bin/env python3
"""
enrich_images.py — Enrich report-data.json with better image assignments.

Merges artboard-index.json and Screen MDs into the scoring pipeline:
  1. Read report-data.json (baseline from convert_report.py)
  2. Build enriched artboard index from artboard-index.json (roles + text)
  3. Parse Screen MD variant tables for semantic descriptions
  4. Re-score UXP and Gap screenshot_path using enriched data
  5. Write back report-data.json (in place, idempotent)

Usage:
  python3 enrich_images.py --module path/to/module/
  python3 enrich_images.py --base path/to/final/
  python3 enrich_images.py --base path/to/final/ --dry-run
"""

import argparse
import json
import os
import re
import sys
import unicodedata
from pathlib import Path


def _strip_vn(text: str) -> str:
    """Normalize Vietnamese text: strip diacritics, lowercase."""
    nfkd = unicodedata.normalize('NFKD', text.lower())
    return ''.join(c for c in nfkd if not unicodedata.combining(c))


# ── Artboard Index ──────────────────────────────────────────────────────────


def _load_artboard_index(module_dir: Path) -> dict[str, dict]:
    """Load artboard-index.json and build enriched lookup.

    Returns: { screen_id: { filename: { role, texts, name } } }
    """
    ai_path = module_dir / 'artboard-index.json'
    if not ai_path.exists():
        return {}

    raw = json.loads(ai_path.read_text(encoding='utf-8'))
    index: dict[str, dict] = {}

    for scr_key, scr_data in raw.items():
        if not isinstance(scr_data, dict):
            continue
        artboards = scr_data.get('artboards', {})
        if not artboards:
            continue

        # Normalize screen key → canonical SCR-xxx-NNN
        scr_id = scr_key
        # Handle keys like "SCR-KHT-001-nhap-thong-tin-the" → "SCR-KHT-001"
        m = re.match(r'(SCR-\w+-\d+)', scr_key)
        if m:
            scr_id = m.group(1)

        if scr_id not in index:
            index[scr_id] = {}

        for ab_fn, ab_data in artboards.items():
            if not isinstance(ab_data, dict):
                continue
            index[scr_id][ab_fn] = {
                'role': ab_data.get('role', ''),
                'texts': ab_data.get('text_elements', []),
                'name': ab_data.get('artboard_name', ''),
            }

    return index


# ── Screen MD Variants ──────────────────────────────────────────────────────


def _parse_screen_md_variants(module_dir: Path) -> dict[str, dict[str, str]]:
    """Parse SCR-*.md files for variant table descriptions.

    Returns: { screen_id: { filename: description } }
    """
    variants: dict[str, dict[str, str]] = {}

    for md_file in module_dir.glob('SCR-*.md'):
        content = md_file.read_text(encoding='utf-8')

        # Extract SCR-ID
        m = re.search(r'(SCR-\w+-\d+)', content[:300])
        if not m:
            continue
        scr_id = m.group(1)

        if scr_id not in variants:
            variants[scr_id] = {}

        # Parse variant tables: | # | Variant | Ảnh | Mô tả |
        # Image refs look like: ![alt](ui/filename.png)
        for match in re.finditer(
            r'\|\s*\d+\s*\|([^|]+)\|[^|]*!\[[^\]]*\]\(ui/([^)]+\.png)\)[^|]*\|([^|]*)\|',
            content
        ):
            variant_name = match.group(1).strip()
            filename = match.group(2).strip()
            description = match.group(3).strip()
            variants[scr_id][filename] = f'{variant_name}: {description}'

    return variants


# ── Enriched Scoring ────────────────────────────────────────────────────────


def _score_enriched(
    images: list[dict],
    context: str,
    ai_screen: dict[str, dict],
    md_variants: dict[str, str],
) -> str:
    """Score images using enriched artboard index + Screen MD data.

    Scoring layers:
      A. Role keyword match (from artboard-index roles) → +5
      B. Artboard text_elements overlap with context → +3/word
      C. MD variant description overlap → +2/word
      D. Filename keyword match → +1/word
      E. State-aware bonus → +3

    Returns best-scoring filename, or '' if no images.
    """
    if not images:
        return ''
    if len(images) == 1:
        return images[0]

    context_lower = context.lower()
    context_norm = _strip_vn(context)
    context_words = set(w for w in context_norm.split() if len(w) > 2)

    _is_error_ctx = any(kw in context_lower for kw in
        ['lỗi', 'error', 'invalid', 'thiếu', 'missing', 'validation',
         'inline error', 'fail', 'chưa', 'sai', 'trống'])
    _is_overlay_ctx = any(kw in context_lower for kw in
        ['overlay', 'popup', 'modal', 'bottom sheet', 'dialog', 'otp',
         'xác nhận', 'confirm', 'thông báo'])
    _is_success_ctx = any(kw in context_lower for kw in
        ['thành công', 'success', 'hoàn tất', 'kết quả'])

    scores: dict[str, int] = {}

    for fn in images:
        score = 0
        ai_data = ai_screen.get(fn, {})
        role = ai_data.get('role', '')
        texts = ai_data.get('texts', [])

        # A: Role keyword match
        if role:
            if _is_error_ctx and ('error' in role or role.startswith('overlay_error')):
                score += 5
            elif _is_overlay_ctx and ('overlay' in role or 'otp' in role):
                score += 5
            elif _is_success_ctx and ('success' in role):
                score += 5
            elif 'primary_form' in role and not _is_error_ctx:
                score += 3

        # B: Artboard text_elements overlap
        if texts and context_words:
            text_norm = set()
            for t in texts:
                text_norm.update(w for w in _strip_vn(t).split() if len(w) > 2)
            overlap = len(context_words & text_norm)
            score += overlap * 3

        # C: MD variant description overlap
        md_desc = md_variants.get(fn, '')
        if md_desc and context_words:
            md_norm = set(w for w in _strip_vn(md_desc).split() if len(w) > 2)
            overlap = len(context_words & md_norm)
            score += overlap * 2

        # D: Filename keyword match
        fn_norm = _strip_vn(fn.replace('.png', '').replace('-', ' ').replace('_', ' '))
        fn_words = set(w for w in fn_norm.split() if len(w) > 2)
        if fn_words and context_words:
            score += len(context_words & fn_words)

        # E: State-aware bonus
        if _is_error_ctx and ('error' in role or 'loi' in fn.lower() or 'case-loi' in fn.lower()):
            score += 3
        if _is_overlay_ctx and 'overlay' in role:
            score += 2
        if role == 'entry_point' and not any(kw in context_lower for kw in ['danh sách', 'list', 'entry']):
            score -= 2

        scores[fn] = score

    if scores:
        best = max(scores, key=lambda k: scores[k])
        if scores[best] >= 2:
            return best

    return ''  # No confident match


# ── Enrichment Engine ───────────────────────────────────────────────────────


def enrich_module(module_dir: Path, dry_run: bool = False) -> dict:
    """Enrich report-data.json images for a single module.

    Returns: { 'uxp_changed': N, 'gap_changed': N, 'module': str }
    """
    rd_path = module_dir / 'report-data.json'
    if not rd_path.exists():
        return {'module': module_dir.name, 'error': 'no report-data.json'}

    data = json.loads(rd_path.read_text(encoding='utf-8'))

    # Load enrichment sources
    ai_index = _load_artboard_index(module_dir)
    md_variants = _parse_screen_md_variants(module_dir)

    # Available UI files
    ui_dir = module_dir / 'ui'
    available = {f.name for f in ui_dir.glob('*.png')} if ui_dir.exists() else set()

    uxp_changed = 0
    gap_changed = 0

    # ── Enrich UXP images ──
    for uxp in data.get('uxps', []):
        screen_tag = uxp.get('screen_tag', '')
        # Resolve screen tag to SCR-ID
        scr_id = ''
        m = re.search(r'(SCR-\w+-\d+)', screen_tag)
        if m:
            scr_id = m.group(1)

        if scr_id not in ai_index:
            continue

        # Build context from UXP fields
        context = ' '.join(filter(None, [
            uxp.get('problem', ''),
            uxp.get('solution', ''),
            uxp.get('gap_ref', ''),
        ]))

        ai_screen = ai_index[scr_id]
        md_v = md_variants.get(scr_id, {})
        candidates = [fn for fn in ai_screen.keys() if fn in available]

        if len(candidates) <= 1:
            continue

        best = _score_enriched(candidates, context, ai_screen, md_v)
        if best:
            new_path = f'ui/{best}'
            old_path = uxp.get('screenshot_path', '')
            if new_path != old_path:
                if not dry_run:
                    uxp['screenshot_path'] = new_path
                    uxp['_img_enriched_from'] = old_path
                uxp_changed += 1

    # ── Enrich Gap images (greedy-aware: maximize diversity) ──
    for sg in data.get('gaps_by_screen', []):
        scr_id = sg.get('screen_id', '')
        if scr_id not in ai_index:
            continue

        ai_screen = ai_index[scr_id]
        md_v = md_variants.get(scr_id, {})
        candidates = [fn for fn in ai_screen.keys() if fn in available]

        if len(candidates) <= 1:
            continue

        gaps = sg.get('gaps', [])
        if not gaps:
            continue

        # Build full score matrix: gap × image (greedy-aware)
        gap_scores: list[list[tuple[str, int]]] = []
        for gap in gaps:
            context = ' '.join(filter(None, [
                gap.get('title', ''),
                gap.get('evidence', ''),
                gap.get('heuristic', ''),
                gap.get('ref', ''),
            ]))
            context_lower = context.lower()
            context_norm = _strip_vn(context)
            context_words = set(w for w in context_norm.split() if len(w) > 2)

            _is_error_ctx = any(kw in context_lower for kw in
                ['lỗi', 'error', 'invalid', 'thiếu', 'missing', 'validation',
                 'inline error', 'fail', 'chưa', 'sai', 'trống'])
            _is_overlay_ctx = any(kw in context_lower for kw in
                ['overlay', 'popup', 'modal', 'bottom sheet', 'dialog', 'otp',
                 'xác nhận', 'confirm', 'thông báo'])
            _is_success_ctx = any(kw in context_lower for kw in
                ['thành công', 'success', 'hoàn tất', 'kết quả'])

            img_scores: list[tuple[str, int]] = []
            for fn in candidates:
                score = 0
                ai_data = ai_screen.get(fn, {})
                role = ai_data.get('role', '')
                texts = ai_data.get('texts', [])

                # A: Role keyword match
                if role:
                    if _is_error_ctx and ('error' in role or role.startswith('overlay_error')):
                        score += 5
                    elif _is_overlay_ctx and ('overlay' in role or 'otp' in role):
                        score += 5
                    elif _is_success_ctx and ('success' in role):
                        score += 5
                    elif 'primary_form' in role and not _is_error_ctx:
                        score += 3

                # B: Artboard text_elements overlap
                if texts and context_words:
                    text_norm = set()
                    for t in texts:
                        text_norm.update(w for w in _strip_vn(t).split() if len(w) > 2)
                    score += len(context_words & text_norm) * 3

                # C: MD variant description overlap
                md_desc = md_v.get(fn, '')
                if md_desc and context_words:
                    md_norm = set(w for w in _strip_vn(md_desc).split() if len(w) > 2)
                    score += len(context_words & md_norm) * 2

                # D: Filename keyword match
                fn_norm = _strip_vn(fn.replace('.png', '').replace('-', ' ').replace('_', ' '))
                fn_words = set(w for w in fn_norm.split() if len(w) > 2)
                if fn_words and context_words:
                    score += len(context_words & fn_words)

                # E: State-aware bonus
                if _is_error_ctx and ('error' in role or 'loi' in fn.lower() or 'case-loi' in fn.lower()):
                    score += 3
                if _is_overlay_ctx and 'overlay' in role:
                    score += 2
                if role == 'entry_point' and not any(kw in context_lower for kw in ['danh sách', 'list', 'entry']):
                    score -= 2

                img_scores.append((fn, score))
            gap_scores.append(sorted(img_scores, key=lambda x: -x[1]))

        # Greedy allocation: maximize unique image utilization
        assigned_images: set[str] = set()
        assignments: list[str] = [''] * len(gaps)

        # Round 1: Give each gap its top-scoring UNUSED image
        for i, scores_list in enumerate(gap_scores):
            for fn, sc in scores_list:
                if fn not in assigned_images:
                    assignments[i] = fn
                    assigned_images.add(fn)
                    break

        # Round 2: Fill any gaps that couldn't get a unique image
        for i in range(len(assignments)):
            if not assignments[i] and gap_scores[i]:
                assignments[i] = gap_scores[i][0][0]

        # Round 3: Redistribute duplicates to unused candidates
        still_unused = set(candidates) - assigned_images
        if still_unused:
            img_count: dict[str, list[int]] = {}
            for i, fn in enumerate(assignments):
                img_count.setdefault(fn, []).append(i)
            for fn, indices in img_count.items():
                if len(indices) > 1 and still_unused:
                    for idx in indices[1:]:
                        if still_unused:
                            best_unused = None
                            best_sc = -999
                            for ufn, usc in gap_scores[idx]:
                                if ufn in still_unused and usc > best_sc:
                                    best_unused = ufn
                                    best_sc = usc
                            if best_unused:
                                assignments[idx] = best_unused
                                still_unused.discard(best_unused)

        # Apply assignments — only change if genuinely better
        for i, gap in enumerate(gaps):
            if assignments[i]:
                new_path = f'ui/{assignments[i]}'
                old_path = gap.get('screenshot_path', '')
                if new_path != old_path:
                    if not dry_run:
                        gap['screenshot_path'] = new_path
                        gap['_img_enriched_from'] = old_path
                    gap_changed += 1

    # Write back
    if not dry_run and (uxp_changed > 0 or gap_changed > 0):
        # Add enrichment metadata
        data['_image_enrichment'] = {
            'uxp_changed': uxp_changed,
            'gap_changed': gap_changed,
            'sources': ['artboard-index.json', 'SCR-*.md'],
        }
        rd_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding='utf-8',
        )

    return {
        'module': module_dir.name,
        'uxp_changed': uxp_changed,
        'gap_changed': gap_changed,
    }


# ── CLI ─────────────────────────────────────────────────────────────────────


def _discover_modules(base_dir: Path) -> list[Path]:
    """Find all module directories containing report-data.json."""
    modules = []
    for root, dirs, files in os.walk(base_dir):
        if 'report-data.json' in files:
            modules.append(Path(root))
    return sorted(modules)


def main():
    parser = argparse.ArgumentParser(
        description='Enrich report-data.json image assignments'
    )
    parser.add_argument('--module', type=Path, help='Single module directory')
    parser.add_argument('--base', type=Path, help='Base directory (all modules)')
    parser.add_argument('--dry-run', action='store_true', help='Audit only, no writes')
    args = parser.parse_args()

    if not args.module and not args.base:
        parser.error('Either --module or --base required')

    modules = [args.module] if args.module else _discover_modules(args.base)

    total_uxp = 0
    total_gap = 0
    errors = 0

    for module_dir in modules:
        try:
            result = enrich_module(module_dir, dry_run=args.dry_run)
            if 'error' in result:
                print(f'  ⚠️  {result["module"]}: {result["error"]}', file=sys.stderr)
                errors += 1
            else:
                uc = result['uxp_changed']
                gc = result['gap_changed']
                total_uxp += uc
                total_gap += gc
                if uc or gc:
                    mode = '[DRY-RUN] ' if args.dry_run else ''
                    print(f'  {mode}✅ {result["module"]}: +{uc} UXP, +{gc} gap images')
        except Exception as e:
            print(f'  ❌ {module_dir.name}: {e}', file=sys.stderr)
            errors += 1

    suffix = ' (dry-run)' if args.dry_run else ''
    print(f'\n{"=" * 60}')
    print(f'✅ Image enrichment{suffix}: {total_uxp} UXP + {total_gap} gap changes')
    print(f'   Modules: {len(modules)} processed, {errors} errors')


if __name__ == '__main__':
    main()
