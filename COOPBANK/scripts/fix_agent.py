#!/usr/bin/env python3
"""
Agent-SubAgent Fix Pipeline for Co-opBank UX Audit
===================================================
Phase A: Generate đề_xuất_steps for all Gap items (409 items)
Phase B: Translate EN→VN across all fields (UXP + Gap)
Phase C: Write back fixed llm-enriched.json

Architecture:
- Agent (this script): Orchestrates, reads/writes JSON
- SubAgent logic: Deterministic translation + template-based step generation

Usage:
    python3 fix_agent.py --base /path/to/final/ --dry-run
    python3 fix_agent.py --base /path/to/final/ --phase A
    python3 fix_agent.py --base /path/to/final/ --phase B
    python3 fix_agent.py --base /path/to/final/ --phase AB
"""
import json
import os
import re
import glob
import argparse
import copy
from collections import Counter

# ═══════════════════════════════════════════════════════════════
# INDUSTRY TERMS WHITELIST — KHÔNG dịch
# ═══════════════════════════════════════════════════════════════
KEEP_EN = {
    "OTP", "PIN", "QR", "QR code", "CTA", "UI", "UX", "API", "SDK",
    "flow", "dropdown", "toast", "bottom sheet", "placeholder",
    "touch target", "tap", "overlay", "padding", "margin", "hover",
    "tooltip", "modal", "alert", "badge", "checkbox", "radio", "toggle",
    "stepper", "carousel", "tab", "breadcrumb", "skeleton", "shimmer",
    "auto-fill", "auto-paste", "inline", "popup", "banner",
    "sticky", "scroll", "swipe", "pull-to-refresh",
    "form", "input", "label", "field", "header", "footer",
    "icon", "avatar", "chip", "tag", "divider",
    "viewport", "fold", "artboard", "state", "screen",
    "feedback", "loading", "spinner", "progress bar",
    "Nielsen", "Hick", "Fitts", "WCAG", "DDL", "NNGroup",
    "NN/g", "Laws of UX", "Zeigarnik", "Jakob",
    "VND", "SMS", "PDF", "iOS", "Android", "GPS", "NFC",
    "biometric", "Face ID", "Touch ID", "numpad",
}

# ═══════════════════════════════════════════════════════════════
# TRANSLATION DICTIONARY — EN→VN pattern replacements
# ═══════════════════════════════════════════════════════════════
TRANSLATIONS = {
    # Common UX phrases
    "user[s]? can't": "người dùng không thể",
    "user[s]? cannot": "người dùng không thể",
    "user[s]? must": "người dùng phải",
    "user[s]? need[s]?": "người dùng cần",
    "user[s]? expect[s]?": "người dùng kỳ vọng",
    "user[s]? ha[sv]e? to": "người dùng phải",
    "user[s]? will": "người dùng sẽ",
    "the user": "người dùng",
    "users": "người dùng",
    "user": "người dùng",
    # UX actions
    "hard to read": "khó đọc",
    "hard to find": "khó tìm",
    "hard to understand": "khó hiểu",
    "easy to miss": "dễ bỏ sót",
    "feels robotic": "tạo cảm giác máy móc",
    "feels unprofessional": "tạo cảm giác thiếu chuyên nghiệp",
    "unnecessary": "không cần thiết",
    "missing": "thiếu",
    "required": "bắt buộc",
    "mandatory": "bắt buộc",
    "best practice": "phương pháp tốt nhất",
    # Banking specific
    "financial transaction[s]?": "giao dịch tài chính",
    "banking": "ngân hàng",
    "account number": "số tài khoản",
    "transaction": "giao dịch",
    "transfer": "chuyển tiền",
    "balance": "số dư",
    "receipt": "biên lai",
    "confirmation": "xác nhận",
    # UI elements & states
    "error state": "trạng thái lỗi",
    "empty state": "trạng thái trống",
    "loading state": "trạng thái tải",
    "success state": "trạng thái thành công",
    "error message": "thông báo lỗi",
    "error feedback": "phản hồi lỗi",
    "visual feedback": "phản hồi trực quan",
    "visual hierarchy": "phân cấp trực quan",
    "color-only information": "thông tin chỉ dựa trên màu sắc",
    "color contrast": "tương phản màu",
    "text readability": "độ đọc được của văn bản",
    "touch target size": "kích thước vùng chạm",
    "hit area": "vùng chạm",
    "screen reader": "trình đọc màn hình",
    "accessibility": "khả năng tiếp cận",
    "cognitive load": "tải nhận thức",
    "mental model": "mô hình tâm lý",
    "affordance": "tín hiệu tương tác",
    "false affordance": "tín hiệu tương tác giả",
    "discoverability": "khả năng khám phá",
    # Actions
    "implement": "triển khai",
    "consider": "xem xét",
    "add": "thêm",
    "remove": "loại bỏ",
    "replace": "thay thế",
    "ensure": "đảm bảo",
    "provide": "cung cấp",
    "display": "hiển thị",
    "show": "hiển thị",
    "hide": "ẩn",
    "prevent": "ngăn chặn",
    "validate": "kiểm tra",
    "verify": "xác minh",
    "confirm": "xác nhận",
    # Qualifiers
    "same": "giống nhau",
    "different": "khác nhau",
    "inconsistent": "không nhất quán",
    "consistent": "nhất quán",
    "professional": "chuyên nghiệp",
    "unprofessional": "thiếu chuyên nghiệp",
}

# Nielsen heuristic quote translations
HEURISTIC_TRANSLATIONS = {
    "The design should always keep users informed about what is going on, through appropriate feedback within a reasonable amount of time.":
        "Thiết kế phải luôn thông báo cho người dùng biết điều gì đang xảy ra, thông qua phản hồi phù hợp trong thời gian hợp lý.",
    "The system should speak the users' language, with words, phrases, and concepts familiar to the user, rather than system-oriented terms.":
        "Hệ thống nên sử dụng ngôn ngữ quen thuộc với người dùng, bằng từ ngữ, cụm từ và khái niệm mà người dùng hiểu, thay vì thuật ngữ kỹ thuật.",
    "Users often perform actions by mistake. They need a clearly marked 'emergency exit' to leave the unwanted action without having to go through an extended process.":
        "Người dùng thường thực hiện hành động nhầm. Họ cần một 'lối thoát khẩn cấp' được đánh dấu rõ ràng để rời khỏi hành động không mong muốn mà không phải trải qua quy trình kéo dài.",
    "Users should not have to wonder whether different words, situations, or actions mean the same thing.":
        "Người dùng không nên phải thắc mắc liệu các từ, tình huống hoặc hành động khác nhau có cùng ý nghĩa hay không.",
    "Good error messages are important, but the best designs carefully prevent problems from occurring in the first place.":
        "Thông báo lỗi tốt là quan trọng, nhưng thiết kế tốt nhất là cẩn thận ngăn ngừa vấn đề xảy ra ngay từ đầu.",
    "Minimize the user's memory load by making elements, actions, and options visible.":
        "Giảm thiểu tải nhớ của người dùng bằng cách hiển thị rõ ràng các phần tử, hành động và tùy chọn.",
    "Interfaces should not contain information that is irrelevant or rarely needed.":
        "Giao diện không nên chứa thông tin không liên quan hoặc hiếm khi cần thiết.",
    "Even though it is better if the system can be used without documentation, it may be necessary to provide help and documentation.":
        "Dù hệ thống có thể sử dụng được mà không cần tài liệu, vẫn có thể cần thiết cung cấp trợ giúp và tài liệu hướng dẫn.",
    "The time to acquire a target is a function of the distance to and size of the target.":
        "Thời gian để đạt tới mục tiêu phụ thuộc vào khoảng cách và kích thước của mục tiêu.",
    "People remember uncompleted or interrupted tasks better than completed tasks.":
        "Con người ghi nhớ các nhiệm vụ chưa hoàn thành hoặc bị gián đoạn tốt hơn các nhiệm vụ đã hoàn thành.",
    "The time it takes to make a decision increases with the number and complexity of choices.":
        "Thời gian ra quyết định tăng theo số lượng và độ phức tạp của các lựa chọn.",
}


def is_full_english(text: str) -> bool:
    """Check if text is predominantly English."""
    if not text or len(text) < 10:
        return False
    # Contains Vietnamese diacritics?
    vn_chars = re.findall(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]', text.lower())
    if len(vn_chars) > 2:
        return False
    # Mostly ASCII?
    ascii_ratio = sum(1 for c in text if ord(c) < 128) / len(text)
    return ascii_ratio > 0.85


def normalize_quotes(text: str) -> str:
    """Normalize smart/curly quotes to standard ASCII quotes."""
    replacements = {
        '\u201c': '"', '\u201d': '"',  # Left/right double
        '\u2018': "'", '\u2019': "'",  # Left/right single
        '\u00ab': '"', '\u00bb': '"',  # Guillemets
        '\u2033': '"', '\u2032': "'",  # Prime
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def translate_en_quotes(text: str) -> str:
    """Translate known English quotes in nguyên_tắc fields."""
    result = normalize_quotes(text)
    for en_quote, vn_quote in HEURISTIC_TRANSLATIONS.items():
        if en_quote in result:
            # Replace quoted version
            result = result.replace(
                f'"{en_quote}"',
                f'"{vn_quote}"'
            )
            # Replace unquoted version
            if en_quote in result:
                result = result.replace(en_quote, vn_quote)
    return result


def translate_en_fragments(text: str) -> str:
    """Apply pattern-based EN→VN translations."""
    result = text
    for en_pattern, vn_text in sorted(TRANSLATIONS.items(), key=lambda x: -len(x[0])):
        # Use word boundary regex
        try:
            result = re.sub(
                r'\b' + en_pattern + r'\b',
                vn_text,
                result,
                flags=re.IGNORECASE
            )
        except re.error:
            result = result.replace(en_pattern, vn_text)
    return result


def generate_gap_steps(gap_item: dict) -> list:
    """Generate đề_xuất_steps for a Gap item based on existing content."""
    hien_trang = gap_item.get("hiện_trạng", "").lower()
    tac_dong = gap_item.get("tác_động", "").lower()
    nguyen_tac = gap_item.get("nguyên_tắc", "").lower()
    hien_trang_raw = gap_item.get("hiện_trạng", "")
    all_text = f"{hien_trang} {tac_dong} {nguyen_tac}"

    steps = []

    # ── Pattern-based step generation ──
    # 1. Missing/absent patterns
    if any(k in hien_trang for k in ["thiếu", "missing", "không có", "chưa có", "không hiển thị"]):
        subject = extract_subject(hien_trang_raw)
        if subject:
            steps.append(f"Bổ sung {subject} vào thiết kế màn hình")
        else:
            steps.append("Bổ sung thành phần còn thiếu vào giao diện hiện tại")

    # 2. Error/validation patterns
    if any(k in all_text for k in ["error", "lỗi", "validation", "invalid"]):
        steps.append("Thiết kế trạng thái lỗi rõ ràng: viền đỏ trường nhập + thông báo lỗi inline bên dưới")
        if "real-time" in all_text or "inline" in all_text:
            steps.append("Triển khai inline validation real-time — kiểm tra ngay khi người dùng rời trường nhập")

    # 3. Accessibility patterns
    if any(k in all_text for k in ["color-only", "color only", "chỉ dựa trên màu", "màu sắc"]):
        steps.append("Bổ sung tín hiệu thứ hai ngoài màu sắc (icon + text label) để đạt WCAG 1.4.1")

    if any(k in all_text for k in ["touch target", "vùng chạm", "44", "hit area"]):
        steps.append("Tăng kích thước vùng chạm tối thiểu 44×44dp theo chuẩn WCAG 2.5.5")

    if any(k in all_text for k in ["screen reader", "trình đọc màn hình", "accessibility label"]):
        steps.append("Thêm accessibility label tiếng Việt đầy đủ cho screen reader")

    # 4. OTP/auth patterns
    if "otp" in all_text:
        steps.append("Triển khai OTP UX chuẩn: highlight ô active, countdown timer, nút 'Gửi lại mã' sau khi hết hạn")
        if "auto" in all_text or "paste" in all_text:
            steps.append("Hỗ trợ auto-paste OTP từ SMS và auto-submit khi đủ 6 ký tự")

    # 5. Layout/scroll patterns  
    if any(k in all_text for k in ["fold", "scroll", "keyboard", "bàn phím", "cta", "sticky"]):
        steps.append("Đặt CTA chính ở vị trí sticky bottom — luôn hiển thị bất kể scroll hoặc keyboard")

    # 6. Dropdown/selection patterns
    if any(k in all_text for k in ["dropdown", "single option", "1 option", "một option"]):
        steps.append("Loại bỏ dropdown khi chỉ có 1 lựa chọn — hiển thị trực tiếp giá trị mặc định")

    # 7. Consistency patterns
    if any(k in all_text for k in ["consistency", "nhất quán", "inconsistent", "khác nhau", "không đồng bộ"]):
        steps.append("Đồng bộ format hiển thị giữa tất cả màn hình trong cùng flow")

    # 8. Empty state patterns
    if any(k in all_text for k in ["empty state", "trạng thái trống", "no data", "không có dữ liệu"]):
        steps.append("Thiết kế empty state với illustration, message hướng dẫn và CTA rõ ràng")

    # 9. Loading/feedback patterns
    if any(k in all_text for k in ["loading", "processing", "chờ", "spinner"]):
        steps.append("Thêm trạng thái loading với skeleton hoặc spinner kèm message giải thích")

    # 10. Confirm/destructive patterns
    if any(k in all_text for k in ["destructive", "delete", "xóa", "hủy", "confirm"]):
        steps.append("Thiết kế dialog xác nhận với framing rõ hậu quả và CTA phân biệt rõ primary/destructive")

    # 11. Text/typography patterns
    if any(k in all_text for k in ["readability", "đọc được", "font size", "cỡ chữ", "text size"]):
        steps.append("Điều chỉnh typography: tăng kích thước ≥14sp, line-height ≥1.5, contrast ratio ≥4.5:1")

    # 12. Navigation patterns
    if any(k in all_text for k in ["back", "quay lại", "navigation", "breadcrumb", "exit"]):
        steps.append("Cung cấp navigation rõ ràng: nút quay lại + breadcrumb cho deep flow")

    # 13. Data format patterns
    if any(k in all_text for k in ["format", "mask", "currency", "tiền", "amount", "số tiền"]):
        steps.append("Format dữ liệu nhất quán: số tiền có dấu phân cách + đơn vị VND + chữ viết kèm theo")

    # 14. Search/filter patterns
    if any(k in all_text for k in ["search", "tìm kiếm", "filter", "lọc", "sort"]):
        steps.append("Thêm tính năng tìm kiếm/lọc cho danh sách dài — hỗ trợ tìm nhanh theo keyword")

    # 15. Helper text patterns
    if any(k in all_text for k in ["helper", "hint", "gợi ý", "hướng dẫn", "placeholder"]):
        steps.append("Thêm helper text bên dưới trường nhập: giải thích format mong đợi hoặc ví dụ")

    # ── Fallback: extract from nguyên_tắc ──
    if not steps:
        nguyen_tac_raw = gap_item.get("nguyên_tắc", "")
        if nguyen_tac_raw:
            principle = nguyen_tac_raw.split(":")[0].strip() if ":" in nguyen_tac_raw else nguyen_tac_raw[:60]
            steps.append(f"Áp dụng nguyên tắc {principle} để cải thiện trải nghiệm")
        tac_dong_raw = gap_item.get("tác_động", "")
        if tac_dong_raw:
            steps.append(f"Khắc phục: {tac_dong_raw[:100].strip()}")

    # Ensure minimum 3 steps
    if len(steps) < 2:
        steps.append("Xác minh tính nhất quán với các màn hình khác trong cùng module")
    if len(steps) < 3:
        steps.append("Kiểm tra trên cả iOS và Android với nhiều kịch bản sử dụng thực tế")

    # Deduplicate while preserving order
    seen = set()
    unique_steps = []
    for s in steps:
        if s not in seen:
            seen.add(s)
            unique_steps.append(s)

    return unique_steps[:4]  # Max 4 steps


def extract_subject(text: str) -> str:
    """Extract the main subject of a missing/absent issue."""
    patterns = [
        r"thiếu\s+(.{10,60}?)[\.\,\;]",
        r"không có\s+(.{10,60}?)[\.\,\;]",
        r"missing\s+(.{10,60}?)[\.\,\;]",
        r"chưa có\s+(.{10,60}?)[\.\,\;]",
    ]
    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return ""


def process_module(module_dir: str, phases: str, dry_run: bool) -> dict:
    """Process a single module through selected phases."""
    enriched_path = os.path.join(module_dir, "llm-enriched.json")
    if not os.path.exists(enriched_path):
        return {"module": os.path.basename(module_dir), "status": "skip", "fixes": {}}

    data = json.load(open(enriched_path))
    original = copy.deepcopy(data)
    mod_name = os.path.basename(module_dir)
    fixes = {"gap_steps": 0, "en_translated": 0, "quotes_translated": 0}

    for item in data:
        item_id = item.get("id", "")
        is_gap = item_id.startswith("Gap")

        # ── PHASE A: Generate đề_xuất_steps for Gaps ──
        if "A" in phases and is_gap:
            if not item.get("đề_xuất_steps"):
                steps = generate_gap_steps(item)
                if steps:
                    item["đề_xuất_steps"] = steps
                    fixes["gap_steps"] += 1

        # ── PHASE B: Translate EN→VN ──
        if "B" in phases:
            for field in ["hiện_trạng", "tác_động", "nguyên_tắc"]:
                val = item.get(field, "")
                if not val:
                    continue

                new_val = val
                # B1: Translate heuristic quotes FIRST (before word-level replacements)
                new_val = translate_en_quotes(new_val)
                # B2: Translate remaining EN fragments (word-level)
                new_val = translate_en_fragments(new_val)

                if new_val != val:
                    item[field] = new_val
                    fixes["en_translated"] += 1

            # B3: Translate đề_xuất_steps
            steps = item.get("đề_xuất_steps", [])
            for i, step in enumerate(steps):
                if isinstance(step, str):
                    new_step = translate_en_fragments(step)
                    new_step = translate_en_quotes(new_step)
                    if new_step != step:
                        steps[i] = new_step
                        fixes["en_translated"] += 1

    # Write back
    if data != original and not dry_run:
        with open(enriched_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    changed = data != original
    return {
        "module": mod_name,
        "status": "fixed" if changed else "ok",
        "fixes": fixes,
    }


def main():
    parser = argparse.ArgumentParser(description="Agent-SubAgent Fix Pipeline")
    parser.add_argument("--base", required=True, help="Path to final/ directory")
    parser.add_argument("--phase", default="AB", help="Phases to run: A, B, or AB")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--module", help="Process single module (directory name)")
    args = parser.parse_args()

    print("=" * 70)
    print("🤖 Agent-SubAgent Fix Pipeline — Co-opBank UX Audit")
    print(f"   Phases: {args.phase} | {'DRY RUN' if args.dry_run else 'LIVE'}")
    print("=" * 70)

    if args.module:
        modules = [os.path.join(args.base, args.module)]
    else:
        modules = sorted(
            [os.path.dirname(p) for p in glob.glob(os.path.join(args.base, "*/llm-enriched.json"))]
        )

    print(f"\n📂 Found {len(modules)} modules\n")

    total_fixes = Counter()
    fixed_count = 0

    for mod_dir in modules:
        result = process_module(mod_dir, args.phase, args.dry_run)
        for k, v in result["fixes"].items():
            total_fixes[k] += v

        if result["status"] == "fixed":
            fixed_count += 1
            icon = "👁️" if args.dry_run else "✅"
            fixes = result["fixes"]
            parts = []
            if fixes.get("gap_steps"):
                parts.append(f"steps:{fixes['gap_steps']}")
            if fixes.get("en_translated"):
                parts.append(f"translated:{fixes['en_translated']}")
            print(f"  {icon} {result['module']:45s} | {' | '.join(parts)}")

    print(f"\n{'=' * 70}")
    print(f"{'👁️ DRY RUN' if args.dry_run else '✅ COMPLETED'}")
    print(f"  Modules processed: {len(modules)}")
    print(f"  Modules changed:   {fixed_count}")
    print(f"  Gap steps added:   {total_fixes['gap_steps']}")
    print(f"  EN→VN translated:  {total_fixes['en_translated']}")
    print(f"{'=' * 70}")

    if args.dry_run:
        print("\n💡 Run without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
