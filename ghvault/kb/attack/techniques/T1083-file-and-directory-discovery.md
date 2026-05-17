---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1083 - File and Directory Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1083` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from File and Directory Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

Many command shell utilities can be used to obtain this information. Examples include <code>dir</code>, <code>tree</code>, <code>ls</code>, <code>find</code>, and <code>locate</code>. Custom tools may also be used to gather file and directory information and interact with the Native API. Adversaries may also leverage a Network Device CLI on network devices to gather file and directory information (e.g. <code>dir</code>, <code>show flash</code>, and/or <code>nvram</code>).

Some files and directories may require elevated or specific user permissions to access.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [CrackMapExec](../../tools/unknown/crackmapexec.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can discover specified filetypes and log files on a targeted system.(Citation: CME Github September 2018) |
| [Diskpart](../../tools/unknown/diskpart.md) | explicit | source | If executed with elevated privileges, [Diskpart](https://attack.mitre.org/software/S9002) can list all volumes, including virtual disks.(Citation: Halcyon_CloakRansomware_Dec2024)    |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) includes various modules for finding files of interest on hosts and network shares.(Citation: Github PowerShell Empire) |
| [Forfiles](../../tools/unknown/forfiles.md) | explicit | source | [Forfiles](https://attack.mitre.org/software/S0193) can be used to locate certain types of files/directories in a system.(ex: locate all files with a specific extension, name, and/or age)(Citation: Überwachung APT28 Forfiles June 2015) |
| [Imminent Monitor](../../tools/unknown/imminent-monitor.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a dynamic debugging feature to check whether it is located in the %TEMP% directory, otherwise it copies itself there.(Citation: QiAnXin APT-C-36 Feb2019) |
| [Koadic](../../tools/unknown/koadic.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can obtain a list of directories.(Citation: MalwareBytes LazyScripter Feb 2021) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) can enumerate files on the local file system and includes a module for enumerating recently accessed files.(Citation: GitHub PoshC2) |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can walk through directories and recursively search for strings in files.(Citation: GitHub Pupy) |
| [Rclone](../../tools/unknown/rclone.md) | explicit | source | [Rclone](https://attack.mitre.org/software/S1040) can list files and directories with the `ls`, `lsd`, and `lsl` commands.(Citation: Rclone) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can search for files on the infected machine.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [RemoteUtilities](../../tools/unknown/remoteutilities.md) | explicit | source | [RemoteUtilities](https://attack.mitre.org/software/S0592) can enumerate files and directories on a target machine.(Citation: Trend Micro Muddy Water March 2021) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has several modules, such as `ls.py`, `pwd.py`, and `recentFiles.py`, to enumerate directories and files.(Citation: GitHub SILENTTRINITY Modules July 2019)  |
| [Sliver](../../tools/unknown/sliver.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) can enumerate files on a target system.(Citation: GitHub Sliver File System August 2021) |
| [TruffleHog](../../tools/unknown/trufflehog.md) | explicit | source | [TruffleHog](https://attack.mitre.org/software/S9009) has can browse and scan individual files and directories.(Citation: Black Hills Information Security TruffleHog January 2024)(Citation: Netskope Shai-Hulud November 2025)(Citation: Github TruffleSecurity Trufflehog April 2025) |
| [cmd](../../tools/unknown/cmd.md) | explicit | source | [cmd](https://attack.mitre.org/software/S0106) can be used to find files and directories with native functionality such as <code>dir</code> commands.(Citation: TechNet Dir) |

## Source Verification

[source record](../../sources/mitre/file-and-directory-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:04.710Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may enumerate files and directories or may search in specific locations of a host or network share
for certain information within a file system. Adversaries may use the information from [File and Directory Discovery](https://attack.mitre.org/techniques/T1083)
during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target
and/or attempts specific actions.
Many command shell utilities can be used to obtain this information. Examples include <code>dir</code>, <code>tree</code>,
<code>ls</code>, <code>find</code>, and <code>locate</code>.(Citation: Windows Commands JPCERT) Custom tools may also be
```
