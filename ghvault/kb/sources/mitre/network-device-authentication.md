---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Device Authentication

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1556.004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Device Authentication](../../attack/techniques/T1556.004-network-device-authentication.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1556.004 |
| name | Network Device Authentication |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1556/004 |

## Preserved Source Material

```yaml
created: '2020-10-19T17:58:04.155Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may use [Patch System Image](https://attack.mitre.org/techniques/T1601/001) to hard code a password
  in the operating system, thus bypassing of native authentication mechanisms for local accounts on network devices.


  [Modify System Image](https://attack.mitre.org/techniques/T1601) may include implanted code to the operating system for
  network devices to provide access for adversaries using a specific password.  The modification includes a specific password
  which is implanted in the operating system image via the patch.  Upon authentication attempts, the inserted code will first
  check to see if the user input is the password. If so, access is granted. Otherwise, the implanted code will pass the credentials
  on for verification of potentially valid credentials.(Citation: Mandiant - Synful Knock)'
external_references:
- external_id: T1556.004
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1556/004
- description: Bill Hau, Tony Lee, Josh Homan. (2015, September 15). SYNful Knock - A Cisco router implant - Part I. Retrieved
    November 17, 2024.
  source_name: Mandiant - Synful Knock
  url: https://cloud.google.com/blog/topics/threat-intelligence/synful-knock-acis/
id: attack-pattern--fa44a152-ac48-441e-a524-dd7b04b8adcd
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2026-04-16T20:07:53.117Z'
name: Network Device Authentication
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Network Devices
x_mitre_version: '3.0'
```
