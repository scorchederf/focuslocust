---
parsed_by: focuslocust
source: mitre
type: generated
---
# Arp

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0099` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Arp displays and modifies information about a system's Address Resolution Protocol (ARP) cache.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/arp.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [Arp](https://attack.mitre.org/software/S0099) can be used to display ARP configuration information on the host.(Citation: TechNet Arp) |
| [T1018 - Remote System Discovery](../../attack/techniques/T1018-remote-system-discovery.md) | explicit | source | [Arp](https://attack.mitre.org/software/S0099) can be used to display a host's ARP cache, which may include address resolutions for remote systems.(Citation: TechNet Arp)(Citation: Palo Alto ARP) |

## Source Verification

[source record](../../sources/mitre/arp.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:33:02.428Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Arp](https://attack.mitre.org/software/S0099) displays and modifies information about a system''s Address Resolution
Protocol (ARP) cache. (Citation: TechNet Arp)'
external_references:
- external_id: S0099
source_name: mitre-attack
url: https://attack.mitre.org/software/S0099
```
