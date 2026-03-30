#!/usr/bin/env python3
"""Audit localization & enrichment status for all UXP + GAP items."""
import json, os, glob, re
from collections import Counter

BASE = "/Users/dataism/Documents/UXtool/COOPBANK/final"
os.chdir(BASE)

# ── 1. UXP ANALYSIS (from llm-enriched.json) ──
print("=" * 70)
print("PART 1: UXP LOCALIZATION AUDIT (llm-enriched.json)")
print("=" * 70)

modules = sorted(glob.glob("*/llm-enriched.json"))
full_en = re.compile(r"^[A-Za-z0-9\s\-\.\,\(\)\:\;\!\?\'\"\#\/\—\–\@\&\%\+\=\[\]\{\}\*\>\<]+$")

uxp_issues = []
total_uxp = 0

for m in modules:
    data = json.load(open(m))
    mod_name = os.path.dirname(m)
    for item in data:
        total_uxp += 1
        item_id = item.get("id", "?")

        # Check each Vietnamese field
        for field in ["hiện_trạng", "tác_động", "nguyên_tắc"]:
            val = item.get(field, "")
            if not val or len(val.strip()) < 5:
                uxp_issues.append((mod_name, item_id, field, "EMPTY", ""))
                continue

            # Check if entire value looks English
            sentences = [s.strip() for s in val.split(". ") if len(s.strip()) > 20]
            for sent in sentences:
                if full_en.match(sent):
                    uxp_issues.append((mod_name, item_id, field, "EN_SENTENCE", sent[:80]))

        # Check đề_xuất_steps
        steps = item.get("đề_xuất_steps", [])
        if not steps:
            uxp_issues.append((mod_name, item_id, "đề_xuất_steps", "EMPTY", ""))
        for i, step in enumerate(steps):
            if isinstance(step, str) and full_en.match(step.strip()) and len(step) > 20:
                uxp_issues.append((mod_name, item_id, f"đề_xuất_steps[{i}]", "EN_STEP", step[:80]))

        # Check references
        refs = item.get("references", [])
        if not refs:
            uxp_issues.append((mod_name, item_id, "references", "NO_REFS", ""))

print(f"\nTotal UXPs scanned: {total_uxp}")
print(f"Total issues found: {len(uxp_issues)}")

type_counts = Counter(i[3] for i in uxp_issues)
print("\nBy type:")
for t, c in type_counts.most_common():
    print(f"  {t:20s}: {c}")

# Show sample EN sentences
en_sents = [i for i in uxp_issues if i[3] == "EN_SENTENCE"]
if en_sents:
    print(f"\n--- EN_SENTENCE samples (showing {min(20, len(en_sents))}) ---")
    for mod, iid, field, itype, sample in en_sents[:20]:
        print(f"  {mod[:40]:40s} | {iid:8s} | {field:12s} | {sample[:60]}")

en_steps = [i for i in uxp_issues if i[3] == "EN_STEP"]
if en_steps:
    print(f"\n--- EN_STEP samples (showing {min(20, len(en_steps))}) ---")
    for mod, iid, field, itype, sample in en_steps[:20]:
        print(f"  {mod[:40]:40s} | {iid:8s} | {field:20s} | {sample[:60]}")

empty_items = [i for i in uxp_issues if i[3] == "EMPTY"]
if empty_items:
    print(f"\n--- EMPTY fields (showing {min(10, len(empty_items))}) ---")
    for mod, iid, field, itype, sample in empty_items[:10]:
        print(f"  {mod[:40]:40s} | {iid:8s} | {field}")

# ── 2. GAP ANALYSIS (from report-data.json) ──
print("\n" + "=" * 70)
print("PART 2: GAP ENRICHMENT AUDIT (report-data.json)")
print("=" * 70)

modules2 = sorted(glob.glob("*/report-data.json"))
total_gaps = 0
gap_issues = []

for m in modules2:
    data = json.load(open(m))
    mod_name = os.path.dirname(m)
    for screen in data.get("gaps_by_screen", []):
        for gap in screen.get("gaps", []):
            total_gaps += 1
            num = gap.get("num", "?")
            gid = f"GAP#{num}"
            title = gap.get("title", "")
            impact = gap.get("user_impact", "")
            ref = gap.get("ref", "")
            severity = gap.get("severity", "")

            # Title in English?
            if title and full_en.match(title.strip()) and len(title) > 5:
                gap_issues.append((mod_name, gid, "title", "EN_TITLE", title[:80]))

            # user_impact empty?
            if not impact or len(impact.strip()) < 10:
                gap_issues.append((mod_name, gid, "user_impact", "EMPTY_IMPACT", ""))
            elif full_en.match(impact[:60].strip()):
                gap_issues.append((mod_name, gid, "user_impact", "EN_IMPACT", impact[:80]))

            # ref missing or just a code?
            if not ref or ref.strip() in ["", "N/A"]:
                gap_issues.append((mod_name, gid, "ref", "NO_REF", ""))

print(f"\nTotal GAPs scanned: {total_gaps}")
print(f"Total issues found: {len(gap_issues)}")

type_counts2 = Counter(i[3] for i in gap_issues)
print("\nBy type:")
for t, c in type_counts2.most_common():
    print(f"  {t:20s}: {c}")

# Show EN title samples
en_titles = [i for i in gap_issues if i[3] == "EN_TITLE"]
if en_titles:
    print(f"\n--- EN_TITLE samples (showing {min(30, len(en_titles))}) ---")
    for mod, gid, field, itype, sample in en_titles[:30]:
        print(f"  {mod[:40]:40s} | {gid:7s} | {sample[:60]}")

# ── 3. CROSS-CHECK: Are GAPs enriched by LLM? ──
print("\n" + "=" * 70)
print("PART 3: GAP vs LLM-ENRICHED CROSS-CHECK")
print("=" * 70)

# Check if any llm-enriched.json contains GAP items
for m in sorted(glob.glob("*/llm-enriched.json")):
    data = json.load(open(m))
    gap_items = [d for d in data if d.get("id", "").startswith("GAP")]
    if gap_items:
        print(f"  {os.path.dirname(m)}: {len(gap_items)} GAP items in llm-enriched")

if not any(
    d.get("id", "").startswith("GAP")
    for m in glob.glob("*/llm-enriched.json")
    for d in json.load(open(m))
):
    print("  >>> NO GAP items found in ANY llm-enriched.json!")
    print("  >>> ROOT CAUSE: LLM enrichment pipeline only processed UXP items,")
    print("  >>>             GAP items were NOT sent through LLM enrichment.")

# ── 4. SUMMARY ──
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"UXP: {total_uxp} items, {len(uxp_issues)} issues")
print(f"GAP: {total_gaps} items, {len(gap_issues)} issues")
print(f"Total findings: {total_uxp + total_gaps}")
print(f"Total issues:   {len(uxp_issues) + len(gap_issues)}")
