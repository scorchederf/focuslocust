---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S1087
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S1087-asyncrat
---

## Description

[[kb/mitre/attack/software/S1087-asyncrat|AsyncRAT]] is an open-source remote access tool originally available through the NYANxCAT Github repository that has been used in malicious campaigns.[^2] [^3] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can enumerate the NetBIOS name on targeted machines.[^1]  |
| [[kb/mitre/attack/techniques/T1033-system-owner-user-discovery\|T1033]] | System Owner/User Discovery | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can check if the current user of a compromised system is an administrator. [^1]  |
| [[kb/mitre/attack/techniques/T1053.005-scheduled-task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can create a scheduled task to maintain persistence on system start-up.[^1]  |
| [[kb/mitre/attack/techniques/T1056.001-keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can capture keystrokes on the victim’s machine.[^1]  |
| [[kb/mitre/attack/techniques/T1057-process-discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can examine running processes to determine if a debugger is present.[^1]  |
| [[kb/mitre/attack/techniques/T1059.003-windows-command-shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can be deployed via batch script.[^1]  |
| [[kb/mitre/attack/techniques/T1090.003-multi-hop-proxy\|T1090.003]] | Multi-hop Proxy | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can proxy C2 through a [[kb/mitre/attack/software/S0183-tor\|Tor]] client.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] has the ability to download files including over SFTP.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1106-native-api\|T1106]] | Native API | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] has the ability to use OS APIs including `CheckRemoteDebuggerPresent`.[^1]  |
| [[kb/mitre/attack/techniques/T1113-screen-capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] has the ability to view the screen on compromised hosts.[^1]  |
| [[kb/mitre/attack/techniques/T1124-system-time-discovery\|T1124]] | System Time Discovery | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can check whether the current system hour and day of the week are within operating hours defined it its configuration.[^1]  |
| [[kb/mitre/attack/techniques/T1125-video-capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can record screen content on targeted systems.[^1]  |
| [[kb/mitre/attack/techniques/T1204.002-malicious-file\|T1204.002]] | Malicious File | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] has been executed through victims opening malicious file attachments.[^1]  |
| [[kb/mitre/attack/techniques/T1497.001-system-checks\|T1497.001]] | System Checks | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can identify strings such as Virtual, vmware, or VirtualBox to detect virtualized environments.[^1]  |
| [[kb/mitre/attack/techniques/T1564.003-hidden-window\|T1564.003]] | Hidden Window | <br>[[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can hide the execution of scheduled tasks using `ProcessWindowStyle.Hidden`.[^1]  |
| [[kb/mitre/attack/techniques/T1566.001-spearphishing-attachment\|T1566.001]] | Spearphishing Attachment | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] has been delivered via malicious email attachments.[^1]  |
| [[kb/mitre/attack/techniques/T1568-dynamic-resolution\|T1568]] | Dynamic Resolution | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can be configured to use dynamic DNS.[^1]  |
| [[kb/mitre/attack/techniques/T1568.002-domain-generation-algorithms\|T1568.002]] | Domain Generation Algorithms | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] use a DGA to generate a C2 domains.[^1]  |
| [[kb/mitre/attack/techniques/T1622-debugger-evasion\|T1622]] | Debugger Evasion | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can use the `CheckRemoteDebuggerPresent` function to detect the presence of a debugger.[^1]  |
| [[kb/mitre/attack/techniques/T1680-local-storage-discovery\|T1680]] | Local Storage Discovery | [[kb/mitre/attack/software/S1087-asyncrat\|AsyncRAT]] can check the disk size through the values obtained with `DeviceInfo.`[^1]  |

 [^1]: [Telefonica Snip3 December 2021](https://telefonicatech.com/blog/snip3-investigacion-malware)
 [^2]: [Morphisec Snip3 May 2021](https://blog.morphisec.com/revealing-the-snip3-crypter-a-highly-evasive-rat-loader)
 [^3]: [Cisco Operation Layover September 2021](https://blog.talosintelligence.com/operation-layover-how-we-tracked-attack/)
 [^4]: [ESET MirrorFace 2025](https://www.welivesecurity.com/en/eset-research/operation-akairyu-mirrorface-invites-europe-expo-2025-revives-anel-backdoor/)
 [^5]: [Recorded Future TAG-144 AUG 2025](https://assets.recordedfuture.com/insikt-report-pdfs/2025/cta-2025-0826.pdf)
 [^6]: [AsyncRAT GitHub](https://github.com/NYAN-x-CAT/AsyncRAT-C-Sharp/blob/master/README.md)
