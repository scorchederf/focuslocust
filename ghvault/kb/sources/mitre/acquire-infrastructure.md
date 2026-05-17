---
parsed_by: focuslocust
source: mitre
type: generated
---
# Acquire Infrastructure

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1583` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Acquire Infrastructure](../../attack/techniques/T1583-acquire-infrastructure.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1583 |
| name | Acquire Infrastructure |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1583 |

## Preserved Source Material

```yaml
created: '2020-09-30T16:37:40.271Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may buy, lease, rent, or obtain infrastructure that can be used during targeting. A wide variety
  of infrastructure exists for hosting and orchestrating adversary operations. Infrastructure solutions include physical or
  cloud servers, domains, and third-party web services.(Citation: TrendmicroHideoutsLease) Some infrastructure providers offer
  free trial periods, enabling infrastructure acquisition at limited to no cost.(Citation: Free Trial PurpleUrchin) Additionally,
  botnets are available for rent or purchase.


  Use of these infrastructure solutions allows adversaries to stage, launch, and execute operations. Solutions may help adversary
  operations blend in with traffic that is seen as normal, such as contacting third-party web services or acquiring infrastructure
  to support [Proxy](https://attack.mitre.org/techniques/T1090), including from residential proxy services.(Citation: amnesty_nso_pegasus)(Citation:
  FBI Proxies Credential Stuffing)(Citation: Mandiant APT29 Microsoft 365 2022) Depending on the implementation, adversaries
  may use infrastructure that makes it difficult to physically tie back to them as well as utilize infrastructure that can
  be rapidly provisioned, modified, and shut down.'
external_references:
- external_id: T1583
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1583
- description: 'Amnesty International Security Lab. (2021, July 18). Forensic Methodology Report: How to catch NSO Group’s
    Pegasus. Retrieved February 22, 2022.'
  source_name: amnesty_nso_pegasus
  url: https://www.amnesty.org/en/latest/research/2021/07/forensic-methodology-report-how-to-catch-nso-groups-pegasus/
- description: 'Douglas Bienstock. (2022, August 18). You Can’t Audit Me: APT29 Continues Targeting Microsoft 365. Retrieved
    February 23, 2023.'
  source_name: Mandiant APT29 Microsoft 365 2022
  url: https://www.mandiant.com/resources/blog/apt29-continues-targeting-microsoft
- description: FBI. (2022, August 18). Proxies and Configurations Used for Credential Stuffing Attacks on Online Customer
    Accounts . Retrieved July 6, 2023.
  source_name: FBI Proxies Credential Stuffing
  url: https://www.ic3.gov/Media/News/2022/220818.pdf
- description: Gamazo, William. Quist, Nathaniel.. (2023, January 5). PurpleUrchin Bypasses CAPTCHA and Steals Cloud Platform
    Resources. Retrieved February 28, 2024.
  source_name: Free Trial PurpleUrchin
  url: https://unit42.paloaltonetworks.com/purpleurchin-steals-cloud-resources/
- description: Koczwara, M. (2021, September 7). Hunting Cobalt Strike C2 with Shodan. Retrieved October 12, 2021.
  source_name: Koczwara Beacon Hunting Sep 2021
  url: https://michaelkoczwara.medium.com/cobalt-strike-c2-hunting-with-shodan-c448d501a6e2
- description: 'Max Goncharov. (2015, July 15). Criminal Hideouts for Lease: Bulletproof Hosting Services. Retrieved March
    6, 2017.'
  source_name: TrendmicroHideoutsLease
  url: https://documents.trendmicro.com/assets/wp/wp-criminal-hideouts-for-lease.pdf
- description: Stephens, A. (2020, July 13). SCANdalous! (External Detection Using Network Scan Data and Automation). Retrieved
    November 17, 2024.
  source_name: Mandiant SCANdalous Jul 2020
  url: https://cloud.google.com/blog/topics/threat-intelligence/scandalous-external-detection-using-network-scan-data-and-automation/
- description: 'ThreatConnect. (2020, December 15). Infrastructure Research and Hunting: Boiling the Domain Ocean. Retrieved
    October 12, 2021.'
  source_name: ThreatConnect Infrastructure Dec 2020
  url: https://threatconnect.com/blog/infrastructure-research-hunting/
id: attack-pattern--0458aab9-ad42-4eac-9e22-706a95bafee2
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-10-24T17:48:20.468Z'
name: Acquire Infrastructure
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Shailesh Tiwary (Indian Army)
- Menachem Goldstein
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.5'
```
