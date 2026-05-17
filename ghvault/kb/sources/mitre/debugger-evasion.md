---
parsed_by: focuslocust
source: mitre
type: generated
---
# Debugger Evasion

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1622` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Debugger Evasion](../../attack/techniques/T1622-debugger-evasion.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1622 |
| name | Debugger Evasion |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1622 |

## Preserved Source Material

```yaml
created: '2022-04-01T17:59:46.156Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may employ various means to detect and avoid debuggers. Debuggers are typically used by defenders
  to trace and/or analyze the execution of potential malware payloads.(Citation: ProcessHacker Github)


  Debugger evasion may include changing behaviors based on the results of the checks for the presence of artifacts indicative
  of a debugged environment. Similar to [Virtualization/Sandbox Evasion](https://attack.mitre.org/techniques/T1497), if the
  adversary detects a debugger, they may alter their malware to disengage from the victim or conceal the core functions of
  the implant. They may also search for debugger artifacts before dropping secondary or additional payloads.


  Specific checks will vary based on the target and/or adversary. On Windows, this may involve [Native API](https://attack.mitre.org/techniques/T1106)
  function calls such as <code>IsDebuggerPresent()</code> and <code> NtQueryInformationProcess()</code>, or manually checking
  the <code>BeingDebugged</code> flag of the Process Environment Block (PEB). On Linux, this may involve querying `/proc/self/status`
  for the `TracerPID` field, which indicates whether or not the process is being traced by dynamic analysis tools.(Citation:
  Cado Security P2PInfect 2023)(Citation: Positive Technologies Hellhounds 2023) Other checks for debugging artifacts may
  also seek to enumerate hardware breakpoints, interrupt assembly opcodes, time checks, or measurements if exceptions are
  raised in the current process (assuming a present debugger would “swallow” or handle the potential error).(Citation: hasherezade
  debug)(Citation: AlKhaser Debug)(Citation: vxunderground debug)


  Malware may also leverage Structured Exception Handling (SEH) to detect debuggers by throwing an exception and detecting
  whether the process is suspended. SEH handles both hardware and software expectations, providing control over the exceptions
  including support for debugging. If a debugger is present, the program’s control will be transferred to the debugger, and
  the execution of the code will be suspended. If the debugger is not present, control will be transferred to the SEH handler,
  which will automatically handle the exception and allow the program’s execution to continue.(Citation: Apriorit)


  Adversaries may use the information learned from these debugger checks during automated discovery to shape follow-on behaviors.
  Debuggers can also be evaded by detaching the process or flooding debug logs with meaningless data via messages produced
  by looping [Native API](https://attack.mitre.org/techniques/T1106) function calls such as <code>OutputDebugStringW()</code>.(Citation:
  wardle evilquest partii)(Citation: Checkpoint Dridex Jan 2021)'
external_references:
- external_id: T1622
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1622
- description: Apriorit. (2024, June 4). Anti Debugging Protection Techniques with Examples. Retrieved March 4, 2025.
  source_name: Apriorit
  url: https://www.apriorit.com/dev-blog/367-anti-reverse-engineering-protection-techniques-to-use-before-releasing-software
- description: 'Check Point Research. (2021, January 4). Stopping Serial Killer: Catching the Next Strike. Retrieved September
    7, 2021.'
  source_name: Checkpoint Dridex Jan 2021
  url: https://research.checkpoint.com/2021/stopping-serial-killer-catching-the-next-strike/
- description: hasherezade. (2021, June 30). Module 3 - Understanding and countering malware's evasion and self-defence. Retrieved
    April 1, 2022.
  source_name: hasherezade debug
  url: https://github.com/hasherezade/malware_training_vol1/blob/main/slides/module3/Module3_2_fingerprinting.pdf
- description: jbowen. (2023, December 4). P2Pinfect - New Variant Targets MIPS Devices. Retrieved March 18, 2025.
  source_name: Cado Security P2PInfect 2023
  url: https://www.cadosecurity.com/blog/p2pinfect-new-variant-targets-mips-devices
- description: Noteworthy. (2019, January 6). Al-Khaser. Retrieved April 1, 2022.
  source_name: AlKhaser Debug
  url: https://github.com/LordNoteworthy/al-khaser/tree/master/al-khaser/AntiDebug
- description: 'Patrick Wardle. (2020, July 3). OSX.EvilQuest Uncovered part ii: insidious capabilities. Retrieved March 21,
    2021.'
  source_name: wardle evilquest partii
  url: https://objective-see.com/blog/blog_0x60.html
- description: ProcessHacker. (2009, October 27). Process Hacker. Retrieved April 11, 2022.
  source_name: ProcessHacker Github
  url: https://github.com/processhacker/processhacker
- description: 'PT Expert Security Center. (2023, November 29). Hellhounds: operation Lahat. Retrieved March 18, 2025.'
  source_name: Positive Technologies Hellhounds 2023
  url: https://global.ptsecurity.com/analytics/pt-esc-threat-intelligence/hellhounds-operation-lahat
- description: vxunderground. (2021, June 30). VX-API. Retrieved April 1, 2022.
  source_name: vxunderground debug
  url: https://web.archive.org/web/20250904153443/https://github.com/vxunderground/VX-API/tree/main#anti-debug
id: attack-pattern--e4dc8c01-417f-458d-9ee0-bb0617c1b391
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
- kill_chain_name: mitre-attack
  phase_name: discovery
modified: '2026-04-15T19:57:49.208Z'
name: Debugger Evasion
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_contributors:
- Joas Antonio dos Santos, @C0d3Cr4zy
- TruKno
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
