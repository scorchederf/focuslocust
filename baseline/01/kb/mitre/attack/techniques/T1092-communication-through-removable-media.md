---
generated_by: focuslocust
source: mitre
type: technique
aliases:
    - T1092
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/command_and_control
    - attack/type/technique
    - platform/linux
    - platform/macos
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1092-communication-through-removable-media
tactic:
    - Command And Control
platforms:
    - Linux
    - macOS
    - Windows
permissions required:
    - none
---

## Description

Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system.[^1]  Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by [[kb/mitre/attack/techniques/T1091-replication-through-removable-media|Replication Through Removable Media]]. Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0023](https://attack.mitre.org/software/S0023) | CHOPSTICK | Part of APT28's operation involved using CHOPSTICK modules to copy itself to air-gapped machines, using files written to USB sticks to transfer data and command traffic.[^3] [^2] [^1]  |
| [S0136](https://attack.mitre.org/software/S0136) | USBStealer | USBStealer drops commands for a second victim onto a removable media drive inserted into the first victim, and commands are executed when the drive is inserted into the second victim.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | Disallow or restrict removable media at an organizational policy level if they are not required for business operations.[^1]  |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Disable Autoruns if it is unnecessary.[^1]  |

 [^1]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
 [^2]: [Microsoft SIR Vol 19](http://download.microsoft.com/download/4/4/C/44CDEF0E-7924-4787-A56A-16261691ACE3/Microsoft_Security_Intelligence_Report_Volume_19_English.pdf)
 [^3]: [ESET Sednit Part 2](http://www.welivesecurity.com/wp-content/uploads/2016/10/eset-sednit-part-2.pdf)
 [^4]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
 [^5]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)
 [^6]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)
