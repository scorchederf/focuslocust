---
parsed_by: focuslocust
source: mitre
type: generated
---
# Indirect Command Execution

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1202` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1202 |
| name | Indirect Command Execution |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1202 |

## Preserved Source Material

```yaml
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may abuse utilities that allow for command execution to bypass security restrictions that limit
  the use of command-line interpreters. Various Windows utilities may be used to execute commands, possibly without invoking
  [cmd](https://attack.mitre.org/software/S0106). For example, [Forfiles](https://attack.mitre.org/software/S0193), the Program
  Compatibility Assistant (`pcalua.exe`), components of the Windows Subsystem for Linux (WSL), `Scriptrunner.exe`, as well
  as other utilities may invoke the execution of programs and commands from a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059),
  Run window, or via scripts.(Citation: VectorSec ForFiles Aug 2017)(Citation: Evi1cg Forfiles Nov 2017)(Citation: Secure
  Team - Scriptrunner.exe)(Citation: SS64)(Citation: Bleeping Computer - Scriptrunner.exe) Adversaries may also abuse the
  `ssh.exe` binary to execute malicious commands via the `ProxyCommand` and `LocalCommand` options, which can be invoked via
  the `-o` flag or by modifying the SSH config file.(Citation: Threat Actor Targets the Manufacturing industry with Lumma
  Stealer and Amadey Bot)


  Adversaries may abuse these features for [Stealth](https://attack.mitre.org/tactics/TA0005), specifically to perform arbitrary
  execution while subverting detections and/or mitigation controls (such as Group Policy) that limit/prevent the usage of
  [cmd](https://attack.mitre.org/software/S0106) or file extensions more commonly associated with malicious payloads.'
external_references:
- external_id: T1202
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1202
- description: Bill Toulas. (2023, January 4). Hackers abuse Windows error reporting tool to deploy malware. Retrieved July
    8, 2024.
  source_name: Bleeping Computer - Scriptrunner.exe
  url: https://www.bleepingcomputer.com/news/security/hackers-abuse-windows-error-reporting-tool-to-deploy-malware/
- description: Cyble. (2024, December 5). Threat Actor Targets the Manufacturing industry with Lumma Stealer and Amadey Bot.
    Retrieved February 4, 2025.
  source_name: Threat Actor Targets the Manufacturing industry with Lumma Stealer and Amadey Bot
  url: https://cyble.com/blog/threat-actor-targets-manufacturing-industry-with-malware/
- description: Evi1cg. (2017, November 26). block cmd.exe ? try this :. Retrieved September 12, 2024.
  source_name: Evi1cg Forfiles Nov 2017
  url: https://x.com/Evi1cg/status/935027922397573120
- description: Secure Team - Information Assurance. (2023, January 8). Windows Error Reporting Tool Abused to Load Malware.
    Retrieved July 8, 2024.
  source_name: Secure Team - Scriptrunner.exe
  url: https://secureteam.co.uk/2023/01/08/windows-error-reporting-tool-abused-to-load-malware/
- description: SS64. (n.d.). ScriptRunner.exe. Retrieved July 8, 2024.
  source_name: SS64
  url: https://ss64.com/nt/scriptrunner.html
- description: vector_sec. (2017, August 11). Defenders watching launches of cmd? What about forfiles?. Retrieved September
    12, 2024.
  source_name: VectorSec ForFiles Aug 2017
  url: https://x.com/vector_sec/status/896049052642533376
id: attack-pattern--3b0e52ce-517a-4614-a523-1bd5deef6c5e
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:31:14.152Z'
name: Indirect Command Execution
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Liran Ravich, CardinalOps
- Matthew Demaske, Adaptforward
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: false
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '2.0'
```
