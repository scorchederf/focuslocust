---
parsed_by: focuslocust
source: mitre
type: generated
---
# Unsecured Credentials

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1552` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Unsecured Credentials](../../attack/techniques/T1552-unsecured-credentials.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1552 |
| name | Unsecured Credentials |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1552 |

## Preserved Source Material

```yaml
created: '2020-02-04T12:47:23.631Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search compromised systems to find and obtain insecurely stored credentials. These credentials
  can be stored and/or misplaced in many locations on a system, including plaintext files (e.g. [Shell History](https://attack.mitre.org/techniques/T1552/003)),
  operating system or application-specific repositories (e.g. [Credentials in Registry](https://attack.mitre.org/techniques/T1552/002)),  or
  other specialized files/artifacts (e.g. [Private Keys](https://attack.mitre.org/techniques/T1552/004)).(Citation: Brining
  MimiKatz to Unix)'
external_references:
- external_id: T1552
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1552
- description: Tim Wadhwa-Brown. (2018, November). Where 2 worlds collide Bringing Mimikatz et al to UNIX. Retrieved October
    13, 2021.
  source_name: Brining MimiKatz to Unix
  url: https://labs.portcullis.co.uk/download/eu-18-Wadhwa-Brown-Where-2-worlds-collide-Bringing-Mimikatz-et-al-to-UNIX.pdf
id: attack-pattern--435dfb86-2697-4867-85b5-2fef496c0517
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2025-10-24T17:48:42.785Z'
name: Unsecured Credentials
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Austin Clark, @c2defense
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- SaaS
- IaaS
- Linux
- macOS
- Containers
- Network Devices
- Office Suite
- Identity Provider
x_mitre_version: '1.5'
```
