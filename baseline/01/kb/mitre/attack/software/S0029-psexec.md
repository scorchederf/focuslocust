---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0029
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0029-psexec
---

## Description

[[kb/mitre/attack/software/S0029-psexec|PsExec]] is a free Microsoft tool that can be used to execute a program on another computer. It is used by IT administrators and attackers.[^2] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1021.002-smb-windows-admin-shares\|T1021.002]] | SMB/Windows Admin Shares | [[kb/mitre/attack/software/S0029-psexec\|PsExec]], a tool that has been used by adversaries, writes programs to the `ADMIN$` network share to execute commands on remote systems.[^1]  |
| [[kb/mitre/attack/techniques/T1136.002-domain-account\|T1136.002]] | Domain Account | [[kb/mitre/attack/software/S0029-psexec\|PsExec]] has the ability to remotely create accounts on target systems.[^1]  |
| [[kb/mitre/attack/techniques/T1543.003-windows-service\|T1543.003]] | Windows Service | [[kb/mitre/attack/software/S0029-psexec\|PsExec]] can leverage Windows services to escalate privileges from administrator to SYSTEM with the `-s` argument.[^1]  |
| [[kb/mitre/attack/techniques/T1569.002-service-execution\|T1569.002]] | Service Execution | Microsoft Sysinternals [[kb/mitre/attack/software/S0029-psexec\|PsExec]] is a popular administration tool that can be used to execute binaries on remote systems using a temporary Windows service.[^1]  |
| [[kb/mitre/attack/techniques/T1570-lateral-tool-transfer\|T1570]] | Lateral Tool Transfer | [[kb/mitre/attack/software/S0029-psexec\|PsExec]] can be used to download or upload a file over a network share.[^1]  |

 [^1]: [SANS PsExec](https://www.sans.org/blog/protecting-privileged-domain-accounts-psexec-deep-dive/)
 [^2]: [Russinovich Sysinternals](https://technet.microsoft.com/en-us/sysinternals/bb897553.aspx)
 [^3]: [PsExec Russinovich](http://windowsitpro.com/systems-management/psexec)
 [^4]: [NCC Group Fivehands June 2021](https://research.nccgroup.com/2021/06/15/handy-guide-to-a-new-fivehands-ransomware-variant/)
