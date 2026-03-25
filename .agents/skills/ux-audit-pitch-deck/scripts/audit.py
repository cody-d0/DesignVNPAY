#!/usr/bin/env python3
"""audit.py — Validate pitch deck output quality.

Quick validation of generated HTML for:
1. UXP card structure (4-block: Hiện trạng → Tác động → Heuristic → Đề xuất)
2. Vietnamese coverage (remaining English labels)
3. Image uniqueness
4. Impact text uniqueness
5. Heuristic quality (no generic "Check #N")

Usage:
    python3 audit.py /path/to/pitch-deck.html
    python3 audit.py --base /path/to/project   # audit all pitch decks
"""
import re, sys, argparse, os
from pathlib import Path
from typing import Any


def audit_html(html_path: Path) -> dict[str, Any]:
    """Audit a single pitch deck HTML file."""
    html = html_path.read_text(encoding='utf-8')
    issues: list[str] = []
    stats: dict[str, int] = {}

    # 1. UXP Card Structure
    finding_cards = re.findall(r'<div class="finding-card[\s\S]*?</div>\s*</div>\s*</div>', html)
    n_cards = len(finding_cards)
    n_hien_trang = len(re.findall(r'<h4>Hiện trạng</h4>', html))
    n_tac_dong = len(re.findall(r'<h4>Tác động</h4>', html))
    n_heuristic = len(re.findall(r'<h4>Nguyên tắc bị vi phạm</h4>', html))
    n_de_xuat = len(re.findall(r'<h4>Đề xuất cải thiện</h4>', html))

    stats['uxp_cards'] = n_cards
    stats['hien_trang'] = n_hien_trang
    stats['tac_dong'] = n_tac_dong
    stats['heuristic'] = n_heuristic
    stats['de_xuat'] = n_de_xuat

    if n_hien_trang < n_cards:
        issues.append(f'CARD_STRUCTURE: {n_cards - n_hien_trang} UXP cards missing "Hiện trạng" section')
    if n_tac_dong < n_cards:
        issues.append(f'CARD_STRUCTURE: {n_cards - n_tac_dong} UXP cards missing "Tác động" section')
    if n_heuristic < n_cards:
        issues.append(f'CARD_STRUCTURE: {n_cards - n_heuristic} UXP cards missing "Nguyên tắc bị vi phạm" section')

    # 2. Vietnamese Coverage
    gap_labels = re.findall(r'(?<=gap-label">)[^<]+', html)
    en_labels = [l for l in gap_labels if re.search(r'[A-Z][a-z]{4,}', l) and not re.search(r'DDL|WCAG|ARIA|Nielsen|Fitts|Hick|Zeigarnik|Miller|Jakob|CSS|HTML|Apple|Doherty|Material|Google|Heuristic', l)]
    stats['gap_labels_total'] = len(gap_labels)
    stats['gap_labels_en'] = len(en_labels)
    if en_labels:
        issues.append(f'I18N: {len(en_labels)} gap labels still in English: {list(en_labels[:3])}')  # type: ignore[index]

    # 3. Image Uniqueness (UXP cards specifically)
    # UXP cards: images inside finding-card divs
    finding_cards_raw = re.findall(r'<div class="finding-card[\s\S]*?</div>\s*</div>\s*</div>', html)
    uxp_imgs: list[str] = []
    for fc in finding_cards_raw:
        fc_img = re.search(r'src="ui/([^"]+)"', fc)
        if fc_img:
            uxp_imgs.append(fc_img.group(1))
    unique_uxp_imgs = set(uxp_imgs)

    # All images (UXP + Gap)
    all_imgs = re.findall(r'src="ui/([^"]+)"', html)
    stats['total_img_tags'] = len(all_imgs)
    stats['unique_images'] = len(unique_uxp_imgs)  # Report UXP-specific
    stats['uxp_img_count'] = len(uxp_imgs)
    if len(uxp_imgs) > 0:
        ratio = len(unique_uxp_imgs) / len(uxp_imgs)
        if ratio < 0.5:
            issues.append(f'IMAGE_DIVERSITY: Only {len(unique_uxp_imgs)}/{len(uxp_imgs)} unique images ({ratio:.0%})')

    # 4. Impact Text Uniqueness (in gap cards)
    gap_impacts = re.findall(r'Tác động đến người dùng</div>\s*<div[^>]*>([^<]+)', html)
    impact_counts: dict[str, int] = {}
    for imp in gap_impacts:
        imp_clean = imp.strip()
        impact_counts[imp_clean] = impact_counts.get(imp_clean, 0) + 1
    duplicates = {k: v for k, v in impact_counts.items() if v > 1}
    stats['gap_impacts'] = len(gap_impacts)
    stats['unique_impacts'] = len(impact_counts)
    stats['dup_impacts'] = len(duplicates)
    if duplicates:
        for text, count in list(sorted(duplicates.items(), key=lambda x: -x[1]))[:3]:  # type: ignore[index]
            issues.append(f'DUP_IMPACT: {count}× "{text[:80]}..."')

    # 5. Heuristic Quality
    generic_heur = re.findall(r'Check\s*#\d+', html)
    stats['generic_heuristics'] = len(generic_heur)
    if generic_heur:
        issues.append(f'HEURISTIC: {len(generic_heur)} generic "Check #N" patterns (should use full heuristic names)')

    # 6. Gap card count
    gap_cards = re.findall(r'<div class="gap-card', html)
    stats['gap_cards'] = len(gap_cards)

    return {
        'file': str(html_path),
        'folder': html_path.parent.name,
        'issues': issues,
        'stats': stats,
    }


def print_report(result: dict, verbose: bool = False):
    """Print audit report for a single file."""
    folder = result['folder']
    stats = result['stats']
    issues = result['issues']

    icon = '✅' if not issues else '⚠️'
    n_uxp = stats.get('uxp_cards', 0)
    n_gaps = stats.get('gap_cards', 0)

    print(f'  {icon} {folder:<45} {n_uxp} UXP, {n_gaps} gaps')

    if verbose or issues:
        # Card structure
        print(f'      📊 Cards: {stats["hien_trang"]}× Hiện trạng, {stats["tac_dong"]}× Tác động, '
              f'{stats["heuristic"]}× Heuristic, {stats["de_xuat"]}× Đề xuất')
        # Image stats
        print(f'      🖼️  Images: {stats["total_img_tags"]} tags, {stats["unique_images"]} unique')
        # Impact stats
        print(f'      📝 Impacts: {stats["gap_impacts"]} total, {stats["unique_impacts"]} unique, {stats["dup_impacts"]} duplicated')
        # Generic heuristics
        if stats['generic_heuristics'] > 0:
            print(f'      ⚠️  Generic "Check #N": {stats["generic_heuristics"]}')
        # English labels
        if stats['gap_labels_en'] > 0:
            print(f'      🌐 English labels: {stats["gap_labels_en"]}/{stats["gap_labels_total"]}')

    if issues:
        for iss in issues:
            print(f'      ❌ {iss}')


def main():
    parser = argparse.ArgumentParser(description='Validate pitch deck HTML output quality')
    parser.add_argument('file', nargs='?', help='Single HTML file to audit')
    parser.add_argument('--base', help='Base directory to find all pitch-deck HTML files')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed stats even for passing files')
    args = parser.parse_args()

    files: list[Path] = []
    if args.file:
        files = [Path(args.file)]
    elif args.base:
        for root, dirs, fnames in os.walk(args.base):
            for f in fnames:
                if 'pitch-deck' in f and f.endswith('.html'):
                    files.append(Path(root) / f)
        files.sort()
    else:
        parser.error('Specify either a file or --base directory')

    print(f'\n🔍 AUDIT — {len(files)} pitch deck(s)\n')

    total_issues = 0
    total_uxp = 0
    total_gaps = 0
    total_dup = 0

    for f in files:
        result = audit_html(f)
        print_report(result, verbose=args.verbose)
        total_issues += len(result['issues'])
        total_uxp += result['stats'].get('uxp_cards', 0)
        total_gaps += result['stats'].get('gap_cards', 0)
        total_dup += result['stats'].get('dup_impacts', 0)

    print(f'\n{"=" * 60}')
    print(f'Total: {total_uxp} UXP cards, {total_gaps} gap cards')
    print(f'Issues: {total_issues}')
    print(f'Impact duplicates: {total_dup}')
    if total_issues == 0:
        print('🎉 All pitch decks pass validation!')
    else:
        print(f'⚠️  {total_issues} issues found — review above')


if __name__ == '__main__':
    main()
