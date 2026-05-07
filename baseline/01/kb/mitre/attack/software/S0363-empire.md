---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0363
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0363-empire
---

## Description

[[kb/mitre/attack/software/S0363-empire|Empire]] is an open-source, cross-platform remote administration and post-exploitation framework that is publicly available on GitHub. While the tool itself is primarily written in Python, the post-exploitation agents are written in pure [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]] for Windows and Python for Linux/macOS. [[kb/mitre/attack/software/S0363-empire|Empire]] was one of five tools singled out by a joint report on public hacking tools being widely used by adversaries.[^3] [^1] [^2] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-lsass-memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0363-empire\|Empire]] contains an implementation of [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] to gather credentials from memory.[^1]  |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] can acquire network configuration information like DNS servers, public IP, and network proxies used by a host.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1020-automated-exfiltration\|T1020]] | Automated Exfiltration | [[kb/mitre/attack/software/S0363-empire\|Empire]] has the ability to automatically send collected data back to the threat actors' C2.[^1]  |
| [[kb/mitre/attack/techniques/T1021.003-distributed-component-object-model\|T1021.003]] | Distributed Component Object Model | [[kb/mitre/attack/software/S0363-empire\|Empire]] can utilize `Invoke-DCOM` to leverage remote COM execution for lateral movement.[^1]  |
| [[kb/mitre/attack/techniques/T1021.004-ssh\|T1021.004]] | SSH | [[kb/mitre/attack/software/S0363-empire\|Empire]] contains modules for executing commands over SSH as well as in-memory VNC agent injection.[^1]  |
| [[kb/mitre/attack/techniques/T1027.010-command-obfuscation\|T1027.010]] | Command Obfuscation | [[kb/mitre/attack/software/S0363-empire\|Empire]] has the ability to obfuscate commands using `Invoke-Obfuscation`.[^1]  |
| [[kb/mitre/attack/techniques/T1033-system-owner-user-discovery\|T1033]] | System Owner/User Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] can enumerate the username on targeted hosts.[^1]  |
| [[kb/mitre/attack/techniques/T1040-network-sniffing\|T1040]] | Network Sniffing | [[kb/mitre/attack/software/S0363-empire\|Empire]] can be used to conduct packet captures on target hosts.[^1]  |
| [[kb/mitre/attack/techniques/T1041-exfiltration-over-c2-channel\|T1041]] | Exfiltration Over C2 Channel | [[kb/mitre/attack/software/S0363-empire\|Empire]] can send data gathered from a target through the command and control channel.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1046-network-service-discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] can perform port scans from an infected host.[^1]  |
| [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use WMI to deliver a payload to a remote host.[^1]   |
| [[kb/mitre/attack/techniques/T1049-system-network-connections-discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] can enumerate the current network connections of a host.[^1]  |
| [[kb/mitre/attack/techniques/T1053.005-scheduled-task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S0363-empire\|Empire]] has modules to interact with the Windows task scheduler.[^1]  |
| [[kb/mitre/attack/techniques/T1055-process-injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0363-empire\|Empire]] contains multiple modules for injecting into processes, such as `Invoke-PSInject`.[^1]  |
| [[kb/mitre/attack/techniques/T1056.001-keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0363-empire\|Empire]] includes keylogging capabilities for Windows, Linux, and macOS systems.[^1]  |
| [[kb/mitre/attack/techniques/T1056.004-credential-api-hooking\|T1056.004]] | Credential API Hooking | [[kb/mitre/attack/software/S0363-empire\|Empire]] contains some modules that leverage API hooking to carry out tasks, such as netripper.[^1]  |
| [[kb/mitre/attack/techniques/T1057-process-discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] can find information about processes running on local and remote systems.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1059-command-and-scripting-interpreter\|T1059]] | Command and Scripting Interpreter | [[kb/mitre/attack/software/S0363-empire\|Empire]] uses a command-line interface to interact with systems.[^1]  |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0363-empire\|Empire]] leverages PowerShell for the majority of its client-side agent tasks. [[kb/mitre/attack/software/S0363-empire\|Empire]] also contains the ability to conduct PowerShell remoting with the `Invoke-PSRemoting` module.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1059.003-windows-command-shell\|T1059.003]] | Windows Command Shell | [[kb/mitre/attack/software/S0363-empire\|Empire]] has modules for executing scripts.[^1]  |
| [[kb/mitre/attack/techniques/T1068-exploitation-for-privilege-escalation\|T1068]] | Exploitation for Privilege Escalation | [[kb/mitre/attack/software/S0363-empire\|Empire]] can exploit vulnerabilities such as MS16-032 and MS16-135.[^1]  |
| [[kb/mitre/attack/techniques/T1070.006-timestomp\|T1070.006]] | Timestomp | [[kb/mitre/attack/software/S0363-empire\|Empire]] can timestomp any files or payloads placed on a target machine to help them blend in.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0363-empire\|Empire]] can conduct command and control over protocols like HTTP and HTTPS.[^1]  |
| [[kb/mitre/attack/techniques/T1082-system-information-discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] can enumerate host system information like OS, architecture, domain name, applied patches, and more.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] includes various modules for finding files of interest on hosts and network shares.[^1]  |
| [[kb/mitre/attack/techniques/T1087.001-local-account\|T1087.001]] | Local Account | [[kb/mitre/attack/software/S0363-empire\|Empire]] can acquire local and domain user account information.[^1]  |
| [[kb/mitre/attack/techniques/T1087.002-domain-account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0363-empire\|Empire]] can acquire local and domain user account information.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1102.002-bidirectional-communication\|T1102.002]] | Bidirectional Communication | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use Dropbox and GitHub for C2.[^1]  |
| [[kb/mitre/attack/techniques/T1105-ingress-tool-transfer\|T1105]] | Ingress Tool Transfer | [[kb/mitre/attack/software/S0363-empire\|Empire]] can upload and download to and from a victim machine.[^1]  |
| [[kb/mitre/attack/techniques/T1106-native-api\|T1106]] | Native API | [[kb/mitre/attack/software/S0363-empire\|Empire]] contains a variety of enumeration modules that have an option to use API calls to carry out tasks.[^1]  |
| [[kb/mitre/attack/techniques/T1113-screen-capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0363-empire\|Empire]] is capable of capturing screenshots on Windows and macOS systems.[^1]  |
| [[kb/mitre/attack/techniques/T1114.001-local-email-collection\|T1114.001]] | Local Email Collection | [[kb/mitre/attack/software/S0363-empire\|Empire]] has the ability to collect emails on a target system.[^1]  |
| [[kb/mitre/attack/techniques/T1115-clipboard-data\|T1115]] | Clipboard Data | [[kb/mitre/attack/software/S0363-empire\|Empire]] can harvest clipboard data on both Windows and macOS systems.[^1]  |
| [[kb/mitre/attack/techniques/T1119-automated-collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S0363-empire\|Empire]] can automatically gather the username, domain name, machine name, and other information from a compromised system.[^1]  |
| [[kb/mitre/attack/techniques/T1125-video-capture\|T1125]] | Video Capture | [[kb/mitre/attack/software/S0363-empire\|Empire]] can capture webcam data on Windows and macOS systems.[^1]  |
| [[kb/mitre/attack/techniques/T1127.001-msbuild\|T1127.001]] | MSBuild | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use built-in modules to abuse trusted utilities like MSBuild.exe.[^1] <br> |
| [[kb/mitre/attack/techniques/T1134-access-token-manipulation\|T1134]] | Access Token Manipulation | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Invoke-TokenManipulation` to manipulate access tokens.[^1]  |
| [[kb/mitre/attack/techniques/T1134.002-create-process-with-token\|T1134.002]] | Create Process with Token | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use `Invoke-RunAs` to make tokens.[^1]  |
| [[kb/mitre/attack/techniques/T1134.005-sid-history-injection\|T1134.005]] | SID-History Injection | [[kb/mitre/attack/software/S0363-empire\|Empire]] can add a SID-History to a user if on a domain controller.[^1]  |
| [[kb/mitre/attack/techniques/T1135-network-share-discovery\|T1135]] | Network Share Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] can find shared drives on the local system.[^1]  |
| [[kb/mitre/attack/techniques/T1136.001-local-account\|T1136.001]] | Local Account | [[kb/mitre/attack/software/S0363-empire\|Empire]] has a module for creating a local user if permissions allow.[^1]  |
| [[kb/mitre/attack/techniques/T1136.002-domain-account\|T1136.002]] | Domain Account | [[kb/mitre/attack/software/S0363-empire\|Empire]] has a module for creating a new domain user if permissions allow.[^1]  |
| [[kb/mitre/attack/techniques/T1210-exploitation-of-remote-services\|T1210]] | Exploitation of Remote Services | [[kb/mitre/attack/software/S0363-empire\|Empire]] has a limited number of built-in modules for exploiting remote SMB, JBoss, and Jenkins servers.[^1]  |
| [[kb/mitre/attack/techniques/T1217-browser-information-discovery\|T1217]] | Browser Information Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] has the ability to gather browser data such as bookmarks and visited sites.[^1]  |
| [[kb/mitre/attack/techniques/T1482-domain-trust-discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] has modules for enumerating domain trusts.[^1]  |
| [[kb/mitre/attack/techniques/T1484.001-group-policy-modification\|T1484.001]] | Group Policy Modification | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use `New-GPOImmediateTask` to modify a GPO that will install and execute a malicious [[kb/mitre/attack/techniques/T1053-scheduled-task-job\|Scheduled Task/Job]].[^1]  |
| [[kb/mitre/attack/techniques/T1518.001-security-software-discovery\|T1518.001]] | Security Software Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] can enumerate antivirus software on the target.[^1]  |
| [[kb/mitre/attack/techniques/T1543.003-windows-service\|T1543.003]] | Windows Service | [[kb/mitre/attack/software/S0363-empire\|Empire]] can utilize built-in modules to modify service binaries and restore them to their original state.[^1]  |
| [[kb/mitre/attack/techniques/T1546.008-accessibility-features\|T1546.008]] | Accessibility Features | [[kb/mitre/attack/software/S0363-empire\|Empire]] can leverage WMI debugging to remotely replace binaries like sethc.exe, Utilman.exe, and Magnify.exe with cmd.exe.[^1]  |
| [[kb/mitre/attack/techniques/T1547.001-registry-run-keys-startup-folder\|T1547.001]] | Registry Run Keys / Startup Folder | [[kb/mitre/attack/software/S0363-empire\|Empire]] can modify the registry run keys `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` and `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.[^1]  |
| [[kb/mitre/attack/techniques/T1547.005-security-support-provider\|T1547.005]] | Security Support Provider | [[kb/mitre/attack/software/S0363-empire\|Empire]] can enumerate Security Support Providers (SSPs) as well as utilize [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Install-SSP` and `Invoke-Mimikatz` to install malicious SSPs and log authentication events.[^1]  |
| [[kb/mitre/attack/techniques/T1547.009-shortcut-modification\|T1547.009]] | Shortcut Modification | [[kb/mitre/attack/software/S0363-empire\|Empire]] can persist by modifying a .LNK file to include a backdoor.[^1]  |
| [[kb/mitre/attack/techniques/T1548.002-bypass-user-account-control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0363-empire\|Empire]] includes various modules to attempt to bypass UAC for escalation of privileges.[^1]  |
| [[kb/mitre/attack/techniques/T1550.002-pass-the-hash\|T1550.002]] | Pass the Hash | [[kb/mitre/attack/software/S0363-empire\|Empire]] can perform pass the hash attacks.[^1]  |
| [[kb/mitre/attack/techniques/T1552.001-credentials-in-files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use various modules to search for files containing passwords.[^1]  |
| [[kb/mitre/attack/techniques/T1552.004-private-keys\|T1552.004]] | Private Keys | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use modules like `Invoke-SessionGopher` to extract private key and session information.[^1]  |
| [[kb/mitre/attack/techniques/T1555.001-keychain\|T1555.001]] | Keychain | [[kb/mitre/attack/software/S0363-empire\|Empire]] uses the command `/usr/bin/security dump-keychain -d` to read the keychain credential.[^1]  |
| [[kb/mitre/attack/techniques/T1555.003-credentials-from-web-browsers\|T1555.003]] | Credentials from Web Browsers | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use modules that extract passwords from common web browsers such as Firefox and Chrome.[^1]  |
| [[kb/mitre/attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use Inveigh to conduct name service poisoning for credential theft and associated relay attacks.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1558.001-golden-ticket\|T1558.001]] | Golden Ticket | [[kb/mitre/attack/software/S0363-empire\|Empire]] can leverage its implementation of [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] to obtain and use golden tickets.[^1]  |
| [[kb/mitre/attack/techniques/T1558.002-silver-ticket\|T1558.002]] | Silver Ticket | [[kb/mitre/attack/software/S0363-empire\|Empire]] can leverage its implementation of [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] to obtain and use silver tickets.[^1]  |
| [[kb/mitre/attack/techniques/T1558.003-kerberoasting\|T1558.003]] | Kerberoasting | [[kb/mitre/attack/software/S0363-empire\|Empire]] uses [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Invoke-Kerberoast` to request service tickets and return crackable ticket hashes.[^1]  |
| [[kb/mitre/attack/techniques/T1560-archive-collected-data\|T1560]] | Archive Collected Data | [[kb/mitre/attack/software/S0363-empire\|Empire]] can ZIP directories on the target system.[^1]  |
| [[kb/mitre/attack/techniques/T1567.001-exfiltration-to-code-repository\|T1567.001]] | Exfiltration to Code Repository | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use GitHub for data exfiltration.[^1]  |
| [[kb/mitre/attack/techniques/T1567.002-exfiltration-to-cloud-storage\|T1567.002]] | Exfiltration to Cloud Storage | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use Dropbox for data exfiltration.[^1]  |
| [[kb/mitre/attack/techniques/T1569.002-service-execution\|T1569.002]] | Service Execution | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use [[kb/mitre/attack/software/S0029-psexec\|PsExec]] to execute a payload on a remote host.[^1]  |
| [[kb/mitre/attack/techniques/T1573.002-asymmetric-cryptography\|T1573.002]] | Asymmetric Cryptography | [[kb/mitre/attack/software/S0363-empire\|Empire]] can use TLS to encrypt its C2 channel.[^1]  |
| [[kb/mitre/attack/techniques/T1574.001-dll\|T1574.001]] | DLL | [[kb/mitre/attack/software/S0363-empire\|Empire]] contains modules that can discover and exploit various DLL hijacking opportunities.[^1]  |
| [[kb/mitre/attack/techniques/T1574.004-dylib-hijacking\|T1574.004]] | Dylib Hijacking | [[kb/mitre/attack/software/S0363-empire\|Empire]] has a dylib hijacker module that generates a malicious dylib given the path to a legitimate dylib of a vulnerable application.[^1]  |
| [[kb/mitre/attack/techniques/T1574.007-path-interception-by-path-environment-variable\|T1574.007]] | Path Interception by PATH Environment Variable | [[kb/mitre/attack/software/S0363-empire\|Empire]] contains modules that can discover and exploit path interception opportunities in the PATH environment variable.[^1]  |
| [[kb/mitre/attack/techniques/T1574.008-path-interception-by-search-order-hijacking\|T1574.008]] | Path Interception by Search Order Hijacking | [[kb/mitre/attack/software/S0363-empire\|Empire]] contains modules that can discover and exploit search order hijacking vulnerabilities.[^1]  |
| [[kb/mitre/attack/techniques/T1574.009-path-interception-by-unquoted-path\|T1574.009]] | Path Interception by Unquoted Path | [[kb/mitre/attack/software/S0363-empire\|Empire]] contains modules that can discover and exploit unquoted path vulnerabilities.[^1]  |
| [[kb/mitre/attack/techniques/T1615-group-policy-discovery\|T1615]] | Group Policy Discovery | [[kb/mitre/attack/software/S0363-empire\|Empire]] includes various modules for enumerating Group Policy.[^1]  |

 [^1]: [Github PowerShell Empire](https://github.com/PowerShellEmpire/Empire)
 [^2]: [GitHub ATTACK Empire](https://github.com/dstepanic/attck_empire)
 [^3]: [NCSC Joint Report Public Tools](https://www.ncsc.gov.uk/report/joint-report-on-publicly-available-hacking-tools)
 [^4]: [GitHub Inveigh](https://github.com/Kevin-Robertson/Inveigh)
 [^5]: [Talos Frankenstein June 2019](https://blog.talosintelligence.com/2019/06/frankenstein-campaign.html)
 [^6]: [Empire Keychain Decrypt](https://github.com/EmpireProject/Empire/blob/08cbd274bef78243d7a8ed6443b8364acd1fc48b/lib/modules/python/collection/osx/keychaindump_decrypt.py)
 [^7]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
