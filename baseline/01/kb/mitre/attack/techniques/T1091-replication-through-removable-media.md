---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1091
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/initial_access
    - attack/tactic/lateral_movement
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1091-replication-through-removable-media
tactic:
    - Initial Access
    - Lateral Movement
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may move onto systems, possibly those on disconnected or air-gapped networks, by copying malware to removable media and taking advantage of Autorun features when the media is inserted into a system and executes. In the case of Lateral Movement, this may occur through modification of executable files stored on removable media or by copying malware and renaming it to look like a legitimate file to trick users into executing it on a separate system. In the case of Initial Access, this may occur through manual manipulation of the media, modification of systems used to initially format the media, or modification to the media's firmware itself.<br><br>Mobile devices may also be used to infect PCs with malware if connected via USB.[^3]  This infection may be achieved using devices (Android, iOS, etc.) and, in some instances, USB charging cables.[^1] [^2]  For example, when a smartphone is connected to a system, it may appear to be mounted similar to a USB-connected disk drive. If malware that is compatible with the connected system is on the mobile device, the malware could infect the machine (especially if Autorun features are enabled).

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0013](https://attack.mitre.org/software/S0013) | PlugX | PlugX has copied itself to infected removable drives for propagation to other victim devices.[^1]  |
| [S0023](https://attack.mitre.org/software/S0023) | CHOPSTICK | Part of APT28's operation involved using CHOPSTICK modules to copy itself to air-gapped machines and using files written to USB sticks to transfer data and command traffic.[^2] [^1] [^3]  |
| [S0028](https://attack.mitre.org/software/S0028) | SHIPSHAPE | APT30 may have used the SHIPSHAPE malware to move onto air-gapped networks. SHIPSHAPE targets removable drives to spread to other systems by modifying the drive to use Autorun to execute or by hiding legitimate document files and copying an executable to the folder with the same name as the legitimate document.[^1]  |
| [S0062](https://attack.mitre.org/software/S0062) | DustySky | DustySky searches for removable media and duplicates itself onto it.[^1]  |
| [S0092](https://attack.mitre.org/software/S0092) | Agent.btz | Agent.btz drops itself onto removable media devices and creates an autorun.inf file with an instruction to run that file. When the device is inserted into another system, it opens autorun.inf and loads the malware.[^1]  |
| [S0115](https://attack.mitre.org/software/S0115) | Crimson | Crimson can spread across systems by infecting removable media.[^1]  |
| [S0130](https://attack.mitre.org/software/S0130) | Unknown Logger | Unknown Logger is capable of spreading to USB devices.[^1]  |
| [S0132](https://attack.mitre.org/software/S0132) | H1N1 | H1N1 has functionality to copy itself to removable media.[^1]  |
| [S0136](https://attack.mitre.org/software/S0136) | USBStealer | USBStealer drops itself onto removable media and relies on Autorun to execute the malicious file when a user opens the removable media on another system.[^1]  |
| [S0143](https://attack.mitre.org/software/S0143) | Flame | Flame contains modules to infect USB sticks and spread laterally to other Windows systems the stick is plugged into using Autorun functionality.[^1]  |
| [S0385](https://attack.mitre.org/software/S0385) | njRAT | njRAT can be configured to spread via removable drives.[^1] [^2]  |
| [S0386](https://attack.mitre.org/software/S0386) | Ursnif | Ursnif has copied itself to and infected removable drives for propagation.[^2] [^1]  |
| [S0452](https://attack.mitre.org/software/S0452) | USBferry | USBferry can copy its installer to attached USB storage devices.[^1]  |
| [S0458](https://attack.mitre.org/software/S0458) | Ramsay | Ramsay can spread itself by infecting other portable executable files on removable drives.[^1] 	 |
| [S0603](https://attack.mitre.org/software/S0603) | Stuxnet | Stuxnet can propagate via removable media using an autorun.inf file or the CVE-2010-2568 LNK vulnerability.[^1]  |
| [S0608](https://attack.mitre.org/software/S0608) | Conficker | Conficker variants used the Windows AUTORUN feature to spread through USB propagation.[^1] [^2]  |
| [S0650](https://attack.mitre.org/software/S0650) | QakBot | QakBot has the ability to use removable drives to spread through compromised networks.[^1]  |
| [S1074](https://attack.mitre.org/software/S1074) | ANDROMEDA | ANDROMEDA has been spread via infected USB keys.[^1]  |
| [S1130](https://attack.mitre.org/software/S1130) | Raspberry Robin | Raspberry Robin has historically used infected USB media to spread to new victims.[^1] [^2]  |
| [S1230](https://attack.mitre.org/software/S1230) | HIUPAN | HIUPAN has periodically checked for removable and hot-plugged drives connected to the infected machine, should one be found HIUPAN will propagate to the removeable drives by copying itself and accompanying malware components to a directory to the new drive in a hidden subdirectory `<Drive_Letter>:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\` and hides any other existing files to ensure UsbConfig.exe is the only visible file on the device.[^1] [^2]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1034-limit-hardware-installation\|M1034]] | Limit Hardware Installation | Limit the use of USB devices and removable media within a network. |
| [[kb/mitre/attack/mitigations/M1040-behavior-prevention-on-endpoint\|M1040]] | Behavior Prevention on Endpoint | On Windows 10, enable Attack Surface Reduction (ASR) rules to block unsigned/untrusted executable files (such as .exe, .dll, or .scr) from running from USB removable drives. [^1]  |
| [[kb/mitre/attack/mitigations/M1042-disable-or-remove-feature-or-program\|M1042]] | Disable or Remove Feature or Program | Disable Autorun if it is unnecessary. [^1]  Disallow or restrict removable media at an organizational policy level if it is not required for business operations. [^2]  |

 [^1]: [Windows Malware Infecting Android](https://www.computerworld.com/article/2486903/windows-malware-tries-to-infect-android-devices-connected-to-pcs.html)
 [^2]: [iPhone Charging Cable Hack](https://techcrunch.com/2019/08/12/iphone-charging-cable-hack-computer-def-con/)
 [^3]: [Exploiting Smartphone USB ](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.226.3427&rep=rep1&type=pdf)
 [^4]: [Kaspersky Flame](https://securelist.com/the-flame-questions-and-answers-51/34344/)
 [^5]: [FireEye APT30](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2015/05/20081935/rpt-apt30.pdf)
 [^6]: [2025_IBM_PUBLOAD_TONESHELL_HIUPAN_CLAIMLOADER_MUSTANG PANDA](https://www.ibm.com/think/x-force/hive0154-targeting-us-philippines-pakistan-taiwan)
 [^7]: [Trend Micro MUSTANG PANDA PUBLOAD HIUPAN SEPTEMBER 2024](https://www.trendmicro.com/en_us/research/24/i/earth-preta-new-malware-and-strategies.html)
 [^8]: [DOJ Affidavit Search and Seizure PlugX December 2024](https://www.justice.gov/archives/opa/media/1384136/dl)
 [^9]: [Forcepoint Monsoon](https://www.forcepoint.com/sites/default/files/resources/files/forcepoint-security-labs-monsoon-analysis-report.pdf)
 [^10]: [DustySky](https://www.clearskysec.com/wp-content/uploads/2016/01/Operation%20DustySky_TLP_WHITE.pdf)
 [^11]: [Cisco H1N1 Part 2](https://web.archive.org/web/20231210122239/https://blogs.cisco.com/security/h1n1-technical-analysis-reveals-new-capabilities-part-2)
 [^12]: [Microsoft Disable Autorun](https://support.microsoft.com/en-us/kb/967715)
 [^13]: [TechNet Removable Media Control](https://technet.microsoft.com/en-us/library/cc772540(v=ws.10).aspx)
 [^14]: [Nicolas Falliere, Liam O Murchu, Eric Chien February 2011](https://docs.broadcom.com/doc/security-response-w32-stuxnet-dossier-11-en)
 [^15]: [TrendMicro RaspberryRobin 2022](https://www.trendmicro.com/en_us/research/22/l/raspberry-robin-malware-targets-telecom-governments.html)
 [^16]: [RedCanary RaspberryRobin 2022](https://redcanary.com/blog/threat-intelligence/raspberry-robin/)
 [^17]: [win10_asr](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/attack-surface-reduction)
 [^18]: [ThreatExpert Agent.btz](http://blog.threatexpert.com/2008/11/agentbtz-threat-that-hit-pentagon.html)
 [^19]: [Fidelis njRAT June 2013](https://www.threatminer.org/_reports/2013/fta-1009---njrat-uncovered-1.pdf)
 [^20]: [Trend Micro njRAT 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/autoit-compiled-worm-affecting-removable-media-delivers-fileless-version-of-bladabindi-njrat-backdoor/)
 [^21]: [TrendMicro Tropic Trooper May 2020](https://documents.trendmicro.com/assets/Tech-Brief-Tropic-Trooper-s-Back-USBferry-Attack-Targets-Air-gapped-Environments.pdf)
 [^22]: [Microsoft SIR Vol 19](http://download.microsoft.com/download/4/4/C/44CDEF0E-7924-4787-A56A-16261691ACE3/Microsoft_Security_Intelligence_Report_Volume_19_English.pdf)
 [^23]: [FireEye APT28](https://web.archive.org/web/20151022204649/https://www.fireeye.com/content/dam/fireeye-www/global/en/current-threats/pdfs/rpt-apt28.pdf)
 [^24]: [Secureworks IRON TWILIGHT Active Measures March 2017](https://www.secureworks.com/research/iron-twilight-supports-active-measures)
 [^25]: [Kaspersky Transparent Tribe August 2020](https://securelist.com/transparent-tribe-part-1/98127/)
 [^26]: [Eset Ramsay May 2020](https://www.welivesecurity.com/2020/05/13/ramsay-cyberespionage-toolkit-airgapped-networks/)
 [^27]: [Trend Micro Qakbot May 2020](https://www.trendmicro.com/vinfo/ph/security/news/cybercrime-and-digital-threats/qakbot-resurges-spreads-through-vbs-files)
 [^28]: [Mandiant Suspected Turla Campaign February 2023](https://www.mandiant.com/resources/blog/turla-galaxy-opportunity)
 [^29]: [ESET Sednit USBStealer 2014](http://www.welivesecurity.com/2014/11/11/sednit-espionage-group-attacking-air-gapped-networks/)
 [^30]: [SANS Conficker](https://web.archive.org/web/20200125132645/https://www.sans.org/security-resources/malwarefaq/conficker-worm)
 [^31]: [Trend Micro Conficker](https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/conficker)
 [^32]: [TrendMicro Ursnif File Dec 2014](https://blog.trendmicro.com/trendlabs-security-intelligence/info-stealing-file-infector-hits-us-uk/)
 [^33]: [TrendMicro Ursnif Mar 2015](https://web.archive.org/web/20210719165945/https://www.trendmicro.com/en_us/research/15/c/ursnif-the-multifaceted-malware.html?_ga=2.165628854.808042651.1508120821-744063452.1505819992)
