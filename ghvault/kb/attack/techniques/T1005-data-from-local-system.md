---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1005 - Data from Local System

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1005` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.

Adversaries may do this using a Command and Scripting Interpreter, such as cmd as well as a Network Device CLI, which have functionality to interact with the file system to gather information. Adversaries may also use Automated Collection on the local system.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | <br>[Brute Ratel C4](https://attack.mitre.org/software/S1063) has the ability to upload files from a compromised system.(Citation: Palo Alto Brute Ratel July 2022) |
| [Forfiles](../../tools/unknown/forfiles.md) | explicit | source | [Forfiles](https://attack.mitre.org/software/S0193) can be used to act on (ex: copy, move, etc.) files/directories in a system during (ex: copy files into a staging area before).(Citation: Überwachung APT28 Forfiles June 2015) |
| [Koadic](../../tools/unknown/koadic.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can download files off the target system to send back to the server.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021) |
| [MCMD](../../tools/unknown/mcmd.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) has the ability to upload files from an infected device.(Citation: Secureworks MCMD July 2019) |
| [NPPSPY](../../tools/unknown/nppspy.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) records data entered from the local system logon at Winlogon to capture credentials in cleartext.(Citation: Huntress NPPSPY 2022) |
| [Out1](../../tools/unknown/out1.md) | explicit | source | [Out1](https://attack.mitre.org/software/S0594) can copy files and Registry data from compromised hosts.(Citation: Trend Micro Muddy Water March 2021) |
| [PcShare](../../tools/unknown/pcshare.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can collect files and information from a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [PowerSploit](../../tools/unknown/powersploit.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can access data from local files, volumes, and processes.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can retrieve files from compromised client machines.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [TruffleHog](../../tools/unknown/trufflehog.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has gathered data from home directories of the victim environment.(Citation: Netskope Shai-Hulud November 2025) |
| [Wevtutil](../../tools/unknown/wevtutil.md) | explicit | source | [Wevtutil](https://attack.mitre.org/software/S0645) can be used to export events from a specific log.(Citation: Wevtutil Microsoft Documentation)(Citation: F-Secure Lazarus Cryptocurrency Aug 2020) |
| [esentutl](../../tools/unknown/esentutl.md) | explicit | source | [esentutl](https://attack.mitre.org/software/S0404) can be used to collect data from local file systems.(Citation: Red Canary 2021 Threat Detection Report March 2021) |

## Source Verification

[source record](../../sources/mitre/data-from-local-system.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:20.537Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual
machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.
Adversaries may do this using a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059), such as
[cmd](https://attack.mitre.org/software/S0106) as well as a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008),
which have functionality to interact with the file system to gather information.(Citation: show_run_config_cmd_cisco) Adversaries
may also use [Automated Collection](https://attack.mitre.org/techniques/T1119) on the local system.
```
