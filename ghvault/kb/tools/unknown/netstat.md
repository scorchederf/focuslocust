---
parsed_by: focuslocust
source: mitre
type: generated
---
# netstat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0104` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

netstat is an operating system utility that displays active TCP connections, listening ports, and network statistics.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/netstat.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1049 - System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md) | explicit | source | [netstat](https://attack.mitre.org/software/S0104) can be used to enumerate local network connections, including active TCP connections and other network statistics.(Citation: TechNet Netstat) |

## Source Verification

[source record](../../sources/mitre/netstat.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:04.545Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[netstat](https://attack.mitre.org/software/S0104) is an operating system utility that displays active TCP connections,
listening ports, and network statistics. (Citation: TechNet Netstat)'
external_references:
- external_id: S0104
source_name: mitre-attack
url: https://attack.mitre.org/software/S0104
```
