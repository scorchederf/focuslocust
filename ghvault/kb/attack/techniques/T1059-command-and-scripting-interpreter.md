---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1059 - Command and Scripting Interpreter

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1059` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces and languages provide ways of interacting with computer systems and are a common feature across many different platforms. Most systems come with some built-in command-line interface and scripting capabilities, for example, macOS and Linux distributions include some flavor of Unix Shell while Windows installations include the Windows Command Shell and PowerShell.

There are also cross-platform interpreters such as Python, as well as those commonly associated with client applications such as JavaScript and Visual Basic.

Adversaries may abuse these technologies in various ways as a means of executing arbitrary commands. Commands and scripts can be embedded in Initial Access payloads delivered to victims as lure documents or as secondary payloads downloaded from an existing C2. Adversaries may also execute commands through interactive terminals/shells, as well as utilize various Remote Services in order to achieve remote Execution.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Donut](../../tools/unknown/donut.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can generate shellcode outputs that execute via Ruby.(Citation: Donut Github)	 |
| [Dotnet.exe](../../tools/windows/dotnet.exe.md) | explicit | source | Command metadata lists T1059: dotnet.exe fsi |
| [Empire](../../tools/unknown/empire.md) | explicit | source | [Empire](https://attack.mitre.org/software/S0363) uses a command-line interface to interact with systems.(Citation: Github PowerShell Empire) |
| [Fsi.exe](../../tools/windows/fsi.exe.md) | explicit | source | Command metadata lists T1059: fsi.exe |
| [FsiAnyCpu.exe](../../tools/windows/fsianycpu.exe.md) | explicit | source | Command metadata lists T1059: fsianycpu.exe |
| [Imminent Monitor](../../tools/unknown/imminent-monitor.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a CommandPromptPacket and ScriptPacket module(s) for creating a remote shell and executing scripts.(Citation: QiAnXin APT-C-36 Feb2019) |

## Source Verification

[source record](../../sources/mitre/command-and-scripting-interpreter.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:30:49.546Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces
and languages provide ways of interacting with computer systems and are a common feature across many different platforms.
Most systems come with some built-in command-line interface and scripting capabilities, for example, macOS and Linux distributions
include some flavor of [Unix Shell](https://attack.mitre.org/techniques/T1059/004) while Windows installations include the
[Windows Command Shell](https://attack.mitre.org/techniques/T1059/003) and [PowerShell](https://attack.mitre.org/techniques/T1059/001).
There are also cross-platform interpreters such as [Python](https://attack.mitre.org/techniques/T1059/006), as well as those
```
