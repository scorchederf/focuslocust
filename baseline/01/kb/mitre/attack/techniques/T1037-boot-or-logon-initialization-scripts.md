---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1037
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/mitigated
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/esxi
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1037-boot-or-logon-initialization-scripts
tactic:
    - Persistence
    - Privilege Escalation
platforms:
    - ESXi
    - Linux
    - macOS
    - Network Devices
    - Windows
permissions required:
    - none
---

## Description

Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.[^2] [^1]  Initialization scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server. These scripts can vary based on operating system and whether applied locally or remotely.  <br><br>Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. <br><br>An adversary may also be able to escalate their privileges since some boot or logon initialization scripts run with higher privileges.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S1078](https://attack.mitre.org/software/S1078) | RotaJakiro | Depending on the Linux distribution and when executing with root permissions, RotaJakiro may install persistence using a `.conf` file in the `/etc/init/` folder.[^1]  |
| [S1217](https://attack.mitre.org/software/S1217) | VIRTUALPITA | VIRTUALPITA can persist as an init.d startup service on Linux vCenter systems.[^1]  |
| [S9024](https://attack.mitre.org/software/S9024) | SPAWNCHIMERA | SPAWNCHIMERA has modified the boot process files within `/tmp/coreboot_fs/bin/init` to establish persistence.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1022-restrict-file-and-directory-permissions\|M1022]] | Restrict File and Directory Permissions | Restrict write access to logon scripts to specific administrators. |
| [[kb/mitre/attack/mitigations/M1024-restrict-registry-permissions\|M1024]] | Restrict Registry Permissions | Ensure proper permissions are set for Registry hives to prevent users from modifying keys for logon scripts that may lead to persistence. |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1037.002-login-hook\|T1037.002]] | Login Hook |
| [[kb/mitre/attack/techniques/T1037.005-startup-items\|T1037.005]] | Startup Items |
| [[kb/mitre/attack/techniques/T1037.003-network-logon-script\|T1037.003]] | Network Logon Script |
| [[kb/mitre/attack/techniques/T1037.004-rc-scripts\|T1037.004]] | RC Scripts |
| [[kb/mitre/attack/techniques/T1037.001-logon-script-windows\|T1037.001]] | Logon Script (Windows) |

 [^1]: [Anomali Rocke March 2019](https://www.anomali.com/blog/rocke-evolves-its-arsenal-with-a-new-malware-family-written-in-golang)
 [^2]: [Mandiant APT29 Eye Spy Email Nov 22](https://www.mandiant.com/resources/blog/unc3524-eye-spy-email)
 [^3]: [CISA SPAWNCHIMERA RESURGE February 2026](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
 [^4]: [RotaJakiro 2021 netlab360 analysis](https://blog.netlab.360.com/stealth_rotajakiro_backdoor_en/)
 [^5]: [Google Cloud Threat Intelligence ESXi VIBs 2022](https://cloud.google.com/blog/topics/threat-intelligence/esxi-hypervisors-malware-persistence)
