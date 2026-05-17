---
parsed_by: focuslocust
source: mitre
type: generated
---
# Vulnerabilities

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1588.006` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Vulnerabilities](../../attack/techniques/T1588.006-vulnerabilities.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1588.006 |
| name | Vulnerabilities |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1588/006 |

## Preserved Source Material

```yaml
created: '2020-10-15T02:59:38.628Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may acquire information about vulnerabilities that can be used during targeting. A vulnerability
  is a weakness in computer hardware or software that can, potentially, be exploited by an adversary to cause unintended or
  unanticipated behavior to occur. Adversaries may find vulnerability information by searching open databases or gaining access
  to closed vulnerability databases.(Citation: National Vulnerability Database)


  An adversary may monitor vulnerability disclosures/databases to understand the state of existing, as well as newly discovered,
  vulnerabilities. There is usually a delay between when a vulnerability is discovered and when it is made public. An adversary
  may target the systems of those known to conduct vulnerability research (including commercial vendors). Knowledge of a vulnerability
  may cause an adversary to search for an existing exploit (i.e. [Exploits](https://attack.mitre.org/techniques/T1588/005))
  or to attempt to develop one themselves (i.e. [Exploits](https://attack.mitre.org/techniques/T1587/004)).'
external_references:
- external_id: T1588.006
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1588/006
- description: National Vulnerability Database. (n.d.). National Vulnerability Database. Retrieved October 15, 2020.
  source_name: National Vulnerability Database
  url: https://nvd.nist.gov/
id: attack-pattern--2b5aa86b-a0df-4382-848d-30abea443327
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: resource-development
modified: '2025-10-24T17:48:34.033Z'
name: Vulnerabilities
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- PRE
x_mitre_version: '1.0'
```
