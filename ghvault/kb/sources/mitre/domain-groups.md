---
parsed_by: focuslocust
source: mitre
type: generated
---
# Domain Groups

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1069.002` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Domain Groups](../../attack/techniques/T1069.002-domain-groups.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1069.002 |
| name | Domain Groups |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1069/002 |

## Preserved Source Material

```yaml
created: '2020-02-21T21:15:06.561Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to find domain-level groups and permission settings. The knowledge of domain-level permission
  groups can help adversaries determine which groups exist and which users belong to a particular group. Adversaries may use
  this information to determine which users have elevated permissions, such as domain administrators.


  Commands such as <code>net group /domain</code> of the [Net](https://attack.mitre.org/software/S0039) utility,  <code>dscacheutil
  -q group</code> on macOS, and <code>ldapsearch</code> on Linux can list domain-level groups.'
external_references:
- external_id: T1069.002
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1069/002
id: attack-pattern--2aed01ad-3df3-4410-a8cb-11ea4ded587c
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2025-10-24T17:48:33.946Z'
name: Domain Groups
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.2.0
x_mitre_contributors:
- Harshal Tupsamudre, Qualys
- Miriam Wiesner, @miriamxyra, Microsoft Security
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '1.2'
```
