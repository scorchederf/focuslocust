---
parsed_by: focuslocust
source: mitre
type: generated
---
# Weaken Encryption

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1600` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Weaken Encryption](../../attack/techniques/T1600-weaken-encryption.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1600 |
| name | Weaken Encryption |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1600 |

## Preserved Source Material

```yaml
created: '2020-10-19T18:47:08.759Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may compromise a network device’s encryption capability in order to bypass encryption that would
  otherwise protect data communications.(Citation: Cisco Synful Knock Evolution)


  Encryption can be used to protect transmitted network traffic to maintain its confidentiality (protect against unauthorized
  disclosure) and integrity (protect against unauthorized changes). Encryption ciphers are used to convert a plaintext message
  to ciphertext and can be computationally intensive to decipher without the associated decryption key. Typically, longer
  keys increase the cost of cryptanalysis, or decryption without the key.


  Adversaries can compromise and manipulate devices that perform encryption of network traffic. For example, through behaviors
  such as [Modify System Image](https://attack.mitre.org/techniques/T1601), [Reduce Key Space](https://attack.mitre.org/techniques/T1600/001),
  and [Disable Crypto Hardware](https://attack.mitre.org/techniques/T1600/002), an adversary can negatively effect and/or
  eliminate a device’s ability to securely encrypt network traffic. This poses a greater risk of unauthorized disclosure and
  may help facilitate data manipulation, Credential Access, or Collection efforts.(Citation: Cisco Blog Legacy Device Attacks)'
external_references:
- external_id: T1600
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1600
- description: Graham Holmes. (2015, October 8). Evolution of attacks on Cisco IOS devices. Retrieved October 19, 2020.
  source_name: Cisco Synful Knock Evolution
  url: https://blogs.cisco.com/security/evolution-of-attacks-on-cisco-ios-devices
- description: Omar Santos. (2020, October 19). Attackers Continue to Target Legacy Devices. Retrieved October 20, 2020.
  source_name: Cisco Blog Legacy Device Attacks
  url: https://community.cisco.com/t5/security-blogs/attackers-continue-to-target-legacy-devices/ba-p/4169954
id: attack-pattern--1f9012ef-1e10-4e48-915e-e03563435fe8
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:53.046Z'
name: Weaken Encryption
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Network Devices
x_mitre_version: '2.0'
```
