---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Logger.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `logger.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Logger.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Logger.exe](../../tools/windows/logger.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | logger.exe |
| name | Logger.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/logger |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
  Command: logger.exe RUN "{CMD}"
  Description: Executes the command specified after the `RUN` parameter as a child of `logger.exe`.
  MitreID: T1202
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Executes an abitrary command via a signed binary to evade detection.
- Category: Execute
  Command: logger.exe RUNW "{CMD}"
  Description: Executes the command specified after the `RUNW` parameter as a child of `logger.exe`.
  MitreID: T1202
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Executes an abitrary command via a signed binary to evade detection.
- Category: Execute
  Command: logger.exe "{CMD}"
  Description: Executes the command specified as a child of `logger.exe`.
  MitreID: T1202
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Executes an abitrary command via a signed binary to evade detection.
Created: 2025-07-13
Description: A logging configuration tool from the Windows Kits used to start and manage process logging.
Full_Path:
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\logger.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\logger.exe
- Path: C:\Program Files\Windows Kits\10\Debuggers\x86\logger.exe
- Path: C:\Program Files\Windows Kits\10\Debuggers\x64\logger.exe
Name: Logger.exe
Resources:
- Link: https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/logger
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Logger.yml
```
