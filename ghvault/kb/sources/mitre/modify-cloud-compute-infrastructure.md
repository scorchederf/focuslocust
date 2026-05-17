---
parsed_by: focuslocust
source: mitre
type: generated
---
# Modify Cloud Compute Infrastructure

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1578` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Modify Cloud Compute Infrastructure](../../attack/techniques/T1578-modify-cloud-compute-infrastructure.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1578 |
| name | Modify Cloud Compute Infrastructure |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1578 |

## Preserved Source Material

```yaml
created: '2019-08-30T18:03:05.864Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may attempt to modify a cloud account''s compute service infrastructure to evade defenses. A modification
  to the compute service infrastructure can include the creation, deletion, or modification of one or more components such
  as compute instances, virtual machines, and snapshots.


  Permissions gained from the modification of infrastructure components may bypass restrictions that prevent access to existing
  infrastructure. Modifying infrastructure components may also allow an adversary to evade detection and remove evidence of
  their presence.(Citation: Mandiant M-Trends 2020)'
external_references:
- external_id: T1578
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1578
- description: Mandiant. (2020, February). M-Trends 2020. Retrieved November 17, 2024.
  source_name: Mandiant M-Trends 2020
  url: https://www.mandiant.com/sites/default/files/2021-09/mtrends-2020.pdf
id: attack-pattern--144e007b-e638-431d-a894-45d90c54ab90
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:52.919Z'
name: Modify Cloud Compute Infrastructure
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- IaaS
x_mitre_version: '2.0'
```
