#!/usr/bin/env python3
"""Render labels onto an image with the bundled skill font."""

from __future__ import annotations

import json
import html
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main() -> int:
    if len(sys.argv) not in {4, 5}:
        print("Usage: render_labels.py <input.png> <output.png> <labels.json> <font.ttf>", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    labels_path = Path(sys.argv[3])
    if len(sys.argv) == 5:
        font_path = Path(sys.argv[4])
    else:
        print(
            "No font provided. This skill does not bundle a font.\n"
            "Pass a handwriting .ttf as the 4th argument, e.g.:\n"
            "  render_labels.py input.png output.png labels.json /path/to/font.ttf",
            file=sys.stderr,
        )
        return 2
    if not font_path.exists():
        print(f"Font not found: {font_path}", file=sys.stderr)
        return 2

    image = Image.open(input_path).convert("RGBA")
    draw = ImageDraw.Draw(image)
    labels = json.loads(labels_path.read_text(encoding="utf-8"))

    width, height = image.size
    for label in labels:
        text = str(label["text"])
        x = float(label["x"]) * width
        y = float(label["y"]) * height
        size = int(label.get("size", max(28, width * 0.035)))
        anchor = label.get("anchor", "mm")
        try:
            font = ImageFont.truetype(str(font_path), size=size)
            draw.text((x, y), text, font=font, fill=(0, 0, 0, 255), anchor=anchor)
        except OSError:
            label_image = render_label_with_quicklook(text, size, font_path)
            paste_label(image, label_image, x, y, anchor)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(output_path)
    return 0


def render_label_with_quicklook(text: str, size: int, font_path: Path) -> Image.Image:
    """Render one label through macOS QuickLook when Pillow cannot use the font."""
    width = max(size * 4, int(size * max(2.5, len(text) * 1.25)))
    height = max(size * 3, int(size * 2.4))
    escaped = html.escape(text)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<style>@font-face {{ font-family: SkillLabelFont; src: url('{font_path.resolve().as_uri()}'); }}</style>
<rect width="{width}" height="{height}" fill="white"/>
<text x="{width / 2}" y="{height / 2}" text-anchor="middle" dominant-baseline="middle" font-family="SkillLabelFont" font-size="{size}" fill="black">{escaped}</text>
</svg>"""
    with tempfile.TemporaryDirectory(prefix="figure-label-") as temp_dir:
        temp_path = Path(temp_dir)
        svg_path = temp_path / "label.svg"
        out_dir = temp_path / "out"
        out_dir.mkdir()
        svg_path.write_text(svg, encoding="utf-8")
        subprocess.run(
            ["qlmanage", "-t", "-s", str(width), "-o", str(out_dir), str(svg_path)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        png_path = out_dir / "label.svg.png"
        label = Image.open(png_path).convert("RGBA")

    pixels = label.load()
    xs: list[int] = []
    ys: list[int] = []
    for py in range(label.height):
        for px in range(label.width):
            r, g, b, a = pixels[px, py]
            if a and (r < 245 or g < 245 or b < 245):
                alpha = 255 - min(r, g, b)
                pixels[px, py] = (0, 0, 0, max(0, min(255, alpha * 2)))
                xs.append(px)
                ys.append(py)
            else:
                pixels[px, py] = (0, 0, 0, 0)

    if not xs:
        return label

    pad = max(4, size // 10)
    box = (
        max(0, min(xs) - pad),
        max(0, min(ys) - pad),
        min(label.width, max(xs) + pad),
        min(label.height, max(ys) + pad),
    )
    return label.crop(box)


def paste_label(base: Image.Image, label: Image.Image, x: float, y: float, anchor: str) -> None:
    left = int(x)
    top = int(y)
    if "m" in anchor:
        left -= label.width // 2
    elif "r" in anchor:
        left -= label.width
    if anchor.startswith("m"):
        top -= label.height // 2
    elif anchor.startswith("d") or anchor.startswith("b"):
        top -= label.height
    base.alpha_composite(label, (left, top))


if __name__ == "__main__":
    raise SystemExit(main())
