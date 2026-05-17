---
parsed_by: focuslocust
source: lolbas
type: generated
---
# IntelliTrace.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `intellitrace.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/IntelliTrace.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [IntelliTrace.exe](../../tools/windows/intellitrace.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | intellitrace.exe |
| name | IntelliTrace.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/visualstudio/debugger/intellitrace |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
  Command: IntelliTrace.exe launch /cp:"collectionplan.xml" /f:"c:\users\public\log" "C:\Windows\System32\calc.exe"
  Description: Launches an executable via Visual Studio command line utility.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Executes an executable under a trusted microsoft signed binary.
Created: 2025-09-21
Description: Visual Studio command-line tool for collecting and managing diagnostic trace files.
Full_Path:
- Path: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\IntelliTrace\IntelliTrace.exe
- Path: C:\Program Files (x86)\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\IntelliTrace\IntelliTrace.exe
Name: IntelliTrace.exe
Resources:
- Link: https://learn.microsoft.com/en-us/visualstudio/debugger/intellitrace
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/IntelliTrace.yml
```
