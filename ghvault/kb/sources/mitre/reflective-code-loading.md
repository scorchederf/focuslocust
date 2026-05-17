---
parsed_by: focuslocust
source: mitre
type: generated
---
# Reflective Code Loading

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

## Generated Concept Page

- [Reflective Code Loading](../../attack/techniques/T1620-reflective-code-loading.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1620 |
| name | Reflective Code Loading |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1620 |

## Preserved Source Material

```yaml
created: '2021-10-05T01:15:06.293Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may reflectively load code into a process in order to conceal the execution of malicious payloads.
  Reflective loading involves allocating then executing payloads directly within the memory of the process, vice creating
  a thread or process backed by a file path on disk (e.g., [Shared Modules](https://attack.mitre.org/techniques/T1129)).


  Reflectively loaded payloads may be compiled binaries, anonymous files (only present in RAM), or just snubs of fileless
  executable code (ex: position-independent shellcode).(Citation: Introducing Donut)(Citation: S1 Custom Shellcode Tool)(Citation:
  Stuart ELF Memory)(Citation: 00sec Droppers)(Citation: Mandiant BYOL) For example, the `Assembly.Load()` method executed
  by [PowerShell](https://attack.mitre.org/techniques/T1059/001) may be abused to load raw code into the running process.(Citation:
  Microsoft AssemblyLoad)


  Reflective code injection is very similar to [Process Injection](https://attack.mitre.org/techniques/T1055) except that
  the “injection” loads code into the processes’ own memory instead of that of a separate process. Reflective loading may
  evade process-based detections since the execution of the arbitrary code may be masked within a legitimate or otherwise
  benign process. Reflectively loading payloads directly into memory may also avoid creating files or other artifacts on disk,
  while also enabling malware to keep these payloads encrypted (or otherwise obfuscated) until execution.(Citation: Stuart
  ELF Memory)(Citation: 00sec Droppers)(Citation: Intezer ACBackdoor)(Citation: S1 Old Rat New Tricks)'
external_references:
- external_id: T1620
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1620
- description: 0x00pico. (2017, September 25). Super-Stealthy Droppers. Retrieved October 4, 2021.
  source_name: 00sec Droppers
  url: https://0x00sec.org/t/super-stealthy-droppers/3715
- description: Bunce, D. (2019, October 31). Building A Custom Tool For Shellcode Analysis. Retrieved October 4, 2021.
  source_name: S1 Custom Shellcode Tool
  url: https://www.sentinelone.com/blog/building-a-custom-tool-for-shellcode-analysis/
- description: Kirk, N. (2018, June 18). Bring Your Own Land (BYOL) – A Novel Red Teaming Technique. Retrieved October 4,
    2021.
  source_name: Mandiant BYOL
  url: https://www.mandiant.com/resources/bring-your-own-land-novel-red-teaming-technique
- description: Landry, J. (2016, April 21). Teaching an old RAT new tricks. Retrieved October 4, 2021.
  source_name: S1 Old Rat New Tricks
  url: https://www.sentinelone.com/blog/teaching-an-old-rat-new-tricks/
- description: Microsoft. (n.d.). Assembly.Load Method. Retrieved February 9, 2024.
  source_name: Microsoft AssemblyLoad
  url: https://learn.microsoft.com/dotnet/api/system.reflection.assembly.load
- description: 'Sanmillan, I. (2019, November 18). ACBackdoor: Analysis of a New Multiplatform Backdoor. Retrieved October
    4, 2021.'
  source_name: Intezer ACBackdoor
  url: https://intezer.com/acbackdoor-analysis-of-a-new-multiplatform-backdoor/
- description: Stuart. (2018, March 31). In-Memory-Only ELF Execution (Without tmpfs). Retrieved October 4, 2021.
  source_name: Stuart ELF Memory
  url: https://magisterquis.github.io/2018/03/31/in-memory-only-elf-execution.html
- description: The Wover. (2019, May 9). Donut - Injecting .NET Assemblies as Shellcode. Retrieved October 4, 2021.
  source_name: Introducing Donut
  url: https://thewover.github.io/Introducing-Donut/
id: attack-pattern--4933e63b-9b77-476e-ab29-761bc5b7d15a
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T22:32:18.632Z'
name: Reflective Code Loading
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- João Paulo de A. Filho, @Hug1nN__
- Shlomi Salem, SentinelOne
- Lior Ribak, SentinelOne
- Rex Guo, @Xiaofei_REX, Confluera
- Joas Antonio dos Santos, @C0d3Cr4zy, Inmetrics
- Jiraput Thamsongkrah
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Linux
- macOS
- Windows
x_mitre_version: '2.0'
```
