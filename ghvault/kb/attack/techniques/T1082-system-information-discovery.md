---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1082 - System Information Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1082` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use this information to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. This behavior is distinct from Local Storage Discovery which is an adversary's discovery of local drive, disks and/or volumes.

Tools such as Systeminfo can be used to gather detailed system information. If running with privileged access, a breakdown of system data can be gathered through the <code>systemsetup</code> configuration tool on macOS. Adversaries may leverage a Network Device CLI on network devices to gather detailed system information (e.g. <code>show version</code>). On ESXi servers, threat actors may gather system information from various esxcli utilities, such as `system hostname get` and `system version get`.

Infrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine.

System Information Discovery combined with information gathered from other forms of discovery and reconnaissance can drive payload development and concealment.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Covenant](../../tools/unknown/covenant.md) | explicit | source | [Covenant](https://attack.mitre.org/software/S1155) implants can gather basic information on infected systems.(Citation: Github Covenant) |
| [Diskpart](../../tools/unknown/diskpart.md) | explicit | source | [Diskpart](https://attack.mitre.org/software/S9002) can show information about the selected disk, partition, volume, or virtual hard disk (VHD).(Citation: Microsoft_diskpart_Feb2023)  |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can enumerate host system information like OS, architecture, domain name, applied patches, and more.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019) |
| [Koadic](../../tools/unknown/koadic.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can obtain the OS version and build, computer name, and processor architecture from a compromised host.(Citation: MalwareBytes LazyScripter Feb 2021) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains modules, such as <code>Get-ComputerInfo</code>, for enumerating common system information.(Citation: GitHub PoshC2) |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can grab a system’s information including the OS version, architecture, etc.(Citation: GitHub Pupy) |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can gather system information from the victim’s machine including the OS type.(Citation: GitHub QuasarRAT) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can collect the OS version and process architecture of compromised hosts.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can collect information related to a compromised host, including OS version.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) gathered the operating system name and specific Windows version of an infected machine.(Citation: FOX-IT May 2016 Mofang) |
| [Systeminfo](../../tools/unknown/systeminfo.md) | explicit | source | [Systeminfo](https://attack.mitre.org/software/S0096) can be used to gather information about the operating system.(Citation: TechNet Systeminfo) |
| [cmd](../../tools/unknown/cmd.md) | explicit | source | [cmd](https://attack.mitre.org/software/S0106) can be used to find information about the operating system.(Citation: TechNet Dir) |
| [dsquery](../../tools/unknown/dsquery.md) | explicit | source | [dsquery](https://attack.mitre.org/software/S0105) has the ability to enumerate various information, such as the operating system and host name, for systems within a domain.(Citation: Mandiant APT41) |

## Source Verification

[source record](../../sources/mitre/system-information-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:04.307Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'An adversary may attempt to get detailed information about the operating system and hardware, including version,
patches, hotfixes, service packs, and architecture. Adversaries may use this information to shape follow-on behaviors, including
whether or not the adversary fully infects the target and/or attempts specific actions. This behavior is distinct from [Local
Storage Discovery](https://attack.mitre.org/techniques/T1680) which is an adversary''s discovery of local drive, disks and/or
volumes.
Tools such as [Systeminfo](https://attack.mitre.org/software/S0096) can be used to gather detailed system information. If
```
