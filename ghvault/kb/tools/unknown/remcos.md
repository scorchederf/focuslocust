---
parsed_by: focuslocust
source: mitre
type: generated
---
# Remcos

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0332` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Remcos is a closed-source tool that is marketed as a remote control and surveillance software by a company called Breaking Security. Remcos has been observed being used in malware campaigns.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/remcos.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1010 - Application Window Discovery](../../attack/techniques/T1010-application-window-discovery.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can list all windows on victim systems.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1012 - Query Registry](../../attack/techniques/T1012-query-registry.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can obtain Registry data from targeted systems.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1027 - Obfuscated Files or Information](../../attack/techniques/T1027-obfuscated-files-or-information.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) uses RC4 and base64 to obfuscate data, including Registry entries and file paths.(Citation: Talos Remcos Aug 2018) [Remcos](https://attack.mitre.org/software/S0332) can also employ control flow flattening to hinder analysis.(Citation: Check Point Blind Eagle MAR 2025) |
| [T1027.013 - Encrypted／Encoded File](../../attack/techniques/T1027.013-encrypted-encoded-file.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can use string encryption to hinder analysis.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1033 - System Owner／User Discovery](../../attack/techniques/T1033-system-owner-user-discovery.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can enumerate the username on targeted hosts.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1055 - Process Injection](../../attack/techniques/T1055-process-injection.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has a command to hide itself by injecting into another process.(Citation: Fortinet Remcos Feb 2017) |
| [T1056.001 - Keylogging](../../attack/techniques/T1056.001-keylogging.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has a command for keylogging.(Citation: Fortinet Remcos Feb 2017)(Citation: Talos Remcos Aug 2018) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can discover running processes on compromised machines.(Citation: Fortinet Remcos Campaign NOV 2024)<br> |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can launch a remote command line to execute commands on the victim’s machine.(Citation: Fortinet Remcos Feb 2017)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1059.005 - Visual Basic](../../attack/techniques/T1059.005-visual-basic.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can execute VBS remotely.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1059.006 - Python](../../attack/techniques/T1059.006-python.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) uses Python scripts.(Citation: Riskiq Remcos Jan 2018) |
| [T1059.007 - JavaScript](../../attack/techniques/T1059.007-javascript.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has the ability to execute JavaScript remotely.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1070 - Indicator Removal](../../attack/techniques/T1070-indicator-removal.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can clean saved cookies and logins from the web browser.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1070.004 - File Deletion](../../attack/techniques/T1070.004-file-deletion.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can delete files and folders from victim machines.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can collect the OS version and process architecture of compromised hosts.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can search for files on the infected machine.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1090 - Proxy](../../attack/techniques/T1090-proxy.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) uses the infected hosts as SOCKS5 proxies to allow for tunneling and proxying.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can upload and download files to and from the victim’s machine.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1112 - Modify Registry](../../attack/techniques/T1112-modify-registry.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has full control of the Registry, including the ability to modify it.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) takes automated screenshots of the infected machine.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1115 - Clipboard Data](../../attack/techniques/T1115-clipboard-data.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) steals and modifies data from the clipboard.(Citation: Riskiq Remcos Jan 2018)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1123 - Audio Capture](../../attack/techniques/T1123-audio-capture.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can capture data from the system’s microphone.(Citation: Fortinet Remcos Feb 2017)(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1125 - Video Capture](../../attack/techniques/T1125-video-capture.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can access a system’s webcam and take pictures.(Citation: Fortinet Remcos Feb 2017) |
| [T1132.001 - Standard Encoding](../../attack/techniques/T1132.001-standard-encoding.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can serialize collected data with Protobuf.(Citation: Check Point Blind Eagle MAR 2025) |
| [T1204.002 - Malicious File](../../attack/techniques/T1204.002-malicious-file.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has been executed by luring victims into opening malicious email attachments including Excel files.(Citation: Fortinet Remcos Campaign NOV 2024)<br> |
| [T1491.001 - Internal Defacement](../../attack/techniques/T1491.001-internal-defacement.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has the ability to modify the desktop wallpaper.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1497.001 - System Checks](../../attack/techniques/T1497.001-system-checks.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) searches for Sandboxie and VMware on the system.(Citation: Talos Remcos Aug 2018) |
| [T1529 - System Shutdown／Reboot](../../attack/techniques/T1529-system-shutdown-reboot.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can shutdown and restart remote devices.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1543.003 - Windows Service](../../attack/techniques/T1543.003-windows-service.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can terminate, suspend, and resume a process by PID.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1547.001 - Registry Run Keys ／ Startup Folder](../../attack/techniques/T1547.001-registry-run-keys-startup-folder.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can add itself to the Registry key <code>HKCU\Software\Microsoft\Windows\CurrentVersion\Run</code> for persistence.(Citation: Fortinet Remcos Feb 2017) |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has a command for UAC bypassing.(Citation: Fortinet Remcos Feb 2017) |
| [T1560.001 - Archive via Utility](../../attack/techniques/T1560.001-archive-via-utility.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can zip files and folders for upload.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1564 - Hide Artifacts](../../attack/techniques/T1564-hide-artifacts.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can modify file attributes to hide the file.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1564.003 - Hidden Window](../../attack/techniques/T1564.003-hidden-window.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can set `ProcessWindowStyle.Hidden` to hide windows.(Citation: Check Point Blind Eagle MAR 2025)<br> |
| [T1566.001 - Spearphishing Attachment](../../attack/techniques/T1566.001-spearphishing-attachment.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has been spread through emails containing malicious documents.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1568 - Dynamic Resolution](../../attack/techniques/T1568-dynamic-resolution.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) has used dynamic DNS domains in C2 communications.(Citation: Check Point Blind Eagle MAR 2025) |
| [T1573.002 - Asymmetric Cryptography](../../attack/techniques/T1573.002-asymmetric-cryptography.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can use TLS to encrypt C2 communication.(Citation: Fortinet Remcos Campaign NOV 2024) |
| [T1614 - System Location Discovery](../../attack/techniques/T1614-system-location-discovery.md) | explicit | source | [Remcos](https://attack.mitre.org/software/S0332) can identify the location of targeted devices.(Citation: Fortinet Remcos Campaign NOV 2024) |

## Source Verification

[source record](../../sources/mitre/remcos.md)

## Evidence Excerpt

```text
created: '2019-01-29T18:55:20.245Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Remcos](https://attack.mitre.org/software/S0332) is a closed-source tool that is marketed as a remote control
and surveillance software by a company called Breaking Security. [Remcos](https://attack.mitre.org/software/S0332) has been
observed being used in malware campaigns.(Citation: Riskiq Remcos Jan 2018)(Citation: Talos Remcos Aug 2018)'
external_references:
- external_id: S0332
source_name: mitre-attack
```
