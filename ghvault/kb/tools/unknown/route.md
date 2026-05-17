---
parsed_by: focuslocust
source: mitre
type: generated
---
# route

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0103` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

route can be used to find or change information within the local system IP routing table.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/route.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [route](https://attack.mitre.org/software/S0103) can be used to discover routing configuration information. |

## Source Verification

[source record](../../sources/mitre/route.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:04.151Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[route](https://attack.mitre.org/software/S0103) can be used to find or change information within the local
system IP routing table. (Citation: TechNet Route)'
external_references:
- external_id: S0103
source_name: mitre-attack
url: https://attack.mitre.org/software/S0103
```
