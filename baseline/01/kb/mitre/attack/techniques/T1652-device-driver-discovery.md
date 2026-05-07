---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1652
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/tactic/discovery
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1652-device-driver-discovery
tactic:
    - Discovery
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries may attempt to enumerate local device drivers on a victim host. Information about device drivers may highlight various insights that shape follow-on behaviors, such as the function/purpose of the host, present security tools (i.e. [[kb/mitre/attack/techniques/T1518.001-security-software-discovery|Security Software Discovery]]) or other defenses (e.g., [[kb/mitre/attack/techniques/T1497-virtualization-sandbox-evasion|Virtualization/Sandbox Evasion]]), as well as potential exploitable vulnerabilities (e.g., [[kb/mitre/attack/techniques/T1068-exploitation-for-privilege-escalation|Exploitation for Privilege Escalation]]).<br><br>Many OS utilities may provide information about local device drivers, such as `driverquery.exe` and the `EnumDeviceDrivers()` API function on Windows.[^4] [^3]  Information about device drivers (as well as associated services, i.e., [[kb/mitre/attack/techniques/T1007-system-service-discovery|System Service Discovery]]) may also be available in the Registry.[^2] <br><br>On Linux/macOS, device drivers (in the form of kernel modules) may be visible within `/dev` or using utilities such as `lsmod` and `modinfo`.[^5] [^1] [^6] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0125](https://attack.mitre.org/software/S0125) | Remsec | Remsec has a plugin to detect active drivers of some security products.[^1]  |
| [S0376](https://attack.mitre.org/software/S0376) | HOPLIGHT | HOPLIGHT can enumerate device drivers located in the registry at `HKLM\Software\WBEM\WDM`.[^1]  |
| [S1139](https://attack.mitre.org/software/S1139) | INC Ransomware | INC Ransomware can verify the presence of specific drivers on compromised hosts including Microsoft Print to PDF and Microsoft XPS Document Writer.[^1]  |

 [^1]: [lsmod man](https://man7.org/linux/man-pages/man8/lsmod.8.html)
 [^2]: [Microsoft Registry Drivers](https://learn.microsoft.com/windows-hardware/drivers/install/overview-of-registry-trees-and-keys)
 [^3]: [Microsoft EnumDeviceDrivers](https://learn.microsoft.com/windows/win32/api/psapi/nf-psapi-enumdevicedrivers)
 [^4]: [Microsoft Driverquery](https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery)
 [^5]: [Linux Kernel Programming](https://www.tldp.org/LDP/lkmpg/2.4/lkmpg.pdf)
 [^6]: [modinfo man](https://linux.die.net/man/8/modinfo)
 [^7]: [US-CERT HOPLIGHT Apr 2019](https://www.us-cert.gov/ncas/analysis-reports/AR19-100A)
 [^8]: [Cybereason INC Ransomware November 2023](https://www.cybereason.com/hubfs/dam/collateral/reports/threat-alert-inc-ransomware.pdf)
 [^9]: [Kaspersky ProjectSauron Technical Analysis](https://securelist.com/files/2016/07/The-ProjectSauron-APT_Technical_Analysis_KL.pdf)
