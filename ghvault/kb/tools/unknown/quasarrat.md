---
parsed_by: focuslocust
source: mitre
type: generated
---
# QuasarRAT

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0262` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

QuasarRAT is an open-source, remote access tool that has been publicly available on GitHub since at least 2014. QuasarRAT is developed in the C# language.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/quasarrat.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can retrieve files from compromised client machines.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1010 - Application Window Discovery](../../attack/techniques/T1010-application-window-discovery.md) | explicit | source | [APT-C-36](https://attack.mitre.org/groups/G0099) used a customized version of [QuasarRAT](https://attack.mitre.org/software/S0262) to monitor browser windows for strings relating to specific Colombian financial institutions.(Citation: Kaspersky BlindEagle AUG 2024)<br> |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) has the ability to enumerate the Wide Area Network (WAN) IP through requests to ip-api[.]com, freegeoip[.]net, or api[.]ipify[.]org observed with user-agent string `Mozilla/5.0 (Windows NT 6.3; rv:48.0) Gecko/20100101 Firefox/48.0`.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1021.001 - Remote Desktop Protocol](../../attack/techniques/T1021.001-remote-desktop-protocol.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) has a module for performing remote desktop access.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) |
| [T1033 - System Owner／User Discovery](../../attack/techniques/T1033-system-owner-user-discovery.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can enumerate the username and account type.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1053.005 - Scheduled Task](../../attack/techniques/T1053.005-scheduled-task.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) contains a .NET wrapper DLL for creating and managing scheduled tasks for maintaining persistence upon reboot.(Citation: Volexity Patchwork June 2018)(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1056.001 - Keylogging](../../attack/techniques/T1056.001-keylogging.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) has a built-in keylogger.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)(Citation: Kaspersky BlindEagle AUG 2024) |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can launch a remote shell to execute commands on the victim’s machine.(Citation: GitHub QuasarRAT)(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1082 - System Information Discovery](../../attack/techniques/T1082-system-information-discovery.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can gather system information from the victim’s machine including the OS type.(Citation: GitHub QuasarRAT) |
| [T1090 - Proxy](../../attack/techniques/T1090-proxy.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can communicate over a reverse proxy using SOCKS5.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) |
| [T1095 - Non-Application Layer Protocol](../../attack/techniques/T1095-non-application-layer-protocol.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can use TCP for C2 communication.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can download files to the victim’s machine and execute them.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) |
| [T1112 - Modify Registry](../../attack/techniques/T1112-modify-registry.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) has a command to edit the Registry on the victim’s machine.(Citation: GitHub QuasarRAT)(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1125 - Video Capture](../../attack/techniques/T1125-video-capture.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can perform webcam viewing.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) |
| [T1547.001 - Registry Run Keys ／ Startup Folder](../../attack/techniques/T1547.001-registry-run-keys-startup-folder.md) | explicit | source | If the [QuasarRAT](https://attack.mitre.org/software/S0262) client process does not have administrator privileges it will add a registry key to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` for persistence.(Citation: GitHub QuasarRAT)(Citation: CISA AR18-352A Quasar RAT December 2018)  |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | <br>[QuasarRAT](https://attack.mitre.org/software/S0262) can generate a UAC pop-up Window to prompt the target user to run a command as the administrator.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1552.001 - Credentials In Files](../../attack/techniques/T1552.001-credentials-in-files.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can obtain passwords from FTP clients.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) |
| [T1553.002 - Code Signing](../../attack/techniques/T1553.002-code-signing.md) | explicit | source | A [QuasarRAT](https://attack.mitre.org/software/S0262) .dll file is digitally signed by a certificate from AirVPN.(Citation: Volexity Patchwork June 2018) |
| [T1555 - Credentials from Password Stores](../../attack/techniques/T1555-credentials-from-password-stores.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can obtain passwords from common FTP clients.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018) |
| [T1555.003 - Credentials from Web Browsers](../../attack/techniques/T1555.003-credentials-from-web-browsers.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can obtain passwords from common web browsers.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)(Citation: Kaspersky BlindEagle AUG 2024)<br> |
| [T1564.001 - Hidden Files and Directories](../../attack/techniques/T1564.001-hidden-files-and-directories.md) | explicit | source | <br>[QuasarRAT](https://attack.mitre.org/software/S0262) has the ability to set file attributes to "hidden" to hide files from the compromised user's view in Windows File Explorer.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1564.003 - Hidden Window](../../attack/techniques/T1564.003-hidden-window.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can hide process windows and make web requests invisible to the compromised user. Requests marked as invisible have been sent with user-agent string `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A` though [QuasarRAT](https://attack.mitre.org/software/S0262) can only be run on Windows systems.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1571 - Non-Standard Port](../../attack/techniques/T1571-non-standard-port.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can use port 4782 on the compromised host for TCP callbacks.(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1573.001 - Symmetric Cryptography](../../attack/techniques/T1573.001-symmetric-cryptography.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) uses AES with a hardcoded pre-shared key to encrypt network communication.(Citation: GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)(Citation: CISA AR18-352A Quasar RAT December 2018) |
| [T1614 - System Location Discovery](../../attack/techniques/T1614-system-location-discovery.md) | explicit | source | [QuasarRAT](https://attack.mitre.org/software/S0262) can determine the country a victim host is located in.(Citation: CISA AR18-352A Quasar RAT December 2018) |

## Source Verification

[source record](../../sources/mitre/quasarrat.md)

## Evidence Excerpt

```text
created: '2018-10-17T00:14:20.652Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[QuasarRAT](https://attack.mitre.org/software/S0262) is an open-source, remote access tool that has been publicly
available on GitHub since at least 2014. [QuasarRAT](https://attack.mitre.org/software/S0262) is developed in the C# language.(Citation:
GitHub QuasarRAT)(Citation: Volexity Patchwork June 2018)'
external_references:
- external_id: S0262
source_name: mitre-attack
```
