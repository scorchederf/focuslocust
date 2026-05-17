---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1033 - System Owner／User Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1033` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly uses a system, or whether a user is actively using the system. They may do this, for example, by retrieving account usernames or by using OS Credential Dumping. The information may be collected in a number of different ways using other Discovery techniques, because user and username details are prevalent throughout a system and include running process ownership, file/directory ownership, session information, and system logs. Adversaries may use the information from System Owner/User Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Various utilities and commands may acquire this information, including <code>whoami</code>. In macOS and Linux, the currently logged in user can be identified with <code>w</code> and <code>who</code>. On macOS the <code>dscl . list /Users | grep -v '_'</code> command can also be used to enumerate user accounts. Environment variables, such as <code>%USERNAME%</code> and <code>$USER</code>, may also be used to access this information.

On network devices, Network Device CLI commands such as `show users` and `show ssh` can be used to display users currently logged into the device.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AsyncRAT](../../tools/unknown/asyncrat.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can check if the current user of a compromised system is an administrator. (Citation: Telefonica Snip3 December 2021) |
| [BloodHound](../../tools/unknown/bloodhound.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can collect information on user sessions.(Citation: CrowdStrike BloodHound April 2018) |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can enumerate the username on targeted hosts.(Citation: Talos Frankenstein June 2019) |
| [Koadic](../../tools/unknown/koadic.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can identify logged in users across the domain and views user sessions.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021) |
| [NBTscan](../../tools/unknown/nbtscan.md) | explicit | source | [NBTscan](https://attack.mitre.org/software/S0590) can list active users on the system.(Citation: Debian nbtscan Nov 2019)(Citation: SecTools nbtscan June 2003)	 |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can enumerate local information for Linux hosts and find currently logged on users for Windows hosts.(Citation: GitHub Pupy) |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can enumerate the username and account type.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can enumerate the username on targeted hosts.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can gather a list of logged on users.(Citation: GitHub SILENTTRINITY Modules July 2019)  |

## Source Verification

[source record](../../sources/mitre/system-owner-user-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:35.733Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to identify the primary user, currently logged in user, set of users that commonly uses
a system, or whether a user is actively using the system. They may do this, for example, by retrieving account usernames
or by using [OS Credential Dumping](https://attack.mitre.org/techniques/T1003). The information may be collected in a number
of different ways using other Discovery techniques, because user and username details are prevalent throughout a system
and include running process ownership, file/directory ownership, session information, and system logs. Adversaries may use
the information from [System Owner/User Discovery](https://attack.mitre.org/techniques/T1033) during automated discovery
```
