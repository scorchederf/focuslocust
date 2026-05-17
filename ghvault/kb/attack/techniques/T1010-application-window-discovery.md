---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1010 - Application Window Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1010` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to get a listing of open application windows. Window listings could convey information about how the system is used. For example, information about application windows could be used identify potential data to collect as well as identifying security tooling (Security Software Discovery) to evade.

Adversaries typically abuse system features for this type of enumeration. For example, they may gather information through native system features such as Command and Scripting Interpreter commands and Native API functions.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [APT-C-36](https://attack.mitre.org/groups/G0099) used a customized version of [QuasarRAT](https://attack.mitre.org/software/S0262) to monitor browser windows for strings relating to specific Colombian financial institutions.(Citation: Kaspersky BlindEagle AUG 2024)<br> |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can list all windows on victim systems.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate the active Window during keylogging through execution of `GetActiveWindowTitle`.(Citation: GitHub SILENTTRINITY Modules July 2019) |

## Source Verification

[source record](../../sources/mitre/application-window-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:24.512Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to get a listing of open application windows. Window listings could convey information
about how the system is used.(Citation: Prevailion DarkWatchman 2021) For example, information about application windows
could be used identify potential data to collect as well as identifying security tooling ([Security Software Discovery](https://attack.mitre.org/techniques/T1518/001))
to evade.(Citation: ESET Grandoreiro April 2020)
Adversaries typically abuse system features for this type of enumeration. For example, they may gather information through
native system features such as [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) commands and
```
