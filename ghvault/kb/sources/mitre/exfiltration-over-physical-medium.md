---
parsed_by: focuslocust
source: mitre
type: generated
---
# Exfiltration Over Physical Medium

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1052` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Exfiltration Over Physical Medium](../../attack/techniques/T1052-exfiltration-over-physical-medium.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1052 |
| name | Exfiltration Over Physical Medium |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1052 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:46.461Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Adversaries may attempt to exfiltrate data via a physical medium, such as a removable drive. In certain circumstances,
  such as an air-gapped network compromise, exfiltration could occur via a physical medium or device introduced by a user.
  Such media could be an external hard drive, USB drive, cellular phone, MP3 player, or other removable storage and processing
  device. The physical medium or device could be used as the final exfiltration point or to hop between otherwise disconnected
  systems.
external_references:
- external_id: T1052
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1052
id: attack-pattern--e6415f09-df0e-48de-9aba-928c902b7549
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:49:32.547Z'
name: Exfiltration Over Physical Medium
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- William Cain
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.3'
```
