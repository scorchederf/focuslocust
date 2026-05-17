---
parsed_by: focuslocust
source: mitre
type: generated
---
# AdFind

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0552` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

AdFind is a free command-line query tool that can be used for gathering information from Active Directory.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/adfind.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [AdFind](https://attack.mitre.org/software/S0552) can extract subnet information from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019) |
| [T1018 - Remote System Discovery](../../attack/techniques/T1018-remote-system-discovery.md) | explicit | source | [AdFind](https://attack.mitre.org/software/S0552) has the ability to query Active Directory for computers.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: Cybereason Bumblebee August 2022) |
| [T1069.002 - Domain Groups](../../attack/techniques/T1069.002-domain-groups.md) | explicit | source | [AdFind](https://attack.mitre.org/software/S0552) can enumerate domain groups.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: Symantec Bumblebee June 2022) |
| [T1087.002 - Domain Account](../../attack/techniques/T1087.002-domain-account.md) | explicit | source | [AdFind](https://attack.mitre.org/software/S0552) can enumerate domain users.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: Cybereason Bumblebee August 2022)(Citation: Symantec Bumblebee June 2022) |
| [T1482 - Domain Trust Discovery](../../attack/techniques/T1482-domain-trust-discovery.md) | explicit | source | [AdFind](https://attack.mitre.org/software/S0552) can gather information about organizational units (OUs) and domain trusts from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr 2019)(Citation: FireEye Ryuk and Trickbot January 2019)(Citation: Symantec Bumblebee June 2022) |

## Source Verification

[source record](../../sources/mitre/adfind.md)

## Evidence Excerpt

```text
created: '2020-12-28T18:35:50.244Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[AdFind](https://attack.mitre.org/software/S0552) is a free command-line query tool that can be used for gathering
information from Active Directory.(Citation: Red Canary Hospital Thwarted Ryuk October 2020)(Citation: FireEye FIN6 Apr
2019)(Citation: FireEye Ryuk and Trickbot January 2019)'
external_references:
- external_id: S0552
source_name: mitre-attack
```
