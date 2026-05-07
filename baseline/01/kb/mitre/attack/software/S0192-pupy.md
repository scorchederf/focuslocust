---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0192
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0192-pupy
---

## Description

[[kb/mitre/attack/software/S0192-pupy|Pupy]] is an open source, cross-platform (Windows, Linux, OSX, Android) remote administration and post-exploitation tool. [^1]  It is written in Python and can be generated as a payload in several different ways (Windows exe, Python file, PowerShell oneliner/file, Linux elf, APK, Rubber Ducky, etc.). [^1]  [[kb/mitre/attack/software/S0192-pupy|Pupy]] is publicly available on GitHub. [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-lsass-memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can execute Lazagne as well as [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] using PowerShell.[^1]  |
| [[kb/mitre/attack/techniques/T1003.004-lsa-secrets\|T1003.004]] | LSA Secrets | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can use Lazagne for harvesting credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1003.005-cached-domain-credentials\|T1003.005]] | Cached Domain Credentials | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can use Lazagne for harvesting credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] has built in commands to identify a host’s IP address and find out other network configuration settings by viewing connected sessions.[^1]  |
| [[kb/mitre/attack/techniques/T1021.001-remote-desktop-protocol\|T1021.001]] | Remote Desktop Protocol | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can enable/disable RDP connection and can start a remote desktop session using a browser web socket client.[^1]  |
| [[kb/mitre/attack/techniques/T1033-system-owner-user-discovery\|T1033]] | System Owner/User Discovery | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can enumerate local information for Linux hosts and find currently logged on users for Windows hosts.[^1]  |
| [[kb/mitre/attack/techniques/T1041-exfiltration-over-c2-channel\|T1041]] | Exfiltration Over C2 Channel | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can send screenshots files, keylogger data, files, and recorded audio back to the C2 server.[^1]  |
| [[kb/mitre/attack/techniques/T1046-network-service-discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] has a built-in module for port scanning.[^1]  |
| [[kb/mitre/attack/techniques/T1049-system-network-connections-discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] has a built-in utility command for `netstat`, can do net session through PowerView, and has an interactive shell which can be used to discover additional information.[^1]  |
| [[kb/mitre/attack/techniques/T1055.001-dynamic-link-library-injection\|T1055.001]] | Dynamic-link Library Injection | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can migrate into another process using reflective DLL injection.[^1]  |
| [[kb/mitre/attack/techniques/T1056.001-keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] uses a keylogger to capture keystrokes it then sends back to the server after it is stopped.[^1]  |
| [[kb/mitre/attack/techniques/T1057-process-discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can list the running processes and get the process ID and parent process’s ID.[^1]  |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] has a module for loading and executing PowerShell scripts.[^1]  |
| [[kb/mitre/attack/techniques/T1059.006-python\|T1059.006]] | Python | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can use an add on feature when creating payloads that allows you to create custom Python scripts (“scriptlets”) to perform tasks offline (without requiring a session) such as sandbox detection, adding persistence, etc.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can communicate over HTTP for C2.[^1]  |
| [[kb/mitre/attack/techniques/T1082-system-information-discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can grab a system’s information including the OS version, architecture, etc.[^1]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can walk through directories and recursively search for strings in files.[^1]  |
| [[kb/mitre/attack/techniques/T1087.001-local-account\|T1087.001]] | Local Account | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] uses PowerView and Pywerview to perform discovery commands such as net user, net group, net local group, etc.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can upload and download to/from a victim machine.[^1]  |
| [[kb/mitre/attack/techniques/T1113-screen-capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can drop a mouse-logger that will take small screenshots around at each click and then send back to the server.[^1]  |
| [[kb/mitre/attack/techniques/T1114.001-local-email-collection\|T1114.001]] | Local Email Collection | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can interact with a victim’s Outlook session and look through folders and emails.[^1]  |
| [[kb/mitre/attack/techniques/T1123-audio-capture\|T1123]] | Audio Capture | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can record sound with the microphone.[^1]  |
| [[kb/mitre/attack/techniques/T1125-video-capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can access a connected webcam and capture pictures.[^1]  |
| [[kb/mitre/attack/techniques/T1134.001-token-impersonation-theft\|T1134.001]] | Token Impersonation/Theft | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can obtain a list of SIDs and provide the option for selecting process tokens to impersonate.[^1]  |
| [[kb/mitre/attack/techniques/T1135-network-share-discovery\|T1135]] | Network Share Discovery | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can list local and remote shared drives and folders over SMB.[^1]  |
| [[kb/mitre/attack/techniques/T1136.001-local-account\|T1136.001]] | Local Account | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can user PowerView to execute “net user” commands and create local system accounts.[^1]  |
| [[kb/mitre/attack/techniques/T1136.002-domain-account\|T1136.002]] | Domain Account | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can user PowerView to execute “net user” commands and create domain accounts.[^1]  |
| [[kb/mitre/attack/techniques/T1497.001-system-checks\|T1497.001]] | System Checks | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] has a module that checks a number of indicators on the system to determine if its running on a virtual machine.[^1]  |
| [[kb/mitre/attack/techniques/T1543.002-systemd-service\|T1543.002]] | Systemd Service | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can be used to establish persistence using a systemd service.[^1]  |
| [[kb/mitre/attack/techniques/T1547.001-registry-run-keys-startup-folder\|T1547.001]] | Registry Run Keys / Startup Folder | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] adds itself to the startup folder or adds itself to the Registry key `SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run` for persistence.[^1]  |
| [[kb/mitre/attack/techniques/T1547.013-xdg-autostart-entries\|T1547.013]] | XDG Autostart Entries | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can use an XDG Autostart to establish persistence.[^1]  |
| [[kb/mitre/attack/techniques/T1548.002-bypass-user-account-control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can bypass Windows UAC through either DLL hijacking, eventvwr, or appPaths.[^1]  |
| [[kb/mitre/attack/techniques/T1550.003-pass-the-ticket\|T1550.003]] | Pass the Ticket | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can also perform pass-the-ticket.[^1]  |
| [[kb/mitre/attack/techniques/T1552.001-credentials-in-files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can use Lazagne for harvesting credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1555-credentials-from-password-stores\|T1555]] | Credentials from Password Stores | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can use Lazagne for harvesting credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1555.003-credentials-from-web-browsers\|T1555.003]] | Credentials from Web Browsers | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can use Lazagne for harvesting credentials.[^1]  |
| [[kb/mitre/attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can sniff plaintext network credentials and use NBNS Spoofing to poison name services.[^1]  |
| [[kb/mitre/attack/techniques/T1560.001-archive-via-utility\|T1560.001]] | Archive via Utility | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] can compress data with Zip before sending it over C2.[^1]  |
| [[kb/mitre/attack/techniques/T1569.002-service-execution\|T1569.002]] | Service Execution | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] uses [[kb/mitre/attack/software/S0029-psexec\|PsExec]] to execute a payload or commands on a remote host.[^1]  |
| [[kb/mitre/attack/techniques/T1573.002-asymmetric-cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S0192-pupy\|Pupy]]'s default encryption for its C2 communication channel is SSL, but it also has transport options for RSA and AES.[^1]  |
| [[kb/mitre/attack/techniques/T1685.005-clear-windows-event-logs\|T1685.005]] | Clear Windows Event Logs | [[kb/mitre/attack/software/S0192-pupy\|Pupy]] has a module to clear event logs with PowerShell.[^1]  |

 [^1]: [GitHub Pupy](https://github.com/n1nj4sec/pupy)
 [^2]: [Red Canary Netwire Linux 2022](https://redcanary.com/blog/netwire-remote-access-trojan-on-linux/)
