---
parsed_by: focuslocust
source: mitre
type: generated
---
# PsExec

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0029` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

PsExec is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/psexec.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1021.002 - SMB／Windows Admin Shares](../../attack/techniques/T1021.002-smb-windows-admin-shares.md) | explicit | source | [PsExec](https://attack.mitre.org/software/S0029), a tool that has been used by adversaries, writes programs to the <code>ADMIN$</code> network share to execute commands on remote systems.(Citation: PsExec Russinovich) |
| [T1136.002 - Domain Account](../../attack/techniques/T1136.002-domain-account.md) | explicit | source | [PsExec](https://attack.mitre.org/software/S0029) has the ability to remotely create accounts on target systems.(Citation: NCC Group Fivehands June 2021) |
| [T1543.003 - Windows Service](../../attack/techniques/T1543.003-windows-service.md) | explicit | source | [PsExec](https://attack.mitre.org/software/S0029) can leverage Windows services to escalate privileges from administrator to SYSTEM with the <code>-s</code> argument.(Citation: Russinovich Sysinternals) |
| [T1569.002 - Service Execution](../../attack/techniques/T1569.002-service-execution.md) | explicit | source | Microsoft Sysinternals [PsExec](https://attack.mitre.org/software/S0029) is a popular administration tool that can be used to execute binaries on remote systems using a temporary Windows service.(Citation: Russinovich Sysinternals) |
| [T1570 - Lateral Tool Transfer](../../attack/techniques/T1570-lateral-tool-transfer.md) | explicit | source | [PsExec](https://attack.mitre.org/software/S0029) can be used to download or upload a file over a network share.(Citation: PsExec Russinovich) |

## Source Verification

[source record](../../sources/mitre/psexec.md)

## Evidence Excerpt

```text
created: '2017-05-31T21:32:21.771Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[PsExec](https://attack.mitre.org/software/S0029) is a free Microsoft tool that can be used to execute a program
on another computer. It is used by IT administrators and attackers.(Citation: Russinovich Sysinternals)(Citation: SANS PsExec)'
external_references:
- external_id: S0029
source_name: mitre-attack
url: https://attack.mitre.org/software/S0029
```
