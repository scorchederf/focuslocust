---
parsed_by: focuslocust
source: mitre
type: generated
---
# Financial Theft

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1657` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Financial Theft](../../attack/techniques/T1657-financial-theft.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1657 |
| name | Financial Theft |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1657 |

## Preserved Source Material

```yaml
created: '2023-08-18T20:50:04.222Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may steal monetary resources from targets through extortion, social engineering, technical theft,\
  \ or other methods aimed at their own financial gain at the expense of the availability of these resources for victims.\
  \ Financial theft is the ultimate objective of several popular campaign types including extortion by ransomware,(Citation:\
  \ FBI-ransomware) business email compromise (BEC) and fraud,(Citation: FBI-BEC) \"pig butchering,\"(Citation: wired-pig\
  \ butchering) bank hacking,(Citation: DOJ-DPRK Heist) and exploiting cryptocurrency networks.(Citation: BBC-Ronin) \n\n\
  Adversaries may [Compromise Accounts](https://attack.mitre.org/techniques/T1586) to conduct unauthorized transfers of funds.(Citation:\
  \ Internet crime report 2022) In the case of business email compromise or email fraud, an adversary may utilize [Impersonation](https://attack.mitre.org/techniques/T1684/001)\
  \ of a trusted entity. Once the social engineering is successful, victims can be deceived into sending money to financial\
  \ accounts controlled by an adversary.(Citation: FBI-BEC) This creates the potential for multiple victims (i.e., compromised\
  \ accounts as well as the ultimate monetary loss) in incidents involving financial theft.(Citation: VEC)\n\nExtortion by\
  \ ransomware may occur, for example, when an adversary demands payment from a victim after [Data Encrypted for Impact](https://attack.mitre.org/techniques/T1486)\
  \ (Citation: NYT-Colonial) and [Exfiltration](https://attack.mitre.org/tactics/TA0010) of data, followed by threatening\
  \ to leak sensitive data to the public unless payment is made to the adversary.(Citation: Mandiant-leaks) Adversaries may\
  \ use dedicated leak sites to distribute victim data.(Citation: Crowdstrike-leaks)\n\nDue to the potentially immense business\
  \ impact of financial theft, an adversary may abuse the possibility of financial theft and seeking monetary gain to divert\
  \ attention from their true goals such as [Data Destruction](https://attack.mitre.org/techniques/T1485) and business disruption.(Citation:\
  \ AP-NotPetya)"
external_references:
- external_id: T1657
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1657
- description: CloudFlare. (n.d.). What is vendor email compromise (VEC)?. Retrieved September 12, 2023.
  source_name: VEC
  url: https://www.cloudflare.com/learning/email-security/what-is-vendor-email-compromise/#:~:text=Vendor%20email%20compromise%2C%20also%20referred,steal%20from%20that%20vendor%27s%20customers.
- description: 'Crowdstrike. (2020, September 24). Double Trouble: Ransomware with Data Leak Extortion, Part 1. Retrieved
    December 6, 2023.'
  source_name: Crowdstrike-leaks
  url: https://www.crowdstrike.com/blog/double-trouble-ransomware-data-leak-extortion-part-1/
- description: DANIEL KAPELLMANN ZAFRA, COREY HIDELBRANDT, NATHAN BRUBAKER, KEITH LUNDEN. (2022, January 31). 1 in 7 OT Ransomware
    Extortion Attacks Leak Critical Operational Technology Information. Retrieved August 18, 2023.
  source_name: Mandiant-leaks
  url: https://www.mandiant.com/resources/blog/ransomware-extortion-ot-docs
- description: Department of Justice. (2021). 3 North Korean Military Hackers Indicted in Wide-Ranging Scheme to Commit Cyber-attacks
    and Financial Crimes Across the Globe. Retrieved August 18, 2023.
  source_name: DOJ-DPRK Heist
  url: https://www.justice.gov/usao-cdca/pr/3-north-korean-military-hackers-indicted-wide-ranging-scheme-commit-cyber-attacks-and
- description: FBI. (2022). FBI 2022 Congressional Report on BEC and Real Estate Wire Fraud. Retrieved August 18, 2023.
  source_name: FBI-BEC
  url: https://www.fbi.gov/file-repository/fy-2022-fbi-congressional-report-business-email-compromise-and-real-estate-wire-fraud-111422.pdf/view
- description: FBI. (n.d.). Ransomware. Retrieved August 18, 2023.
  source_name: FBI-ransomware
  url: https://www.cisa.gov/sites/default/files/Ransomware_Trifold_e-version.pdf
- description: FRANK BAJAK AND RAPHAEL SATTER. (2017, June 30). Companies still hobbled from fearsome cyberattack. Retrieved
    August 18, 2023.
  source_name: AP-NotPetya
  url: https://apnews.com/article/russia-ukraine-technology-business-europe-hacking-ce7a8aca506742ab8e8873e7f9f229c2
- description: IC3. (2022). 2022 Internet Crime Report. Retrieved August 18, 2023.
  source_name: Internet crime report 2022
  url: https://www.ic3.gov/Media/PDF/AnnualReport/2022_IC3Report.pdf
- description: 'Joe Tidy. (2022, March 30). Ronin Network: What a $600m hack says about the state of crypto. Retrieved August
    18, 2023.'
  source_name: BBC-Ronin
  url: https://www.bbc.com/news/technology-60933174
- description: Lily Hay Newman. (n.d.). ‘Pig Butchering’ Scams Are Now a $3 Billion Threat. Retrieved August 18, 2023.
  source_name: wired-pig butchering
  url: https://www.wired.com/story/pig-butchering-fbi-ic3-2022-report/
- description: Nicole Perlroth. (2021, May 13). Colonial Pipeline paid 75 Bitcoin, or roughly $5 million, to hackers.. Retrieved
    August 18, 2023.
  source_name: NYT-Colonial
  url: https://www.nytimes.com/2021/05/13/technology/colonial-pipeline-ransom.html
id: attack-pattern--851e071f-208d-4c79-adc6-5974c85c78f3
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: impact
modified: '2026-04-17T16:12:12.496Z'
name: Financial Theft
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Blake Strom, Microsoft Threat Intelligence
- Pawel Partyka, Microsoft Threat Intelligence
- Menachem Goldstein
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_impact_type:
- Availability
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Office Suite
- SaaS
- Windows
x_mitre_version: '1.2'
```
