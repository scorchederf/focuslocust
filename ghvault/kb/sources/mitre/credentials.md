---
parsed_by: focuslocust
source: mitre
type: generated
---
# Credentials

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1589.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Credentials](../../attack/techniques/T1589.001-credentials.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1589.001 |
| name | Credentials |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1589/001 |

## Preserved Source Material

```yaml
created: '2020-10-02T14:55:43.815Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may gather credentials that can be used during targeting. Account credentials gathered by adversaries
  may be those directly associated with the target victim organization or attempt to take advantage of the tendency for users
  to use the same passwords across personal and business accounts.


  Adversaries may gather credentials from potential victims in various ways, such as direct elicitation via [Phishing for
  Information](https://attack.mitre.org/techniques/T1598). Adversaries may also compromise sites then add malicious content
  designed to collect website authentication cookies from visitors.(Citation: ATT ScanBox) (Citation: Register Deloitte)(Citation:
  Register Uber)(Citation: Detectify Slack Tokens)(Citation: Forbes GitHub Creds)(Citation: GitHub truffleHog)(Citation: GitHub
  Gitrob)(Citation: CNET Leaks) Where multi-factor authentication (MFA) based on out-of-band communications is in use, adversaries
  may compromise a service provider to gain access to MFA codes and one-time passwords (OTP).(Citation: Okta Scatter Swine
  2022)


  Credential information may also be exposed to adversaries via leaks to online or other accessible data sets (ex: [Search
  Engines](https://attack.mitre.org/techniques/T1593/002), breach dumps, code repositories, etc.). Adversaries may purchase
  credentials from dark web markets, such as Russian Market and 2easy, or through access to Telegram channels that distribute
  logs from infostealer malware.(Citation: Bleeping Computer 2easy 2021)(Citation: SecureWorks Infostealers 2023)(Citation:
  Bleeping Computer Stealer Logs 2023)


  Gathering this information may reveal opportunities for other forms of reconnaissance (ex: [Search Open Websites/Domains](https://attack.mitre.org/techniques/T1593)
  or [Phishing for Information](https://attack.mitre.org/techniques/T1598)), establishing operational resources (ex: [Compromise
  Accounts](https://attack.mitre.org/techniques/T1586)), and/or initial access (ex: [External Remote Services](https://attack.mitre.org/techniques/T1133)
  or [Valid Accounts](https://attack.mitre.org/techniques/T1078)). '
external_references:
- external_id: T1589.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1589/001
- description: Bill Toulas. (2021, December 21). 2easy now a significant dark web marketplace for stolen data. Retrieved October
    7, 2024.
  source_name: Bleeping Computer 2easy 2021
  url: https://www.bleepingcomputer.com/news/security/2easy-now-a-significant-dark-web-marketplace-for-stolen-data/
- description: 'Blasco, J. (2014, August 28). Scanbox: A Reconnaissance Framework Used with Watering Hole Attacks. Retrieved
    October 19, 2020.'
  source_name: ATT ScanBox
  url: https://cybersecurity.att.com/blogs/labs-research/scanbox-a-reconnaissance-framework-used-on-watering-hole-attacks
- description: Detectify. (2016, April 28). Slack bot token leakage exposing business critical information. Retrieved November
    17, 2024.
  source_name: Detectify Slack Tokens
  url: https://labs.detectify.com/writeups/slack-bot-token-leakage-exposing-business-critical-information/
- description: Dylan Ayrey. (2016, December 31). truffleHog. Retrieved October 19, 2020.
  source_name: GitHub truffleHog
  url: https://github.com/dxa4481/truffleHog
- description: 'Flare. (2023, June 6). Dissecting the Dark Web Supply Chain: Stealer Logs in Context. Retrieved October 10,
    2024.'
  source_name: Bleeping Computer Stealer Logs 2023
  url: https://www.bleepingcomputer.com/news/security/dissecting-the-dark-web-supply-chain-stealer-logs-in-context/
- description: McCarthy, K. (2015, February 28). FORK ME! Uber hauls GitHub into court to find who hacked database of 50,000
    drivers. Retrieved October 19, 2020.
  source_name: Register Uber
  url: https://www.theregister.com/2015/02/28/uber_subpoenas_github_for_hacker_details/
- description: 'Michael Henriksen. (2018, June 9). Gitrob: Putting the Open Source in OSINT. Retrieved October 19, 2020.'
  source_name: GitHub Gitrob
  url: https://github.com/michenriksen/gitrob
- description: Ng, A. (2019, January 17). Massive breach leaks 773 million email addresses, 21 million passwords. Retrieved
    October 20, 2020.
  source_name: CNET Leaks
  url: https://www.cnet.com/news/massive-breach-leaks-773-million-emails-21-million-passwords/
- description: 'Okta. (2022, August 25). Detecting Scatter Swine: Insights into a Relentless Phishing Campaign. Retrieved
    February 24, 2023.'
  source_name: Okta Scatter Swine 2022
  url: https://sec.okta.com/scatterswine
- description: Sandvik, R. (2014, January 14). Attackers Scrape GitHub For Cloud Service Credentials, Hijack Account To Mine
    Virtual Currency. Retrieved October 19, 2020.
  source_name: Forbes GitHub Creds
  url: https://www.forbes.com/sites/runasandvik/2014/01/14/attackers-scrape-github-for-cloud-service-credentials-hijack-account-to-mine-virtual-currency/#242c479d3196
- description: SecureWorks Counter Threat Unit Research Team. (2023, May 16). The Growing Threat from Infostealers. Retrieved
    October 10, 2024.
  source_name: SecureWorks Infostealers 2023
  url: https://www.secureworks.com/research/the-growing-threat-from-infostealers
- description: 'Thomson, I. (2017, September 26). Deloitte is a sitting duck: Key systems with RDP open, VPN and proxy ''login
    details leaked''. Retrieved October 19, 2020.'
  source_name: Register Deloitte
  url: https://www.theregister.com/2017/09/26/deloitte_leak_github_and_google/
id: attack-pattern--bc76d0a4-db11-4551-9ac4-01a469cfb161
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:49:18.246Z'
name: Credentials
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Vinayak Wadhwa, Lucideus
- Lee Christensen, SpecterOps
- Toby Kohlenberg
- Massimo Giaimo, Würth Group Cyber Defence Center
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.2'
```
