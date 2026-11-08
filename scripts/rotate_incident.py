#!/usr/bin/env python3
"""Randomly rotate a historical cyber-incident brief on the profile."""
from pathlib import Path
from urllib.parse import quote_plus
import random, re

ROOT = Path(__file__).resolve().parents[1]
DATA = """1988|Morris Worm|An early internet worm spread uncontrollably and disrupted thousands of Unix systems.
1994|Citibank online bank robbery|Attackers used compromised banking systems to attempt fraudulent international transfers.
1999|Melissa|A macro virus spread through Outlook address books and overwhelmed corporate email systems.
2000|ILOVEYOU|A malicious email attachment spread globally, overwriting files and stealing credentials.
2001|Code Red|A worm exploited Microsoft IIS and rapidly compromised internet-facing web servers.
2001|Nimda|A multi-vector worm spread through email, web servers, network shares and vulnerable clients.
2003|SQL Slammer|A tiny worm exploited SQL Server and caused widespread network congestion within minutes.
2003|Blaster|Malware exploited a Windows RPC vulnerability and triggered widespread system instability.
2004|Sasser|A Windows worm exploited LSASS and spread without requiring user interaction.
2005|TJX breach|Payment-card and personal data were stolen after network security weaknesses were exploited.
2007|Estonia DDoS attacks|DDoS campaigns disrupted government, banking and media services.
2007|Zeus banking trojan|Credential-stealing malware targeted online banking and industrialized financial cybercrime.
2008|Conficker|A Windows worm used multiple propagation methods and created a massive botnet.
2008|Heartland Payment Systems|Payment-card data was stolen in a major breach involving malware.
2009|Operation Aurora|Targeted intrusions compromised major technology companies and sought intellectual property.
2010|Stuxnet|A sophisticated worm manipulated industrial control systems and damaged Iranian nuclear centrifuges.
2011|RSA SecurID breach|Attackers stole information related to RSA token technology, creating downstream authentication risk.
2011|Sony PlayStation Network|A major intrusion exposed personal information and forced a prolonged service shutdown.
2011|DigiNotar CA compromise|Fraudulent certificates enabled interception of trusted encrypted connections.
2012|Shamoon|A destructive wiper erased data on tens of thousands of computers at Saudi Aramco.
2012|LinkedIn breach|Password hashes for millions of accounts were stolen and later circulated.
2013|Adobe breach|Attackers stole customer credentials and source-code-related data at large scale.
2013|Target breach|Stolen vendor credentials enabled access to payment systems and theft of card data.
2013|Yahoo breach|Attackers accessed Yahoo accounts in a breach later estimated to affect billions of accounts.
2013|Bangladesh Bank SWIFT heist preparation|Attackers compromised bank systems and prepared fraudulent SWIFT payment instructions.
2014|Yahoo breach disclosure|Yahoo disclosed a massive account compromise ultimately estimated at about three billion accounts.
2014|Sony Pictures|Destructive malware and data theft disrupted a major entertainment company and leaked internal files.
2014|JPMorgan Chase breach|Attackers accessed customer contact information at one of the largest US banks.
2014|Home Depot breach|Payment-card data was stolen after attackers gained access through compromised credentials.
2014|German steel mill attack|A cyber intrusion disrupted industrial control processes and caused physical equipment damage.
2015|US OPM breach|Sensitive personnel and background-investigation records were stolen from a federal agency.
2015|Anthem breach|Personal information of nearly 79 million people was exposed in a major healthcare breach.
2015|Ukraine power grid|Attackers remotely disrupted electricity distribution, demonstrating cyber-physical impact.
2016|Bangladesh Bank heist|Fraudulent SWIFT transfers stole about $81 million from the central bank's account.
2016|Mirai botnet|Malware hijacked poorly secured IoT devices and launched record-scale DDoS attacks.
2016|Dyn DNS attack|Mirai-powered DDoS traffic disrupted DNS services and made major websites unreachable.
2016|Shadow Brokers leak|Exploit tools attributed to the NSA were leaked, including EternalBlue.
2016|DNC email compromise|Political campaign emails were stolen and publicly released.
2016|Operation Ghoul / banking malware campaigns|Credential theft and targeted malware demonstrated the growing scale of financially motivated intrusions.
2017|WannaCry|Ransomware used EternalBlue to spread rapidly across more than 150 countries.
2017|NotPetya|A destructive wiper spread through a compromised software update and caused billions in losses.
2017|Equifax breach|An unpatched web application vulnerability exposed sensitive information of about 147 million people.
2017|CCleaner supply-chain compromise|Attackers inserted a backdoor into legitimate software distributed to users.
2017|Triton / Trisis|Malware targeted industrial safety systems, raising the risk of physical harm.
2017|Uber breach disclosure|Attackers accessed personal data and the company paid intruders to conceal the incident.
2018|Marriott / Starwood breach|Guest records from the Starwood reservation environment were exposed at enormous scale.
2018|SingHealth breach|Health records of about 1.5 million people in Singapore were stolen.
2018|Exactis data exposure|A publicly accessible database exposed personal information on hundreds of millions of people.
2018|Coincheck theft|Cryptocurrency worth roughly $530 million was stolen from the exchange.
2019|Capital One breach|A cloud access-control weakness exposed data of about 100 million people.
2019|Norsk Hydro ransomware|LockerGoga disrupted global aluminium operations and forced manual processes.
2019|Baltimore city ransomware|RobbinHood ransomware disrupted municipal services and caused substantial recovery costs.
2019|Citrix ADC exploitation|Attackers exploited gateway flaws to access enterprise networks.
2020|SolarWinds SUNBURST|A compromised software build process inserted a backdoor into trusted Orion updates.
2020|Twitter account takeover|Social engineering of employees enabled attackers to hijack high-profile accounts.
2020|Garmin ransomware|A ransomware incident disrupted services and business operations.
2020|Blackbaud ransomware|A ransomware attack exposed data held by a widely used cloud services provider.
2020|Microsoft Exchange ecosystem attacks|Exchange weaknesses became a major route for enterprise compromise and persistence.
2021|Microsoft Exchange ProxyLogon|Chained zero-days enabled unauthenticated server compromise and web-shell deployment.
2021|Colonial Pipeline|Ransomware forced a major US fuel pipeline operator to suspend operations.
2021|Kaseya VSA|REvil abused a managed-service platform to distribute ransomware to downstream customers.
2021|Accellion FTA|Zero-day exploitation enabled data theft from organizations using a legacy file-transfer appliance.
2021|Log4Shell|A critical Log4j flaw enabled remote code execution across many exposed Java applications.
2021|Codecov supply-chain compromise|A modified code-coverage tool exported secrets from customer CI environments.
2021|Twitch source-code leak|A large data dump exposed source code, creator payout data and internal information.
2022|Costa Rica ransomware crisis|Ransomware disrupted government services and led to a national emergency declaration.
2022|Ronin Network hack|Attackers stole cryptocurrency worth roughly $625 million from a blockchain bridge.
2022|Uber breach|Social engineering and MFA fatigue helped an intruder access internal systems.
2022|Medibank breach|Criminals stole sensitive personal and health information from millions of customers.
2022|LastPass breach|Intruders accessed development information and later obtained encrypted customer vault backups.
2022|Optus breach|Personal information of millions of Australian customers was exposed.
2023|MOVEit Transfer|Cl0p exploited a zero-day in file-transfer software to steal data from many organizations.
2023|MGM Resorts|Social engineering led to major operational disruption across hotel and casino systems.
2023|Caesars Entertainment|A social-engineering-led intrusion resulted in data theft and a reported ransom payment.
2023|3CX supply-chain attack|A compromised software build chain distributed malware through a trusted business application.
2023|Barracuda ESG zero-day|Attackers exploited an appliance vulnerability and compromised email security gateways.
2023|T-Mobile API breach|Customer data was accessed through an API-related exposure.
2023|Microsoft Storm-0558|A stolen signing key enabled access to email accounts at multiple organizations.
2023|Okta support-system breach|Attackers accessed customer support files and session-related information.
2023|23andMe credential stuffing|Reused passwords enabled access to user accounts and related profile data.
2023|ICBC Financial Services ransomware|A ransomware incident disrupted US broker-dealer operations and Treasury-market settlement activity.
2024|Change Healthcare|Ransomware severely disrupted US healthcare claims, payments and prescription workflows.
2024|Snowflake customer-account attacks|Stolen credentials were used to access customer environments and exfiltrate data.
2024|CDK Global ransomware|A cyberattack disrupted dealership management systems across much of the US auto retail sector.
2024|Ticketmaster / Live Nation data theft|A cloud-hosted dataset was advertised for sale after unauthorized access claims.
2024|Synnovis ransomware|A ransomware attack disrupted pathology services and affected London hospitals.
2024|Sisense breach|A compromise exposed customer-related credentials and prompted urgent security guidance.
2024|National Public Data breach|A large dataset containing personal information was exposed and circulated online.
2024|Salt Typhoon telecom intrusions|A state-linked espionage campaign compromised telecom providers and accessed sensitive communications data.
2024|AnyDesk compromise|Attackers accessed parts of the company's production systems and code-signing-related environment.
2024|Ivanti Connect Secure exploitation|Zero-day vulnerabilities were used to compromise perimeter appliances and maintain access.
2025|Bybit cryptocurrency theft|Attackers stole approximately $1.5 billion in digital assets in one of the largest crypto heists.
2025|PowerSchool data breach|A compromised support credential enabled theft of student and staff information from school districts.
2025|Marks & Spencer cyber disruption|A cyberattack disrupted retail operations, online services and customer-facing processes.
2025|Co-op cyberattack|A major UK retailer suffered disruption and reported customer data theft.
2025|Jaguar Land Rover cyberattack|A major incident halted production and disrupted supply chains and business operations.
2025|Salt Typhoon follow-on investigations|Telecom espionage investigations highlighted the risk of persistent access to communications infrastructure.
2025|Oracle Cloud credential exposure claims|Reports of stolen credentials and customer data triggered investigations and disputed claims.
2025|Global ransomware and identity-driven intrusions|A wave of attacks reinforced the role of stolen credentials, social engineering and third-party access.
2025|Healthcare ransomware ecosystem|Attacks on healthcare providers and suppliers exposed systemic dependence on shared digital infrastructure.
2025|Third-party SaaS compromise campaigns|Credential and token theft from cloud vendors highlighted risks in interconnected enterprise services."""
items = [tuple(line.split("|", 2)) for line in DATA.splitlines() if line.strip()]
if len(items) < 100:
    raise SystemExit(f"Expected at least 100 entries, got {len(items)}")
items = items[:100]

catalog = ["# 100 landmark cybersecurity incidents", "",
"Short historical briefs spanning malware, espionage, data breaches, ransomware, supply-chain compromise, financial theft and critical infrastructure.",
"",
"| # | Year | Incident | Brief |", "|---:|---:|---|---|"]
for i, (year, name, brief) in enumerate(items, 1):
    catalog.append(f"| {i} | {year} | {name} | {brief} |")
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

# Shuffle the complete list and build a continuously animated typing-SVG URL.
# The external typing-SVG renderer is used because GitHub's README image proxy
# does not reliably play SVG SMIL animations.
random.shuffle(items)
incident_lines = ";".join(f"{year} / {name}" for year, name, _ in items)
typing_url = (
    "https://readme-typing-svg.demolab.com/?"
    "font=Fira+Code&size=16&pause=900&color=00FF99"
    "&center=true&vCenter=true&width=1000&height=50"
    "&repeat=true&lines=" + quote_plus(incident_lines)
)
readme = f"""<div align="center">

  <img src="https://raw.githubusercontent.com/ashAKT/ashAKT/main/assets/minimal-cyber-banner.svg" alt="The best defense begins before the attack" width="100%">

  <br><br>

  <img src="{typing_url}" alt="Continuously rotating briefs of 100 landmark cybersecurity incidents" width="100%">

</div>
"""
(ROOT / "README.md").write_text(readme, encoding="utf-8")
print(f"Generated continuously animated ticker URL for {len(items)} incidents ({len(typing_url)} URL characters).")
