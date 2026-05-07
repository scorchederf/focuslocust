---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0250
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0250-koadic
---

## Description

[[kb/mitre/attack/software/S0250-koadic|Koadic]] is a Windows post-exploitation framework and penetration testing tool that is publicly available on GitHub. [[kb/mitre/attack/software/S0250-koadic|Koadic]] has several options for staging payloads and creating implants, and performs most of its operations using Windows Script Host.[^3] [^2] [^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.002-security-account-manager\|T1003.002]] | Security Account Manager | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can gather hashed passwords by dumping SAM/SECURITY hive.[^1]  |
| [[kb/mitre/attack/techniques/T1003.003-ntds\|T1003.003]] | NTDS | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can gather hashed passwords by gathering domain controller hashes from NTDS.[^1]  |
| [[kb/mitre/attack/techniques/T1005-data-from-local-system\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can download files off the target system to send back to the server.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can retrieve the contents of the IP routing table as well as information about the Windows domain.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1021.001-remote-desktop-protocol\|T1021.001]] | Remote Desktop Protocol | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can enable remote desktop on the victim's machine.[^1]  |
| [[kb/mitre/attack/techniques/T1033-system-owner-user-discovery\|T1033]] | System Owner/User Discovery | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can identify logged in users across the domain and views user sessions.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1046-network-service-discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can scan for open TCP ports on the target network.[^1]  |
| [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can use WMI to execute commands.[^1]  |
| [[kb/mitre/attack/techniques/T1053.005-scheduled-task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] has used scheduled tasks to add persistence.[^1]   |
| [[kb/mitre/attack/techniques/T1055.001-dynamic-link-library-injection\|T1055.001]] | Dynamic-link Library Injection | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can perform process injection by using a reflective DLL.[^1]  |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] has used PowerShell to establish persistence.[^1]   |
| [[kb/mitre/attack/techniques/T1059.003-windows-command-shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can open an interactive command-shell to perform command line functions on victim machines. [[kb/mitre/attack/software/S0250-koadic\|Koadic]] performs most of its operations using Windows Script Host (Jscript) and to run arbitrary shellcode.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1059.005-visual-basic\|T1059.005]] | Visual Basic | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] performs most of its operations using Windows Script Host (VBScript) and runs arbitrary shellcode .[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] has used HTTP for C2 communications.[^1]  |
| [[kb/mitre/attack/techniques/T1082-system-information-discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can obtain the OS version and build, computer name, and processor architecture from a compromised host.[^1]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can obtain a list of directories.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can download additional files and tools.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1115-clipboard-data\|T1115]] | Clipboard Data | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can retrieve the current content of the user clipboard.[^1]  |
| [[kb/mitre/attack/techniques/T1135-network-share-discovery\|T1135]] | Network Share Discovery | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can scan local network for open SMB.[^1]  |
| [[kb/mitre/attack/techniques/T1218.005-mshta\|T1218.005]] | Mshta | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can use mshta to serve additional payloads and to help schedule tasks for persistence.[^2] [^1]   |
| [[kb/mitre/attack/techniques/T1218.010-regsvr32\|T1218.010]] | Regsvr32 | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can use Regsvr32 to execute additional payloads.[^1]  |
| [[kb/mitre/attack/techniques/T1218.011-rundll32\|T1218.011]] | Rundll32 | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can use Rundll32 to execute additional payloads.[^1]  |
| [[kb/mitre/attack/techniques/T1547.001-registry-run-keys-startup-folder\|T1547.001]] | Registry Run Keys / Startup Folder | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] has added persistence to the `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` Registry key.[^1]  |
| [[kb/mitre/attack/techniques/T1548.002-bypass-user-account-control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] has 2 methods for elevating integrity. It can bypass UAC through `eventvwr.exe` and `sdclt.exe`.[^1]  |
| [[kb/mitre/attack/techniques/T1564.003-hidden-window\|T1564.003]] | Hidden Window | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] has used the command `Powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden` to hide its window.[^1]  |
| [[kb/mitre/attack/techniques/T1569.002-service-execution\|T1569.002]] | Service Execution | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can run a command on another machine using [[kb/mitre/attack/software/S0029-psexec\|PsExec]].[^1]  |
| [[kb/mitre/attack/techniques/T1573.002-asymmetric-cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S0250-koadic\|Koadic]] can use SSL and TLS for communications.[^1]  |

 [^1]: [MalwareBytes LazyScripter Feb 2021](https://web.archive.org/web/20211003035156/https://www.malwarebytes.com/resources/files/2021/02/lazyscripter.pdf)
 [^2]: [Palo Alto Sofacy 06-2018](https://researchcenter.paloaltonetworks.com/2018/06/unit42-sofacy-groups-parallel-attacks/)
 [^3]: [Github Koadic](https://github.com/offsecginger/koadic)
