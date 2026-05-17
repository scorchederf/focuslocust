---
parsed_by: focuslocust
source: mitre
type: generated
---
# Koadic

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0250` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Koadic is a Windows post-exploitation framework and penetration testing tool that is publicly available on GitHub. Koadic has several options for staging payloads and creating implants, and performs most of its operations using Windows Script Host.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/koadic.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.002 - Security Account Manager](../../attack/techniques/T1003.002-security-account-manager.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can gather hashed passwords by dumping SAM/SECURITY hive.(Citation: Github Koadic) |
| [T1003.003 - NTDS](../../attack/techniques/T1003.003-ntds.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can gather hashed passwords by gathering domain controller hashes from NTDS.(Citation: Github Koadic) |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can download files off the target system to send back to the server.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021) |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can retrieve the contents of the IP routing table as well as information about the Windows domain.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021) |
| [T1021.001 - Remote Desktop Protocol](../../attack/techniques/T1021.001-remote-desktop-protocol.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can enable remote desktop on the victim's machine.(Citation: Github Koadic) |
| [T1033 - System Owner／User Discovery](../../attack/techniques/T1033-system-owner-user-discovery.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can identify logged in users across the domain and views user sessions.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021) |
| [T1046 - Network Service Discovery](../../attack/techniques/T1046-network-service-discovery.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can scan for open TCP ports on the target network.(Citation: Github Koadic) |
| [T1047 - Windows Management Instrumentation](../../attack/techniques/T1047-windows-management-instrumentation.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can use WMI to execute commands.(Citation: Github Koadic) |
| [T1053.005 - Scheduled Task](../../attack/techniques/T1053.005-scheduled-task.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) has used scheduled tasks to add persistence.(Citation: MalwareBytes LazyScripter Feb 2021)  |
| [T1055.001 - Dynamic-link Library Injection](../../attack/techniques/T1055.001-dynamic-link-library-injection.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can perform process injection by using a reflective DLL.(Citation: Github Koadic) |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) has used PowerShell to establish persistence.(Citation: MalwareBytes LazyScripter Feb 2021)  |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can open an interactive command-shell to perform command line functions on victim machines. [Koadic](https://attack.mitre.org/software/S0250) performs most of its operations using Windows Script Host (Jscript) and to run arbitrary shellcode.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021) |
| [T1059.005 - Visual Basic](../../attack/techniques/T1059.005-visual-basic.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) performs most of its operations using Windows Script Host (VBScript) and runs arbitrary shellcode .(Citation: Github Koadic) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) has used HTTP for C2 communications.(Citation: MalwareBytes LazyScripter Feb 2021) |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can obtain the OS version and build, computer name, and processor architecture from a compromised host.(Citation: MalwareBytes LazyScripter Feb 2021) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can obtain a list of directories.(Citation: MalwareBytes LazyScripter Feb 2021) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can download additional files and tools.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021) |
| [T1115 - Clipboard Data](../../attack/techniques/T1115-clipboard-data.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can retrieve the current content of the user clipboard.(Citation: Github Koadic) |
| [T1135 - Network Share Discovery](../../attack/techniques/T1135-network-share-discovery.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can scan local network for open SMB.(Citation: Github Koadic) |
| [T1218.005 - Mshta](../../attack/techniques/T1218.005-mshta.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can use mshta to serve additional payloads and to help schedule tasks for persistence.(Citation: Github Koadic)(Citation: MalwareBytes LazyScripter Feb 2021)  |
| [T1218.010 - Regsvr32](../../attack/techniques/T1218.010-regsvr32.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can use Regsvr32 to execute additional payloads.(Citation: Github Koadic) |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can use Rundll32 to execute additional payloads.(Citation: Github Koadic) |
| [T1547.001 - Registry Run Keys ／ Startup Folder](../../attack/techniques/T1547.001-registry-run-keys-startup-folder.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) has added persistence to the `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run` Registry key.(Citation: MalwareBytes LazyScripter Feb 2021) |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) has 2 methods for elevating integrity. It can bypass UAC through `eventvwr.exe` and `sdclt.exe`.(Citation: Github Koadic) |
| [T1564.003 - Hidden Window](../../attack/techniques/T1564.003-hidden-window.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) has used the command <code>Powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden</code> to hide its window.(Citation: MalwareBytes LazyScripter Feb 2021) |
| [T1569.002 - Service Execution](../../attack/techniques/T1569.002-service-execution.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can run a command on another machine using [PsExec](https://attack.mitre.org/software/S0029).(Citation: Github Koadic) |
| [T1573.002 - Asymmetric Cryptography](../../attack/techniques/T1573.002-asymmetric-cryptography.md) | explicit | source | [Koadic](https://attack.mitre.org/software/S0250) can use SSL and TLS for communications.(Citation: Github Koadic) |

## Source Verification

[source record](../../sources/mitre/koadic.md)

## Evidence Excerpt

```text
created: '2018-10-17T00:14:20.652Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Koadic](https://attack.mitre.org/software/S0250) is a Windows post-exploitation framework and penetration testing
tool that is publicly available on GitHub. [Koadic](https://attack.mitre.org/software/S0250) has several options for staging
payloads and creating implants, and performs most of its operations using Windows Script Host.(Citation: Github Koadic)(Citation:
Palo Alto Sofacy 06-2018)(Citation: MalwareBytes LazyScripter Feb 2021)'
external_references:
- external_id: S0250
```
