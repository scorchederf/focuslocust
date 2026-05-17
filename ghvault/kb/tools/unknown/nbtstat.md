---
parsed_by: focuslocust
source: mitre
type: generated
---
# nbtstat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0102` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

nbtstat is a utility used to troubleshoot NetBIOS name resolution.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/nbtstat.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [nbtstat](https://attack.mitre.org/software/S0102) can be used to discover local NetBIOS domain names. |
| [T1049 - System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md) | explicit | source | [nbtstat](https://attack.mitre.org/software/S0102) can be used to discover current NetBIOS sessions. |

## Source Verification

[source record](../../sources/mitre/nbtstat.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:03.773Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[nbtstat](https://attack.mitre.org/software/S0102) is a utility used to troubleshoot NetBIOS name resolution.
(Citation: TechNet Nbtstat)'
external_references:
- external_id: S0102
source_name: mitre-attack
url: https://attack.mitre.org/software/S0102
```
