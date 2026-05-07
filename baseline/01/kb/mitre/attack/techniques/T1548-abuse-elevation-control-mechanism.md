---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1548
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/iaas
    - platform/identity_provider
    - platform/linux
    - platform/macos
    - platform/office_suite
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1548-abuse-elevation-control-mechanism
tactic:
    - Privilege Escalation
platforms:
    - Linux
    - macOS
    - Windows
    - IaaS
    - Office Suite
    - Identity Provider
permissions required:
    - none
---

## Description

Adversaries may circumvent mechanisms designed to control privilege elevation to gain higher-level permissions. Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can perform on a machine. Authorization has to be granted to specific users in order to perform tasks that can be considered of higher risk.[^1] [^4]  An adversary can perform several methods to take advantage of built-in control mechanisms in order to escalate privileges on a system.[^2] [^3] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin implements a variation of the `ucmDccwCOMMethod` technique abusing the Windows AutoElevate backdoor to bypass UAC while elevating privileges.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | Limit the privileges of cloud accounts to assume, create, or impersonate additional roles, policies, and permissions to only those required. Where just-in-time access is enabled, consider requiring manual approval for temporary elevation of privileges. |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | The sudoers file should be strictly edited such that passwords are always required and that users can't spawn risky processes as users with higher privilege. |
| [[kb/mitre/attack/mitigations/M1026-privileged-account-management\|M1026]] | Privileged Account Management | Remove users from the local administrator group on systems.<br><br>By requiring a password, even if an adversary can get terminal access, they must know the password to run anything in the sudoers file. Setting the timestamp_timeout to 0 will require the user to input their password every time sudo is executed. |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | Applications with known vulnerabilities or known shell escapes should not have the setuid or setgid bits set to reduce potential damage if an application is compromised. Additionally, the number of programs with setuid or setgid bits set should be minimized across a system. Ensuring that the sudo tty_tickets setting is enabled will prevent this leakage across tty sessions. |
| [[kb/mitre/attack/mitigations/M1038-execution-prevention\|M1038]] | Execution Prevention | System settings can prevent applications from running that haven't been downloaded from legitimate repositories which may help mitigate some of these issues. Not allowing unsigned applications from being run may also mitigate some risk. |
| [[kb/mitre/attack/mitigations/M1047-audit\|M1047]] | Audit | Check for common UAC bypass weaknesses on Windows systems to be aware of the risk posture and address issues where appropriate.[^1]  |
| [[kb/mitre/attack/mitigations/M1051-update-software\|M1051]] | Update Software | Perform regular software updates to mitigate exploitation risk. |
| [[kb/mitre/attack/mitigations/M1052-user-account-control\|M1052]] | User Account Control | Although UAC bypass techniques exist, it is still prudent to use the highest enforcement level for UAC when possible and mitigate bypass opportunities that exist with techniques such as [[kb/mitre/attack/techniques/T1574.001-dll\|DLL]]. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1548.002-bypass-user-account-control\|T1548.002]] | Bypass User Account Control |
| [[kb/mitre/attack/techniques/T1548.003-sudo-and-sudo-caching\|T1548.003]] | Sudo and Sudo Caching |
| [[kb/mitre/attack/techniques/T1548.001-setuid-and-setgid\|T1548.001]] | Setuid and Setgid |
| [[kb/mitre/attack/techniques/T1548.005-temporary-elevated-cloud-access\|T1548.005]] | Temporary Elevated Cloud Access |
| [[kb/mitre/attack/techniques/T1548.004-elevated-execution-with-prompt\|T1548.004]] | Elevated Execution with Prompt |
| [[kb/mitre/attack/techniques/T1548.006-tcc-manipulation\|T1548.006]] | TCC Manipulation |

 [^1]: [TechNet How UAC Works](https://technet.microsoft.com/en-us/itpro/windows/keep-secure/how-user-account-control-works)
 [^2]: [OSX Keydnap malware](https://www.welivesecurity.com/2016/07/06/new-osxkeydnap-malware-hungry-credentials/)
 [^3]: [Fortinet Fareit](https://blog.fortinet.com/2016/12/16/malicious-macro-bypasses-uac-to-elevate-privilege-for-fareit-malware)
 [^4]: [sudo man page 2018](https://www.sudo.ws/)
 [^5]: [Github UACMe](https://github.com/hfiref0x/UACME)
 [^6]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
