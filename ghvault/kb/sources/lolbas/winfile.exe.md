---
parsed_by: focuslocust
source: lolbas
type: generated
---
# winfile.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `winfile.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/winfile.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [winfile.exe](../../tools/windows/winfile.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | winfile.exe |
| name | winfile.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/microsoft/winfile |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
  Command: winfile.exe {PATH:.exe}
  Description: Execute an executable file with WinFile as a parent process.
  MitreID: T1202
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Performs execution of specified file, can be used as a defense evasion
Created: 2024-04-30
Description: Windows File Manager executable
Full_Path:
- Path: C:\Windows\System32\winfile.exe
- Path: C:\Windows\winfile.exe
- Path: C:\Program Files\WinFile\winfile.exe
- Path: C:\Program Files (x86)\WinFile\winfile.exe
- Path: C:\Program Files\WindowsApps\Microsoft.WindowsFileManager_10.3.0.0_x64__8wekyb3d8bbwe\WinFile\winfile.exe
Name: winfile.exe
Resources:
- Link: https://github.com/microsoft/winfile
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/winfile.yml
```
