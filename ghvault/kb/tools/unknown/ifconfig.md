---
parsed_by: focuslocust
source: mitre
type: generated
---
# ifconfig

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0101` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ifconfig is a Unix-based utility used to gather information about and interact with the TCP/IP settings on a system.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/ifconfig.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [ifconfig](https://attack.mitre.org/software/S0101) can be used to display adapter configuration on Unix systems, including information for TCP/IP, DNS, and DHCP. |

## Source Verification

[source record](../../sources/mitre/ifconfig.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:03.377Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[ifconfig](https://attack.mitre.org/software/S0101) is a Unix-based utility used to gather information about
and interact with the TCP/IP settings on a system. (Citation: Wikipedia Ifconfig)'
external_references:
- external_id: S0101
source_name: mitre-attack
url: https://attack.mitre.org/software/S0101
```
