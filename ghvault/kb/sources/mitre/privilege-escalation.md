---
parsed_by: focuslocust
source: mitre
type: generated
---
# Privilege Escalation

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tactic` |
| Record ID | `TA0004` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Privilege Escalation](../../attack/tactics/privilege-escalation.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | TA0004 |
| name | Privilege Escalation |
| type | tactic |
| source | mitre |
| url | https://attack.mitre.org/tactics/TA0004 |

## Preserved Source Material

```yaml
created: '2018-10-17T00:14:20.652Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "The adversary is trying to gain higher-level permissions.\n\nPrivilege Escalation consists of techniques that\
  \ adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network\
  \ with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are\
  \ to take advantage of system weaknesses, misconfigurations, and vulnerabilities. Examples of elevated access include: \n\
  \n* SYSTEM/root level\n* local administrator\n* user account with admin-like access \n* user accounts with access to specific\
  \ system or perform specific function\n\nThese techniques often overlap with Persistence techniques, as OS features that\
  \ let an adversary persist can execute in an elevated context.  "
external_references:
- external_id: TA0004
  source_name: mitre-attack
  url: https://attack.mitre.org/tactics/TA0004
id: x-mitre-tactic--5e29b093-294e-49e9-a803-dab3d73b77dd
modified: '2025-04-25T14:45:33.853Z'
name: Privilege Escalation
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
spec_version: '2.1'
type: x-mitre-tactic
x_mitre_attack_spec_version: 3.2.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_shortname: privilege-escalation
x_mitre_version: '1.0'
```
