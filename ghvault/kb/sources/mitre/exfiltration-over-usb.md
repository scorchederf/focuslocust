---
parsed_by: focuslocust
source: mitre
type: generated
---
# Exfiltration over USB

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1052.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Exfiltration over USB](../../attack/techniques/T1052.001-exfiltration-over-usb.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1052.001 |
| name | Exfiltration over USB |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1052/001 |

## Preserved Source Material

```yaml
created: '2020-03-11T13:50:11.467Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: Adversaries may attempt to exfiltrate data over a USB connected physical device. In certain circumstances, such
  as an air-gapped network compromise, exfiltration could occur via a USB device introduced by a user. The USB device could
  be used as the final exfiltration point or to hop between otherwise disconnected systems.
external_references:
- external_id: T1052.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1052/001
id: attack-pattern--a3e1e6c5-9c74-4fc0-a16c-a9d228c17829
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:49:10.994Z'
name: Exfiltration over USB
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
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- Windows
- macOS
x_mitre_version: '1.2'
```
