---
parsed_by: focuslocust
source: mitre
type: generated
---
# Automated Collection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1119` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Automated Collection](../../attack/techniques/T1119-automated-collection.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1119 |
| name | Automated Collection |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1119 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:31:27.985Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Once established within a system or network, an adversary may use automated techniques for collecting internal\
  \ data. Methods for performing this technique could include use of a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059)\
  \ to search for and copy information fitting set criteria such as file type, location, or name at specific time intervals.\
  \ \n\nIn cloud-based environments, adversaries may also use cloud APIs, data pipelines, command line interfaces, or extract,\
  \ transform, and load (ETL) services to automatically collect data.(Citation: Mandiant UNC3944 SMS Phishing 2023) \n\nThis\
  \ functionality could also be built into remote access tools. \n\nThis technique may incorporate use of other techniques\
  \ such as [File and Directory Discovery](https://attack.mitre.org/techniques/T1083) and [Lateral Tool Transfer](https://attack.mitre.org/techniques/T1570)\
  \ to identify and move files, as well as [Cloud Service Dashboard](https://attack.mitre.org/techniques/T1538) and [Cloud\
  \ Storage Object Discovery](https://attack.mitre.org/techniques/T1619) to identify resources in cloud environments."
external_references:
- external_id: T1119
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1119
- description: Mandiant Intelligence. (2023, September 14). Why Are You Texting Me? UNC3944 Leverages SMS Phishing Campaigns
    for SIM Swapping, Ransomware, Extortion, and Notoriety. Retrieved January 2, 2024.
  source_name: Mandiant UNC3944 SMS Phishing 2023
  url: https://www.mandiant.com/resources/blog/unc3944-sms-phishing-sim-swapping-ransomware
id: attack-pattern--30208d3e-0d6b-43c8-883e-44462a514619
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:35.995Z'
name: Automated Collection
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Praetorian
- Arun Seelagan, CISA
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
- Linux
- macOS
- Office Suite
- SaaS
- Windows
x_mitre_version: '1.4'
```
