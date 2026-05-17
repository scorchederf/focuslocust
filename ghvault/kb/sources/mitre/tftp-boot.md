---
parsed_by: focuslocust
source: mitre
type: generated
---
# TFTP Boot

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1542.005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [TFTP Boot](../../attack/techniques/T1542.005-tftp-boot.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1542.005 |
| name | TFTP Boot |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1542/005 |

## Preserved Source Material

```yaml
created: '2020-10-20T00:06:56.180Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse netbooting to load an unauthorized network device operating system from a Trivial File
  Transfer Protocol (TFTP) server. TFTP boot (netbooting) is commonly used by network administrators to load configuration-controlled
  network device images from a centralized management server. Netbooting is one option in the boot sequence and can be used
  to centralize, manage, and control device images.


  Adversaries may manipulate the configuration on the network device specifying use of a malicious TFTP server, which may
  be used in conjunction with [Modify System Image](https://attack.mitre.org/techniques/T1601) to load a modified image on
  device startup or reset. The unauthorized image allows adversaries to modify device configuration, add malicious capabilities
  to the device, and introduce backdoors to maintain control of the network device while minimizing detection through use
  of a standard functionality. This technique is similar to [ROMMONkit](https://attack.mitre.org/techniques/T1542/004) and
  may result in the network device running a modified image. (Citation: Cisco Blog Legacy Device Attacks)'
external_references:
- external_id: T1542.005
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1542/005
- description: Omar Santos. (2020, October 19). Attackers Continue to Target Legacy Devices. Retrieved October 20, 2020.
  source_name: Cisco Blog Legacy Device Attacks
  url: https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954
id: attack-pattern--28abec6c-4443-4b03-8206-07f2e264a6b4
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2026-04-17T18:38:49.555Z'
name: TFTP Boot
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
