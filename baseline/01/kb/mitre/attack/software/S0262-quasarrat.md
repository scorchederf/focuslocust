---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0262
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0262-quasarrat
---

## Description

[[kb/mitre/attack/software/S0262-quasarrat|QuasarRAT]] is an open-source, remote access tool that has been publicly available on GitHub since at least 2014. [[kb/mitre/attack/software/S0262-quasarrat|QuasarRAT]] is developed in the C# language.[^3] [^4] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1005-data-from-local-system\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can retrieve files from compromised client machines.[^1]  |
| [[kb/mitre/attack/techniques/T1010-application-window-discovery\|T1010]] | Application Window Discovery | APT-C-36 used a customized version of [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] to monitor browser windows for strings relating to specific Colombian financial institutions.[^1] <br> |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] has the ability to enumerate the Wide Area Network (WAN) IP through requests to ip-api[.]com, freegeoip[.]net, or api[.]ipify[.]org observed with user-agent string `Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0`.[^1]  |
| [[kb/mitre/attack/techniques/T1021.001-remote-desktop-protocol\|T1021.001]] | Remote Desktop Protocol | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] has a module for performing remote desktop access.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1033-system-owner-user-discovery\|T1033]] | System Owner/User Discovery | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can enumerate the username and account type.[^1]  |
| [[kb/mitre/attack/techniques/T1053.005-scheduled-task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] contains a .NET wrapper DLL for creating and managing scheduled tasks for maintaining persistence upon reboot.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1056.001-keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] has a built-in keylogger.[^2] [^3] [^1]  |
| [[kb/mitre/attack/techniques/T1059.003-windows-command-shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can launch a remote shell to execute commands on the victim’s machine.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1082-system-information-discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can gather system information from the victim’s machine including the OS type.[^1]  |
| [[kb/mitre/attack/techniques/T1090-proxy\|T1090]] | Proxy | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can communicate over a reverse proxy using SOCKS5.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1095-non-application-layer-protocol\|T1095]] | Non-Application Layer Protocol | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can use TCP for C2 communication.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can download files to the victim’s machine and execute them.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1112-modify-registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] has a command to edit the Registry on the victim’s machine.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1125-video-capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can perform webcam viewing.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1547.001-registry-run-keys-startup-folder\|T1547.001]] | Registry Run Keys / Startup Folder | If the [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] client process does not have administrator privileges it will add a registry key to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^2] [^1]   |
| [[kb/mitre/attack/techniques/T1548.002-bypass-user-account-control\|T1548.002]] | Bypass User Account Control | <br>[[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can generate a UAC pop-up Window to prompt the target user to run a command as the administrator.[^1]  |
| [[kb/mitre/attack/techniques/T1552.001-credentials-in-files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can obtain passwords from FTP clients.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1553.002-code-signing\|T1553.002]] | Code Signing | A [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] .dll file is digitally signed by a certificate from AirVPN.[^1]  |
| [[kb/mitre/attack/techniques/T1555-credentials-from-password-stores\|T1555]] | Credentials from Password Stores | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can obtain passwords from common FTP clients.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1555.003-credentials-from-web-browsers\|T1555.003]] | Credentials from Web Browsers | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can obtain passwords from common web browsers.[^2] [^3] [^1] <br> |
| [[kb/mitre/attack/techniques/T1564.001-hidden-files-and-directories\|T1564.001]] | Hidden Files and Directories | <br>[[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] has the ability to set file attributes to "hidden" to hide files from the compromised user's view in Windows File Explorer.[^1]  |
| [[kb/mitre/attack/techniques/T1564.003-hidden-window\|T1564.003]] | Hidden Window | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can hide process windows and make web requests invisible to the compromised user. Requests marked as invisible have been sent with user-agent string `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A` though [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can only be run on Windows systems.[^1]  |
| [[kb/mitre/attack/techniques/T1571-non-standard-port\|T1571]] | Non-Standard Port | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can use port 4782 on the compromised host for TCP callbacks.[^1]  |
| [[kb/mitre/attack/techniques/T1573.001-symmetric-cryptography\|T1573.001]] | Symmetric Cryptography | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] uses AES with a hardcoded pre-shared key to encrypt network communication.[^2] [^3] [^1]  |
| [[kb/mitre/attack/techniques/T1614-system-location-discovery\|T1614]] | System Location Discovery | [[kb/mitre/attack/software/S0262-quasarrat\|QuasarRAT]] can determine the country a victim host is located in.[^1]  |

 [^1]: [Securelist APT10 March 2021](https://securelist.com/apt10-sophisticated-multi-layered-loader-ecipekac-discovered-in-a41apt-campaign/101519/)
 [^2]: [TrendMicro Patchwork Dec 2017](https://documents.trendmicro.com/assets/tech-brief-untangling-the-patchwork-cyberespionage-group.pdf)
 [^3]: [GitHub QuasarRAT](https://github.com/quasar/QuasarRAT)
 [^4]: [Volexity Patchwork June 2018](https://www.volexity.com/blog/2018/06/07/patchwork-apt-group-targets-us-think-tanks/)
 [^5]: [Kaspersky BlindEagle AUG 2024](https://securelist.com/blindeagle-apt/113414/)
 [^6]: [CISA AR18-352A Quasar RAT December 2018](https://www.cisa.gov/uscert/ncas/analysis-reports/AR18-352A)
