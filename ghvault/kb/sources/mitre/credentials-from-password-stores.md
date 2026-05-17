---
parsed_by: focuslocust
source: mitre
type: generated
---
# Credentials from Password Stores

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1555` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Credentials from Password Stores](../../attack/techniques/T1555-credentials-from-password-stores.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1555 |
| name | Credentials from Password Stores |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1555 |

## Preserved Source Material

```yaml
created: '2020-02-11T18:48:28.456Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search for common password storage locations to obtain user credentials.(Citation: F-Secure
  The Dukes) Passwords are stored in several places on a system, depending on the operating system or application holding
  the credentials. There are also specific applications and services that store passwords to make them easier for users to
  manage and maintain, such as password managers and cloud secrets vaults. Once credentials are obtained, they can be used
  to perform lateral movement and access restricted information.'
external_references:
- external_id: T1555
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1555
- description: 'F-Secure Labs. (2015, September 17). The Dukes: 7 years of Russian cyberespionage. Retrieved December 10,
    2015.'
  source_name: F-Secure The Dukes
  url: https://www.f-secure.com/documents/996508/1030745/dukes_whitepaper.pdf
id: attack-pattern--3fc9b85a-2862-4363-a64d-d692e3ffbee0
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:41.974Z'
name: Credentials from Password Stores
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
- IaaS
- Linux
- macOS
- Windows
x_mitre_version: '1.2'
```
