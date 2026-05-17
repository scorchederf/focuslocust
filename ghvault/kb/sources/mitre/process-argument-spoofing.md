---
parsed_by: focuslocust
source: mitre
type: generated
---
# Process Argument Spoofing

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1564.010` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Process Argument Spoofing](../../attack/techniques/T1564.010-process-argument-spoofing.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | T1564.010 |
| name | Process Argument Spoofing |
| type | technique |
| source | mitre |
| url | https://attack.mitre.org/techniques/T1564/010 |

## Preserved Source Material

```yaml
created: '2021-11-19T14:13:11.335Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may attempt to hide process command-line arguments by overwriting process memory. Process command-line
  arguments are stored in the process environment block (PEB), a data structure used by Windows to store various information
  about/used by a process. The PEB includes the process command-line arguments that are referenced when executing the process.
  When a process is created, defensive tools/sensors that monitor process creations may retrieve the process arguments from
  the PEB.(Citation: Microsoft PEB 2021)(Citation: Xpn Argue Like Cobalt 2019)


  Adversaries may manipulate a process PEB to evade defenses. For example, [Process Hollowing](https://attack.mitre.org/techniques/T1055/012)
  can be abused to spawn a process in a suspended state with benign arguments. After the process is spawned and the PEB is
  initialized (and process information is potentially logged by tools/sensors), adversaries may override the PEB to modify
  the command-line arguments (ex: using the [Native API](https://attack.mitre.org/techniques/T1106) <code>WriteProcessMemory()</code>
  function) then resume process execution with malicious arguments.(Citation: Cobalt Strike Arguments 2019)(Citation: Xpn
  Argue Like Cobalt 2019)(Citation: Nviso Spoof Command Line 2020)


  Adversaries may also execute a process with malicious command-line arguments then patch the memory with benign arguments
  that may bypass subsequent process memory analysis.(Citation: FireEye FiveHands April 2021)


  This behavior may also be combined with other tricks (such as [Parent PID Spoofing](https://attack.mitre.org/techniques/T1134/004))
  to manipulate or further evade process-based detections.'
external_references:
- external_id: T1564.010
  source_name: mitre-attack
  url: https://attack.mitre.org/techniques/T1564/010
- description: Chester, A. (2019, January 28). How to Argue like Cobalt Strike. Retrieved November 19, 2021.
  source_name: Xpn Argue Like Cobalt 2019
  url: https://blog.xpnsec.com/how-to-argue-like-cobalt-strike/
- description: 'Daman, R. (2020, February 4). The return of the spoof part 2: Command line spoofing. Retrieved November 19,
    2021.'
  source_name: Nviso Spoof Command Line 2020
  url: https://blog.nviso.eu/2020/02/04/the-return-of-the-spoof-part-2-command-line-spoofing/
- description: 'McLellan, T.  and Moore, J. et al. (2021, April 29). UNC2447 SOMBRAT and FIVEHANDS Ransomware: A Sophisticated
    Financial Threat. Retrieved June 2, 2021.'
  source_name: FireEye FiveHands April 2021
  url: https://www.fireeye.com/blog/threat-research/2021/04/unc2447-sombrat-and-fivehands-ransomware-sophisticated-financial-threat.html
- description: Microsoft. (2021, October 6). PEB structure (winternl.h). Retrieved November 19, 2021.
  source_name: Microsoft PEB 2021
  url: https://docs.microsoft.com/en-us/windows/win32/api/winternl/ns-winternl-peb
- description: Mudge, R. (2019, January 2). https://blog.cobaltstrike.com/2019/01/02/cobalt-strike-3-13-why-do-we-argue/.
    Retrieved November 19, 2021.
  source_name: Cobalt Strike Arguments 2019
  url: https://blog.cobaltstrike.com/2019/01/02/cobalt-strike-3-13-why-do-we-argue/
id: attack-pattern--ffe59ad3-ad9b-4b9f-b74f-5beb3c309dc1
kill_chain_phases:
- kill_chain_name: mitre-attack
  phase_name: stealth
modified: '2026-04-15T20:25:25.946Z'
name: Process Argument Spoofing
object_marking_refs:
- marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168
revoked: false
spec_version: '2.1'
type: attack-pattern
x_mitre_attack_spec_version: 3.3.0
x_mitre_deprecated: false
x_mitre_domains:
- enterprise-attack
x_mitre_is_subtechnique: true
x_mitre_modified_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
x_mitre_platforms:
- Windows
x_mitre_version: '2.0'
```
