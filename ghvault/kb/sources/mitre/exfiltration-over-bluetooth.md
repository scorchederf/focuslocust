---
parsed_by: focuslocust
source: mitre
type: generated
---
# Exfiltration Over Bluetooth

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1011.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Exfiltration Over Bluetooth](../../attack/techniques/T1011.001-exfiltration-over-bluetooth.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1011.001 |
| name | Exfiltration Over Bluetooth |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1011/001 |

## Preserved Source Material

```yaml
created: '2020-03-09T17:07:57.392Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to exfiltrate data over Bluetooth rather than the command and control channel. If the
  command and control network is a wired Internet connection, an adversary may opt to exfiltrate data using a Bluetooth communication
  channel.


  Adversaries may choose to do this if they have sufficient access and proximity. Bluetooth connections might not be secured
  or defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.'
external_references:
- external_id: T1011.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1011/001
id: attack-pattern--613d08bc-e8f4-4791-80b0-c8b974340dfd
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:48:51.095Z'
name: Exfiltration Over Bluetooth
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.2'
```
