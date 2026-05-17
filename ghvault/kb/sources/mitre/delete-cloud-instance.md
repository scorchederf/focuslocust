---
parsed_by: focuslocust
source: mitre
type: generated
---
# Delete Cloud Instance

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1578.003` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Delete Cloud Instance](../../attack/techniques/T1578.003-delete-cloud-instance.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1578.003 |
| name | Delete Cloud Instance |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1578/003 |

## Preserved Source Material

```yaml
created: '2020-06-16T17:23:06.508Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may delete a cloud instance after they have performed malicious activities in an attempt to evade
  detection and remove evidence of their presence.  Deleting an instance or virtual machine can remove valuable forensic artifacts
  and other evidence of suspicious behavior if the instance is not recoverable.


  An adversary may also [Create Cloud Instance](https://attack.mitre.org/techniques/T1578/002) and later terminate the instance
  after achieving their objectives.(Citation: Mandiant M-Trends 2020)'
external_references:
- external_id: T1578.003
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1578/003
- description: Mandiant. (2020, February). M-Trends 2020. Retrieved November 17, 2024.
  source_name: Mandiant M-Trends 2020
  url: https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf
id: attack-pattern--70857657-bd0b-4695-ad3e-b13f92cac1b4
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:52.915Z'
name: Delete Cloud Instance
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Arun Seelagan, CISA
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
x_mitre_version: '2.0'
```
