#!/usr/bin/env python3
"""Auto-fix UXP sections in ux-review-report.md files.
Converts EXPANDED/TRA_SOAT/LOGIN/COMPACT patterns to canonical 5-field format.
"""
import re, sys, os
from pathlib import Path

def extract_gap_refs(check_tables_text, uxp_body):
    """Try to find Check # from check tables that relate to this UXP."""
    # Look for "Xem UXP-NNN" references in check tables
    uxp_id_match = re.search(r'UXP-(\d+)', uxp_body[:100])
    if not uxp_id_match:
        return '—'
    uxp_id = f'UXP-{uxp_id_match.group(1)}'
    
    # Find check # that reference this UXP
    refs = []
    for m in re.finditer(r'\|\s*(\d+)\s*\|.*?❌\s*Gap\s*\|.*?' + re.escape(uxp_id), check_tables_text):
        refs.append(f'Check #{m.group(1)}')
    
    if refs:
        return ', '.join(refs)
    
    # Fallback: search for gap rows mentioning similar content
    return '—'

def extract_gap_refs_v2(full_text, uxp_id):
    """Find Check # from gap rows that reference this UXP ID."""
    refs = []
    # Pattern: | N | ... | ❌ Gap | ... UXP-NNN
    for m in re.finditer(r'\|\s*(\d+)\s*\|[^|]*\|[^|]*\|[^|]*\|\s*❌\s*Gap\s*\|[^|]*' + re.escape(uxp_id), full_text):
        refs.append(f'Check #{m.group(1)}')
    
    if not refs:
        # Try simpler pattern
        for line in full_text.split('\n'):
            if uxp_id in line and '❌ Gap' in line:
                num_m = re.match(r'\|\s*(\d+)\s*\|', line)
                if num_m:
                    refs.append(f'Check #{num_m.group(1)}')
    
    return ', '.join(refs) if refs else '—'

def get_field(name, body):
    """Extract field value from table row. Handles both **Field** and plain Field."""
    for n in name.split('|'):
        n = n.strip()
        # Try **bold** field first
        m = re.search(rf'\|\s*\*\*{re.escape(n)}\*\*\s*\|\s*(.+?)\s*\|', body)
        if m:
            return m.group(1).strip()
        # Try plain field (TRA SOAT pattern: | Field | Value |)
        m = re.search(rf'\|\s*{re.escape(n)}\s*\|\s*(.+?)\s*\|', body)
        if m:
            return m.group(1).strip()
    return ''

def summarize_hientrang(body):
    """Extract 1-line summary from Hiện trạng section (multiple formats)."""
    # Pattern 1: **🔍 Hiện trạng** (EXPANDED)
    m = re.search(r'\*\*🔍 Hiện trạng\*\*\s*\n\n(.+?)(?:\n\n|\n>)', body, re.DOTALL)
    if not m:
        # Pattern 2: **Hiện trạng:** (TRA SOAT/LOGIN)
        m = re.search(r'\*\*Hiện trạng:\*\*\s*(.+?)(?:\n\n|\n\*\*)', body, re.DOTALL)
    if m:
        text = m.group(1).strip()
        first = text.split('.')[0].strip()
        if len(first) > 120:
            first = first[:117] + '...'
        return first
    return ''

def extract_proposal(body):
    """Extract proposal from multiple format sources."""
    # Try table field first
    p = get_field('Đề xuất|Giải pháp', body)
    if p:
        return p
    
    # Try ✅ section table (EXPANDED)
    m = re.search(r'\*\*✅ Giải pháp đề xuất\*\*', body)
    if m:
        rows = re.findall(r'\|\s*\d+\s*\|[^|]+\|\s*(.+?)\s*\|', body[m.end():m.end()+1000])
        if rows:
            items = [r.strip() for r in rows[:3]]
            return '; '.join(items)
    
    # Try **Đề xuất:** bullet list (TRA SOAT/LOGIN)
    m = re.search(r'\*\*Đề xuất:\*\*\s*\n((?:\s*-\s*.+\n)+)', body)
    if m:
        bullets = re.findall(r'-\s*(.+)', m.group(1))
        if bullets:
            return '; '.join(b.strip() for b in bullets[:3])
    
    return ''

def convert_uxp_section(full_text):
    """Convert non-canonical UXP section to canonical 5-field format."""
    # Split into before-UXP, UXP section, after-UXP (check tables)
    
    # Find UXP section start (multiple section title variants)
    uxp_section_start = re.search(r'^## Đề xuất cải tiến|^## Đề xuất cải thiện', full_text, re.MULTILINE)
    if not uxp_section_start:
        return full_text, 0
    
    # Find check tables start (## Chi tiết theo màn hình)
    check_start = re.search(r'^## Chi tiết theo màn hình|^## Chi tiết kiểm tra', full_text, re.MULTILINE)
    if not check_start:
        return full_text, 0
    
    before = full_text[:uxp_section_start.start()]
    uxp_section = full_text[uxp_section_start.start():check_start.start()]
    after = full_text[check_start.start():]
    
    # Parse UXP blocks
    parts = re.split(r'####\s+(UXP-\d+)\s*·?\s*(.*)', uxp_section)
    
    if len(parts) < 4:
        return full_text, 0  # No UXPs found
    
    # Check if already canonical (has "Vấn đề" and "Gap ref")
    if '**Vấn đề**' in uxp_section and '**Gap ref**' in uxp_section:
        return full_text, 0  # Already canonical
    
    # Build new UXP section
    new_uxps = []
    i = 1
    count = 0
    while i < len(parts) - 2:
        uxp_id = parts[i].strip()
        sev_raw = parts[i+1].strip()
        body = parts[i+2]
        i += 3
        
        # Clean severity
        sev = 'Minor'
        if 'Critical' in sev_raw or '🔴' in sev_raw:
            sev = 'Critical'
        elif 'Major' in sev_raw or '🟡' in sev_raw:
            sev = 'Major'
        
        # Extract fields — handle all known field name variants
        screen = get_field('Màn hình|Screen', body) or '—'
        ddl = get_field('DDL|DDL Ref|Ref', body) or '—'
        
        # Issue - try multiple sources
        issue = get_field('Vấn đề', body)
        if not issue:
            issue = summarize_hientrang(body)
        if not issue:
            issue = get_field('Hiện trạng|Hiện tại|Tác động', body)
        if not issue:
            # Try bold title after UXP header (TRA SOAT pattern)
            title_m = re.match(r'\s*\n\*\*(.+?)\*\*', body)
            if title_m:
                issue = title_m.group(1).strip()
        if not issue:
            # Get first non-table line
            lines = [l.strip() for l in body.split('\n') if l.strip() and not l.startswith('|') and not l.startswith('---') and not l.startswith('>') and not l.startswith('**')]
            if lines:
                issue = lines[0][:120]
        if not issue:
            issue = f'{uxp_id} finding'
        
        # Proposal
        proposal = extract_proposal(body)
        if not proposal:
            proposal = '—'
        if len(proposal) > 150:
            proposal = proposal[:147] + '...'
        
        # Gap ref - cross-reference check tables
        gap_ref = extract_gap_refs_v2(after, uxp_id)
        
        # Heuristic → merge into DDL if present
        heuristic = get_field('Heuristic', body)
        ux_law = get_field('UX Law', body)
        if ux_law and ux_law != '—':
            ddl = f'{ddl} · Law:{ux_law}'
        
        new_uxps.append(f"""#### {uxp_id} · {sev}
| **Màn hình** | {screen} |
|:---|:---|
| **Vấn đề** | {issue} |
| **Gap ref** | {gap_ref} |
| **DDL** | {ddl} |
| **Giải pháp** | {proposal} |

---
""")
        count += 1
    
    new_section = "## Đề xuất cải tiến (Priority)\n\n" + "\n".join(new_uxps) + "\n"
    return before + new_section + after, count

def process_file(filepath):
    """Process a single ux-review-report.md file."""
    text = Path(filepath).read_text(encoding='utf-8')
    new_text, count = convert_uxp_section(text)
    if count > 0:
        Path(filepath).write_text(new_text, encoding='utf-8')
        print(f'  ✅ Fixed {count} UXPs → canonical 5-field')
    else:
        print(f'  ⏭️  Skipped (already canonical or no UXPs)')
    return count

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 fix_uxp_format.py <path-to-ux-review-report.md>')
        print('       python3 fix_uxp_format.py --batch <base-dir>')
        sys.exit(1)
    
    if sys.argv[1] == '--batch':
        base = Path(sys.argv[2])
        total = 0
        files = sorted(base.rglob('ux-review-report.md'))
        for f in files:
            print(f'📄 {f.relative_to(base)}')
            total += process_file(f)
        print(f'\n✅ Total: {total} UXPs fixed across {len(files)} files')
    else:
        filepath = sys.argv[1]
        print(f'📄 {filepath}')
        process_file(filepath)
