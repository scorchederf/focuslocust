---
generated_by: focuslocust
source: mitre
type: tool
aliases:
    - S0378
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0378-poshc2
---

## Description

[[kb/mitre/attack/software/S0378-poshc2|PoshC2]] is an open source remote administration and post-exploitation framework that is publicly available on GitHub. The server-side components of the tool are primarily written in Python, while the implants are written in [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]]. Although [[kb/mitre/attack/software/S0378-poshc2|PoshC2]] is primarily focused on Windows implantation, it does contain a basic Python dropper for Linux/macOS.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-lsass-memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains an implementation of [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]] to gather credentials from memory.[^1]  |
| [[kb/mitre/attack/techniques/T1007-system-service-discovery\|T1007]] | System Service Discovery | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can enumerate service and service permission information.[^1]  |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can enumerate network adapter information.[^1]  |
| [[kb/mitre/attack/techniques/T1040-network-sniffing\|T1040]] | Network Sniffing | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains a module for taking packet captures on compromised hosts.[^1]  |
| [[kb/mitre/attack/techniques/T1046-network-service-discovery\|T1046]] | Network Service Discovery | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can perform port scans from an infected host.[^1]  |
| [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] has a number of modules that use WMI to execute tasks.[^1]  |
| [[kb/mitre/attack/techniques/T1049-system-network-connections-discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains an implementation of [[kb/mitre/attack/software/S0104-netstat\|netstat]] to enumerate TCP and UDP connections.[^1]  |
| [[kb/mitre/attack/techniques/T1055-process-injection\|T1055]] | Process Injection | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains multiple modules for injecting into processes, such as `Invoke-PSInject`.[^1]  |
| [[kb/mitre/attack/techniques/T1056.001-keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] has modules for keystroke logging and capturing credentials from spoofed Outlook authentication messages.[^1]  |
| [[kb/mitre/attack/techniques/T1068-exploitation-for-privilege-escalation\|T1068]] | Exploitation for Privilege Escalation | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains modules for local privilege escalation exploits such as CVE-2016-9192 and CVE-2016-0099.[^1]  |
| [[kb/mitre/attack/techniques/T1069.001-local-groups\|T1069.001]] | Local Groups | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains modules, such as `Get-LocAdm` for enumerating permission groups.[^1]  |
| [[kb/mitre/attack/techniques/T1071.001-web-protocols\|T1071.001]] | Web Protocols | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can use protocols like HTTP/HTTPS for command and control traffic.[^1]  |
| [[kb/mitre/attack/techniques/T1082-system-information-discovery\|T1082]] | System Information Discovery | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains modules, such as `Get-ComputerInfo`, for enumerating common system information.[^1]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can enumerate files on the local file system and includes a module for enumerating recently accessed files.[^1]  |
| [[kb/mitre/attack/techniques/T1087.001-local-account\|T1087.001]] | Local Account | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can enumerate local and domain user account information.[^1]  |
| [[kb/mitre/attack/techniques/T1087.002-domain-account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can enumerate local and domain user account information.[^1]  |
| [[kb/mitre/attack/techniques/T1090-proxy\|T1090]] | Proxy | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains modules that allow for use of proxies in command and control.[^1]  |
| [[kb/mitre/attack/techniques/T1110-brute-force\|T1110]] | Brute Force | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] has modules for brute forcing local administrator and AD user accounts.[^1]  |
| [[kb/mitre/attack/techniques/T1119-automated-collection\|T1119]] | Automated Collection | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains a module for recursively parsing through files and directories to gather valid credit card numbers.[^1]  |
| [[kb/mitre/attack/techniques/T1134-access-token-manipulation\|T1134]] | Access Token Manipulation | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can use Invoke-TokenManipulation for manipulating tokens.[^1]  |
| [[kb/mitre/attack/techniques/T1134.002-create-process-with-token\|T1134.002]] | Create Process with Token | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can use Invoke-RunAs to make tokens.[^1]  |
| [[kb/mitre/attack/techniques/T1201-password-policy-discovery\|T1201]] | Password Policy Discovery | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can use `Get-PassPol` to enumerate the domain password policy.[^1]  |
| [[kb/mitre/attack/techniques/T1210-exploitation-of-remote-services\|T1210]] | Exploitation of Remote Services | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains a module for exploiting SMB via EternalBlue.[^1]  |
| [[kb/mitre/attack/techniques/T1482-domain-trust-discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] has modules for enumerating domain trusts.[^1]  |
| [[kb/mitre/attack/techniques/T1546.003-windows-management-instrumentation-event-subscription\|T1546.003]] | Windows Management Instrumentation Event Subscription | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] has the ability to persist on a system using WMI events.[^1]  |
| [[kb/mitre/attack/techniques/T1548.002-bypass-user-account-control\|T1548.002]] | Bypass User Account Control | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can utilize multiple methods to bypass UAC.[^1]  |
| [[kb/mitre/attack/techniques/T1550.002-pass-the-hash\|T1550.002]] | Pass the Hash | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] has a number of modules that leverage pass the hash for lateral movement.[^1]  |
| [[kb/mitre/attack/techniques/T1552.001-credentials-in-files\|T1552.001]] | Credentials In Files | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains modules for searching for passwords in local and remote files.[^1]  |
| [[kb/mitre/attack/techniques/T1555-credentials-from-password-stores\|T1555]] | Credentials from Password Stores | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can decrypt passwords stored in the RDCMan configuration file.[^1]  |
| [[kb/mitre/attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay\|T1557.001]] | Name Resolution Poisoning and SMB Relay | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] can use Inveigh to conduct name service poisoning for credential theft and associated relay attacks.[^1]  |
| [[kb/mitre/attack/techniques/T1560.001-archive-via-utility\|T1560.001]] | Archive via Utility | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains a module for compressing data using ZIP.[^1]  |
| [[kb/mitre/attack/techniques/T1569.002-service-execution\|T1569.002]] | Service Execution | [[kb/mitre/attack/software/S0378-poshc2\|PoshC2]] contains an implementation of [[kb/mitre/attack/software/S0029-psexec\|PsExec]] for remote execution.[^1]  |

 [^1]: [GitHub PoshC2](https://github.com/nettitude/PoshC2_Python)
 [^2]: [SecureWorks August 2019](https://www.secureworks.com/blog/lyceum-takes-center-stage-in-middle-east-campaign)
