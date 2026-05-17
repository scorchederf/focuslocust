---
parsed_by: focuslocust
source: mitre
type: generated
---
# Imminent Monitor

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0434` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Imminent Monitor was a commodity remote access tool (RAT) offered for sale from 2012 until 2019, when an operation was conducted to take down the Imminent Monitor infrastructure. Various cracked versions and variations of this RAT are still in circulation.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/imminent-monitor.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1021.001 - Remote Desktop Protocol](../../attack/techniques/T1021.001-remote-desktop-protocol.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a module for performing remote desktop access.(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1027 - Obfuscated Files or Information](../../attack/techniques/T1027-obfuscated-files-or-information.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has encrypted the spearphish attachments to avoid detection from email gateways; the debugger also encrypts information before sending to the C2.(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1041 - Exfiltration Over C2 Channel](../../attack/techniques/T1041-exfiltration-over-c2-channel.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has uploaded a file containing debugger logs, network information and system information to the C2.(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1056.001 - Keylogging](../../attack/techniques/T1056.001-keylogging.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a keylogging module.(Citation: Imminent Unit42 Dec2019) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a "Process Watcher" feature to monitor processes in case the client ever crashes or gets closed.(Citation: Imminent Unit42 Dec2019) |
| [T1059 - Command and Scripting Interpreter](../../attack/techniques/T1059-command-and-scripting-interpreter.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a CommandPromptPacket and ScriptPacket module(s) for creating a remote shell and executing scripts.(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1070.004 - File Deletion](../../attack/techniques/T1070.004-file-deletion.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has deleted files related to its dynamic debugger feature.(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1083 - File and Directory Discovery](../../attack/techniques/T1083-file-and-directory-discovery.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a dynamic debugging feature to check whether it is located in the %TEMP% directory, otherwise it copies itself there.(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1106 - Native API](../../attack/techniques/T1106-native-api.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has leveraged CreateProcessW() call to execute the debugger.(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1123 - Audio Capture](../../attack/techniques/T1123-audio-capture.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a remote microphone monitoring capability.(Citation: Imminent Unit42 Dec2019)(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1125 - Video Capture](../../attack/techniques/T1125-video-capture.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a remote webcam monitoring capability.(Citation: Imminent Unit42 Dec2019)(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1140 - Deobfuscate／Decode Files or Information](../../attack/techniques/T1140-deobfuscate-decode-files-or-information.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has decoded malware components that are then dropped to the system.(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1496.001 - Compute Hijacking](../../attack/techniques/T1496.001-compute-hijacking.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has the capability to run a cryptocurrency miner on the victim machine.(Citation: Imminent Unit42 Dec2019) |
| [T1555.003 - Credentials from Web Browsers](../../attack/techniques/T1555.003-credentials-from-web-browsers.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a PasswordRecoveryPacket module for recovering browser passwords.(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1564.001 - Hidden Files and Directories](../../attack/techniques/T1564.001-hidden-files-and-directories.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a dynamic debugging feature to set the file attribute to hidden.(Citation: QiAnXin APT-C-36 Feb2019) |
| [T1685 - Disable or Modify Tools](../../attack/techniques/T1685-disable-or-modify-tools.md) | explicit | source | [Imminent Monitor](https://attack.mitre.org/software/S0434) has a feature to disable Windows Task Manager.(Citation: Imminent Unit42 Dec2019)	 |

## Source Verification

[source record](../../sources/mitre/imminent-monitor.md)

## Evidence Excerpt

```text
created: '2020-05-05T18:45:36.358Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[Imminent Monitor](https://attack.mitre.org/software/S0434) was a commodity remote access tool (RAT) offered
for sale from 2012 until 2019, when an operation was conducted to take down the Imminent Monitor infrastructure. Various
cracked versions and variations of this RAT are still in circulation.(Citation: Imminent Unit42 Dec2019)'
external_references:
- external_id: S0434
source_name: mitre-attack
```
