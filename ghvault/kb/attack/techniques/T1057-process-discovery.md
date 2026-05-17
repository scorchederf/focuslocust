---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1057 - Process Discovery

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1057` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may attempt to get information about running processes on a system. Information obtained could be used to gain an understanding of common software/applications running on systems within the network. Administrator or otherwise elevated access may provide better process details. Adversaries may use the information from Process Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions.

In Windows environments, adversaries could obtain details on running processes using the Tasklist utility via cmd or <code>Get-Process</code> via PowerShell. Information about processes can also be extracted from the output of Native API calls such as <code>CreateToolhelp32Snapshot</code>. In Mac and Linux, this is accomplished with the <code>ps</code> command. Adversaries may also opt to enumerate processes via `/proc`. ESXi also supports use of the `ps` command, as well as `esxcli system process list`.

On network devices, Network Device CLI commands such as `show processes` can be used to display current running processes.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AsyncRAT](../../tools/unknown/asyncrat.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can examine running processes to determine if a debugger is present.(Citation: Telefonica Snip3 December 2021) |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can enumerate all processes and locate specific process IDs (PIDs).(Citation: Palo Alto Brute Ratel July 2022) |
| [Donut](../../tools/unknown/donut.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) includes subprojects that enumerate and identify information about [Process Injection](https://attack.mitre.org/techniques/T1055) candidates.(Citation: Donut Github)	 |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) can find information about processes running on local and remote systems.(Citation: Github PowerShell Empire)(Citation: Talos Frankenstein June 2019) |
| [Imminent Monitor](../../tools/unknown/imminent-monitor.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a "Process Watcher" feature to monitor processes in case the client ever crashes or gets closed.(Citation: Imminent Unit42 Dec2019) |
| [IronNetInjector](../../tools/unknown/ironnetinjector.md) | explicit | source | [IronNetInjector](https://attack.mitre.org/software/S0581) can identify processes via C# methods such as <code>GetProcessesByName</code> and running [Tasklist](https://attack.mitre.org/software/S0057) with the Python <code>os.popen</code> function.(Citation: Unit 42 IronNetInjector February 2021 ) |
| [PcShare](../../tools/unknown/pcshare.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can obtain a list of running processes on a compromised host.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [PowerSploit](../../tools/unknown/powersploit.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-ProcessTokenPrivilege</code> Privesc-PowerUp module can enumerate privileges for a given process.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [Pupy](../../tools/unknown/pupy.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can list the running processes and get the process ID and parent process’s ID.(Citation: GitHub Pupy) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can discover running processes on compromised machines.(Citation: Fortinet Remcos Campaign NOV 2024)<br> |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can enumerate processes, including properties to determine if they have the Common Language Runtime (CLR) loaded.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) listed all running processes on the machine.(Citation: FOX-IT May 2016 Mofang) |
| [Tasklist](../../tools/unknown/tasklist.md) | explicit | source | [Tasklist](https://attack.mitre.org/software/S0057) can be used to discover processes running on a system.(Citation: Microsoft Tasklist) |

## Source Verification

[source record](../../sources/mitre/process-discovery.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:48.728Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to get information about running processes on a system. Information obtained could be
used to gain an understanding of common software/applications running on systems within the network. Administrator or otherwise
elevated access may provide better process details. Adversaries may use the information from [Process Discovery](https://attack.mitre.org/techniques/T1057)
during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target
and/or attempts specific actions.
In Windows environments, adversaries could obtain details on running processes using the [Tasklist](https://attack.mitre.org/software/S0057)
```
