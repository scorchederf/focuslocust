---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1106 - Native API

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1106` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may interact with the native OS application programming interface (API) to execute behaviors. Native APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices, memory, and processes. These native APIs are leveraged by the OS during system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine operations.

Adversaries may abuse these OS API functions as a means of executing behaviors. Similar to Command and Scripting Interpreter, the native API and its hierarchy of interfaces provide mechanisms to interact with and utilize various components of a victimized system.

Native API functions (such as <code>NtCreateProcess</code>) may be directed invoked via system calls / syscalls, but these features are also often exposed to user-mode applications via interfaces and libraries. For example, functions such as the Windows API <code>CreateProcess()</code> or GNU <code>fork()</code> will allow programs and scripts to start other processes. This may allow API callers to execute a binary, run a CLI command, load modules, etc. as thousands of similar API functions exist for various system operations.

Higher level software frameworks, such as Microsoft .NET and macOS Cocoa, are also available to interact with native APIs. These frameworks typically provide language wrappers/abstractions to API functionalities and are designed for ease-of-use/portability of code.

Adversaries may use assembly to directly or in-directly invoke syscalls in an attempt to subvert defensive sensors and detection signatures such as user mode API-hooks. Adversaries may also attempt to tamper with sensors and defensive tools associated with API monitoring, such as unhooking monitored functions via Disable or Modify Tools.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AsyncRAT](../../tools/unknown/asyncrat.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to use OS APIs including `CheckRemoteDebuggerPresent`.(Citation: Telefonica Snip3 December 2021) |
| [BloodHound](../../tools/unknown/bloodhound.md) | explicit | source | [BloodHound](https://attack.mitre.org/software/S0521) can use .NET API calls in the SharpHound ingestor component to pull Active Directory data.(Citation: GitHub Bloodhound) |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) can call multiple Windows APIs for execution, to share memory, and defense evasion.(Citation: Palo Alto Brute Ratel July 2022)(Citation: MDSec Brute Ratel August 2022) |
| [Donut](../../tools/unknown/donut.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) code modules use various API functions to load and inject code.(Citation: Donut Github)	 |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) contains a variety of enumeration modules that have an option to use API calls to carry out tasks.(Citation: Github PowerShell Empire) |
| [Imminent Monitor](../../tools/unknown/imminent-monitor.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has leveraged CreateProcessW() call to execute the debugger.(Citation: QiAnXin APT-C-36 Feb2019) |
| [PcShare](../../tools/unknown/pcshare.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) has used a variety of Windows API functions.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) has the ability to leverage API including `GetProcAddress` and `LoadLibrary`.(Citation: GitHub SILENTTRINITY Modules July 2019) |
| [ShimRatReporter](../../tools/unknown/shimratreporter.md) | explicit | source | [ShimRatReporter](https://attack.mitre.org/software/S0445) used several Windows API functions to gather information from the infected system.(Citation: FOX-IT May 2016 Mofang) |

## Source Verification

[source record](../../sources/mitre/native-api.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:17.472Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may interact with the native OS application programming interface (API) to execute behaviors. Native
APIs provide a controlled means of calling low-level OS services within the kernel, such as those involving hardware/devices,
memory, and processes.(Citation: NT API Windows)(Citation: Linux Kernel API) These native APIs are leveraged by the OS during
system boot (when other system components are not yet initialized) as well as carrying out tasks and requests during routine
operations.
Adversaries may abuse these OS API functions as a means of executing behaviors. Similar to [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059),
```
