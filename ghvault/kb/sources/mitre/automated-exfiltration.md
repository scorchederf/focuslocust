---
parsed_by: focuslocust
source: mitre
type: generated
---
# Automated Exfiltration

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1020` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Automated Exfiltration](../../attack/techniques/T1020-automated-exfiltration.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1020 |
| name | Automated Exfiltration |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1020 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:29.458Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may exfiltrate data, such as sensitive documents, through the use of automated processing after\
  \ being gathered during Collection.(Citation: ESET Gamaredon June 2020) \n\nWhen automated exfiltration is used, other exfiltration\
  \ techniques likely apply as well to transfer the information out of the network, such as [Exfiltration Over C2 Channel](https://attack.mitre.org/techniques/T1041)\
  \ and [Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048)."
external_references:
- external_id: T1020
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1020
- description: Boutin, J. (2020, June 11). Gamaredon group grows its game. Retrieved June 16, 2020.
  source_name: ESET Gamaredon June 2020
  url: https://www.welivesecurity.com/2020/06/11/gamaredon-group-grows-its-game/
id: attack-pattern--774a3188-6ba9-4dc4-879d-d54ee48a5ce9
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:48:58.340Z'
name: Automated Exfiltration
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- ExtraHop
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.3'
```
