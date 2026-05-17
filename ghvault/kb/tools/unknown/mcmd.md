---
parsed_by: focuslocust
source: mitre
type: generated
---
# MCMD

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `mitre` |
| Type | `tool` |
| Record ID | `S0500` |
| Source file | `` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

MCMD is a remote access tool that provides remote command shell capability used by Dragonfly.

## Fast Retrieval

- Platform: `unknown`
- Command page: No command page generated from parsed source commands.
- Source verification: [source record](../../sources/mitre/mcmd.md)

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1005 - Data from Local System](../../attack/techniques/T1005-data-from-local-system.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) has the ability to upload files from an infected device.(Citation: Secureworks MCMD July 2019) |
| [T1027 - Obfuscated Files or Information](../../attack/techniques/T1027-obfuscated-files-or-information.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) can Base64 encode output strings prior to sending to C2.(Citation: Secureworks MCMD July 2019) |
| [T1036.005 - Match Legitimate Resource Name or Location](../../attack/techniques/T1036.005-match-legitimate-resource-name-or-location.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) has been named Readme.txt to appear legitimate.(Citation: Secureworks MCMD July 2019) |
| [T1053.005 - Scheduled Task](../../attack/techniques/T1053.005-scheduled-task.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) can use scheduled tasks for persistence.(Citation: Secureworks MCMD July 2019) |
| [T1059.003 - Windows Command Shell](../../attack/techniques/T1059.003-windows-command-shell.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) can launch a console process (cmd.exe) with redirected standard input and output.(Citation: Secureworks MCMD July 2019) |
| [T1070.009 - Clear Persistence](../../attack/techniques/T1070.009-clear-persistence.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) has the ability to remove set Registry Keys, including those used for persistence.(Citation: Secureworks MCMD July 2019) |
| [T1071.001 - Web Protocols](../../attack/techniques/T1071.001-web-protocols.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) can use HTTPS in communication with C2 web servers.(Citation: Secureworks MCMD July 2019) |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) can upload additional files to a compromised host.(Citation: Secureworks MCMD July 2019) |
| [T1547.001 - Registry Run Keys ／ Startup Folder](../../attack/techniques/T1547.001-registry-run-keys-startup-folder.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) can use Registry Run Keys for persistence.(Citation: Secureworks MCMD July 2019) |
| [T1564.003 - Hidden Window](../../attack/techniques/T1564.003-hidden-window.md) | explicit | source | [MCMD](https://attack.mitre.org/software/S0500) can modify processes to prevent them from being visible on the desktop.(Citation: Secureworks MCMD July 2019) |

## Source Verification

[source record](../../sources/mitre/mcmd.md)

## Evidence Excerpt

```text
created: '2020-08-13T17:15:25.702Z'
created_by_ref: identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5
description: '[MCMD](https://attack.mitre.org/software/S0500) is a remote access tool that provides remote command shell capability
used by [Dragonfly](https://attack.mitre.org/groups/G0035).(Citation: Secureworks MCMD July 2019)'
external_references:
- external_id: S0500
source_name: mitre-attack
url: https://attack.mitre.org/software/S0500
```
