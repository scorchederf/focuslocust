---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0332
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0332-remcos
---

## Description

[[kb/mitre/attack/software/S0332-remcos|Remcos]] is a closed-source tool that is marketed as a remote control and surveillance software by a company called Breaking Security. [[kb/mitre/attack/software/S0332-remcos|Remcos]] has been observed being used in malware campaigns.[^3] [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1010-application-window-discovery\|T1010]] | Application Window Discovery | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can list all windows on victim systems.[^1]  |
| [[kb/mitre/attack/techniques/T1012-query-registry\|T1012]] | Query Registry | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can obtain Registry data from targeted systems.[^1]  |
| [[kb/mitre/attack/techniques/T1027-obfuscated-files-or-information\|T1027]] | Obfuscated Files or Information | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] uses RC4 and base64 to obfuscate data, including Registry entries and file paths.[^1]  [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can also employ control flow flattening to hinder analysis.[^2]  |
| [[kb/mitre/attack/techniques/T1027.013-encrypted-encoded-file\|T1027.013]] | Encrypted/Encoded File | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can use string encryption to hinder analysis.[^1]  |
| [[kb/mitre/attack/techniques/T1033-system-owner-user-discovery\|T1033]] | System Owner/User Discovery | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can enumerate the username on targeted hosts.[^1]  |
| [[kb/mitre/attack/techniques/T1055-process-injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] has a command to hide itself by injecting into another process.[^1]  |
| [[kb/mitre/attack/techniques/T1056.001-keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] has a command for keylogging.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1057-process-discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can discover running processes on compromised machines.[^1] <br> |
| [[kb/mitre/attack/techniques/T1059.003-windows-command-shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can launch a remote command line to execute commands on the victim’s machine.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1059.005-visual-basic\|T1059.005]] | Visual Basic | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can execute VBS remotely.[^1]  |
| [[kb/mitre/attack/techniques/T1059.006-python\|T1059.006]] | Python | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] uses Python scripts.[^1]  |
| [[kb/mitre/attack/techniques/T1059.007-javascript\|T1059.007]] | JavaScript | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] has the ability to execute JavaScript remotely.[^1]  |
| [[kb/mitre/attack/techniques/T1070-indicator-removal\|T1070]] | Indicator Removal | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can clean saved cookies and logins from the web browser.[^1]  |
| [[kb/mitre/attack/techniques/T1070.004-file-deletion\|T1070.004]] | File Deletion | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can delete files and folders from victim machines.[^1]  |
| [[kb/mitre/attack/techniques/T1082-system-information-discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can collect the OS version and process architecture of compromised hosts.[^1]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can search for files on the infected machine.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1090-proxy\|T1090]] | Proxy | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] uses the infected hosts as SOCKS5 proxies to allow for tunneling and proxying.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can upload and download files to and from the victim’s machine.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1112-modify-registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] has full control of the Registry, including the ability to modify it.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1113-screen-capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] takes automated screenshots of the infected machine.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1115-clipboard-data\|T1115]] | Clipboard Data | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] steals and modifies data from the clipboard.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1123-audio-capture\|T1123]] | Audio Capture | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can capture data from the system’s microphone.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1125-video-capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can access a system’s webcam and take pictures.[^1]  |
| [[kb/mitre/attack/techniques/T1132.001-standard-encoding\|T1132.001]] | Standard Encoding | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can serialize collected data with Protobuf.[^1]  |
| [[kb/mitre/attack/techniques/T1204.002-malicious-file\|T1204.002]] | Malicious File | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] has been executed by luring victims into opening malicious email attachments including Excel files.[^1] <br> |
| [[kb/mitre/attack/techniques/T1491.001-internal-defacement\|T1491.001]] | Internal Defacement | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] has the ability to modify the desktop wallpaper.[^1]  |
| [[kb/mitre/attack/techniques/T1497.001-system-checks\|T1497.001]] | System Checks | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] searches for Sandboxie and VMware on the system.[^1]  |
| [[kb/mitre/attack/techniques/T1529-system-shutdown-reboot\|T1529]] | System Shutdown/Reboot | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can shutdown and restart remote devices.[^1]  |
| [[kb/mitre/attack/techniques/T1543.003-windows-service\|T1543.003]] | Windows Service | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can terminate, suspend, and resume a process by PID.[^1]  |
| [[kb/mitre/attack/techniques/T1547.001-registry-run-keys-startup-folder\|T1547.001]] | Registry Run Keys / Startup Folder | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can add itself to the Registry key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^1]  |
| [[kb/mitre/attack/techniques/T1548.002-bypass-user-account-control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] has a command for UAC bypassing.[^1]  |
| [[kb/mitre/attack/techniques/T1560.001-archive-via-utility\|T1560.001]] | Archive via Utility | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can zip files and folders for upload.[^1]  |
| [[kb/mitre/attack/techniques/T1564-hide-artifacts\|T1564]] | Hide Artifacts | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can modify file attributes to hide the file.[^1]  |
| [[kb/mitre/attack/techniques/T1564.003-hidden-window\|T1564.003]] | Hidden Window | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can set `ProcessWindowStyle.Hidden` to hide windows.[^1] <br> |
| [[kb/mitre/attack/techniques/T1566.001-spearphishing-attachment\|T1566.001]] | Spearphishing Attachment | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] has been spread through emails containing malicious documents.[^1]  |
| [[kb/mitre/attack/techniques/T1568-dynamic-resolution\|T1568]] | Dynamic Resolution | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] has used dynamic DNS domains in C2 communications.[^1]  |
| [[kb/mitre/attack/techniques/T1573.002-asymmetric-cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can use TLS to encrypt C2 communication.[^1]  |
| [[kb/mitre/attack/techniques/T1614-system-location-discovery\|T1614]] | System Location Discovery | [[kb/mitre/attack/software/S0332-remcos\|Remcos]] can identify the location of targeted devices.[^1]  |

 [^1]: [Fortinet Remcos Feb 2017](https://www.fortinet.com/blog/threat-research/remcos-a-new-rat-in-the-wild-2.html)
 [^2]: [Talos Remcos Aug 2018](https://blog.talosintelligence.com/2018/08/picking-apart-remcos.html)
 [^3]: [Riskiq Remcos Jan 2018](https://web.archive.org/web/20180124082756/https://www.riskiq.com/blog/labs/spear-phishing-turkish-defense-contractors/)
 [^4]: [Fortinet Remcos Campaign NOV 2024](https://www.fortinet.com/blog/threat-research/new-campaign-uses-remcos-rat-to-exploit-victims)
 [^5]: [Check Point Blind Eagle MAR 2025](https://research.checkpoint.com/2025/blind-eagle-and-justice-for-all/)
