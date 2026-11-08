from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 760, 210
BG = (5, 13, 20)
GREEN = (0, 245, 160)
WHITE = (215, 229, 235)
MUTED = (91, 139, 148)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
title_font = ImageFont.truetype(BOLD, 16)
body_font = ImageFont.truetype(FONT, 11)
small_font = ImageFont.truetype(BOLD, 9)

incidents = [
    ("2010 / STUXNET", [
        "Discovery: A sophisticated worm targeted Siemens industrial control",
        "systems and manipulated PLC operations at Iranian nuclear facilities.",
        "Technique: Used multiple Windows zero-days and stolen certificates",
        "to spread and conceal its activity.",
        "Impact: Demonstrated the destructive potential of cyber operations",
        "against industrial and critical infrastructure."
    ]),
    ("2013 / TARGET DATA BREACH", [
        "Initial access: Attackers reportedly used credentials stolen from",
        "a third-party HVAC vendor to access Target's network.",
        "Execution: Point-of-sale malware captured payment-card data",
        "and other customer information.",
        "Impact: Payment data from about 40 million cards was affected."
    ]),
    ("2014 / SONY PICTURES", [
        "Attack: A destructive intrusion disrupted Sony Pictures' corporate",
        "systems and resulted in large-scale data theft and public leaks.",
        "Activity: Employee data, internal documents, emails and unreleased",
        "film material were released publicly.",
        "Impact: Business operations were disrupted and sensitive data exposed."
    ]),
    ("2017 / NOTPETYA", [
        "Initial access: A compromised M.E.Doc software update delivered",
        "destructive malware into trusted corporate environments.",
        "Lateral movement: SMB exploitation and stolen credentials enabled",
        "rapid propagation across connected enterprise networks.",
        "Impact: Global business disruption and billions of dollars in losses."
    ]),
    ("2017 / WANNACRY", [
        "Initial access: Exploited Windows SMBv1 (CVE-2017-0144 / MS17-010)",
        "using the EternalBlue exploit against vulnerable systems.",
        "Propagation: Self-spreading ransomware encrypted files and",
        "demanded Bitcoin payments from victims.",
        "Impact: 200,000+ computers in 150+ countries; NHS disruption."
    ]),
    ("2017 / EQUIFAX", [
        "Initial access: Attackers exploited an unpatched Apache Struts flaw",
        "(CVE-2017-5638) in a public-facing web application.",
        "Data exposure: Sensitive personal and financial information was",
        "accessed and exfiltrated from the organisation.",
        "Impact: Approximately 147 million people were affected."
    ]),
    ("2018 / MARRIOTT STARWOOD", [
        "Discovery: Attackers had accessed the Starwood guest reservation",
        "database before Marriott's acquisition of Starwood.",
        "Exposure: Personal details and, for some guests, passport data",
        "were accessed over an extended period.",
        "Impact: Up to 383 million guest records were initially reported."
    ]),
    ("2019 / CAPITAL ONE", [
        "Initial access: An attacker exploited a misconfigured web application",
        "firewall in a cloud-hosted environment.",
        "Data exposure: Data relating to approximately 100 million US and",
        "6 million Canadian individuals was accessed.",
        "Lesson: Enforce least privilege and validate cloud configurations."
    ]),
    ("2020 / SOLARWINDS SUNBURST", [
        "Initial access: Attackers compromised the SolarWinds software build",
        "environment and inserted a backdoor into Orion platform updates.",
        "Execution: SUNBURST enabled stealthy command-and-control activity",
        "and follow-on access to affected networks.",
        "Impact: Government agencies and enterprises were compromised."
    ]),
    ("2021 / COLONIAL PIPELINE", [
        "Initial access: DarkSide operators accessed the network using a",
        "compromised VPN account that lacked multifactor authentication.",
        "Response: The company temporarily halted pipeline operations",
        "following the ransomware incident.",
        "Impact: Fuel supply disruption across parts of the United States."
    ]),
    ("2023 / MOVEIT TRANSFER", [
        "Initial access: Cl0p exploited a SQL injection vulnerability",
        "(CVE-2023-34362) in internet-facing MOVEit Transfer servers.",
        "Execution: A web shell enabled unauthorised access and data theft",
        "from organisations using the file-transfer platform.",
        "Impact: A large supply-chain data-theft campaign affected many firms."
    ]),
    ("2024 / CHANGE HEALTHCARE", [
        "Initial access: Attackers used compromised credentials to access",
        "a remote access portal that did not have MFA enabled.",
        "Execution: ALPHV/BlackCat ransomware disrupted claims and payment",
        "services across the US healthcare ecosystem.",
        "Impact: Pharmacies, providers and patients faced major disruption."
    ])
]

frames = []
for idx, (title, lines) in enumerate(incidents, 1):
    base = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle((1, 1, W - 2, H - 2), radius=10, outline=(0, 104, 83), width=1)
    draw.text((20, 12), "THREAT INTELLIGENCE / CYBER INCIDENT BRIEF", font=small_font, fill=MUTED)
    draw.text((20, 34), title, font=title_font, fill=GREEN)
    draw.line((20, 62, W - 20, 62), fill=(0, 78, 66), width=1)
    draw.text((20, 190), f"INCIDENT {idx:02d}/{len(incidents):02d}  |  TYPEWRITER BRIEF", font=small_font, fill=GREEN)

    for row, line in enumerate(lines):
        for n in range(1, len(line) + 1, 9):
            frame = base.copy()
            d = ImageDraw.Draw(frame)
            for previous in range(row):
                d.text((20, 72 + previous * 18), lines[previous], font=body_font, fill=WHITE)
            partial = line[:n]
            d.text((20, 72 + row * 18), partial, font=body_font, fill=WHITE)
            cursor_x = 20 + d.textlength(partial, font=body_font)
            d.rectangle((int(cursor_x + 1), 74 + row * 18, int(cursor_x + 5), 83 + row * 18), fill=GREEN)
            frames.append(frame)

    complete = base.copy()
    d = ImageDraw.Draw(complete)
    for row, line in enumerate(lines):
        d.text((20, 72 + row * 18), line, font=body_font, fill=WHITE)
    frames.extend([complete.copy()] * 26)

palette_frames = [
    frame.quantize(colors=32, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    for frame in frames
]
Path("assets").mkdir(exist_ok=True)
palette_frames[0].save(
    "assets/incident-ticker.gif",
    save_all=True,
    append_images=palette_frames[1:],
    duration=85,
    loop=0,
    optimize=True,
    disposal=1
)
