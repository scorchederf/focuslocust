---
parsed_by: focuslocust
source: mitre
type: generated
---
# Reduce Key Space

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1600.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Reduce Key Space](../../attack/techniques/T1600.001-reduce-key-space.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1600.001 |
| name | Reduce Key Space |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1600/001 |

## Preserved Source Material

```yaml
created: '2020-10-19T19:03:48.310Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may reduce the level of effort required to decrypt data transmitted over the network by reducing
  the cipher strength of encrypted communications.(Citation: Cisco Synful Knock Evolution)


  Adversaries can weaken the encryption software on a compromised network device by reducing the key size used by the software
  to convert plaintext to ciphertext (e.g., from hundreds or thousands of bytes to just a couple of bytes). As a result, adversaries
  dramatically reduce the amount of effort needed to decrypt the protected information without the key.


  Adversaries may modify the key size used and other encryption parameters using specialized commands in a [Network Device
  CLI](https://attack.mitre.org/techniques/T1059/008) introduced to the system through [Modify System Image](https://attack.mitre.org/techniques/T1601)
  to change the configuration of the device. (Citation: Cisco Blog Legacy Device Attacks)'
external_references:
- external_id: T1600.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1600/001
- description: Graham Holmes. (2015, October 8). Evolution of attacks on Cisco IOS devices. Retrieved October 19, 2020.
  source_name: Cisco Synful Knock Evolution
  url: https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices
- description: Omar Santos. (2020, October 19). Attackers Continue to Target Legacy Devices. Retrieved October 20, 2020.
  source_name: Cisco Blog Legacy Device Attacks
  url: https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954
id: attack-pattern--3a40f208-a9c1-4efa-a598-4003c3681fb8
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:53.005Z'
name: Reduce Key Space
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
