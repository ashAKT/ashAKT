#!/usr/bin/env python3
"""Randomly rotate a historical cyber-incident brief on the profile."""
from pathlib import Path
import random, re, textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
DATA = """1988|Morris Worm|An early internet worm spread uncontrollably and disrupted thousands of Unix systems.|Thousands of systems were slowed or disabled; it exposed the fragility of the early internet.
1994|Citibank online bank robbery|Attackers used compromised banking systems to attempt fraudulent international transfers.|Attempted transfers exposed weaknesses in online banking controls and caused financial and reputational risk.
1999|Melissa|A macro virus spread through Outlook address books and overwhelmed corporate email systems.|Email infrastructure was overwhelmed, disrupting business communications and productivity.
2000|ILOVEYOU|A malicious email attachment spread globally, overwriting files and stealing credentials.|Organizations suffered file damage, credential exposure and costly email-system recovery.
2001|Code Red|A worm exploited Microsoft IIS and rapidly compromised internet-facing web servers.|Websites were defaced or taken offline, while infected servers generated large volumes of traffic.
2001|Nimda|A multi-vector worm spread through email, web servers, network shares and vulnerable clients.|Networks experienced rapid reinfection, service degradation and extensive incident-response costs.
2003|SQL Slammer|A tiny worm exploited SQL Server and caused widespread network congestion within minutes.|Network congestion disrupted services, including some critical and financial systems.
2003|Blaster|Malware exploited a Windows RPC vulnerability and triggered widespread system instability.|Repeated crashes and instability disrupted Windows workstations and servers.
2004|Sasser|A Windows worm exploited LSASS and spread without requiring user interaction.|Infected systems repeatedly rebooted, interrupting business and public services.
2005|TJX breach|Payment-card and personal data were stolen after network security weaknesses were exploited.|Millions of payment-card and personal records were exposed, contributing to major financial and regulatory consequences.
2007|Estonia DDoS attacks|DDoS campaigns disrupted government, banking and media services.|Essential online government, banking and media services became difficult or impossible to access.
2007|Zeus banking trojan|Credential-stealing malware targeted online banking and industrialized financial cybercrime.|Victims lost funds and banking credentials; the malware ecosystem enabled large-scale financial fraud.
2008|Conficker|A Windows worm used multiple propagation methods and created a massive botnet.|Large numbers of Windows systems were infected, creating a persistent botnet and costly remediation effort.
2008|Heartland Payment Systems|Payment-card data was stolen in a major breach involving malware.|Payment-card data exposure affected millions of transactions and led to substantial legal and compliance costs.
2009|Operation Aurora|Targeted intrusions compromised major technology companies and sought intellectual property.|Intellectual property and sensitive corporate information were exposed, prompting major security changes.
2010|Stuxnet|A sophisticated worm manipulated industrial control systems and damaged Iranian nuclear centrifuges.|Industrial centrifuges were damaged, demonstrating that malware can cause physical and strategic consequences.
2011|RSA SecurID breach|Attackers stole information related to RSA token technology, creating downstream authentication risk.|Theft of token-related information increased the risk of targeted attacks against customers relying on the authentication system.
2011|Sony PlayStation Network|A major intrusion exposed personal information and forced a prolonged service shutdown.|Services were unavailable for weeks and personal data of users was exposed.
2011|DigiNotar CA compromise|Fraudulent certificates enabled interception of trusted encrypted connections.|Fraudulent certificates undermined trust in digital certificates and enabled interception of user communications.
2012|Shamoon|A destructive wiper erased data on tens of thousands of computers at Saudi Aramco.|Tens of thousands of computers were rendered unusable, disrupting corporate operations and recovery.
2012|LinkedIn breach|Password hashes for millions of accounts were stolen and later circulated.|Stolen password hashes enabled account takeover attempts and large-scale credential reuse attacks.
2013|Adobe breach|Attackers stole customer credentials and source-code-related data at large scale.|Customer passwords and source code were exposed, increasing account-compromise and software-security risks.
2013|Target breach|Stolen vendor credentials enabled access to payment systems and theft of card data.|Payment-card and customer data theft affected millions and resulted in major remediation and settlement costs.
2013|Yahoo breach|Attackers accessed Yahoo accounts in a breach later estimated to affect billions of accounts.|Account data exposure enabled risks of identity theft, phishing and account takeover at unprecedented scale.
2013|Bangladesh Bank SWIFT heist preparation|Attackers compromised bank systems and prepared fraudulent SWIFT payment instructions.|The intrusion enabled fraudulent payment attempts and exposed weaknesses in bank payment-network security.
2014|Yahoo breach disclosure|Yahoo disclosed a massive account compromise ultimately estimated at about three billion accounts.|The scale of exposure created long-term identity, account-security, legal and reputational consequences.
2014|Sony Pictures|Destructive malware and data theft disrupted a major entertainment company and leaked internal files.|Business operations were disrupted, confidential communications leaked and employees' personal information exposed.
2014|JPMorgan Chase breach|Attackers accessed customer contact information at one of the largest US banks.|Customer contact data was exposed, increasing phishing risk and triggering major security remediation.
2014|Home Depot breach|Payment-card data was stolen after attackers gained access through compromised credentials.|Payment-card data theft affected customers and led to significant investigation, legal and security costs.
2014|German steel mill attack|A cyber intrusion disrupted industrial control processes and caused physical equipment damage.|Industrial processes were disrupted and equipment suffered physical damage.
2015|US OPM breach|Sensitive personnel and background-investigation records were stolen from a federal agency.|Highly sensitive background-investigation records created long-term risks to affected personnel and national security.
2015|Anthem breach|Personal information of nearly 79 million people was exposed in a major healthcare breach.|Sensitive health and identity information of nearly 79 million people was exposed, creating lasting privacy and fraud risks.
2015|Ukraine power grid|Attackers remotely disrupted electricity distribution, demonstrating cyber-physical impact.|Electricity outages affected customers and demonstrated the potential for cyberattacks to disrupt critical infrastructure.
2016|Bangladesh Bank heist|Fraudulent SWIFT transfers stole about $81 million from the central bank's account.|Approximately $81 million was stolen, exposing weaknesses in international payment controls.
2016|Mirai botnet|Malware hijacked poorly secured IoT devices and launched record-scale DDoS attacks.|Compromised IoT devices formed a large botnet capable of disrupting internet services through DDoS attacks.
2016|Dyn DNS attack|Mirai-powered DDoS traffic disrupted DNS services and made major websites unreachable.|Major websites and online platforms became unreachable across parts of the internet.
2016|Shadow Brokers leak|Exploit tools attributed to the NSA were leaked, including EternalBlue.|Leaked exploit tools enabled widespread follow-on attacks, including WannaCry and NotPetya.
2016|DNC email compromise|Political campaign emails were stolen and publicly released.|Stolen political communications were publicly disclosed, affecting campaign operations and public trust.
2016|Operation Ghoul / banking malware campaigns|Credential theft and targeted malware demonstrated the growing scale of financially motivated intrusions.|Organizations and individuals faced credential theft, financial losses and increased targeted-malware risk.
2017|WannaCry|Ransomware used EternalBlue to spread rapidly across more than 150 countries.|Hundreds of thousands of systems were affected; hospitals, businesses and public services suffered disruption.
2017|NotPetya|A destructive wiper spread through a compromised software update and caused billions in losses.|Global companies suffered destructive outages and billions of dollars in losses.
2017|Equifax breach|An unpatched web application vulnerability exposed sensitive information of about 147 million people.|Highly sensitive personal data of about 147 million people was exposed, creating long-term identity-fraud risk.
2017|CCleaner supply-chain compromise|Attackers inserted a backdoor into legitimate software distributed to users.|Trusted software updates infected users, undermining confidence in software distribution and exposing systems to further compromise.
2017|Triton / Trisis|Malware targeted industrial safety systems, raising the risk of physical harm.|Compromise of industrial safety controllers created the potential for unsafe plant conditions and physical harm.
2017|Uber breach disclosure|Attackers accessed personal data and the company paid intruders to conceal the incident.|Personal data was exposed and concealment of the incident led to regulatory, legal and reputational consequences.
2018|Marriott / Starwood breach|Guest records from the Starwood reservation environment were exposed at enormous scale.|Guest personal and travel information was exposed at massive scale, creating privacy and regulatory consequences.
2018|SingHealth breach|Health records of about 1.5 million people in Singapore were stolen.|Health and identity records of about 1.5 million people were stolen, including information belonging to Singapore's prime minister.
2018|Exactis data exposure|A publicly accessible database exposed personal information on hundreds of millions of people.|Large volumes of personal information were accessible, increasing risks of profiling, phishing and identity fraud.
2018|Coincheck theft|Cryptocurrency worth roughly $530 million was stolen from the exchange.|Approximately $530 million in cryptocurrency was stolen, causing major customer losses and exchange-security reforms.
2019|Capital One breach|A cloud access-control weakness exposed data of about 100 million people.|Data belonging to about 100 million people was exposed, leading to regulatory penalties and remediation costs.
2019|Norsk Hydro ransomware|LockerGoga disrupted global aluminium operations and forced manual processes.|Production was disrupted across global operations, forcing manual workarounds and significant recovery spending.
2019|Baltimore city ransomware|RobbinHood ransomware disrupted municipal services and caused substantial recovery costs.|Municipal services and payment systems were disrupted, delaying public services and causing substantial recovery costs.
2019|Citrix ADC exploitation|Attackers exploited gateway flaws to access enterprise networks.|Attackers could gain footholds in enterprise networks, exposing sensitive systems and data to further compromise.
2020|SolarWinds SUNBURST|A compromised software build process inserted a backdoor into trusted Orion updates.|Trusted software updates gave attackers access to government agencies and major organizations, creating a far-reaching espionage risk.
2020|Twitter account takeover|Social engineering of employees enabled attackers to hijack high-profile accounts.|High-profile accounts were used in a cryptocurrency scam, undermining platform trust and exposing internal access weaknesses.
2020|Garmin ransomware|A ransomware incident disrupted services and business operations.|Connected services and business operations were disrupted, affecting customers and employees.
2020|Blackbaud ransomware|A ransomware attack exposed data held by a widely used cloud services provider.|Data held for nonprofit, education and other customers was exposed, creating privacy and extortion risks.
2020|Microsoft Exchange ecosystem attacks|Exchange weaknesses became a major route for enterprise compromise and persistence.|Internet-facing mail servers were compromised, enabling data theft, persistence and follow-on intrusions.
2021|Microsoft Exchange ProxyLogon|Chained zero-days enabled unauthenticated server compromise and web-shell deployment.|Thousands of exposed servers were compromised, enabling mailbox theft, web shells and ransomware deployment.
2021|Colonial Pipeline|Ransomware forced a major US fuel pipeline operator to suspend operations.|Fuel pipeline operations were halted, causing regional fuel shortages, panic buying and economic disruption.
2021|Kaseya VSA|REvil abused a managed-service platform to distribute ransomware to downstream customers.|A supply-chain ransomware attack affected managed service providers and downstream businesses, disrupting operations at scale.
2021|Accellion FTA|Zero-day exploitation enabled data theft from organizations using a legacy file-transfer appliance.|Sensitive files were stolen from multiple organizations, leading to extortion, privacy and legal consequences.
2021|Log4Shell|A critical Log4j flaw enabled remote code execution across many exposed Java applications.|Attackers gained potential remote-code-execution paths across widely used Java applications, creating urgent global patching work.
2021|Codecov supply-chain compromise|A modified code-coverage tool exported secrets from customer CI environments.|Secrets in CI environments were exposed, potentially enabling access to source code, cloud accounts and production systems.
2021|Twitch source-code leak|A large data dump exposed source code, creator payout data and internal information.|Source code, internal information and creator payout data became public, creating security and privacy concerns.
2022|Costa Rica ransomware crisis|Ransomware disrupted government services and led to a national emergency declaration.|Government agencies lost access to systems and services, disrupting public administration and national operations.
2022|Ronin Network hack|Attackers stole cryptocurrency worth roughly $625 million from a blockchain bridge.|Approximately $625 million in cryptocurrency was stolen, causing major losses and undermining confidence in the bridge.
2022|Uber breach|Social engineering and MFA fatigue helped an intruder access internal systems.|Internal systems and tools were accessed, exposing corporate data and disrupting confidence in security controls.
2022|Medibank breach|Criminals stole sensitive personal and health information from millions of customers.|Sensitive health information of millions was stolen and leaked, causing serious privacy harm and extortion pressure.
2022|LastPass breach|Intruders accessed development information and later obtained encrypted customer vault backups.|Encrypted customer vault backups were stolen, increasing the risk of offline password-cracking and account compromise.
2022|Optus breach|Personal information of millions of Australian customers was exposed.|Personal identity information of millions was exposed, creating fraud and identity-theft risks.
2023|MOVEit Transfer|Cl0p exploited a zero-day in file-transfer software to steal data from many organizations.|Data from hundreds of organizations was stolen through mass exploitation, leading to extortion and regulatory exposure.
2023|MGM Resorts|Social engineering led to major operational disruption across hotel and casino systems.|Hotel, casino and booking operations were disrupted, causing major revenue losses and customer-service outages.
2023|Caesars Entertainment|A social-engineering-led intrusion resulted in data theft and a reported ransom payment.|Customer data was stolen and the company reportedly paid a ransom, creating privacy and financial consequences.
2023|3CX supply-chain attack|A compromised software build chain distributed malware through a trusted business application.|Customers installing trusted software could be infected, creating downstream compromise and espionage risk.
2023|Barracuda ESG zero-day|Attackers exploited an appliance vulnerability and compromised email security gateways.|Email security appliances were compromised and data stolen, requiring affected devices to be replaced.
2023|T-Mobile API breach|Customer data was accessed through an API-related exposure.|Customer information was exposed, adding to repeated privacy concerns and regulatory scrutiny.
2023|Microsoft Storm-0558|A stolen signing key enabled access to email accounts at multiple organizations.|Government and enterprise email accounts were accessed, exposing sensitive communications.
2023|Okta support-system breach|Attackers accessed customer support files and session-related information.|Customer support files and session tokens were exposed, creating potential downstream customer-account compromise.
2023|23andMe credential stuffing|Reused passwords enabled access to user accounts and related profile data.|Genetic and profile information was accessed and shared, creating unusually sensitive privacy risks.
2023|ICBC Financial Services ransomware|A ransomware incident disrupted US broker-dealer operations and Treasury-market settlement activity.|Broker-dealer operations and Treasury-market settlement activity were disrupted, highlighting financial-sector dependencies.
2024|Change Healthcare|Ransomware severely disrupted US healthcare claims, payments and prescription workflows.|Claims processing, prescriptions and provider payments were disrupted across US healthcare, creating financial strain and patient-care delays.
2024|Snowflake customer-account attacks|Stolen credentials were used to access customer environments and exfiltrate data.|Customer records were exfiltrated from multiple organizations, resulting in extortion and notification obligations.
2024|CDK Global ransomware|A cyberattack disrupted dealership management systems across much of the US auto retail sector.|Dealership sales, service and financing workflows were disrupted across the US automotive retail sector.
2024|Ticketmaster / Live Nation data theft|A cloud-hosted dataset was advertised for sale after unauthorized access claims.|Customer-related data was reportedly accessed and offered for sale, raising privacy and account-security concerns.
2024|Synnovis ransomware|A ransomware attack disrupted pathology services and affected London hospitals.|Pathology services were disrupted, causing cancelled appointments, delayed diagnoses and operational pressure on hospitals.
2024|Sisense breach|A compromise exposed customer-related credentials and prompted urgent security guidance.|Customer credentials and secrets were exposed, creating downstream access risks for connected customer environments.
2024|National Public Data breach|A large dataset containing personal information was exposed and circulated online.|Personal records were circulated online, increasing risks of identity theft, fraud and targeted scams.
2024|Salt Typhoon telecom intrusions|A state-linked espionage campaign compromised telecom providers and accessed sensitive communications data.|Sensitive communications data and call records were accessed, raising national-security and privacy concerns.
2024|AnyDesk compromise|Attackers accessed parts of the company's production systems and code-signing-related environment.|Production-system access and code-signing concerns triggered credential resets and heightened software-supply-chain risk.
2024|Ivanti Connect Secure exploitation|Zero-day vulnerabilities were used to compromise perimeter appliances and maintain access.|Perimeter appliances were compromised, enabling persistent access, espionage and potential lateral movement.
2025|Bybit cryptocurrency theft|Attackers stole approximately $1.5 billion in digital assets in one of the largest crypto heists.|Approximately $1.5 billion in digital assets was stolen, creating major financial and custody-security consequences.
2025|PowerSchool data breach|A compromised support credential enabled theft of student and staff information from school districts.|Student and staff records were stolen from school districts, creating privacy and identity risks for children and employees.
2025|Marks & Spencer cyber disruption|A cyberattack disrupted retail operations, online services and customer-facing processes.|Retail, online ordering and payment-related operations were disrupted, affecting customers, revenue and supply chains.
2025|Co-op cyberattack|A major UK retailer suffered disruption and reported customer data theft.|Retail operations were disrupted and customer data exposure increased privacy and fraud risks.
2025|Jaguar Land Rover cyberattack|A major incident halted production and disrupted supply chains and business operations.|Production stoppages affected manufacturing, suppliers, employees and the wider automotive supply chain.
2025|Salt Typhoon follow-on investigations|Telecom espionage investigations highlighted the risk of persistent access to communications infrastructure.|The campaign reinforced the risk of prolonged espionage and sensitive communications exposure across telecom infrastructure.
2025|Oracle Cloud credential exposure claims|Reports of stolen credentials and customer data triggered investigations and disputed claims.|Disputed reports prompted customer investigation and credential-risk reviews; the claimed scope and impact remained contested.
2025|Global ransomware and identity-driven intrusions|A wave of attacks reinforced the role of stolen credentials, social engineering and third-party access.|Organizations faced service outages, data theft, extortion costs and prolonged recovery from identity compromise.
2025|Healthcare ransomware ecosystem|Attacks on healthcare providers and suppliers exposed systemic dependence on shared digital infrastructure.|Hospitals and suppliers faced care delays, operational disruption, data exposure and cascading effects across shared services."""
items = [tuple(line.split("|", 3)) for line in DATA.splitlines() if line.strip()]
if len(items) < 100:
    raise SystemExit(f"Expected at least 100 entries, got {len(items)}")
items = items[:100]

catalog = ["# 100 landmark cybersecurity incidents", "",
"An educational selection spanning malware, espionage, data breaches, ransomware, supply-chain compromise, financial theft and critical infrastructure. Each entry separates the incident summary from its operational, financial, privacy or societal impact.",
"",
"| # | Year | Incident | What happened | Impact |", "|---:|---:|---|---|---|"]
for i, (year, name, brief, impact) in enumerate(items, 1):
    catalog.append(f"| {i} | {year} | {name} | {brief} | {impact} |")
catalog += ["", "## Further reading", "",
"- [CSIS – Significant Cyber Incidents](https://www.csis.org/programs/strategic-technologies-program/significant-cyber-incidents)",
"- [CERT-EU – Threat Landscape Report](https://cert.europa.eu/publications/tlr-10-years/)",
"- [FBI – Morris Worm history](https://www.fbi.gov/news/stories/morris-worm-30-years-since-first-major-attack-on-internet-110218)",
"- [Canadian Centre for Cyber Security – Operational technology incidents](https://www.cyber.gc.ca/en/guidance/cyber-threat-bulletin-cyber-threat-operational-technology)",
"- [MITRE ATT&CK – SolarWinds compromise](https://attack.mitre.org/campaigns/C0024/)",
"- [US GAO – SolarWinds and Microsoft Exchange](https://www.gao.gov/products/gao-22-104746)",
"",
"**Curation note:** This is an educational selection, not a definitive ranking. Some entries describe campaigns or broader incident patterns. Dates, attribution and impact figures should be verified against primary sources before formal reporting."]
(ROOT / "CYBER_INCIDENTS.md").write_text("\n".join(catalog) + "\n", encoding="utf-8")

# Randomize the incidents and render a readable animated GIF for the README.
random.shuffle(items)

# Keep the catalogue comprehensive, with separate incident and impact columns.
catalog = ["# 100 landmark cybersecurity incidents", "",
"An educational selection spanning malware, espionage, data breaches, ransomware, supply-chain compromise, financial theft and critical infrastructure. Each entry separates what happened from its operational, financial, privacy or societal impact.",
"",
"| # | Year | Incident | What happened | Impact |", "|---:|---:|---|---|---|"]
for i, (year, name, brief, impact) in enumerate(items, 1):
    catalog.append(f"| {i} | {year} | {name} | {brief} | {impact} |")
catalog += ["", "## Further reading", "",
"- [CSIS – Significant Cyber Incidents](https://www.csis.org/programs/strategic-technologies-program/significant-cyber-incidents)",
"- [CERT-EU – Threat Landscape Report](https://cert.europa.eu/publications/tlr-10-years/)",
"- [FBI – Morris Worm history](https://www.fbi.gov/news/stories/morris-worm-30-years-since-first-major-attack-on-internet-110218)",
"- [Canadian Centre for Cyber Security – Operational technology incidents](https://www.cyber.gc.ca/en/guidance/cyber-threat-bulletin-cyber-threat-operational-technology)",
"- [MITRE ATT&CK – SolarWinds compromise](https://attack.mitre.org/campaigns/C0024/)",
"- [US GAO – SolarWinds and Microsoft Exchange](https://www.gao.gov/products/gao-22-104746)",
"",
"**Curation note:** Educational selection, not a definitive ranking. Some entries describe campaigns or broader incident patterns. Dates, attribution and impact figures should be verified against primary sources before formal reporting."]
(ROOT / "CYBER_INCIDENTS.md").write_text("\n".join(catalog) + "\n", encoding="utf-8")

# Render a typewriter-style animated GIF: each case is typed in,
# then held on screen before the next randomly selected incident begins.
WIDTH, HEIGHT = 1000, 260
BG = (8, 15, 20)
GREEN = (0, 255, 153)
WHITE = (225, 235, 240)
MUTED = (120, 150, 160)
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
BOLD_FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
title_font = ImageFont.truetype(BOLD_FONT_PATH, 22)
label_font = ImageFont.truetype(BOLD_FONT_PATH, 15)
body_font = ImageFont.truetype(FONT_PATH, 15)
small_font = ImageFont.truetype(FONT_PATH, 12)

def wrap_pixels(draw, text, font, max_width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=font)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines

def reveal_steps(text, chunk=18):
    """Return progressively longer text prefixes for a typewriter effect."""
    if not text:
        return [""]
    return [text[:end] for end in range(chunk, len(text), chunk)] + [text]

def render_case(year, name, brief, impact, number, brief_chars, impact_chars):
    frame = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(frame)
    draw.rectangle((0, 0, WIDTH, 6), fill=GREEN)
    draw.text((40, 22), "CYBER INCIDENT ARCHIVE  //  HISTORICAL CASE FILE", font=small_font, fill=MUTED)
    draw.text((40, 49), f"{year}  |  {name}", font=title_font, fill=GREEN)
    draw.line((40, 91, WIDTH - 40, 91), fill=(35, 75, 68), width=2)

    draw.text((40, 107), "WHAT HAPPENED", font=label_font, fill=WHITE)
    y = 135
    brief_lines = wrap_pixels(draw, brief, body_font, WIDTH - 80)
    remaining = brief_chars
    for line in brief_lines[:2]:
        visible = line[:max(0, min(len(line), remaining))]
        draw.text((40, y), visible, font=body_font, fill=WHITE)
        remaining -= len(line)
        y += 24

    y += 7
    draw.text((40, y), "IMPACT", font=label_font, fill=GREEN)
    y += 25
    impact_lines = wrap_pixels(draw, impact, body_font, WIDTH - 80)
    remaining = impact_chars
    for line in impact_lines[:2]:
        visible = line[:max(0, min(len(line), remaining))]
        draw.text((40, y), visible, font=body_font, fill=WHITE)
        remaining -= len(line)
        y += 24

    draw.text((WIDTH - 130, HEIGHT - 25), f"{number:03d} / 100", font=small_font, fill=MUTED)
    return frame

frames = []
durations = []
for index, (year, name, brief, impact) in enumerate(items, 1):
    probe = Image.new("RGB", (WIDTH, HEIGHT), BG)
    probe_draw = ImageDraw.Draw(probe)
    brief_lines = wrap_pixels(probe_draw, brief, body_font, WIDTH - 80)[:2]
    impact_lines = wrap_pixels(probe_draw, impact, body_font, WIDTH - 80)[:2]
    brief_text = " ".join(brief_lines)
    impact_text = " ".join(impact_lines)

    # Type the incident summary first, then the impact, and hold the
    # completed case on screen so the viewer has time to read it.
    for count in range(0, len(brief_text) + 1, 42):
        frames.append(render_case(year, name, brief, impact, index, count, 0))
        durations.append(110)
    frames.append(render_case(year, name, brief, impact, index, len(brief_text), 0))
    durations.append(160)

    for count in range(0, len(impact_text) + 1, 42):
        frames.append(render_case(year, name, brief, impact, index, len(brief_text), count))
        durations.append(90)
    frames.append(render_case(year, name, brief, impact, index, len(brief_text), len(impact_text)))
    durations.append(2400)

gif_path = ROOT / "assets" / "cyber-incident-ticker.gif"
gif_path.parent.mkdir(parents=True, exist_ok=True)
palette = frames[0].quantize(colors=96, method=Image.Quantize.MEDIANCUT)
frames = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
frames[0].save(
    gif_path, save_all=True, append_images=frames[1:],
    duration=durations, loop=0, optimize=True, disposal=2
)

readme = f"""<div align="center">

  <img src="https://raw.githubusercontent.com/ashAKT/ashAKT/main/assets/minimal-cyber-banner.svg" alt="The best defense begins before the attack" width="100%">

  <br><br>

  <img src="https://raw.githubusercontent.com/ashAKT/ashAKT/main/assets/cyber-incident-ticker.gif" alt="Typewriter-animated archive of 100 cybersecurity incidents, including what happened and the impact" width="100%">

</div>
"""
(ROOT / "README.md").write_text(readme, encoding="utf-8")
print(f"Generated a typewriter-animated ticker with {len(items)} incident cases and {len(frames)} animation frames.")
