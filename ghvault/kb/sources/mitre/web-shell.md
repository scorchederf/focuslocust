---
parsed_by: focuslocust
source: mitre
type: generated
---
# Web Shell

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1505.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Web Shell](../../attack/techniques/T1505.003-web-shell.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1505.003 |
| name | Web Shell |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1505/003 |

## Preserved Source Material

```yaml
created: '2019-12-13T16:46:18.927Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may backdoor web servers with web shells to establish persistent access to systems. A Web shell
  is a Web script that is placed on an openly accessible Web server to allow an adversary to access the Web server as a gateway
  into a network. A Web shell may provide a set of functions to execute or a command-line interface on the system that hosts
  the Web server.(Citation: volexity_0day_sophos_FW)


  In addition to a server-side script, a Web shell may have a client interface program that is used to talk to the Web server
  (e.g. [China Chopper](https://attack.mitre.org/software/S0020) Web shell client).(Citation: Lee 2013)'
external_references:
- external_id: T1505.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1505/003
- description: ' NSA Cybersecurity Directorate. (n.d.). Mitigating Web Shells. Retrieved July 22, 2021.'
  source_name: NSA Cyber Mitigating Web Shells
  url: https://github.com/nsacyber/Mitigating-Web-Shells
- description: 'Adair, S., Lancaster, T., Volexity Threat Research. (2022, June 15). DriftingCloud: Zero-Day Sophos Firewall
    Exploitation and an Insidious Breach. Retrieved July 1, 2022.'
  source_name: volexity_0day_sophos_FW
  url: https://www.volexity.com/blog/2022/06/15/driftingcloud-zero-day-sophos-firewall-exploitation-and-an-insidious-breach/
- description: Lee, T., Hanzlik, D., Ahl, I. (2013, August 7). Breaking Down the China Chopper Web Shell - Part I. Retrieved
    March 27, 2015.
  source_name: Lee 2013
  url: https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-i.html
- description: US-CERT. (2015, November 13). Compromised Web Servers and Web Shells - Threat Awareness and Guidance. Retrieved
    June 8, 2016.
  source_name: US-CERT Alert TA15-314A Web Shells
  url: https://www.us-cert.gov/ncas/alerts/TA15-314A
id: attack-pattern--5d0d3609-d06d-49e1-b9c9-b544e0c618cb
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:48:50.387Z'
name: Web Shell
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Arnim Rupp, Deutsche Lufthansa AG
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '1.5'
```
