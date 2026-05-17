---
parsed_by: focuslocust
source: mitre
type: generated
---
# ipconfig

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0100` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ipconfig is a Windows utility that can be used to find information about a system's TCP/IP, DNS, DHCP, and adapter configuration.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/ipconfig.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [ipconfig](https://attack.mitre.org/software/S0100) can be used to display adapter configuration on Windows systems, including information for TCP/IP, DNS, and DHCP. |

## Source Verification

[source record](../../sources/mitre/ipconfig.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:02.863Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[ipconfig](https://attack.mitre.org/software/S0100) is a Windows utility that can be used to find information
about a system''s TCP/IP, DNS, DHCP, and adapter configuration. (Citation: TechNet Ipconfig)'
external_references:
- external_id: S0100
source_name: mitre-attack
url: https://attack.mitre.org/software/S0100
```
