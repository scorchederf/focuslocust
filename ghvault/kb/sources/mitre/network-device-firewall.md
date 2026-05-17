---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Device Firewall

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1686.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Device Firewall](../../attack/techniques/T1686.002-network-device-firewall.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1686.002 |
| name | Network Device Firewall |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1686/002 |

## Preserved Source Material

```yaml
created: '2026-04-14T22:54:05.016Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may disable network device-based firewall mechanisms entirely or add, delete, or modify particular\
  \ rules in order to bypass controls limiting network usage.  \n\nAdversaries may obtain access to devices such as routers,\
  \ switches, or other perimeter/network devices and change access control lists (ACLs), security zones, or policy rules to\
  \ permit otherwise blocked traffic. For example, adversaries may add new network firewall rules to allow access to all internal\
  \ network subnets without restrictions. Allowing access to internal network subsets may enable unrestricted inbound/outbound\
  \ connectivity or open paths for command and control and lateral movement.\n\nAdversaries may obtain access to network device\
  \ management interfaces via [Valid Accounts](https://attack.mitre.org/techniques/T1078) or by exploiting vulnerabilities.\
  \ In some cases, threat actors may target firewalls and other network infrastructure that are exposed to the internet by\
  \ leveraging weaknesses in public-facing applications ([Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190)).(Citation:\
  \ CVE-2024-55591 Detail)\n\nAdversaries may also modify host networking configurations that indirectly manipulate system\
  \ firewalls, such as adjusting interface bandwidth or network connection request thresholds. "
external_references:
- external_id: T1686.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1686/002
- description: NIST NVD. (2025, January 22). Retrieved September 22, 2025.
  source_name: CVE-2024-55591 Detail
  url: https://nvd.nist.gov/vuln/detail/CVE-2024-55591
id: attack-pattern--a29aa77c-a88d-4f19-bab9-7751941b2e2d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-22T15:38:51.612Z'
name: Network Device Firewall
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Marco Pedrinazzi, @pedrinazziM, InTheCyber
- Tommaso Tosi, @tosto92, InTheCyber
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Network Devices
x_mitre_version: '1.0'
```
