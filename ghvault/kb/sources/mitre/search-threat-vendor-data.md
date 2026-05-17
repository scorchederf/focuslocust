---
parsed_by: focuslocust
source: mitre
type: generated
---
# Search Threat Vendor Data

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1681` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Search Threat Vendor Data](../../attack/techniques/T1681-search-threat-vendor-data.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1681 |
| name | Search Threat Vendor Data |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1681 |

## Preserved Source Material

```yaml
created: '2025-09-26T15:42:30.468Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Threat actors may seek information/indicators from closed or open threat intelligence sources gathered about\
  \ their own campaigns, as well as those conducted by other adversaries that may align with their target industries, capabilities/objectives,\
  \ or other operational concerns. These reports may include descriptions of behavior, detailed breakdowns of attacks, atomic\
  \ indicators such as malware hashes or IP addresses, timelines of a group’s activity, and more. Adversaries may change their\
  \ behavior when planning their future operations. \n\nAdversaries have been observed replacing atomic indicators mentioned\
  \ in blog posts in under a week.(Citation: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023) Adversaries have\
  \ also been seen searching for their own domain names in threat vendor data and then taking them down, likely to avoid seizure\
  \ or further investigation.(Citation: Sentinel One Contagious Interview ClickFix September 2025)\n\nThis technique is distinct\
  \ from [Threat Intel Vendors](https://attack.mitre.org/techniques/T1597/001) in that it describes threat actors performing\
  \ reconnaissance on their own activity, not in search of victim information. "
external_references:
- external_id: T1681
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1681
- description: Aleksandar Milenkoski, Sreekar Madabushi, Kenneth Kinion. (2025, September 4). Contagious Interview | North
    Korean Threat Actors Reveal Plans and Ops by Abusing Cyber Intel Platforms. Retrieved October 20, 2025.
  source_name: Sentinel One Contagious Interview ClickFix September 2025
  url: https://www.sentinelone.com/labs/contagious-interview-threat-actors-scout-cyber-intel-platforms-reveal-plans-and-ops/
- description: Alexander Marvi, Brad Slaybaugh, Ron Craft, and Rufus Brown. (2023, June 13). VMware ESXi Zero-Day Used by
    Chinese Espionage Actor to Perform Privileged Guest Operations on Compromised Hypervisors. Retrieved March 26, 2025.
  source_name: Google Cloud Threat Intelligence VMWare ESXi Zero-Day 2023
  url: https://cloud.google.com/blog/topics/threat-intelligence/vmware-esxi-zero-day-bypass/
id: attack-pattern--63b24abc-5702-4745-b1e4-ac70b20a43f2
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: reconnaissance
modified: '2025-10-24T17:48:51.996Z'
name: Search Threat Vendor Data
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.0'
```
