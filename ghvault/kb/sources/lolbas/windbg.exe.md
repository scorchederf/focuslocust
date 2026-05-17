---
parsed_by: focuslocust
source: lolbas
type: generated
---
# WinDbg.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `windbg.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/WinDbg.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [WinDbg.exe](../../tools/windows/windbg.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | windbg.exe |
| name | WinDbg.exe |
| type | tool |
| source | lolbas |
| url | https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/windbg-command-line-options |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
  Command: windbg.exe -g {CMD}
  Description: Launches a command line through the debugging process; optionally add `-G` to exit the debugger automatically.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Executes an executable under a trusted microsoft signed binary.
Created: 2025-07-16
Description: Windows Debugger for advanced user-mode and kernel-mode debugging.
Full_Path:
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\windbg.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\arm\windbg.exe
- Path: C:\Program Files (x86)\Windows Kits\10\Debuggers\arm64\windbg.exe
Name: WinDbg.exe
Resources:
- Link: https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/windbg-command-line-options
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/WinDbg.yml
```
