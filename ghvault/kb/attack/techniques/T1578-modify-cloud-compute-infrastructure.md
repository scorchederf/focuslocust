---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1578 - Modify Cloud Compute Infrastructure

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

## Summary

An adversary may attempt to modify a cloud account's compute service infrastructure to evade defenses. A modification to the compute service infrastructure can include the creation, deletion, or modification of one or more components such as compute instances, virtual machines, and snapshots.

Permissions gained from the modification of infrastructure components may bypass restrictions that prevent access to existing infrastructure. Modifying infrastructure components may also allow an adversary to evade detection and remove evidence of their presence.

## Source Verification

[source record](../../sources/mitre/modify-cloud-compute-infrastructure.md)

## Evidence Excerpt

```text
created: '2019-08-30T18:03:05.864Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may attempt to modify a cloud account''s compute service infrastructure to evade defenses. A modification
to the compute service infrastructure can include the creation, deletion, or modification of one or more components such
as compute instances, virtual machines, and snapshots.
Permissions gained from the modification of infrastructure components may bypass restrictions that prevent access to existing
infrastructure. Modifying infrastructure components may also allow an adversary to evade detection and remove evidence of
their presence.(Citation: Mandiant M-Trends 2020)'
```
