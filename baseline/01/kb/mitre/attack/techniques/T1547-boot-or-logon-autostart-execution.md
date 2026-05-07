---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1547
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/has_subtechniques
    - attack/tactic/persistence
    - attack/tactic/privilege_escalation
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/network_devices
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1547-boot-or-logon-autostart-execution
tactic:
    - Persistence
    - Privilege Escalation
platforms:
    - Linux
    - macOS
    - Windows
    - Network Devices
permissions required:
    - none
---

## Description

Adversaries may configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically running a program on system boot or account logon.[^3] [^2] [^4] [^1] [^5]  These mechanisms may include automatically executing programs that are placed in specially designated directories or are referenced by repositories that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying or extending features of the kernel.<br><br>Since some boot or logon autostart programs run with higher privileges, an adversary may leverage these to elevate privileges.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0083](https://attack.mitre.org/software/S0083) | Misdat | Misdat has created registry keys for persistence, including `HKCU\Software\dnimtsoleht\StubPath`, `HKCU\Software\snimtsOleht\StubPath`, `HKCU\Software\Backtsaleht\StubPath`, `HKLM\SOFTWARE\Microsoft\Active Setup\Installed. Components\{3bf41072-b2b1-21c8-b5c1-bd56d32fbda7}`, and `HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\{3ef41072-a2f1-21c8-c5c1-70c2c3bc7905}`.[^1]   |
| [S0084](https://attack.mitre.org/software/S0084) | Mis-Type | Mis-Type has created registry keys for persistence, including `HKCU\Software\bkfouerioyou`, `HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\{6afa8072-b2b1-31a8-b5c1-{Unique Identifier}`, and `HKLM\SOFTWARE\Microsoft\Active Setup\Installed Components\{3BF41072-B2B1-31A8-B5C1-{Unique Identifier}`.[^1]  |
| [S0567](https://attack.mitre.org/software/S0567) | Dtrack | Dtrack’s RAT makes a persistent target file with auto execution on the host start.[^1]  |
| [S0651](https://attack.mitre.org/software/S0651) | BoxCaon | BoxCaon established persistence by setting the `HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows\load` registry key to point to its executable.[^1]  |
| [S0653](https://attack.mitre.org/software/S0653) | xCaon | xCaon has added persistence via the Registry key `HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\Windows\load` which causes the malware to run each time any user logs in.[^1]  |

## Sub-techniques
| ID | Name |
| --- | --- |
| [[kb/mitre/attack/techniques/T1547.014-active-setup\|T1547.014]] | Active Setup |
| [[kb/mitre/attack/techniques/T1547.012-print-processors\|T1547.012]] | Print Processors |
| [[kb/mitre/attack/techniques/T1547.010-port-monitors\|T1547.010]] | Port Monitors |
| [[kb/mitre/attack/techniques/T1547.009-shortcut-modification\|T1547.009]] | Shortcut Modification |
| [[kb/mitre/attack/techniques/T1547.005-security-support-provider\|T1547.005]] | Security Support Provider |
| [[kb/mitre/attack/techniques/T1547.003-time-providers\|T1547.003]] | Time Providers |
| [[kb/mitre/attack/techniques/T1547.004-winlogon-helper-dll\|T1547.004]] | Winlogon Helper DLL |
| [[kb/mitre/attack/techniques/T1547.015-login-items\|T1547.015]] | Login Items |
| [[kb/mitre/attack/techniques/T1547.001-registry-run-keys-startup-folder\|T1547.001]] | Registry Run Keys ／ Startup Folder |
| [[kb/mitre/attack/techniques/T1547.006-kernel-modules-and-extensions\|T1547.006]] | Kernel Modules and Extensions |
| [[kb/mitre/attack/techniques/T1547.002-authentication-package\|T1547.002]] | Authentication Package |
| [[kb/mitre/attack/techniques/T1547.013-xdg-autostart-entries\|T1547.013]] | XDG Autostart Entries |
| [[kb/mitre/attack/techniques/T1547.007-re-opened-applications\|T1547.007]] | Re-opened Applications |
| [[kb/mitre/attack/techniques/T1547.008-lsass-driver\|T1547.008]] | LSASS Driver |

 [^1]: [Cylance Reg Persistence Sept 2013](https://web.archive.org/web/20160214140250/http://blog.cylance.com/windows-registry-persistence-part-2-the-run-keys-and-search-order)
 [^2]: [MSDN Authentication Packages](https://msdn.microsoft.com/library/windows/desktop/aa374733.aspx)
 [^3]: [Microsoft Run Key](https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys)
 [^4]: [Microsoft TimeProvider](https://msdn.microsoft.com/library/windows/desktop/ms725475.aspx)
 [^5]: [Linux Kernel Programming](https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf)
 [^6]: [TechNet Autoruns](https://technet.microsoft.com/en-us/sysinternals/bb963902)
 [^7]: [Checkpoint IndigoZebra July 2021](https://research.checkpoint.com/2021/indigozebra-apt-continues-to-attack-central-asia-with-evolving-tools/)
 [^8]: [Securelist Dtrack](https://securelist.com/my-name-is-dtrack/93338/)
 [^9]: [Cylance Dust Storm](https://s7d2.scene7.com/is/content/cylance/prod/cylance-web/en-us/resources/knowledge-center/resource-library/reports/Op_Dust_Storm_Report.pdf)
