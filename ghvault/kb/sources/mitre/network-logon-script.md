---
parsed_by: focuslocust
source: mitre
type: generated
---
# Network Logon Script

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1037.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Network Logon Script](../../attack/techniques/T1037.003-network-logon-script.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1037.003 |
| name | Network Logon Script |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1037/003 |

## Preserved Source Material

```yaml
created: '2020-01-10T18:01:03.666Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may use network logon scripts automatically executed at logon initialization to establish persistence.\
  \ Network logon scripts can be assigned using Active Directory or Group Policy Objects.(Citation: Petri Logon Script AD)\
  \ These logon scripts run with the privileges of the user they are assigned to. Depending on the systems within the network,\
  \ initializing one of these scripts could apply to more than one or potentially all systems.  \n \nAdversaries may use these\
  \ scripts to maintain persistence on a network. Depending on the access configuration of the logon scripts, either local\
  \ credentials or an administrator account may be necessary."
external_references:
- external_id: T1037.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1037/003
- description: Daniel Petri. (2009, January 8). Setting up a Logon Script through Active Directory Users and Computers in
    Windows Server 2008. Retrieved November 15, 2019.
  source_name: Petri Logon Script AD
  url: https://www.petri.com/setting-up-logon-script-through-active-directory-users-computers-windows-server-2008
id: attack-pattern--c63a348e-ffc2-486a-b9d9-d7f11ec54d99
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: persistence
- kill_chain_name: mitre-attack
  phase_name: privilege-escalation
modified: '2025-10-24T17:49:21.921Z'
name: Network Logon Script
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
- Windows
x_mitre_version: '1.0'
```
