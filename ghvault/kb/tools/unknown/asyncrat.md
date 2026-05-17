---
parsed_by: focuslocust
source: mitre
type: generated
---
# AsyncRAT

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S1087` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

AsyncRAT is an open-source remote access tool originally available through the NYANxCAT Github repository that has been used in malicious campaigns.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/asyncrat.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1016 - System Network Configuration Discovery](../../attack/techniques/T1016-system-network-configuration-discovery.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can enumerate the NetBIOS name on targeted machines.(Citation: ESET MirrorFace 2025) |
| [T1033 - System Owner／User Discovery](../../attack/techniques/T1033-system-owner-user-discovery.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can check if the current user of a compromised system is an administrator. (Citation: Telefonica Snip3 December 2021) |
| [T1053.005 - Scheduled Task](../../attack/techniques/T1053.005-scheduled-task.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can create a scheduled task to maintain persistence on system start-up.(Citation: Telefonica Snip3 December 2021) |
| [T1056.001 - Keylogging](../../attack/techniques/T1056.001-keylogging.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can capture keystrokes on the victim’s machine.(Citation: AsyncRAT GitHub) |
| [T1057 - Process Discovery](../../attack/techniques/T1057-process-discovery.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can examine running processes to determine if a debugger is present.(Citation: Telefonica Snip3 December 2021) |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can be deployed via batch script.(Citation: ESET MirrorFace 2025) |
| [T1090.003 - Multi-hop Proxy](../../attack/techniques/T1090.003-multi-hop-proxy.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can proxy C2 through a [Tor](https://attack.mitre.org/software/S0183) client.(Citation: ESET MirrorFace 2025) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to download files including over SFTP.(Citation: AsyncRAT GitHub)(Citation: ESET MirrorFace 2025) |
| [T1106 - Native API](../../attack/techniques/T1106-native-api.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to use OS APIs including `CheckRemoteDebuggerPresent`.(Citation: Telefonica Snip3 December 2021) |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) has the ability to view the screen on compromised hosts.(Citation: AsyncRAT GitHub) |
| [T1124 - System Time Discovery](../../attack/techniques/T1124-system-time-discovery.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can check whether the current system hour and day of the week are within operating hours defined it its configuration.(Citation: ESET MirrorFace 2025) |
| [T1125 - Video Capture](../../attack/techniques/T1125-video-capture.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can record screen content on targeted systems.(Citation: AsyncRAT GitHub) |
| [T1204.002 - Malicious File](../../attack/techniques/T1204.002-malicious-file.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) has been executed through victims opening malicious file attachments.(Citation: Recorded Future TAG-144 AUG 2025) |
| [T1497.001 - System Checks](../../attack/techniques/T1497.001-system-checks.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can identify strings such as Virtual, vmware, or VirtualBox to detect virtualized environments.(Citation: Telefonica Snip3 December 2021) |
| [T1564.003 - Hidden Window](../../attack/techniques/T1564.003-hidden-window.md) | explicit | source | <br>[AsyncRAT](https://attack.mitre.org/software/S1087) can hide the execution of scheduled tasks using `ProcessWindowStyle.Hidden`.(Citation: Telefonica Snip3 December 2021) |
| [T1566.001 - Spearphishing Attachment](../../attack/techniques/T1566.001-spearphishing-attachment.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) has been delivered via malicious email attachments.(Citation: Recorded Future TAG-144 AUG 2025) |
| [T1568 - Dynamic Resolution](../../attack/techniques/T1568-dynamic-resolution.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can be configured to use dynamic DNS.(Citation: AsyncRAT GitHub) |
| [T1568.002 - Domain Generation Algorithms](../../attack/techniques/T1568.002-domain-generation-algorithms.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) use a DGA to generate a C2 domains.(Citation: ESET MirrorFace 2025) |
| [T1622 - Debugger Evasion](../../attack/techniques/T1622-debugger-evasion.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can use the `CheckRemoteDebuggerPresent` function to detect the presence of a debugger.(Citation: Telefonica Snip3 December 2021) |
| [T1680 - Local Storage Discovery](../../attack/techniques/T1680-local-storage-discovery.md) | explicit | source | [AsyncRAT](https://attack.mitre.org/software/S1087) can check the disk size through the values obtained with `DeviceInfo.`(Citation: Telefonica Snip3 December 2021) |

## Source Verification

[source record](../../sources/mitre/asyncrat.md)

## Evidence Excerpt

```text
created: '2023-09-20T17:32:59.932Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[AsyncRAT](https://attack.mitre.org/software/S1087) is an open-source remote access tool originally available
through the NYANxCAT Github repository that has been used in malicious campaigns.(Citation: Morphisec Snip3 May 2021)(Citation:
Cisco Operation Layover September 2021)(Citation: Telefonica Snip3 December 2021)'
external_references:
- external_id: S1087
source_name: mitre-attack
```
