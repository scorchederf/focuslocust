---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0488
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0488-crackmapexec
---

## Description

[[kb/mitre/attack/software/S0488-crackmapexec|CrackMapExec]], or CME, is a post-exploitation tool developed in Python and designed for penetration testing against networks. [[kb/mitre/attack/software/S0488-crackmapexec|CrackMapExec]] collects Active Directory information to conduct lateral movement through targeted networks.[^1] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.002-security-account-manager\|T1003.002]] | Security Account Manager | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can dump usernames and hashed passwords from the SAM.[^1]  |
| [[kb/mitre/attack/techniques/T1003.003-ntds\|T1003.003]] | NTDS | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can dump hashed passwords associated with Active Directory using Windows' Directory Replication Services API (DRSUAPI), or Volume Shadow Copy.[^1]  |
| [[kb/mitre/attack/techniques/T1003.004-lsa-secrets\|T1003.004]] | LSA Secrets | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can dump hashed passwords from LSA secrets for the targeted system.[^1]  |
| [[kb/mitre/attack/techniques/T1016-system-network-configuration-discovery\|T1016]] | System Network Configuration Discovery | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can collect DNS information from the targeted system.[^1]  |
| [[kb/mitre/attack/techniques/T1018-remote-system-discovery\|T1018]] | Remote System Discovery | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can discover active IP addresses, along with the machine name, within a targeted network.[^1]  |
| [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can execute remote commands using Windows Management Instrumentation.[^1] 	 |
| [[kb/mitre/attack/techniques/T1049-system-network-connections-discovery\|T1049]] | System Network Connections Discovery | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can discover active sessions for a targeted system.[^1]  |
| [[kb/mitre/attack/techniques/T1053.002-at\|T1053.002]] | At | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can set a scheduled task on the target system to execute commands remotely using [[kb/mitre/attack/software/S0110-at\|at]].[^1]  |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can execute PowerShell commands via WMI.[^1]  |
| [[kb/mitre/attack/techniques/T1069.002-domain-groups\|T1069.002]] | Domain Groups | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can gather the user accounts within domain groups.[^1]  |
| [[kb/mitre/attack/techniques/T1083-file-and-directory-discovery\|T1083]] | File and Directory Discovery | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can discover specified filetypes and log files on a targeted system.[^1]  |
| [[kb/mitre/attack/techniques/T1087.002-domain-account\|T1087.002]] | Domain Account | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can enumerate the domain user accounts on a targeted system.[^1]  |
| [[kb/mitre/attack/techniques/T1110-brute-force\|T1110]] | Brute Force | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can brute force supplied user credentials across a network range.[^1]  |
| [[kb/mitre/attack/techniques/T1110.001-password-guessing\|T1110.001]] | Password Guessing | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can brute force passwords for a specified user on a single target system or across an entire network.[^1]  |
| [[kb/mitre/attack/techniques/T1110.003-password-spraying\|T1110.003]] | Password Spraying | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can brute force credential authentication by using a supplied list of usernames and a single password.[^1]  |
| [[kb/mitre/attack/techniques/T1112-modify-registry\|T1112]] | Modify Registry | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can create a registry key using wdigest.[^1]  |
| [[kb/mitre/attack/techniques/T1135-network-share-discovery\|T1135]] | Network Share Discovery | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can enumerate the shared folders and associated permissions for a targeted network.[^1]  |
| [[kb/mitre/attack/techniques/T1201-password-policy-discovery\|T1201]] | Password Policy Discovery | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can discover the password policies applied to the target system.[^1]  |
| [[kb/mitre/attack/techniques/T1550.002-pass-the-hash\|T1550.002]] | Pass the Hash | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can pass the hash to authenticate via SMB.[^1]  |
| [[kb/mitre/attack/techniques/T1680-local-storage-discovery\|T1680]] | Local Storage Discovery | [[kb/mitre/attack/software/S0488-crackmapexec\|CrackMapExec]] can enumerate the system drives and associated system name.[^1]  |

 [^1]: [CME Github September 2018](https://github.com/byt3bl33d3r/CrackMapExec/wiki/SMB-Command-Reference)
