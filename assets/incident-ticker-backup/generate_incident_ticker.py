#!/usr/bin/env python3
"""Regenerate the animated incident GIF from the companion SVG.

Usage:
    python -m pip install Pillow
    python generate_incident_ticker.py

The SVG is the canonical source for the 100 incident records and animation order.
"""
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SVG_PATH = HERE / "animated-cyber-incidents-descending.svg"
GIF_PATH = HERE / "incident-ticker.gif"
W, H = 1100, 540
BG = (5, 12, 9)
GREEN = (88, 255, 145)
PALE = (190, 255, 211)
MUTED = (116, 190, 145)
TRACK = (24, 61, 41)

def parse_incidents():
    root = ET.parse(SVG_PATH).getroot()
    ns = {"svg": "http://www.w3.org/2000/svg"}
    records = []
    for group in root.findall(".//svg:g[@class='incident']", ns):
        texts = group.findall("svg:text", ns)
        if len(texts) < 2:
            continue
        title = texts[0].text or ""
        sections = {}
        current = None
        for node in texts[2:]:
            value = node.text or ""
            if value.startswith("[") and value.endswith("]"):
                current = value[1:-1]
                sections[current] = []
            elif current:
                sections[current].append(value)
        records.append({
            "title": title,
            "attack": " ".join(sections.get("ATTACK VECTOR", [])),
            "impact": " ".join(sections.get("IMPACT", [])),
            "significance": " ".join(sections.get("SIGNIFICANCE", [])),
        })
    if not records:
        raise RuntimeError("No incident entries found in the SVG.")
    return records

def get_font(bold, size):
    candidates = (
        ["/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
         "/usr/share/fonts/truetype/liberation2/LiberationMono-Bold.ttf"]
        if bold else
        ["/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
         "/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf"]
    )
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()

def wrap_pixels(draw, text, face, max_width):
    words, lines, line = text.split(), [], ""
    for word in words:
        candidate = word if not line else line + " " + word
        if draw.textbbox((0, 0), candidate, font=face)[2] <= max_width:
            line = candidate
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines

def render(record, number, stage, fonts):
    title_font, label_font, body_font, small_font = fonts
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    draw.text((48, 72), record["title"], font=title_font, fill=GREEN)
    draw.text((48, 125), f"CASE {number:03d} / 100", font=small_font, fill=MUTED)
    y = 183
    sections = [
        ("ATTACK VECTOR", "attack"),
        ("IMPACT", "impact"),
        ("SIGNIFICANCE", "significance"),
    ]
    for index, (label, key) in enumerate(sections):
        if index > stage:
            continue
        draw.text((48, y), f"[{label}]", font=label_font, fill=GREEN)
        y += 31
        for line in wrap_pixels(draw, record[key], body_font, W - 105)[:3]:
            color = PALE if index == stage else MUTED
            draw.text((62, y), line, font=body_font, fill=color)
            y += 27
        y += 19
    draw.rectangle((48, 498, W - 48, 501), fill=TRACK)
    draw.rectangle((48, 498, 48 + int(number / 100 * (W - 96)), 501), fill=GREEN)
    return image

def main():
    records = parse_incidents()
    fonts = (
        get_font(True, 25), get_font(True, 17),
        get_font(False, 18), get_font(False, 14)
    )
    frames, durations = [], []
    for number, record in enumerate(records, start=1):
        for stage, duration in ((0, 1200), (1, 1500), (2, 3900)):
            frames.append(render(record, number, stage, fonts))
            durations.append(duration)
    frames[0].save(
        GIF_PATH, save_all=True, append_images=frames[1:],
        duration=durations, loop=0, optimize=True, disposal=2
    )
    print(f"Created {GIF_PATH} from {len(records)} SVG incidents ({len(frames)} frames).")

if __name__ == "__main__":
    main()
