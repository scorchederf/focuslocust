---
parsed_by: focuslocust
source: mitre
type: generated
---
# Local Accounts

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1078.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Local Accounts](../../attack/techniques/T1078.003-local-accounts.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1078.003 |
| name | Local Accounts |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1078/003 |

## Preserved Source Material

```yaml
created: '2020-03-13T20:26:46.695Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may obtain and abuse credentials of a local account as a means of gaining Initial Access, Persistence,
  Privilege Escalation, or Defense Evasion. Local accounts are those configured by an organization for use by users, remote
  support, services, or for administration on a single system or service.


  Local Accounts may also be abused to elevate privileges and harvest credentials through [OS Credential Dumping](https://attack.mitre.org/techniques/T1003).
  Password reuse may allow the abuse of local accounts across a set of machines on a network for the purposes of Privilege
  Escalation and Lateral Movement. '
external_references:
- external_id: T1078.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1078/003
id: attack-pattern--fdc47f44-dd32-4b99-af5f-209f556f63c2
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
- kill_chain_name: mitre-attack
  phase_name: initial-access
modified: '2026-04-15T22:51:08.702Z'
name: Local Accounts
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
- Containers
- ESXi
- Linux
- macOS
- Network Devices
- Windows
x_mitre_version: '2.0'
```
