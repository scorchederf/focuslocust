---
parsed_by: focuslocust
source: mitre
type: generated
---
# NBTscan

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0590` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

NBTscan is an open source tool that has been used by state groups to conduct internal reconnaissance within a compromised network.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/nbtscan.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [NBTscan](https://attack.mitre.org/software/S0590) can be used to collect MAC addresses.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	 |
| [T1018 - Remote System Discovery](../../attack/techniques/T1018-remote-system-discovery.md) | explicit | source | [NBTscan](https://attack.mitre.org/software/S0590) can list NetBIOS computer names.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	 |
| [T1033 - System Owner／User Discovery](../../attack/techniques/T1033-system-owner-user-discovery.md) | explicit | source | [NBTscan](https://attack.mitre.org/software/S0590) can list active users on the system.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	 |
| [T1040 - Network Sniffing](../../attack/techniques/T1040-network-sniffing.md) | explicit | source | [NBTscan](https://attack.mitre.org/software/S0590) can dump and print whole packet content.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	 |
| [T1046 - Network Service Discovery](../../attack/techniques/T1046-network-service-discovery.md) | explicit | source | [NBTscan](https://attack.mitre.org/software/S0590) can be used to scan IP networks.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003) |

## Source Verification

[source record](../../sources/mitre/nbtscan.md)

## Evidence Excerpt

```text
created: '2021-03-17T15:26:20.015Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[NBTscan](https://attack.mitre.org/software/S0590) is an open source tool that has been used by state groups
to conduct internal reconnaissance within a compromised network.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan
June 2003)(Citation: Symantec Waterbug Jun 2019)(Citation: FireEye APT39 Jan 2019)'
external_references:
- external_id: S0590
source_name: mitre-attack
```
