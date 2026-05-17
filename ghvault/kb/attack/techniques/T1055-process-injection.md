---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1055 - Process Injection

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1055` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process. Running code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via process injection may also evade detection from security products since the execution is masked under a legitimate process. 

There are many different ways to inject code into a process, many of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific. 

More sophisticated samples may perform multiple process injections to segment modules and further evade detection, utilizing named pipes or other inter-process communication (IPC) mechanisms as a communication channel.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Donut](../../tools/unknown/donut.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) includes a subproject <code>DonutTest</code> to inject shellcode into a target process.(Citation: Donut Github)	 |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) contains multiple modules for injecting into processes, such as <code>Invoke-PSInject</code>.(Citation: Github PowerShell Empire) |
| [HTRAN](../../tools/unknown/htran.md) | explicit | source | [HTRAN](https://attack.mitre.org/software/S0040) can inject into into running processes.(Citation: NCSC Joint Report Public Tools) |
| [IronNetInjector](../../tools/unknown/ironnetinjector.md) | explicit | source | [IronNetInjector](https://attack.mitre.org/software/S0581) can use an IronPython scripts to load a .NET injector to inject a payload into its own or a remote process.(Citation: Unit 42 IronNetInjector February 2021 ) |
| [PcShare](../../tools/unknown/pcshare.md) | explicit | source | The [PcShare](https://attack.mitre.org/software/S1050) payload has been injected into the `logagent.exe` and `rdpclip.exe` processes.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [PoshC2](../../tools/unknown/poshc2.md) | explicit | source | [PoshC2](https://attack.mitre.org/software/S0378) contains multiple modules for injecting into processes, such as <code>Invoke-PSInject</code>.(Citation: GitHub PoshC2) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has a command to hide itself by injecting into another process.(Citation: Fortinet Remcos Feb 2017) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can inject shellcode directly into Excel.exe or a specific process.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [Sliver](../../tools/unknown/sliver.md) | explicit | source | [Sliver](https://attack.mitre.org/software/S0633) includes multiple methods to perform process injection to migrate the framework into other, potentially privileged processes on the victim machine.(Citation: Microsoft Sliver 2022)(Citation: Cybereason Sliver Undated)(Citation: Bishop Fox Sliver Framework August 2019)(Citation: GitHub Sliver C2) |
| [coregen.exe](../../tools/windows/coregen.exe.md) | explicit | source | Command metadata lists T1055: coregen.exe dummy_assembly_name |

## Source Verification

[source record](../../sources/mitre/process-injection.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:47.843Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: "Adversaries may inject code into processes in order to evade process-based defenses as well as possibly elevate\
\ privileges. Process injection is a method of executing arbitrary code in the address space of a separate live process.\
\ Running code in the context of another process may allow access to the process's memory, system/network resources, and\
\ possibly elevated privileges. Execution via process injection may also evade detection from security products since the\
\ execution is masked under a legitimate process. \n\nThere are many different ways to inject code into a process, many\
\ of which abuse legitimate functionalities. These implementations exist for every major OS but are typically platform specific.\
```
