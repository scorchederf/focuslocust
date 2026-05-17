---
parsed_by: focuslocust
source: mitre
type: generated
---
# BloodHound

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0521` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

BloodHound is an Active Directory (AD) reconnaissance tool that can reveal hidden relationships and identify attack paths within an AD environment.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/bloodhound.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1018 - Remote System Discovery](../../attack/techniques/T1018-remote-system-discovery.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can enumerate and collect the properties of domain computers, including domain controllers.(Citation: CrowdStrike BloodHound April 2018) |
| [T1033 - System Owner／User Discovery](../../attack/techniques/T1033-system-owner-user-discovery.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can collect information on user sessions.(Citation: CrowdStrike BloodHound April 2018) |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can use PowerShell to pull Active Directory information from the target environment.(Citation: CrowdStrike BloodHound April 2018) |
| [T1069.001 - Local Groups](../../attack/techniques/T1069.001-local-groups.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can collect information about local groups and members.(Citation: CrowdStrike BloodHound April 2018) |
| [T1069.002 - Domain Groups](../../attack/techniques/T1069.002-domain-groups.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can collect information about domain groups and members.(Citation: CrowdStrike BloodHound April 2018) |
| [T1087.001 - Local Account](../../attack/techniques/T1087.001-local-account.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can identify users with local administrator rights.(Citation: CrowdStrike BloodHound April 2018) |
| [T1087.002 - Domain Account](../../attack/techniques/T1087.002-domain-account.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can collect information about domain users, including identification of domain admin accounts.(Citation: CrowdStrike BloodHound April 2018) |
| [T1106 - Native API](../../attack/techniques/T1106-native-api.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can use .NET API calls in the SharpHound ingestor component to pull Active Directory data.(Citation: GitHub Bloodhound) |
| [T1482 - Domain Trust Discovery](../../attack/techniques/T1482-domain-trust-discovery.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) has the ability to map domain trusts and identify misconfigurations for potential abuse.(Citation: CrowdStrike BloodHound April 2018) |
| [T1560 - Archive Collected Data](../../attack/techniques/T1560-archive-collected-data.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can compress data collected by its SharpHound ingestor into a ZIP file to be written to disk.(Citation: GitHub Bloodhound)(Citation: Trend Micro Black Basta October 2022) |
| [T1615 - Group Policy Discovery](../../attack/techniques/T1615-group-policy-discovery.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) has the ability to collect local admin information via GPO.(Citation: GitHub Bloodhound) |

## Source Verification

[source record](../../sources/mitre/bloodhound.md)

## Evidence Excerpt

```text
created: '2020-10-28T12:51:29.358Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[BloodHound](https://attack.mitre.org/software/S0521) is an Active Directory (AD) reconnaissance tool that can
reveal hidden relationships and identify attack paths within an AD environment.(Citation: GitHub Bloodhound)(Citation: CrowdStrike
BloodHound April 2018)(Citation: FoxIT Wocao December 2019)'
external_references:
- external_id: S0521
source_name: mitre-attack
```
