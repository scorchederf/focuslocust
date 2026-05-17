---
parsed_by: focuslocust
source: mitre
type: generated
---
# Scheduled Transfer

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1029` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Scheduled Transfer](../../attack/techniques/T1029-scheduled-transfer.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1029 |
| name | Scheduled Transfer |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1029 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:34.139Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may schedule data exfiltration to be performed only at certain times of day or at certain intervals.
  This could be done to blend traffic patterns with normal activity or availability.


  When scheduled exfiltration is used, other exfiltration techniques likely apply as well to transfer the information out
  of the network, such as [Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041) or [Exfiltration Over
  Alternative Protocol](https://attack.mitre.org/techniques/T1048).'
external_references:
- external_id: T1029
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1029
id: attack-pattern--4eeaf8a9-c86b-4954-a663-9555fb406466
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:48:45.522Z'
name: Scheduled Transfer
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.1'
```
