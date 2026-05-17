---
parsed_by: focuslocust
source: mitre
type: generated
---
# Exfiltration Over Other Network Medium

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1011` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Exfiltration Over Other Network Medium](../../attack/techniques/T1011-exfiltration-over-other-network-medium.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1011 |
| name | Exfiltration Over Other Network Medium |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1011 |

## Preserved Source Material

```yaml
created: '2017-05-31T21:30:25.159Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to exfiltrate data over a different network medium than the command and control channel.
  If the command and control network is a wired Internet connection, the exfiltration may occur, for example, over a WiFi
  connection, modem, cellular data connection, Bluetooth, or another radio frequency (RF) channel.


  Adversaries may choose to do this if they have sufficient access or proximity, and the connection might not be secured or
  defended as well as the primary Internet-connected channel because it is not routed through the same enterprise network.'
external_references:
- external_id: T1011
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1011
id: attack-pattern--51ea26b1-ff1e-4faa-b1a0-1114cd298c87
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: exfiltration
modified: '2025-10-24T17:48:47.042Z'
name: Exfiltration Over Other Network Medium
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Itzik Kotler, SafeBreach
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.2'
```
