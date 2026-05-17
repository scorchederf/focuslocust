---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1620 - Reflective Code Loading

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1620` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads. Reflective loading involves allocating then executing payloads directly within the memory of the process, vice creating a thread or process backed by a file path on disk (e.g., Shared Modules).

Reflectively loaded payloads may be compiled binaries, anonymous files (only present in RAM), or just snubs of fileless executable code (ex: position-independent shellcode). For example, the `Assembly.Load()` method executed by PowerShell may be abused to load raw code into the running process.

Reflective code injection is very similar to Process Injection except that the “injection” loads code into the processes’ own memory instead of that of a separate process. Reflective loading may evade process-based detections since the execution of the arbitrary code may be masked within a legitimate or otherwise benign process. Reflectively loading payloads directly into memory may also avoid creating files or other artifacts on disk, while also enabling malware to keep these payloads encrypted (or otherwise obfuscated) until execution.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [Brute Ratel C4](../../tools/unknown/brute-ratel-c4.md) | explicit | source | [Brute Ratel C4](https://attack.mitre.org/software/S1063) has used reflective loading to execute malicious DLLs.(Citation: MDSec Brute Ratel August 2022) |
| [Donut](../../tools/unknown/donut.md) | explicit | source | [Donut](https://attack.mitre.org/software/S0695) can generate code modules that enable in-memory execution of VBScript, JScript, EXE, DLL, and dotNET payloads.(Citation: Donut Github) |
| [PowerSploit](../../tools/unknown/powersploit.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) reflectively loads a Windows PE file into a process.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can run a .NET executable within the memory of a sacrificial process by loading the CLR.(Citation: Github_SILENTTRINITY)   |

## Source Verification

[source record](../../sources/mitre/reflective-code-loading.md)

## Evidence Excerpt

```text
created: '2021-10-05T01:15:06.293Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads.
Reflective loading involves allocating then executing payloads directly within the memory of the process, vice creating
a thread or process backed by a file path on disk (e.g., [Shared Modules](https://attack.mitre.org/techniques/T1129)).
Reflectively loaded payloads may be compiled binaries, anonymous files (only present in RAM), or just snubs of fileless
executable code (ex: position-independent shellcode).(Citation: Introducing Donut)(Citation: S1 Custom Shellcode Tool)(Citation:
Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Mandiant BYOL) For example, the `Assembly.Load()` method executed
```
