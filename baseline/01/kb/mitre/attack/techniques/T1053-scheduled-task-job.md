---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1053
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/execution
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/containers
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1053-scheduled-task-job
tactic:
    - Execution
    - Persistence
    - Privilege Escalation
platforms:
    - Containers
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may abuse task scheduling functionality to facilitate initial or recurring execution of malicious code. Utilities exist within all major operating systems to schedule programs or scripts to be executed at a specified date and time. A task can also be scheduled on a remote system, provided the proper authentication is met (ex: RPC and file and printer sharing in Windows environments). Scheduling a task on a remote system typically may require being a member of an admin or otherwise privileged group on the remote system.[^2] <br><br>Adversaries may use task scheduling to execute programs at system startup or on a scheduled basis for persistence. These mechanisms can also be abused to run a process under the context of a specified account (such as one with elevated permissions/privileges). Similar to [[kb/mitre/attack/techniques/T1218-system-binary-proxy-execution|System Binary Proxy Execution]], adversaries have also abused task scheduling to potentially mask one-time execution under a trusted system process.[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0447](https://attack.mitre.org/software/S0447) | Lokibot | Lokibot's second stage DLL has set a timer using “timeSetEvent” to schedule its next execution.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Limit privileges of user accounts and remediate Privilege Escalation vectors so only authorized administrators can create scheduled tasks on remote systems. |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Restrict access by setting directory and file permissions that are not specific to users or privileged accounts. |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Configure the Increase Scheduling Priority option to only allow the Administrators group the rights to schedule a priority process. This can be can be configured through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > User Rights Assignment: Increase scheduling priority. [^1]  |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | Configure settings for scheduled tasks to force tasks to run under the context of the authenticated account instead of allowing them to run as SYSTEM. The associated Registry key is located at `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\SubmitControl`. The setting can be configured through GPO: Computer Configuration > [Policies] > Windows Settings > Security Settings > Local Policies > Security Options: Domain Controller: Allow server operators to schedule tasks, set to disabled. [^1]  |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Toolkits like the PowerSploit framework contain PowerUp modules that can be used to explore systems for permission weaknesses in scheduled tasks that could be used to escalate privileges. [^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1053.005-scheduled-task\|T1053.005]] | Scheduled Task |
| [[kb/mitre/attack/techniques/T1053.007-container-orchestration-job\|T1053.007]] | Container Orchestration Job |
| [[kb/mitre/attack/techniques/T1053.003-cron\|T1053.003]] | Cron |
| [[kb/mitre/attack/techniques/T1053.006-systemd-timers\|T1053.006]] | Systemd Timers |
| [[kb/mitre/attack/techniques/T1053.002-at\|T1053.002]] | At |

 [^1]: [ProofPoint Serpent](https://www.proofpoint.com/us/blog/threat-insight/serpent-no-swiping-new-backdoor-targets-french-entities-unique-attack-chain)
 [^2]: [TechNet Task Scheduler Security](https://technet.microsoft.com/en-us/library/cc785125.aspx)
 [^3]: [TechNet Server Operator Scheduled Task](https://technet.microsoft.com/library/jj852168.aspx)
 [^4]: [Talos Lokibot Jan 2021](https://blog.talosintelligence.com/2021/01/a-deep-dive-into-lokibot-infection-chain.html)
 [^5]: [TechNet Scheduling Priority](https://technet.microsoft.com/library/dn221960.aspx)
 [^6]: [Powersploit](https://github.com/mattifestation/PowerSploit)
