---
parsed_by: focuslocust
source: mitre
type: generated
---
# CSPY Downloader

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0527` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

CSPY Downloader is a tool designed to evade analysis and download additional payloads used by Kimsuky.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/cspy-downloader.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1027.002 - Software Packing](../../attack/techniques/T1027.002-software-packing.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) has been packed with UPX.(Citation: Cybereason Kimsuky November 2020) |
| [T1036.004 - Masquerade Task or Service](../../attack/techniques/T1036.004-masquerade-task-or-service.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) has attempted to appear as a legitimate Windows service with a fake description claiming it is used to support packed applications.(Citation: Cybereason Kimsuky November 2020) |
| [T1053.005 - Scheduled Task](../../attack/techniques/T1053.005-scheduled-task.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) can use the schtasks utility to bypass UAC.(Citation: Cybereason Kimsuky November 2020) |
| [T1070 - Indicator Removal](../../attack/techniques/T1070-indicator-removal.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) has the ability to remove values it writes to the Registry.(Citation: Cybereason Kimsuky November 2020) |
| [T1070.004 - File Deletion](../../attack/techniques/T1070.004-file-deletion.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) has the ability to self delete.(Citation: Cybereason Kimsuky November 2020) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) can use GET requests to download additional payloads from C2.(Citation: Cybereason Kimsuky November 2020) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) can download additional tools to a compromised host.(Citation: Cybereason Kimsuky November 2020) |
| [T1112 - Modify Registry](../../attack/techniques/T1112-modify-registry.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) can write to the Registry under the <code>%windir%</code> variable to execute tasks.(Citation: Cybereason Kimsuky November 2020) |
| [T1204.002 - Malicious File](../../attack/techniques/T1204.002-malicious-file.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) has been delivered via malicious documents with embedded macros.(Citation: Cybereason Kimsuky November 2020) |
| [T1497.001 - System Checks](../../attack/techniques/T1497.001-system-checks.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) can search loaded modules, PEB structure, file paths, Registry keys, and memory to determine if it is being debugged or running in a virtual environment.(Citation: Cybereason Kimsuky November 2020) |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) can bypass UAC using the SilentCleanup task to execute the binary with elevated privileges.(Citation: Cybereason Kimsuky November 2020) |
| [T1553.002 - Code Signing](../../attack/techniques/T1553.002-code-signing.md) | explicit | source | [CSPY Downloader](https://attack.mitre.org/software/S0527) has come signed with revoked certificates.(Citation: Cybereason Kimsuky November 2020) |

## Source Verification

[source record](../../sources/mitre/cspy-downloader.md)

## Evidence Excerpt

```text
created: '2020-11-09T14:30:35.202Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[CSPY Downloader](https://attack.mitre.org/software/S0527) is a tool designed to evade analysis and download
additional payloads used by [Kimsuky](https://attack.mitre.org/groups/G0094).(Citation: Cybereason Kimsuky November 2020)'
external_references:
- external_id: S0527
source_name: mitre-attack
url: https://attack.mitre.org/software/S0527
```
