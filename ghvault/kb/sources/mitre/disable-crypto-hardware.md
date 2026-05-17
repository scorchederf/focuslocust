---
parsed_by: focuslocust
source: mitre
type: generated
---
# Disable Crypto Hardware

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1600.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Disable Crypto Hardware](../../attack/techniques/T1600.002-disable-crypto-hardware.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1600.002 |
| name | Disable Crypto Hardware |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1600/002 |

## Preserved Source Material

```yaml
created: '2020-10-19T19:11:18.757Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries disable a network device’s dedicated hardware encryption, which may enable them to leverage weaknesses
  in software encryption in order to reduce the effort involved in collecting, manipulating, and exfiltrating transmitted
  data.


  Many network devices such as routers, switches, and firewalls, perform encryption on network traffic to secure transmission
  across networks. Often, these devices are equipped with special, dedicated encryption hardware to greatly increase the speed
  of the encryption process as well as to prevent malicious tampering. When an adversary takes control of such a device, they
  may disable the dedicated hardware, for example, through use of [Modify System Image](https://attack.mitre.org/techniques/T1601),
  forcing the use of software to perform encryption on general processors. This is typically used in conjunction with attacks
  to weaken the strength of the cipher in software (e.g., [Reduce Key Space](https://attack.mitre.org/techniques/T1600/001)).
  (Citation: Cisco Blog Legacy Device Attacks)'
external_references:
- external_id: T1600.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1600/002
- description: Omar Santos. (2020, October 19). Attackers Continue to Target Legacy Devices. Retrieved October 20, 2020.
  source_name: Cisco Blog Legacy Device Attacks
  url: https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954
id: attack-pattern--7efba77e-3bc4-4ca5-8292-d8201dcd64b5
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:53.028Z'
name: Disable Crypto Hardware
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
