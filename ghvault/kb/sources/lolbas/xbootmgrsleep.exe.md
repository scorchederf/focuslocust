---
parsed_by: focuslocust
source: lolbas
type: generated
---
# XBootMgrSleep.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `xbootmgrsleep.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/XBootMgrSleep.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [XBootMgrSleep.exe](../../tools/windows/xbootmgrsleep.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | xbootmgrsleep.exe |
| name | XBootMgrSleep.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/previous-versions/windows/desktop/xperf/reference |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
- Handle: '@yuvalsaban3'
  Person: Yuval Saban
Author: Avihay Eldad
Commands:
- Category: Execute
  Command: xbootmgrsleep.exe 1000 {PATH:.exe}
  Description: Execute executable via XBootMgrSleep, with a 1 second (=1000 milliseconds) delay. Alternatively, it is also
    possible to replace the delay with any string for immediate execution.
  MitreID: T1202
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Performs execution of specified executable, can be used as a defense evasion
Created: 2024-06-13
Description: Windows Performance Toolkit binary used for tracing and analyzing system performance during sleep and resume
  transitions.
Full_Path:
- Path: C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgrsleep.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\xbootmgrsleep.exe
Name: XBootMgrSleep.exe
Resources:
- Link: https://learn.microsoft.com/en-us/previous-versions/windows/desktop/xperf/reference
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/XBootMgrSleep.yml
```
