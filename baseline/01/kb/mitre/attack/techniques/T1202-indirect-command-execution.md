---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1202
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/stealth
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1202-indirect-command-execution
tactic:
    - Stealth
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may abuse utilities that allow for command execution to bypass security restrictions that limit the use of command-line interpreters. Various Windows utilities may be used to execute commands, possibly without invoking [[kb/mitre/attack/software/S0106-cmd|cmd]]. For example, [[kb/mitre/attack/software/S0193-forfiles|Forfiles]], the Program Compatibility Assistant (`pcalua.exe`), components of the Windows Subsystem for Linux (WSL), `Scriptrunner.exe`, as well as other utilities may invoke the execution of programs and commands from a [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter|Command and Scripting Interpreter]], Run window, or via scripts.[^6] [^3] [^4] [^5] [^1]  Adversaries may also abuse the `ssh.exe` binary to execute malicious commands via the `ProxyCommand` and `LocalCommand` options, which can be invoked via the `-o` flag or by modifying the SSH config file.[^2] <br><br>Adversaries may abuse these features for [[kb/mitre/attack/tactics/TA0005-stealth|Stealth]], specifically to perform arbitrary execution while subverting detections and/or mitigation controls (such as Group Policy) that limit/prevent the usage of [[kb/mitre/attack/software/S0106-cmd|cmd]] or file extensions more commonly associated with malicious payloads.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/software/S0193-forfiles\|S0193]] | Forfiles | [[kb/mitre/attack/software/S0193-forfiles\|Forfiles]] can be used to subvert controls and possibly conceal command execution by not directly invoking [[kb/mitre/attack/software/S0106-cmd\|cmd]].[^2] [^1]  |
| [S0379](https://attack.mitre.org/software/S0379) | Revenge RAT | Revenge RAT uses the [[kb/mitre/attack/software/S0193-forfiles\|Forfiles]] utility to execute commands on the system.[^1]  |

 [^1]: [Bleeping Computer - Scriptrunner.exe](https://www.bleepingcomputer.com/news/security/hackers-abuse-windows-error-reporting-tool-to-deploy-malware/)
 [^2]: [Threat Actor Targets the Manufacturing industry with Lumma Stealer and Amadey Bot](https://cyble.com/blog/threat-actor-targets-manufacturing-industry-with-malware/)
 [^3]: [Evi1cg Forfiles Nov 2017](https://x.com/Evi1cg/status/935027922397573120)
 [^4]: [Secure Team - Scriptrunner.exe](https://secureteam.co.uk/2023/01/08/windows-error-reporting-tool-abused-to-load-malware/)
 [^5]: [SS64](https://ss64.com/nt/scriptrunner.html)
 [^6]: [VectorSec ForFiles Aug 2017](https://x.com/vector_sec/status/896049052642533376)
 [^7]: [Cofense RevengeRAT Feb 2019](https://web.archive.org/web/20200428173819/https://cofense.com/upgrades-delivery-support-infrastructure-revenge-rat-malware-bigger-threat/)
