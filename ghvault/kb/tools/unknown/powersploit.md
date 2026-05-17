---
parsed_by: focuslocust
source: mitre
type: generated
---
# PowerSploit

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0194` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

PowerSploit is an open source, offensive security framework comprised of PowerShell modules and scripts that perform a wide range of tasks related to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/powersploit.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can harvest credentials using [Mimikatz](https://attack.mitre.org/software/S0002).(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can access data from local files, volumes, and processes.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1012 - Query Registry](../../attack/techniques/T1012-query-registry.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can query Registry keys for potential opportunities.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1027.005 - Indicator Removal from Tools](../../attack/techniques/T1027.005-indicator-removal-from-tools.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Find-AVSignature</code> AntivirusBypass module can be used to locate single byte anti-virus signatures.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1027.010 - Command Obfuscation](../../attack/techniques/T1027.010-command-obfuscation.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of ScriptModification modules that compress and encode scripts and payloads.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1047 - Windows Management Instrumentation](../../attack/techniques/T1047-windows-management-instrumentation.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-WmiCommand</code> CodeExecution module uses WMI to execute and retrieve the output from a [PowerShell](https://attack.mitre.org/techniques/T1086) payload.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1053.005 - Scheduled Task](../../attack/techniques/T1053.005-scheduled-task.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>New-UserPersistenceOption</code> Persistence argument can be used to establish via a [Scheduled Task/Job](https://attack.mitre.org/techniques/T1053).(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1055.001 - Dynamic-link Library Injection](../../attack/techniques/T1055.001-dynamic-link-library-injection.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of CodeExecution modules that inject code (DLL, shellcode) into a process.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1056.001 - Keylogging](../../attack/techniques/T1056.001-keylogging.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-Keystrokes</code> Exfiltration module can log keystrokes.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-ProcessTokenPrivilege</code> Privesc-PowerUp module can enumerate privileges for a given process.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) modules are written in and executed via [PowerShell](https://attack.mitre.org/techniques/T1086).(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1087.001 - Local Account](../../attack/techniques/T1087.001-local-account.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-ProcessTokenGroup</code> Privesc-PowerUp module can enumerate all SIDs associated with its current token.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-TimedScreenshot</code> Exfiltration module can take screenshots at regular intervals.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1123 - Audio Capture](../../attack/techniques/T1123-audio-capture.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Get-MicrophoneAudio</code> Exfiltration module can record system microphone audio.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1134 - Access Token Manipulation](../../attack/techniques/T1134-access-token-manipulation.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-TokenManipulation</code> Exfiltration module can be used to manipulate tokens.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1482 - Domain Trust Discovery](../../attack/techniques/T1482-domain-trust-discovery.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) has modules such as <code>Get-NetDomainTrust</code> and <code>Get-NetForestTrust</code> to enumerate domain and forest trusts.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1543.003 - Windows Service](../../attack/techniques/T1543.003-windows-service.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and replace/modify service binaries, paths, and configs.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1547.001 - Registry Run Keys ／ Startup Folder](../../attack/techniques/T1547.001-registry-run-keys-startup-folder.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>New-UserPersistenceOption</code> Persistence argument can be used to establish via the <code>HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run</code> Registry key.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1547.005 - Security Support Provider](../../attack/techniques/T1547.005-security-support-provider.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Install-SSP</code> Persistence module can be used to establish by installing a SSP DLL.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1552.002 - Credentials in Registry](../../attack/techniques/T1552.002-credentials-in-registry.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) has several modules that search the Windows Registry for stored credentials: <code>Get-UnattendedInstallFile</code>, <code>Get-Webconfig</code>, <code>Get-ApplicationHost</code>, <code>Get-SiteListPassword</code>, <code>Get-CachedGPPPassword</code>, and <code>Get-RegistryAutoLogon</code>.(Citation: Pentestlab Stored Credentials) |
| [T1552.006 - Group Policy Preferences](../../attack/techniques/T1552.006-group-policy-preferences.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can harvest credentials from Group Policy Preferences.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1555.004 - Windows Credential Manager](../../attack/techniques/T1555.004-windows-credential-manager.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Exfiltration modules that can harvest credentials from Windows vault credential objects.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1558.003 - Kerberoasting](../../attack/techniques/T1558.003-kerberoasting.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194)'s <code>Invoke-Kerberoast</code> module can request service tickets and return crackable ticket hashes.(Citation: PowerSploit Invoke Kerberoast)(Citation: Harmj0y Kerberoast Nov 2016) |
| [T1574.001 - DLL](../../attack/techniques/T1574.001-dll.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit DLL hijacking opportunities in services and processes.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1574.007 - Path Interception by PATH Environment Variable](../../attack/techniques/T1574.007-path-interception-by-path-environment-variable.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit path interception opportunities in the PATH environment variable.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1574.008 - Path Interception by Search Order Hijacking](../../attack/techniques/T1574.008-path-interception-by-search-order-hijacking.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit search order hijacking vulnerabilities.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1574.009 - Path Interception by Unquoted Path](../../attack/techniques/T1574.009-path-interception-by-unquoted-path.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) contains a collection of Privesc-PowerUp modules that can discover and exploit unquoted path vulnerabilities.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |
| [T1620 - Reflective Code Loading](../../attack/techniques/T1620-reflective-code-loading.md) | explicit | source | [PowerSploit](https://attack.mitre.org/software/S0194) reflectively loads a Windows PE file into a process.(Citation: GitHub PowerSploit May 2012)(Citation: PowerSploit Documentation) |

## Source Verification

[source record](../../sources/mitre/powersploit.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[PowerSploit](https://attack.mitre.org/software/S0194) is an open source, offensive security framework comprised
of [PowerShell](https://attack.mitre.org/techniques/T1059/001) modules and scripts that perform a wide range of tasks related
to penetration testing such as code execution, persistence, bypassing anti-virus, recon, and exfiltration. (Citation: GitHub
PowerSploit May 2012) (Citation: PowerShellMagazine PowerSploit July 2014) (Citation: PowerSploit Documentation)'
external_references:
- external_id: S0194
```
