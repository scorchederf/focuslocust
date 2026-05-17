---
parsed_by: focuslocust
source: mitre
type: generated
---
# Password Filter DLL

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1556.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Password Filter DLL](../../attack/techniques/T1556.002-password-filter-dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1556.002 |
| name | Password Filter DLL |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1556/002 |

## Preserved Source Material

```yaml
created: '2020-02-11T19:05:45.829Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may register malicious password filter dynamic link libraries (DLLs) into the authentication process\
  \ to acquire user credentials as they are validated. \n\nWindows password filters are password policy enforcement mechanisms\
  \ for both domain and local accounts. Filters are implemented as DLLs containing a method to validate potential passwords\
  \ against password policies. Filter DLLs can be positioned on local computers for local accounts and/or domain controllers\
  \ for domain accounts. Before registering new passwords in the Security Accounts Manager (SAM), the Local Security Authority\
  \ (LSA) requests validation from each registered filter. Any potential changes cannot take effect until every registered\
  \ filter acknowledges validation. \n\nAdversaries can register malicious password filters to harvest credentials from local\
  \ computers and/or entire domains. To perform proper validation, filters must receive plain-text credentials from the LSA.\
  \ A malicious password filter would receive these plain-text credentials every time a password request is made.(Citation:\
  \ Carnal Ownage Password Filters Sept 2013)"
external_references:
- external_id: T1556.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1556/002
- description: Fuller, R. (2013, September 11). Stealing passwords every time they change. Retrieved November 21, 2017.
  source_name: Carnal Ownage Password Filters Sept 2013
  url: http://carnal0wnage.attackresearch.com/2013/09/stealing-passwords-every-time-they.html
id: attack-pattern--3731fbcd-0e43-47ae-ae6c-d15e510f0d42
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: credential-access
modified: '2026-04-16T20:07:53.031Z'
name: Password Filter DLL
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Vincent Le Toux
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '3.0'
```
