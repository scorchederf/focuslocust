---
parsed_by: focuslocust
source: mitre
type: tool
aliases:
    - S0194
tags:
    - attack/domain/enterprise_attack
    - attack/software/tool
    - attack/type/software
mitre-attack: kb/mitre/attack/software/S0194-powersploit
---

## Description

[[kb/mitre/attack/software/S0194-powersploit|PowerSploit]] is an open source, offensive security framework comprised of [[kb/mitre/attack/techniques/T1059.001-powershell|PowerShell]] modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. [^2]  [^1]  [^3] 

## Techniques Used
| ID | Name | Use |
| --- | --- | --- |
| [[kb/mitre/attack/techniques/T1003.001-lsass-memory\|T1003.001]] | LSASS Memory | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Exfiltration modules that can harvest credentials using [[kb/mitre/attack/software/S0002-mimikatz\|Mimikatz]].[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1005-data-from-local-system\|T1005]] | Data from Local System | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Exfiltration modules that can access data from local files, volumes, and processes.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1012-query-registry\|T1012]] | Query Registry | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can query Registry keys for potential opportunities.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1027.005-indicator-removal-from-tools\|T1027.005]] | Indicator Removal from Tools | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Find-AVSignature` AntivirusBypass module can be used to locate single byte anti-virus signatures.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1027.010-command-obfuscation\|T1027.010]] | Command Obfuscation | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of ScriptModification modules that compress and encode scripts and payloads.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1047-windows-management-instrumentation\|T1047]] | Windows Management Instrumentation | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Invoke-WmiCommand` CodeExecution module uses WMI to execute and retrieve the output from a PowerShell payload.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1053.005-scheduled-task\|T1053.005]] | Scheduled Task | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `New-UserPersistenceOption` Persistence argument can be used to establish via a [[kb/mitre/attack/techniques/T1053-scheduled-task-job\|Scheduled Task/Job]].[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1055.001-dynamic-link-library-injection\|T1055.001]] | Dynamic-link Library Injection | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of CodeExecution modules that inject code (DLL, shellcode) into a process.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1056.001-keylogging\|T1056.001]] | Keylogging | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Get-Keystrokes` Exfiltration module can log keystrokes.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1057-process-discovery\|T1057]] | Process Discovery | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Get-ProcessTokenPrivilege` Privesc-PowerUp module can enumerate privileges for a given process.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1059.001-powershell\|T1059.001]] | PowerShell | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] modules are written in and executed via PowerShell.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1087.001-local-account\|T1087.001]] | Local Account | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Get-ProcessTokenGroup` Privesc-PowerUp module can enumerate all SIDs associated with its current token.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1113-screen-capture\|T1113]] | Screen Capture | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Get-TimedScreenshot` Exfiltration module can take screenshots at regular intervals.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1123-audio-capture\|T1123]] | Audio Capture | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Get-MicrophoneAudio` Exfiltration module can record system microphone audio.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1134-access-token-manipulation\|T1134]] | Access Token Manipulation | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Invoke-TokenManipulation` Exfiltration module can be used to manipulate tokens.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1482-domain-trust-discovery\|T1482]] | Domain Trust Discovery | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] has modules such as `Get-NetDomainTrust` and `Get-NetForestTrust` to enumerate domain and forest trusts.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1543.003-windows-service\|T1543.003]] | Windows Service | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can discover and replace/modify service binaries, paths, and configs.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1547.001-registry-run-keys-startup-folder\|T1547.001]] | Registry Run Keys / Startup Folder | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `New-UserPersistenceOption` Persistence argument can be used to establish via the `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` Registry key.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1547.005-security-support-provider\|T1547.005]] | Security Support Provider | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Install-SSP` Persistence module can be used to establish by installing a SSP DLL.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1552.002-credentials-in-registry\|T1552.002]] | Credentials in Registry | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] has several modules that search the Windows Registry for stored credentials: `Get-UnattendedInstallFile`, `Get-Webconfig`, `Get-ApplicationHost`, `Get-SiteListPassword`, `Get-CachedGPPPassword`, and `Get-RegistryAutoLogon`.[^1]  |
| [[kb/mitre/attack/techniques/T1552.006-group-policy-preferences\|T1552.006]] | Group Policy Preferences | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Exfiltration modules that can harvest credentials from Group Policy Preferences.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1555.004-windows-credential-manager\|T1555.004]] | Windows Credential Manager | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Exfiltration modules that can harvest credentials from Windows vault credential objects.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1558.003-kerberoasting\|T1558.003]] | Kerberoasting | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]]'s `Invoke-Kerberoast` module can request service tickets and return crackable ticket hashes.[^2] [^1]  |
| [[kb/mitre/attack/techniques/T1574.001-dll\|T1574.001]] | DLL | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can discover and exploit DLL hijacking opportunities in services and processes.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1574.007-path-interception-by-path-environment-variable\|T1574.007]] | Path Interception by PATH Environment Variable | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can discover and exploit path interception opportunities in the PATH environment variable.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1574.008-path-interception-by-search-order-hijacking\|T1574.008]] | Path Interception by Search Order Hijacking | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can discover and exploit search order hijacking vulnerabilities.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1574.009-path-interception-by-unquoted-path\|T1574.009]] | Path Interception by Unquoted Path | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] contains a collection of Privesc-PowerUp modules that can discover and exploit unquoted path vulnerabilities.[^1] [^2]  |
| [[kb/mitre/attack/techniques/T1620-reflective-code-loading\|T1620]] | Reflective Code Loading | [[kb/mitre/attack/software/S0194-powersploit\|PowerSploit]] reflectively loads a Windows PE file into a process.[^1] [^2]  |

 [^1]: [PowerShellMagazine PowerSploit July 2014](http://www.powershellmagazine.com/2014/07/08/powersploit/)
 [^2]: [GitHub PowerSploit May 2012](https://github.com/PowerShellMafia/PowerSploit)
 [^3]: [PowerSploit Documentation](http://powersploit.readthedocs.io)
 [^4]: [Pentestlab Stored Credentials](https://pentestlab.blog/2017/04/19/stored-credentials/)
 [^5]: [Harmj0y Kerberoast Nov 2016](https://blog.harmj0y.net/powershell/kerberoasting-without-mimikatz/)
 [^6]: [PowerSploit Invoke Kerberoast](https://powersploit.readthedocs.io/en/latest/Recon/Invoke-Kerberoast/)
