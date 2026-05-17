---
parsed_by: focuslocust
source: lolbas
type: generated
---
# XBootMgr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `xbootmgr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/XBootMgr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [XBootMgr.exe](../../tools/windows/xbootmgr.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | xbootmgr.exe |
| name | XBootMgr.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/previous-versions/windows/desktop/xperf/reference |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
- Person: Tommy Warren
Author: Avihay Eldad
Commands:
- Category: Execute
  Command: xbootmgr.exe -trace "{boot|hibernate|standby|shutdown|rebootCycle}" -callBack {PATH:.exe}
  Description: Executes an executable after the trace is complete using the callBack parameter.
  MitreID: T1202
  OperatingSystem: Windows
  Privileges: Administrator
  Tags:
  - Execute: EXE
  Usecase: Executes code as part of post-trace automation flow.
- Category: Execute
  Command: xbootmgr.exe -trace "{boot|hibernate|standby|shutdown|rebootCycle}" -preTraceCmd {PATH:.exe}
  Description: Executes an executable before each trace run using the preTraceCmd parameter.
  MitreID: T1202
  OperatingSystem: Windows
  Privileges: Administrator
  Tags:
  - Execute: EXE
  Usecase: Executes code as part of pre-trace automation or staging.
Created: 2025-07-10
Description: Windows Performance Toolkit binary used to start performance traces.
Full_Path:
- Path: C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgr.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\xbootmgr.exe
Name: XBootMgr.exe
Resources:
- Link: https://learn.microsoft.com/en-us/previous-versions/windows/desktop/xperf/reference
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/XBootMgr.yml
```
