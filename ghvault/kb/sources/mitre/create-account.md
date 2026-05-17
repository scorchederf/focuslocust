---
parsed_by: focuslocust
source: mitre
type: generated
---
# Create Account

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1136` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Create Account](../../attack/techniques/T1136-create-account.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1136 |
| name | Create Account |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1136 |

## Preserved Source Material

```yaml
created: '2017-12-14T16:46:06.044Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may create an account to maintain access to victim systems.(Citation: Symantec WastedLocker June
  2020) With a sufficient level of access, creating such accounts may be used to establish secondary credentialed access that
  do not require persistent remote access tools to be deployed on the system.


  Accounts may be created on the local system or within a domain or cloud tenant. In cloud environments, adversaries may create
  accounts that only have access to specific services, which can reduce the chance of detection.'
external_references:
- external_id: T1136
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1136
- description: 'Lich, B., Miroshnikov, A. (2017, April 5). 4720(S): A user account was created. Retrieved June 30, 2017.'
  source_name: Microsoft User Creation Event
  url: https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4720
- description: 'Symantec Threat Intelligence. (2020, June 25). WastedLocker: Symantec Identifies Wave of Attacks Against U.S.
    Organizations. Retrieved May 20, 2021.'
  source_name: Symantec WastedLocker June 2020
  url: https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/wastedlocker-ransomware-us
id: attack-pattern--e01be9c5-e763-4caf-aeb7-000b416aef67
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
modified: '2025-10-24T17:49:30.136Z'
name: Create Account
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Microsoft Threat Intelligence Center (MSTIC)
- Praetorian
- Austin Clark, @c2defense
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
- IaaS
- Linux
- macOS
- Network Devices
- Containers
- SaaS
- Office Suite
- Identity Provider
- ESXi
x_mitre_version: '2.6'
```
