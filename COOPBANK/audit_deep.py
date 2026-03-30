#!/usr/bin/env python3
"""Deep audit: categorize exact issues for UXP and Gap items separately."""
import json, os, glob, re
from collections import Counter, defaultdict

BASE = "/Users/dataism/Documents/UXtool/COOPBANK/final"
os.chdir(BASE)

full_en = re.compile(r"^[A-Za-z0-9\s\-\.\,\(\)\:\;\!\?\'\"\#\/\—\–\@\&\%\+\=\[\]\{\}\*\>\<\~\|\`\_]+$")

modules = sorted(glob.glob("*/llm-enriched.json"))

uxp_issues = []
gap_issues = []
uxp_ok = 0
gap_ok = 0

for m in modules:
    data = json.load(open(m))
    mod_name = os.path.dirname(m)
    for item in data:
        item_id = item.get("id", "?")
        is_gap = item_id.startswith("Gap")
        issues_list = gap_issues if is_gap else uxp_issues
        item_has_issue = False

        for field in ["hiện_trạng", "tác_động", "nguyên_tắc"]:
            val = item.get(field, "")
            if not val or len(val.strip()) < 5:
                issues_list.append((mod_name, item_id, field, "EMPTY", ""))
                item_has_issue = True
                continue
            # Check for English-only sentences
            sentences = [s.strip() for s in re.split(r'[.;]\s+', val) if len(s.strip()) > 25]
            for sent in sentences:
                if full_en.match(sent):
                    issues_list.append((mod_name, item_id, field, "EN_SENTENCE", sent[:90]))
                    item_has_issue = True

        steps = item.get("đề_xuất_steps", [])
        if not steps:
            issues_list.append((mod_name, item_id, "đề_xuất_steps", "EMPTY", ""))
            item_has_issue = True
        for i, step in enumerate(steps):
            if isinstance(step, str) and full_en.match(step.strip()) and len(step) > 20:
                issues_list.append((mod_name, item_id, f"step[{i}]", "EN_STEP", step[:90]))
                item_has_issue = True

        refs = item.get("references", [])
        if not refs:
            issues_list.append((mod_name, item_id, "references", "NO_REFS", ""))
            item_has_issue = True

        if not item_has_issue:
            if is_gap:
                gap_ok += 1
            else:
                uxp_ok += 1

# ── REPORT ──
total_uxp = 247
total_gap = 656 - 247  # 409

print("=" * 80)
print("DEEP AUDIT: UXP vs GAP LOCALIZATION & ENRICHMENT")
print("=" * 80)

print(f"\n{'Category':<20} {'Total':<10} {'OK':<10} {'With Issues':<15} {'Issue Count':<15}")
print("-" * 70)
print(f"{'UXP':<20} {total_uxp:<10} {uxp_ok:<10} {total_uxp - uxp_ok:<15} {len(uxp_issues):<15}")
print(f"{'Gap':<20} {total_gap:<10} {gap_ok:<10} {total_gap - gap_ok:<15} {len(gap_issues):<15}")
print(f"{'TOTAL':<20} {total_uxp+total_gap:<10} {uxp_ok+gap_ok:<10} {(total_uxp-uxp_ok)+(total_gap-gap_ok):<15} {len(uxp_issues)+len(gap_issues):<15}")

for label, issues, total in [("UXP", uxp_issues, total_uxp), ("Gap", gap_issues, total_gap)]:
    print(f"\n{'='*80}")
    print(f"{label} ISSUE BREAKDOWN ({total} items, {len(issues)} issues)")
    print(f"{'='*80}")

    type_counts = Counter(i[3] for i in issues)
    for t, c in type_counts.most_common():
        print(f"  {t:20s}: {c:4d}")

    # Group by module
    mod_counts = Counter(i[0] for i in issues)
    print(f"\n  Top modules by issue count:")
    for mod, c in mod_counts.most_common(10):
        print(f"    {mod:45s}: {c:3d} issues")

# ── SPECIFIC PATTERNS ──
print(f"\n{'='*80}")
print("PATTERN ANALYSIS: What English content remains?")
print(f"{'='*80}")

# Collect unique EN patterns
all_en = [(i[0], i[1], i[2], i[4]) for i in uxp_issues + gap_issues if i[3] in ("EN_SENTENCE", "EN_STEP")]
print(f"\nTotal English content fragments: {len(all_en)}")

# Categorize EN content
technical_terms = 0
full_sentences = 0
mixed = 0
for _, _, _, text in all_en:
    words = text.split()
    if len(words) <= 6:
        technical_terms += 1
    elif any(vn in text.lower() for vn in ["cho", "khi", "của", "với", "và", "không", "tại", "này"]):
        mixed += 1
    else:
        full_sentences += 1

print(f"  Short technical terms (<=6 words): {technical_terms}")
print(f"  Mixed VN+EN sentences:             {mixed}")
print(f"  Full English sentences:            {full_sentences}")

# Show full EN sentence samples
full_en_samples = [(i[0], i[1], i[2], i[4]) for i in uxp_issues + gap_issues 
                   if i[3] in ("EN_SENTENCE", "EN_STEP")
                   and not any(vn in i[4].lower() for vn in ["cho", "khi", "của", "với", "và", "không", "tại", "này", "trong", "hoặc"])
                   and len(i[4].split()) > 6]

print(f"\n--- FULL ENGLISH SENTENCES (need translation): {len(full_en_samples)} ---")
for mod, iid, field, text in full_en_samples[:25]:
    print(f"  {mod[:35]:35s} | {iid[:15]:15s} | {field:12s} | {text[:55]}")

# ── EMPTY FIELDS ──
empty_items = [i for i in uxp_issues + gap_issues if i[3] == "EMPTY"]
print(f"\n--- EMPTY FIELDS: {len(empty_items)} ---")
field_counts = Counter(i[2] for i in empty_items)
for f, c in field_counts.most_common():
    print(f"  {f:20s}: {c}")

# ── NO REFERENCES ──
no_refs = [i for i in uxp_issues + gap_issues if i[3] == "NO_REFS"]
print(f"\n--- NO REFERENCES: {len(no_refs)} ---")
# Count by type
uxp_no_refs = sum(1 for i in uxp_issues if i[3] == "NO_REFS")
gap_no_refs = sum(1 for i in gap_issues if i[3] == "NO_REFS")
print(f"  UXP without references: {uxp_no_refs}")
print(f"  Gap without references: {gap_no_refs}")
