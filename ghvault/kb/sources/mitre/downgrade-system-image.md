---
parsed_by: focuslocust
source: mitre
type: generated
---
# Downgrade System Image

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1601.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Downgrade System Image](../../attack/techniques/T1601.002-downgrade-system-image.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1601.002 |
| name | Downgrade System Image |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1601/002 |

## Preserved Source Material

```yaml
created: '2020-10-19T19:53:10.576Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may install an older version of the operating system of a network device to weaken security.  Older
  operating system versions on network devices often have weaker encryption ciphers and, in general, fewer/less updated defensive
  features. (Citation: Cisco Synful Knock Evolution)


  On embedded devices, downgrading the version typically only requires replacing the operating system file in storage.  With
  most embedded devices, this can be achieved by downloading a copy of the desired version of the operating system file and
  reconfiguring the device to boot from that file on next system restart.  The adversary could then restart the device to
  implement the change immediately or they could wait until the next time the system restarts.


  Downgrading the system image to an older versions may allow an adversary to evade defenses by enabling behaviors such as
  [Weaken Encryption](https://attack.mitre.org/techniques/T1600).  Downgrading of a system image can be done on its own, or
  it can be used in conjunction with [Patch System Image](https://attack.mitre.org/techniques/T1601/001).  '
external_references:
- external_id: T1601.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1601/002
- description: Graham Holmes. (2015, October 8). Evolution of attacks on Cisco IOS devices. Retrieved October 19, 2020.
  source_name: Cisco Synful Knock Evolution
  url: https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices
id: attack-pattern--fc74ba38-dc98-461f-8611-b3dbf9978e3d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:53.109Z'
name: Downgrade System Image
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
x_mitre_version: '2.0'
```
