---
parsed_by: focuslocust
source: mitre
type: generated
---
# Domain Controller Authentication

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1556.001` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Domain Controller Authentication](../../attack/techniques/T1556.001-domain-controller-authentication.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1556.001 |
| name | Domain Controller Authentication |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1556/001 |

## Preserved Source Material

```yaml
created: '2020-02-11T19:05:02.399Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may patch the authentication process on a domain controller to bypass the typical authentication\
  \ mechanisms and enable access to accounts. \n\nMalware may be used to inject false credentials into the authentication\
  \ process on a domain controller with the intent of creating a backdoor used to access any user’s account and/or credentials\
  \ (ex: [Skeleton Key](https://attack.mitre.org/software/S0007)). Skeleton key works through a patch on an enterprise domain\
  \ controller authentication process (LSASS) with credentials that adversaries may use to bypass the standard authentication\
  \ system. Once patched, an adversary can use the injected password to successfully authenticate as any domain user account\
  \ (until the the skeleton key is erased from memory by a reboot of the domain controller). Authenticated access may enable\
  \ unfettered access to hosts and/or resources within single-factor authentication environments.(Citation: Dell Skeleton)"
external_references:
- external_id: T1556.001
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1556/001
- description: Dell SecureWorks. (2015, January 12). Skeleton Key Malware Analysis. Retrieved April 8, 2019.
  source_name: Dell Skeleton
  url: https://www.secureworks.com/research/skeleton-key-malware-analysis
id: attack-pattern--d4b96d2c-1032-4b22-9235-2b5b649d0605
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2026-04-16T20:07:53.091Z'
name: Domain Controller Authentication
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
- Windows
x_mitre_version: '3.0'
```
