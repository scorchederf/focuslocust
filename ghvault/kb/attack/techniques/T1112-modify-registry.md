---
parsed_by: focuslocust
source: mitre
type: generated
---
# T1112 - Modify Registry

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `technique` |
| Record ID | `T1112` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Adversaries may interact with the Windows Registry as part of a variety of other techniques to aid in defense evasion, persistence, and execution.

Access to specific areas of the Registry depends on account permissions, with some keys requiring administrator-level access. The built-in Windows command-line utility Reg may be used for local or remote Registry modification. Other tools, such as remote access tools, may also contain functionality to interact with the Registry through the Windows API.

The Registry may be modified in order to hide configuration information or malicious payloads via Obfuscated Files or Information. The Registry may also be modified to impair defenses, such as by enabling macros for all Microsoft Office products, allowing privilege escalation without alerting the user, increasing the maximum number of allowed outbound requests, and/or modifying systems to store plaintext credentials in memory.

The Registry of a remote system may be modified to aid in execution of files as part of lateral movement. It requires the remote Registry service to be running on the target system. Often Valid Accounts are required, along with access to the remote system's SMB/Windows Admin Shares for RPC communication.

Finally, Registry modifications may also include actions to hide keys, such as prepending key names with a null character, which will cause an error and/or be ignored when read via Reg or other utilities using the Win32 API. Adversaries may abuse these pseudo-hidden keys to conceal payloads/commands used to maintain persistence.

## Related Tools

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [AADInternals](../../tools/unknown/aadinternals.md) | explicit | source | [AADInternals](https://attack.mitre.org/software/S0677) can modify registry keys as part of setting a new pass-through authentication agent.(Citation: AADInternals Documentation) |
| [CSPY Downloader](../../tools/unknown/cspy-downloader.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) can write to the Registry under the <code>%windir%</code> variable to execute tasks.(Citation: Cybereason Kimsuky November 2020) |
| [CrackMapExec](../../tools/unknown/crackmapexec.md) | explicit | source | [CrackMapExec](https://attack.mitre.org/software/S0488) can create a registry key using wdigest.(Citation: CME Github September 2018) |
| [NPPSPY](../../tools/unknown/nppspy.md) | explicit | source | [NPPSPY](https://attack.mitre.org/software/S1131) modifies the Registry to record the malicious listener for output from the Winlogon process.(Citation: Huntress NPPSPY 2022) |
| [PcShare](../../tools/unknown/pcshare.md) | explicit | source | [PcShare](https://attack.mitre.org/software/S1050) can delete its persistence mechanisms from the registry.(Citation: Bitdefender FunnyDream Campaign November 2020) |
| [QuasarRAT](../../tools/unknown/quasarrat.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) has a command to edit the Registry on the victim’s machine.(Citation: GitHub QuasarRAT)(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [Reg](../../tools/unknown/reg.md) | explicit | source | [Reg](https://attack.mitre.org/software/S0075) may be used to interact with and modify the Windows Registry of a local or remote system at the command-line interface.(Citation: Microsoft Reg) |
| [Remcos](../../tools/unknown/remcos.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has full control of the Registry, including the ability to modify it.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [SILENTTRINITY](../../tools/unknown/silenttrinity.md) | explicit | source | [SILENTTRINITY](https://attack.mitre.org/software/S0692) can modify registry keys, including to enable or disable Remote Desktop Protocol (RDP).(Citation: GitHub SILENTTRINITY Modules July 2019) |

## Source Verification

[source record](../../sources/mitre/modify-registry.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:31:23.587Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: 'Adversaries may interact with the Windows Registry as part of a variety of other techniques to aid in defense
evasion, persistence, and execution.
Access to specific areas of the Registry depends on account permissions, with some keys requiring administrator-level access.
The built-in Windows command-line utility [Reg](https://attack.mitre.org/software/S0075) may be used for local or remote
Registry modification.(Citation: Microsoft Reg) Other tools, such as remote access tools, may also contain functionality
to interact with the Registry through the Windows API.
```
