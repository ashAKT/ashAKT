# Cyber Incident Case Studies

A research-led companion to the [100-incident catalogue](CYBER_INCIDENTS.md). Each case study looks beyond the incident name at the attack chain, operational disruption, people or systems affected, financial impact and defensive lessons.

> **How to read the figures:** Potential exposure is not confirmed compromise. People notified are not necessarily unique victims. Ransom, direct response costs, business interruption, settlement and estimated economic damage are different measures. Where a reliable consolidated figure is unavailable, this archive says so rather than inventing one.

## 1. NotPetya — 2017

**Type:** Destructive wiper · Software supply-chain compromise

- **Attack chain:** A compromised update mechanism for Ukrainian accounting software delivered the destructive payload. It spread laterally through enterprise networks, abusing credentials and Windows administration mechanisms.
- **Business reach:** International shipping, pharmaceutical, consumer-goods and professional-services companies were disrupted. Maersk reported IT outages across multiple sites and business units; some APM Terminals operations were affected.
- **Reported financial impact:** A Federal Reserve Bank of New York staff report summarised company disclosures of approximately **$300 million for Maersk**, **$670 million for Merck**, and **$180 million for Mondelez**. These are company-specific reported costs, not a single global-loss estimate.
- **Why it mattered:** A trusted software update became the entry point; weak segmentation and privileged credential reuse amplified the damage.
- **Defensive takeaways:** Secure build/update systems, segment networks, protect privileged credentials, monitor lateral movement and maintain tested offline recovery.

**Sources:** [Maersk incident update](https://investor.maersk.com/news-releases/news-release-details/cyber-attack-update) · [Federal Reserve Bank of New York staff report](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr937.pdf)

## 2. WannaCry — 2017

**Type:** Ransomware worm · SMB exploitation

- **Attack chain:** Exploited the Windows SMBv1 vulnerability addressed by Microsoft bulletin MS17-010, allowing rapid propagation between unpatched systems.
- **Global scale:** NHS England records approximately **200,000 PCs infected across 156 countries**.
- **Healthcare impact:** In England, around **80 of 236 NHS trusts** experienced disruption. The UK Parliament reported nearly **20,000 hospital appointments and operations cancelled**.
- **Financial impact:** The UK National Audit Office said the Department did not know the total cost of disruption to the NHS. Do not present an unverified NHS loss figure as confirmed.
- **Defensive takeaways:** Prioritise wormable vulnerabilities, retire unsupported systems, disable legacy SMB where possible, segment endpoints and test patching and restoration.

**Sources:** [NHS England case study](https://www.england.nhs.uk/long-read/case-study-wannacry-attack/) · [UK National Audit Office](https://www.nao.org.uk/reports/investigation-wannacry-cyber-attack-and-the-nhs/) · [UK Parliament report](https://publications.parliament.uk/pa/cm201719/cmselect/cmpubacc/787/78704.htm)

## 3. Equifax — 2017

**Type:** Data breach · Unpatched web application vulnerability

- **Attack chain:** Attackers exploited a vulnerability in an internet-facing Apache Struts application and accessed sensitive databases.
- **People affected:** Approximately **147 million consumers**. The FTC complaint cited at least **145.5 million Social Security numbers** and **209,000 payment-card numbers** among exposed information.
- **Financial / regulatory impact:** The 2019 global settlement was **at least $575 million and potentially up to $700 million**. This was a settlement and consumer-relief package, not a direct estimate of total breach cost.
- **Business impact:** Investigations, remediation, consumer support, litigation and long-term identity-theft concerns.
- **Defensive takeaways:** Maintain asset and vulnerability inventories, patch exposed applications, segment sensitive databases and monitor unusual database queries and data transfers.

**Sources:** [FTC settlement announcement](https://www.ftc.gov/news-events/news/press-releases/2019/07/equifax-pay-575-million-part-settlement-ftc-cfpb-states-related-2017-data-breach) · [CFPB enforcement summary](https://www.consumerfinance.gov/enforcement/actions/equifax-inc/)

## 4. SolarWinds SUNBURST — 2020

**Type:** Software supply-chain compromise · Espionage

- **Attack chain:** Malicious code was inserted into signed SolarWinds Orion software updates. Selected downstream victims were then targeted for follow-on access and espionage.
- **Exposure vs compromise:** SolarWinds initially said up to **18,000 customers** may have downloaded affected versions. It later estimated **fewer than 100 customers** had servers that communicated with attacker command-and-control infrastructure. These are different measures and must not be conflated.
- **Government impact:** FBI testimony identified **nine federal agencies** and fewer than 100 non-government entities in the relevant compromised category at that time.
- **Financial impact:** No single authoritative public global-loss figure has been established; victim costs included investigation, rebuild, remediation and legal work.
- **Defensive takeaways:** Secure build pipelines, protect code-signing systems, validate software provenance and monitor unusual outbound traffic from management servers.

**Sources:** [CISA joint advisory](https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a) · [FBI testimony](https://www.fbi.gov/news/speeches-and-testimony/understanding-and-responding-to-the-solarwinds-supply-chain-attack-the-federal-perspective) · [SolarWinds investigative update](https://www.solarwinds.com/blog/an-investigative-update-of-the-cyberattack)

## 5. Colonial Pipeline — 2021

**Type:** Ransomware · Critical infrastructure

- **Operational impact:** Colonial proactively shut down pipeline operations after detecting ransomware. The system was shut from **May 7 to May 13, 2021**, disrupting fuel distribution and prompting government coordination.
- **Ransom:** The company paid approximately **75 bitcoin**, reported at roughly **$4.4 million** at the time. The U.S. Department of Justice later seized 63.7 bitcoin valued at approximately **$2.3 million** at seizure time.
- **Important distinction:** The ransom is not the same as total business loss. A reliable consolidated total for all economic impact is not stated here.
- **Why it mattered:** A cyber incident in corporate IT led to a precautionary shutdown of physical energy infrastructure.
- **Defensive takeaways:** Separate IT and OT, rehearse manual operating procedures, secure remote access and test safety-critical incident-response plans.

**Sources:** [U.S. Department of Energy](https://www.energy.gov/ceser/colonial-pipeline-cyber-incident) · [U.S. Department of Justice](https://www.justice.gov/archives/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside) · [Colonial Pipeline statement](https://www.colpipe.com/news-insights/media-resources/post/media-statement-update-colonial-pipeline-system-disruption/)

## 6. MOVEit Transfer mass exploitation — 2023

**Type:** Zero-day exploitation · Mass data theft · Third-party risk

- **Attack chain:** The Cl0p extortion operation exploited a SQL-injection vulnerability in Progress MOVEit Transfer (CVE-2023-34362) to access systems and steal data.
- **Scale:** Emsisoft's public-disclosure tally dated **June 28, 2024** counted **2,773 organizations** and **95,788,491 individuals** known to have been impacted. It is a compiled disclosure count; overlap between organizations means it should not be treated as a precise unique-person total.
- **Healthcare example:** CMS said the MOVEit breach at contractor Maximus potentially affected approximately **612,000 current Medicare beneficiaries**.
- **Financial impact:** No single confirmed global loss figure. Costs include response, notification, legal exposure, monitoring and downstream customer impact.
- **Defensive takeaways:** Minimise internet exposure, patch rapidly, hunt for web shells and suspicious file access, rotate exposed secrets and map vendor data flows.

**Sources:** [Emsisoft MOVEit analysis](https://www.emsisoft.com/en/blog/44123/unpacking-the-moveit-breach-statistics-and-analysis/) · [CMS / Maximus notice](https://www.cms.gov/newsroom/press-releases/cms-responding-data-breach-contractor) · [UK NCSC guidance](https://www.ncsc.gov.uk/information/moveit-vulnerability)

## 7. Change Healthcare — 2024

**Type:** Ransomware · Healthcare ecosystem disruption

- **People affected:** UnitedHealth Group's 2024 SEC filing estimated approximately **190 million individuals** were impacted.
- **Business impact:** Claims processing, pharmacy workflows and provider payments were disrupted across the U.S. healthcare ecosystem. Providers experienced cash-flow pressure and operational disruption.
- **Financial impact:** UnitedHealth reported **$2.2 billion in direct response costs** for 2024 and estimated **$867 million in business disruption impacts** for the year. These are company-reported figures, not an independent estimate of all healthcare-sector losses.
- **Why it mattered:** A single intermediary outage propagated across a highly interconnected healthcare system.
- **Defensive takeaways:** Reduce single points of failure, establish tested downtime procedures, protect remote access with phishing-resistant MFA and validate third-party continuity plans.

**Sources:** [UnitedHealth 2024 Form 10-K (SEC)](https://www.sec.gov/Archives/edgar/data/731766/000073176625000063/unh-20241231.htm) · [CMS provider support response](https://www.cms.gov/newsroom/fact-sheets/change-healthcare-optum-payment-disruption-chopd-accelerated-payments-part-providers-advance)

## 8. 3CX supply-chain attack — 2023

**Type:** Software supply-chain compromise · Multi-stage intrusion

- **Attack chain:** MITRE ATT&CK describes a compromised X_Trader application leading to compromise of 3CX build environments and malicious 3CX desktop application updates.
- **Potential reach:** MITRE notes 3CX served **more than 600,000 customers and 12 million users**. This is the product's customer/user base—not the number of confirmed victims.
- **Targeting:** Follow-on activity focused on selected victims, including organizations in cryptocurrency and defence. Only a subset of the broad user base was affected.
- **Financial impact:** A reliable consolidated global loss figure has not been publicly established.
- **Defensive takeaways:** Validate updates, monitor endpoint behaviour after trusted application updates, use application control and investigate unusual child processes and outbound connections.

**Source:** [MITRE ATT&CK campaign C0057](https://attack.mitre.org/campaigns/C0057/)

## 9. Log4Shell — 2021

**Type:** Critical vulnerability · Remote code execution · Widespread exposure

- **Vulnerability:** CVE-2021-44228 affected Apache Log4j 2 and could allow remote code execution in vulnerable configurations.
- **Scale:** CISA's Cyber Safety Review Board described thousands of security professionals mobilising to identify and mitigate **hundreds of millions of potentially affected devices**. This is potential exposure/remediation scope, not confirmed compromise.
- **Business impact:** Organizations had to discover Log4j embedded in applications, products, appliances and cloud workloads, then patch or mitigate. Exploitation attempts began rapidly after disclosure.
- **Financial impact:** No authoritative single global loss figure. Costs were distributed across emergency discovery, patching, testing, service restarts and incident response.
- **Defensive takeaways:** Maintain software bills of materials, inventory transitive dependencies, scan containers and appliances, prioritise exposed assets and monitor exploit attempts.

**Source:** [CISA Cyber Safety Review Board Log4j report](https://www.cisa.gov/sites/default/files/2023-02/CSRB-Report-on-Log4-July-11-2022_508_0.pdf)

## Comparing incident impact correctly

| Metric | Meaning | Example |
|---|---|---|
| Potential exposure | Systems/users that could have been affected | SolarWinds: up to 18,000 affected-version downloads |
| Confirmed compromise | Systems with evidence of attacker access/activity | SolarWinds: vendor's later estimate of fewer than 100 communicating customers |
| People impacted | Individuals estimated or confirmed to have had data involved | Change Healthcare: approximately 190 million estimated individuals |
| Direct response cost | Investigation, restoration, notifications and support | Change Healthcare: $2.2 billion in 2024 |
| Business disruption | Estimated lost revenue or operating impact | Change Healthcare: $867 million in 2024 |
| Settlement / penalty | Legal or regulatory payment | Equifax: settlement up to $700 million |

## Research standards

- Prefer primary sources: SEC filings, regulators, government agencies, affected-company statements and incident-response reports.
- Record the publication date and date the metric was measured.
- Do not equate downloads with compromises, records with unique people, ransom with total loss, or settlement with direct incident cost.
- Where a reliable number is unavailable, state **“not publicly established”** rather than inventing an estimate.

*Educational resource, not a definitive ranking. Figures may change as investigations and disclosures are updated.*
