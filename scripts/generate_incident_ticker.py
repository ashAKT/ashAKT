from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1000, 190
BG, GREEN, WHITE = (7, 19, 27), (0, 247, 165), (215, 229, 233)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
title_font = ImageFont.truetype(BOLD, 20)
body_font = ImageFont.truetype(FONT, 14)
foot_font = ImageFont.truetype(FONT, 11)

incidents = [
    ("2017 / NOTPETYA", [
        "A compromised M.E.Doc software update delivered destructive malware.",
        "It spread through networks using SMB exploits and stolen credentials,",
        "disrupting global businesses and causing billions of dollars in damage."
    ]),
    ("2017 / WANNACRY", [
        "Exploited Windows SMBv1 (MS17-010) using the EternalBlue exploit.",
        "More than 200,000 computers across 150+ countries were affected,",
        "including major disruption to the UK's National Health Service."
    ]),
    ("2017 / EQUIFAX", [
        "Attackers exploited an unpatched Apache Struts flaw (CVE-2017-5638)",
        "to access sensitive data. Personal information belonging to about",
        "147 million people was exposed."
    ]),
    ("2020 / SOLARWINDS SUNBURST", [
        "Attackers compromised the software build process and inserted a",
        "backdoor into Orion updates, enabling stealthy access and espionage",
        "across government agencies and enterprise networks."
    ]),
    ("2021 / COLONIAL PIPELINE", [
        "DarkSide ransomware disrupted operations and forced a temporary",
        "shutdown of a major US fuel pipeline, highlighting the operational",
        "and economic impact ransomware can have on critical infrastructure."
    ])
]

frames = []
for title, lines in incidents:
    segments = [title] + lines
    total = sum(map(len, segments))
    for step in range(41):
        count = round(total * step / 40)
        remaining = count
        shown = []
        for segment in segments:
            shown.append(segment[:remaining])
            remaining = max(0, remaining - len(segment))
        im = Image.new("RGB", (W, H), BG)
        d = ImageDraw.Draw(im)
        d.rounded_rectangle((1, 1, W-2, H-2), radius=12, outline=(0, 100, 80), width=2)
        d.text((42, 30), shown[0], font=title_font, fill=GREEN)
        for row, text in enumerate(shown[1:]):
            d.text((42, 75 + row*23), text, font=body_font, fill=WHITE)
        d.text((42, 168), "THREAT LANDSCAPE / INCIDENT BRIEF", font=foot_font, fill=GREEN)
        frames.append(im)
    for _ in range(12):
        frames.append(frames[-1].copy())
    blank = Image.new("RGB", (W, H), BG)
    ImageDraw.Draw(blank).rounded_rectangle((1, 1, W-2, H-2), radius=12, outline=(0, 100, 80), width=2)
    frames.extend([blank.copy(), blank.copy()])

Path("assets").mkdir(exist_ok=True)
frames[0].save(
    "assets/incident-ticker.gif",
    save_all=True,
    append_images=frames[1:],
    duration=125,
    loop=0,
    optimize=True,
    disposal=2
)
