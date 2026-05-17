---
parsed_by: focuslocust
source: mitre
type: generated
---
# Modify System Image

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1601` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Modify System Image](../../attack/techniques/T1601-modify-system-image.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1601 |
| name | Modify System Image |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1601 |

## Preserved Source Material

```yaml
created: '2020-10-19T19:42:19.740Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may make changes to the operating system of embedded network devices to weaken defenses and provide
  new capabilities for themselves.  On such devices, the operating systems are typically monolithic and most of the device
  functionality and capabilities are contained within a single file.


  To change the operating system, the adversary typically only needs to affect this one file, replacing or modifying it.  This
  can either be done live in memory during system runtime for immediate effect, or in storage to implement the change on the
  next boot of the network device.'
external_references:
- external_id: T1601
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1601
id: attack-pattern--ae7f3575-0a5e-427e-991b-fe03ad44c754
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: defense-impairment
modified: '2026-04-16T20:07:53.013Z'
name: Modify System Image
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
- Network Devices
x_mitre_version: '2.0'
```
