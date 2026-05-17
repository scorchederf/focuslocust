---
parsed_by: focuslocust
source: mitre
type: generated
---
# Password Cracking

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1110.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password Cracking](../../attack/techniques/T1110.002-password-cracking.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1110.002 |
| name | Password Cracking |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1110/002 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:38:56.197Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use password cracking to attempt to recover usable credentials, such as plaintext passwords,\
  \ when credential material such as password hashes are obtained. [OS Credential Dumping](https://attack.mitre.org/techniques/T1003)\
  \ can be used to obtain password hashes, this may only get an adversary so far when [Pass the Hash](https://attack.mitre.org/techniques/T1550/002)\
  \ is not an option. Further,  adversaries may leverage [Data from Configuration Repository](https://attack.mitre.org/techniques/T1602)\
  \ in order to obtain hashed credentials for network devices.(Citation: US-CERT-TA18-106A) \n\nTechniques to systematically\
  \ guess the passwords used to compute hashes are available, or the adversary may use a pre-computed rainbow table to crack\
  \ hashes. Cracking hashes is usually done on adversary-controlled systems outside of the target network.(Citation: Wikipedia\
  \ Password cracking) The resulting plaintext password resulting from a successfully cracked hash may be used to log into\
  \ systems, resources, and services in which the account has access."
external_references:
- external_id: T1110.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1110/002
- description: US-CERT. (2018, April 20). Alert (TA18-106A) Russian State-Sponsored Cyber Actors Targeting Network Infrastructure
    Devices. Retrieved October 19, 2020.
  source_name: US-CERT-TA18-106A
  url: https://www.us-cert.gov/ncas/alerts/TA18-106A
- description: Wikipedia. (n.d.). Password cracking. Retrieved December 23, 2015.
  source_name: Wikipedia Password cracking
  url: https://en.wikipedia.org/wiki/Password_cracking
id: attack-pattern--1d24cdee-9ea2-4189-b08e-af110bf2435d
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:29.397Z'
name: Password Cracking
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Mohamed Kmal
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Identity Provider
- Linux
- macOS
- Network Devices
- Office Suite
- Windows
x_mitre_version: '1.4'
```
