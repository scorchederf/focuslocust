---
parsed_by: focuslocust
source: mitre
type: technique
aliases:
    - T1197
tags:
    - attack/domain/enterprise_attack
    - attack/has_procedures
    - attack/mitigated
    - attack/tactic/execution
    - attack/tactic/persistence
    - attack/tactic/stealth
    - attack/type/technique
    - platform/windows
mitre-attack: kb/mitre/attack/techniques/T1197-bits-jobs
tactic:
    - Execution
    - Persistence
    - Stealth
platforms:
    - Windows
permissions required:
    - none
---

## Description

Adversaries may abuse BITS jobs to persistently execute code and perform various background tasks. Windows Background Intelligent Transfer Service (BITS) is a low-bandwidth, asynchronous file transfer mechanism exposed through [[kb/mitre/attack/techniques/T1559.001-component-object-model|Component Object Model]] (COM).[^6] [^4]  BITS is commonly used by updaters, messengers, and other applications preferred to operate in the background (using available idle bandwidth) without interrupting other networked applications. File transfer tasks are implemented as BITS jobs, which contain a queue of one or more file operations.<br><br>The interface to create and manage BITS jobs is accessible through [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]] and the [[kb/mitre/attack/software/S0190-bitsadmin|BITSAdmin]] tool.[^4] [^5] <br><br>Adversaries may abuse BITS to download (e.g. [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer|Ingress Tool Transfer]]), execute, and even clean up after running malicious code (e.g. [[kb/mitre/attack/techniques/T1070-indicator-removal|Indicator Removal]]). BITS tasks are self-contained in the BITS job database, without new files or registry modifications, and often permitted by host firewalls.[^1] [^7] [^2]  BITS enabled execution may also enable persistence by creating long-standing jobs (the default maximum lifetime is 90 days and extendable) or invoking an arbitrary program when a job completes or errors (including after system reboots).[^3] [^1] <br><br>BITS upload functionalities can also be used to perform [[kb/mitre/attack/techniques/T1048-exfiltration-over-alternative-protocol|Exfiltration Over Alternative Protocol]].[^1] 

## Procedure Examples
| ID | Name | Use |
| --- | --- | --- |
| [S0154](https://attack.mitre.org/software/S0154) | Cobalt Strike | Cobalt Strike can download a hosted "beacon" payload using [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]].[^3] [^1] [^2]  |
| [[kb/mitre/attack/software/S0190-bitsadmin\|S0190]] | BITSAdmin | [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]] can be used to create [[kb/mitre/attack/techniques/T1197-bits-jobs\|BITS Jobs]] to launch a malicious process.[^1]  |
| [S0201](https://attack.mitre.org/software/S0201) | JPIN | A JPIN variant downloads the backdoor payload via the BITS service.[^1]  |
| [S0333](https://attack.mitre.org/software/S0333) | UBoatRAT | UBoatRAT takes advantage of the /SetNotifyCmdLine option in [[kb/mitre/attack/software/S0190-bitsadmin\|BITSAdmin]] to ensure it stays running on a system to maintain persistence.[^1]  |
| [S0534](https://attack.mitre.org/software/S0534) | Bazar | Bazar has been downloaded via Windows BITS functionality.[^1]  |
| [S0554](https://attack.mitre.org/software/S0554) | Egregor | Egregor has used BITSadmin to download and execute malicious DLLs.[^1]  |
| [S0652](https://attack.mitre.org/software/S0652) | MarkiRAT | MarkiRAT can use BITS Utility to connect with the C2 server.[^1]  |
| [S0654](https://attack.mitre.org/software/S0654) | ProLock | ProLock can use BITS jobs to download its malicious payload.[^1]  |

## Mitigations
| ID | Name | Description |
| --- | --- | --- |
| [[kb/mitre/attack/mitigations/M1018-user-account-management\|M1018]] | User Account Management | <br>Consider limiting access to the BITS interface to specific users or groups.[^1]  |
| [[kb/mitre/attack/mitigations/M1028-operating-system-configuration\|M1028]] | Operating System Configuration | <br>Consider reducing the default BITS job lifetime in Group Policy or by editing the `JobInactivityTimeout` and `MaxDownloadTime` Registry values in ` HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\BITS`.[^1]  |
| [[kb/mitre/attack/mitigations/M1037-filter-network-traffic\|M1037]] | Filter Network Traffic | Modify network and/or host firewall rules, as well as other network controls, to only allow legitimate BITS traffic. |

 [^1]: [CTU BITS Malware June 2016](https://www.secureworks.com/blog/malware-lingers-with-bits)
 [^2]: [Symantec BITS May 2007](https://www.symantec.com/connect/blogs/malware-update-windows-update)
 [^3]: [PaloAlto UBoatRAT Nov 2017](https://researchcenter.paloaltonetworks.com/2017/11/unit42-uboatrat-navigates-east-asia/)
 [^4]: [Microsoft BITS](https://msdn.microsoft.com/library/windows/desktop/bb968799.aspx)
 [^5]: [Microsoft BITSAdmin](https://msdn.microsoft.com/library/aa362813.aspx)
 [^6]: [Microsoft COM](https://msdn.microsoft.com/library/windows/desktop/ms680573.aspx)
 [^7]: [Mondok Windows PiggyBack BITS May 2007](https://arstechnica.com/information-technology/2007/05/malware-piggybacks-on-windows-background-intelligent-transfer-service/)
 [^8]: [Kaspersky Ferocious Kitten Jun 2021](https://securelist.com/ferocious-kitten-6-years-of-covert-surveillance-in-iran/102806/)
 [^9]: [NCC Group Team9 June 2020](https://research.nccgroup.com/2020/06/02/in-depth-analysis-of-the-new-team9-malware-family/)
 [^10]: [Talos Cobalt Strike September 2020](https://web.archive.org/web/20210219195905/https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/095/031/original/Talos_Cobalt_Strike.pdf)
 [^11]: [Cobalt Strike Manual 4.3 November 2020](https://web.archive.org/web/20210708035426/https://www.cobaltstrike.com/downloads/csmanual43.pdf)
 [^12]: [CobaltStrike Scripted Web Delivery](https://www.cobaltstrike.com/help-scripted-web-delivery)
 [^13]: [Intrinsec Egregor Nov 2020](https://www.intrinsec.com/egregor-prolock/?cn-reloaded=1)
 [^14]: [Microsoft PLATINUM April 2016](https://download.microsoft.com/download/2/2/5/225BFE3E-E1DE-4F5B-A77B-71200928D209/Platinum%20feature%20article%20-%20Targeted%20attacks%20in%20South%20and%20Southeast%20Asia%20April%202016.pdf)
 [^15]: [Group IB Ransomware September 2020](https://web.archive.org/web/20220119114433/https://groupib.pathfactory.com/ransomware-reports/prolock_wp)
 [^16]: [TrendMicro Tropic Trooper Mar 2018](https://blog.trendmicro.com/trendlabs-security-intelligence/tropic-trooper-new-strategy/)
