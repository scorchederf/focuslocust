---
parsed_by: focuslocust
source: mitre
type: generated
---
# Server Software Component

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1505` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Server Software Component](../../attack/techniques/T1505-server-software-component.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1505 |
| name | Server Software Component |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1505 |

## Preserved Source Material

```yaml
created: '2019-06-28T17:52:07.296Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse legitimate extensible development features of servers to establish persistent access to
  systems. Enterprise server applications may include features that allow developers to write and install software or scripts
  to extend the functionality of the main application. Adversaries may install malicious components to extend and abuse server
  applications.(Citation: volexity_0day_sophos_FW)'
external_references:
- external_id: T1505
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1505
- description: 'Adair, S., Lancaster, T., Volexity Threat Research. (2022, June 15). DriftingCloud: Zero-Day Sophos Firewall
    Exploitation and an Insidious Breach. Retrieved July 1, 2022.'
  source_name: volexity_0day_sophos_FW
  url: https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/
- description: US-CERT. (2015, November 13). Compromised Web Servers and Web Shells - Threat Awareness and Guidance. Retrieved
    June 8, 2016.
  source_name: US-CERT Alert TA15-314A Web Shells
  url: https://www.us-cert.gov/ncas/alerts/TA15-314A
id: attack-pattern--d456de47-a16f-4e46-8980-e67478a12dcb
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:49:27.065Z'
name: Server Software Component
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
- Windows
- Linux
- macOS
- Network Devices
- ESXi
x_mitre_version: '1.5'
```
