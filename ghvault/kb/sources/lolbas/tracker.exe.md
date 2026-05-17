---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Tracker.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `tracker.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Tracker.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Tracker.exe](../../tools/windows/tracker.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | tracker.exe |
| name | Tracker.exe |
| type | tool |
| source | lolbas |
| url | https://attack.mitre.org/wiki/Execution |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subTee'
  Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe
  Description: Use tracker.exe to proxy execution of an arbitrary DLL into another process. Since tracker.exe is also signed
    it can be used to bypass application whitelisting solutions.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Injection of locally stored DLL file into target process.
- Category: AWL Bypass
  Command: Tracker.exe /d {PATH:.dll} /c C:\Windows\write.exe
  Description: Use tracker.exe to proxy execution of an arbitrary DLL into another process. Since tracker.exe is also signed
    it can be used to bypass application whitelisting solutions.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: DLL
  Usecase: Injection of locally stored DLL file into target process.
Created: 2018-05-25
Description: Tool included with Microsoft .Net Framework.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_tracker.yml
Full_Path:
- Path: no default
Name: Tracker.exe
Resources:
- Link: https://twitter.com/subTee/status/793151392185589760
- Link: https://attack.mitre.org/wiki/Execution
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Tracker.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_tracker.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_tracker.yml
```
