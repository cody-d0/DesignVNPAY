#!/usr/bin/env python3
"""
Normalize mockup canvas: two modes.

1) Default (portrait): portrait 1:2, fixed width, equal margin 5%.
   Use for legacy device+content mockups.

2) Frame mode (--mode frame): for wireframe-only screen mockups. White canvas,
   width fixed (default 400px), min-height 800px, height follows content with 5% margin.
   Top-constrained: content starts at top margin, flows downward (not vertically centered).
   Reference: handdrawn-mockup-common/MOCKUP_DESIGN_SYSTEM.md (width 400, min-height 800, top-constrained).

Usage:
  python normalize-mockup-canvas.py input.png [output.png]
  python normalize-mockup-canvas.py --mode frame --width 400 --min-height 800 --in-place input.png
"""

import argparse
import sys
from pathlib import Path

# Design system: margin 5% each side, device 90% of canvas (portrait mode)
MARGIN_RATIO = 0.05
DEVICE_RATIO = 0.9
ASPECT = 0.5  # width/height = 1:2 for portrait mode


def normalize_image_frame(img, width: int, min_height: int = 800, margin_ratio: float = 0.05):
    """Return new image: white canvas width=width, height follows content with 5% margin.

    - Content is scaled to fit (1 - 2*margin_ratio) * width.
    - Canvas height is max(min_height, content_height / (1 - 2*margin_ratio)).
    - Top-constrained: paste content at top margin (not vertically centered).
    """
    try:
        from PIL import Image
    except ImportError:
        print("Pillow required: pip install Pillow", file=sys.stderr)
        sys.exit(1)

    w, h = img.size
    content_w = int(width * (1 - 2 * margin_ratio))
    scale = content_w / w if w else 1
    new_w = content_w
    new_h = int(h * scale) if h else 0
    if new_h < 1:
        new_h = 1
    content_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS)
    if content_resized.mode != "RGBA":
        content_resized = content_resized.convert("RGBA")

    canvas_h = max(int(new_h / (1 - 2 * margin_ratio)), int(min_height))
    margin_px_h = int(width * margin_ratio)
    margin_px_v = int(canvas_h * margin_ratio)
    canvas = Image.new("RGBA", (width, canvas_h), (255, 255, 255, 255))
    canvas.paste(content_resized, (margin_px_h, margin_px_v))
    return canvas


def normalize_image(img, canonical_width: int, canonical_height: int, margin_px: int, device_w: int, device_h: int):
    """Return a new image: portrait canvas with device region resized and pasted."""
    try:
        from PIL import Image
    except ImportError:
        print("Pillow required: pip install Pillow", file=sys.stderr)
        sys.exit(1)

    w, h = img.size

    # 1. If landscape, center-crop to portrait 1:2 (width = height * ASPECT)
    if w >= h:
        target_w = int(h * ASPECT)
        left = (w - target_w) // 2
        img = img.crop((left, 0, left + target_w, h))
        w, h = img.size

    # 2. Treat center 90% of current image as "device" region; crop it
    crop_margin_w = int(w * (1 - DEVICE_RATIO) / 2)
    crop_margin_h = int(h * (1 - DEVICE_RATIO) / 2)
    device_crop = img.crop(
        (
            crop_margin_w,
            crop_margin_h,
            w - crop_margin_w,
            h - crop_margin_h,
        )
    )

    # 3. Resize device crop to canonical device size
    try:
        device_resized = device_crop.resize((device_w, device_h), Image.Resampling.LANCZOS)
    except AttributeError:
        device_resized = device_crop.resize((device_w, device_h), Image.LANCZOS)

    # 4. Create white canvas and paste device at margin
    canvas = Image.new("RGBA", (canonical_width, canonical_height), (255, 255, 255, 255))
    if device_resized.mode != "RGBA":
        device_resized = device_resized.convert("RGBA")
    canvas.paste(device_resized, (margin_px, margin_px))
    return canvas


def run_one(input_path: Path, output_path, width: int, in_place: bool, mode: str, min_height: int):
    try:
        from PIL import Image
    except ImportError:
        print("Pillow required: pip install Pillow", file=sys.stderr)
        sys.exit(1)

    img = Image.open(input_path).convert("RGBA")

    if mode == "frame":
        out_img = normalize_image_frame(img, width=width, min_height=min_height, margin_ratio=MARGIN_RATIO)
    else:
        height = int(width / ASPECT)
        margin_px = int(width * MARGIN_RATIO)
        device_w = width - 2 * margin_px
        device_h = height - 2 * margin_px
        out_img = normalize_image(
            img,
            canonical_width=width,
            canonical_height=height,
            margin_px=margin_px,
            device_w=device_w,
            device_h=device_h,
        )

    if output_path is not None:
        dest = Path(output_path)
    elif in_place:
        dest = Path(input_path)
    else:
        dest = Path(input_path).parent / f"{Path(input_path).stem}-normalized{Path(input_path).suffix}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    out_img.save(dest)
    print(f"Saved {dest}")


def main():
    parser = argparse.ArgumentParser(
        description="Normalize mockup canvas: portrait 1:2 (default) or frame mode (400×free, min-height 800, 5%% margin, top-constrained)"
    )
    parser.add_argument("input", type=Path, nargs="+", help="Input PNG path(s)")
    parser.add_argument("output", type=Path, nargs="?", default=None, help="Output path (single input); ignored if --in-place or multiple inputs")
    parser.add_argument("--width", type=int, default=400, help="Canvas width. Default 400.")
    parser.add_argument("--min-height", type=int, default=800, help="Min height for --mode frame. Default 800.")
    parser.add_argument("--mode", type=str, choices=["portrait", "frame"], default="portrait", help="portrait = 1:2 vertical, device 90%%; frame = wireframe on white canvas (width fixed, min-height, free height), 5%% margin, top-constrained.")
    parser.add_argument("--in-place", action="store_true", help="Overwrite input file(s)")
    args = parser.parse_args()

    inputs = list(args.input)
    single_output = args.output
    # One input + optional output: "input.png output.png" -> input=[input.png], output=output.png
    if len(inputs) == 2 and single_output is None and not args.in_place:
        single_output = inputs.pop(1)
    elif len(inputs) > 1 and single_output is not None and not single_output.is_dir():
        single_output = None

    for inp in inputs:
        inp = Path(inp)
        if not inp.is_file():
            print(f"Skip (not a file): {inp}", file=sys.stderr)
            continue
        out = single_output
        if len(inputs) > 1:
            if out is not None and out.is_dir():
                out = out / f"{inp.stem}-normalized{inp.suffix}"
            elif not args.in_place:
                out = None
        run_one(inp, out, width=args.width, in_place=args.in_place, mode=args.mode, min_height=args.min_height)


if __name__ == "__main__":
    main()
