---
parsed_by: focuslocust
source: mitre
type: generated
---
# Data from Removable Media

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1025` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Data from Removable Media](../../attack/techniques/T1025-data-from-removable-media.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1025 |
| name | Data from Removable Media |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1025 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:31.584Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may search connected removable media on computers they have compromised to find files of interest.\
  \ Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised\
  \ system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [cmd](https://attack.mitre.org/software/S0106)\
  \ may be used to gather information. \n\nSome adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T1119)\
  \ on removable media."
external_references:
- external_id: T1025
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1025
id: attack-pattern--1b7ba276-eedc-4951-a762-0ceea2c030ec
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: collection
modified: '2025-10-24T17:48:28.431Z'
name: Data from Removable Media
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
