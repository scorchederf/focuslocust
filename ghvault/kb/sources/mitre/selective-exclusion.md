---
parsed_by: focuslocust
source: mitre
type: generated
---
# Selective Exclusion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1679` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Selective Exclusion](../../attack/techniques/T1679-selective-exclusion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1679 |
| name | Selective Exclusion |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1679 |

## Preserved Source Material

```yaml
created: '2025-09-25T14:45:54.760Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may intentionally exclude certain files, folders, directories, file types, or system components\
  \ from encryption or tampering during a ransomware or malicious payload execution. Some file extensions that adversaries\
  \ may avoid encrypting include `.dll`, `.exe`, and `.lnk`.(Citation: Palo Alto Unit 42 Medusa Group Medusa Ransomware January\
  \ 2024)  \n\nAdversaries may perform this behavior to avoid alerting users, to evade detection by security tools and analysts,\
  \ or, in the case of ransomware, to ensure that the system remains operational enough to deliver the ransom notice. \n\n\
  Exclusions may target files and components whose corruption would cause instability, break core services, or immediately\
  \ expose the attack. By carefully avoiding these areas, adversaries maintain system responsiveness while minimizing indicators\
  \ that could trigger alarms or otherwise inhibit achieving their goals. "
external_references:
- external_id: T1679
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1679
- description: Anthony Galiette, Doel Santos. (2024, January 11). Medusa Ransomware Turning Your Files into Stone. Retrieved
    October 15, 2025.
  source_name: Palo Alto Unit 42 Medusa Group Medusa Ransomware January 2024
  url: https://unit42.paloaltonetworks.com/medusa-ransomware-escalation-new-leak-site/
id: attack-pattern--9b00925a-7c4b-4e53-bfc8-9a6a806fde03
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:32:31.453Z'
name: Selective Exclusion
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
- Windows
x_mitre_version: '2.0'
```
