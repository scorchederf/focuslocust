---
parsed_by: focuslocust
source: mitre
type: generated
---
# Domain Account

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1136.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Domain Account](../../attack/techniques/T1136.002-domain-account.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1136.002 |
| name | Domain Account |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1136/002 |

## Preserved Source Material

```yaml
created: '2020-01-28T14:05:17.825Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may create a domain account to maintain access to victim systems. Domain accounts are those managed
  by Active Directory Domain Services where access and permissions are configured across systems and services that are part
  of that domain. Domain accounts can cover user, administrator, and service accounts. With a sufficient level of access,
  the <code>net user /add /domain</code> command can be used to create a domain account.(Citation: Savill 1999)


  Such accounts may be used to establish secondary credentialed access that do not require persistent remote access tools
  to be deployed on the system.'
external_references:
- external_id: T1136.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1136/002
- description: 'Lich, B., Miroshnikov, A. (2017, April 5). 4720(S): A user account was created. Retrieved June 30, 2017.'
  source_name: Microsoft User Creation Event
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720
- description: Savill, J. (1999, March 4). Net.exe reference. Retrieved September 22, 2015.
  source_name: Savill 1999
  url: https://web.archive.org/web/20150511162820/http://windowsitpro.com/windows/netexe-reference
id: attack-pattern--7610cada-1499-41a4-b3dd-46467b68d177
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:48:57.883Z'
name: Domain Account
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
- Linux
- macOS
- Windows
x_mitre_version: '1.1'
```
