---
parsed_by: focuslocust
source: mitre
type: generated
---
# Pupy

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0192` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Pupy is an open source, cross-platform (Windows, Linux, OSX, Android) remote administration and post-exploitation tool.  It is written in Python and can be generated as a payload in several different ways (Windows exe, Python file, PowerShell oneliner/file, Linux elf, APK, Rubber Ducky, etc.).  Pupy is publicly available on GitHub.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/pupy.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can execute Lazagne as well as [Mimikatz](https://attack.mitre.org/software/S0002) using PowerShell.(Citation: GitHub Pupy) |
| [T1003.004 - LSA Secrets](../../attack/techniques/T1003.004-lsa-secrets.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.(Citation: GitHub Pupy) |
| [T1003.005 - Cached Domain Credentials](../../attack/techniques/T1003.005-cached-domain-credentials.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.(Citation: GitHub Pupy) |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) has built in commands to identify a host’s IP address and find out other network configuration settings by viewing connected sessions.(Citation: GitHub Pupy) |
| [T1021.001 - Remote Desktop Protocol](../../attack/techniques/T1021.001-remote-desktop-protocol.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can enable/disable RDP connection and can start a remote desktop session using a browser web socket client.(Citation: GitHub Pupy) |
| [T1033 - System Owner／User Discovery](../../attack/techniques/T1033-system-owner-user-discovery.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can enumerate local information for Linux hosts and find currently logged on users for Windows hosts.(Citation: GitHub Pupy) |
| [T1041 - Exfiltration Over C2 Channel](../../attack/techniques/T1041-exfiltration-over-c2-channel.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can send screenshots files, keylogger data, files, and recorded audio back to the C2 server.(Citation: GitHub Pupy) |
| [T1046 - Network Service Discovery](../../attack/techniques/T1046-network-service-discovery.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) has a built-in module for port scanning.(Citation: GitHub Pupy) |
| [T1049 - System Network Connections Discovery](../../attack/techniques/T1049-system-network-connections-discovery.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) has a built-in utility command for <code>netstat</code>, can do net session through PowerView, and has an interactive shell which can be used to discover additional information.(Citation: GitHub Pupy) |
| [T1055.001 - Dynamic-link Library Injection](../../attack/techniques/T1055.001-dynamic-link-library-injection.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can migrate into another process using reflective DLL injection.(Citation: GitHub Pupy) |
| [T1056.001 - Keylogging](../../attack/techniques/T1056.001-keylogging.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) uses a keylogger to capture keystrokes it then sends back to the server after it is stopped.(Citation: GitHub Pupy) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can list the running processes and get the process ID and parent process’s ID.(Citation: GitHub Pupy) |
| [T1059.001 - PowerShell](../../attack/techniques/T1059.001-powershell.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) has a module for loading and executing PowerShell scripts.(Citation: GitHub Pupy) |
| [T1059.006 - Python](../../attack/techniques/T1059.006-python.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can use an add on feature when creating payloads that allows you to create custom Python scripts (“scriptlets”) to perform tasks offline (without requiring a session) such as sandbox detection, adding persistence, etc.(Citation: GitHub Pupy) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can communicate over HTTP for C2.(Citation: GitHub Pupy) |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can grab a system’s information including the OS version, architecture, etc.(Citation: GitHub Pupy) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can walk through directories and recursively search for strings in files.(Citation: GitHub Pupy) |
| [T1087.001 - Local Account](../../attack/techniques/T1087.001-local-account.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) uses PowerView and Pywerview to perform discovery commands such as net user, net group, net local group, etc.(Citation: GitHub Pupy) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can upload and download to/from a victim machine.(Citation: GitHub Pupy) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can drop a mouse-logger that will take small screenshots around at each click and then send back to the server.(Citation: GitHub Pupy) |
| [T1114.001 - Local Email Collection](../../attack/techniques/T1114.001-local-email-collection.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can interact with a victim’s Outlook session and look through folders and emails.(Citation: GitHub Pupy) |
| [T1123 - Audio Capture](../../attack/techniques/T1123-audio-capture.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can record sound with the microphone.(Citation: GitHub Pupy) |
| [T1125 - Video Capture](../../attack/techniques/T1125-video-capture.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can access a connected webcam and capture pictures.(Citation: GitHub Pupy) |
| [T1134.001 - Token Impersonation／Theft](../../attack/techniques/T1134.001-token-impersonation-theft.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can obtain a list of SIDs and provide the option for selecting process tokens to impersonate.(Citation: GitHub Pupy) |
| [T1135 - Network Share Discovery](../../attack/techniques/T1135-network-share-discovery.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can list local and remote shared drives and folders over SMB.(Citation: GitHub Pupy) |
| [T1136.001 - Local Account](../../attack/techniques/T1136.001-local-account.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can user PowerView to execute “net user” commands and create local system accounts.(Citation: GitHub Pupy) |
| [T1136.002 - Domain Account](../../attack/techniques/T1136.002-domain-account.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can user PowerView to execute “net user” commands and create domain accounts.(Citation: GitHub Pupy) |
| [T1497.001 - System Checks](../../attack/techniques/T1497.001-system-checks.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) has a module that checks a number of indicators on the system to determine if its running on a virtual machine.(Citation: GitHub Pupy) |
| [T1543.002 - Systemd Service](../../attack/techniques/T1543.002-systemd-service.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can be used to establish persistence using a systemd service.(Citation: GitHub Pupy) |
| [T1547.001 - Registry Run Keys ／ Startup Folder](../../attack/techniques/T1547.001-registry-run-keys-startup-folder.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) adds itself to the startup folder or adds itself to the Registry key <code>SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run</code> for persistence.(Citation: GitHub Pupy) |
| [T1547.013 - XDG Autostart Entries](../../attack/techniques/T1547.013-xdg-autostart-entries.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can use an XDG Autostart to establish persistence.(Citation: Red Canary Netwire Linux 2022) |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can bypass Windows UAC through either DLL hijacking, eventvwr, or appPaths.(Citation: GitHub Pupy) |
| [T1550.003 - Pass the Ticket](../../attack/techniques/T1550.003-pass-the-ticket.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can also perform pass-the-ticket.(Citation: GitHub Pupy) |
| [T1552.001 - Credentials In Files](../../attack/techniques/T1552.001-credentials-in-files.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.(Citation: GitHub Pupy) |
| [T1555 - Credentials from Password Stores](../../attack/techniques/T1555-credentials-from-password-stores.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.(Citation: GitHub Pupy) |
| [T1555.003 - Credentials from Web Browsers](../../attack/techniques/T1555.003-credentials-from-web-browsers.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can use Lazagne for harvesting credentials.(Citation: GitHub Pupy) |
| [T1557.001 - Name Resolution Poisoning and SMB Relay](../../attack/techniques/T1557.001-name-resolution-poisoning-and-smb-relay.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can sniff plaintext network credentials and use NBNS Spoofing to poison name services.(Citation: GitHub Pupy) |
| [T1560.001 - Archive via Utility](../../attack/techniques/T1560.001-archive-via-utility.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) can compress data with Zip before sending it over C2.(Citation: GitHub Pupy) |
| [T1569.002 - Service Execution](../../attack/techniques/T1569.002-service-execution.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) uses [PsExec](https://attack.mitre.org/software/S0029) to execute a payload or commands on a remote host.(Citation: GitHub Pupy) |
| [T1573.002 - Asymmetric Cryptography](../../attack/techniques/T1573.002-asymmetric-cryptography.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192)'s default encryption for its C2 communication channel is SSL, but it also has transport options for RSA and AES.(Citation: GitHub Pupy) |
| [T1685.005 - Clear Windows Event Logs](../../attack/techniques/T1685.005-clear-windows-event-logs.md) | explicit | source | [Pupy](https://attack.mitre.org/software/S0192) has a module to clear event logs with PowerShell.(Citation: GitHub Pupy) |

## Source Verification

[source record](../../sources/mitre/pupy.md)

## Evidence Excerpt

```text
created: '2018-04-18T17:59:24.739Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Pupy](https://attack.mitre.org/software/S0192) is an open source, cross-platform (Windows, Linux, OSX, Android)
remote administration and post-exploitation tool. (Citation: GitHub Pupy) It is written in Python and can be generated as
a payload in several different ways (Windows exe, Python file, PowerShell oneliner/file, Linux elf, APK, Rubber Ducky, etc.).
(Citation: GitHub Pupy) [Pupy](https://attack.mitre.org/software/S0192) is publicly available on GitHub. (Citation: GitHub
Pupy)'
external_references:
```
