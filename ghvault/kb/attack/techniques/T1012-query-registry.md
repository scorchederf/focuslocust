---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1012 - Query Registry

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1012` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may interact with the Windows Registry to gather information about the system, configuration, and installed software.

The Registry contains a significant amount of information about the operating system, configuration, software, and security. Information can easily be queried using the Reg utility, though other means to access the Registry exist. Some of the information may help adversaries to further their operation within a network. Adversaries may use the information from Query Registry during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [PcShare](../../tools/unknown/pcshare.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can search the registry files of a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [PowerSploit](../../tools/unknown/powersploit.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can query Registry keys for potential opportunities.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [Reg](../../tools/unknown/reg.md) | explicit | source | [Reg](https://attack.mitre.org/software/S0075) may be used to gather details from the Windows Registry of a local or remote system at the command-line interface.(Citation: Microsoft Reg) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can obtain Registry data from targeted systems.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can use the `GetRegValue` function to check Registry keys within `HKCU\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated` and `HKLM\Software\Policies\Microsoft\Windows\Installer\AlwaysInstallElevated`. It also contains additional modules that can check software AutoRun values and use the Win32 namespace to get values from HKCU, HKLM, HKCR, and HKCC hives.(Citation: GitHub SILENTTRINITY Modules July 2019) |

## Source Verification

[source record](../../sources/mitre/query-registry.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:25.584Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may interact with the Windows Registry to gather information about the system, configuration, and
installed software.
The Registry contains a significant amount of information about the operating system, configuration, software, and security.(Citation:
Wikipedia Windows Registry) Information can easily be queried using the [Reg](https://attack.mitre.org/software/S0075) utility,
though other means to access the Registry exist. Some of the information may help adversaries to further their operation
within a network. Adversaries may use the information from [Query Registry](https://attack.mitre.org/techniques/T1012) during
```
