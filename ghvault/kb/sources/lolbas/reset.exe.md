---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Reset.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `reset.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Reset.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Reset.exe](../../tools/windows/reset.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | reset.exe |
| name | Reset.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@Bl4ckShad3'
  Person: Matan Bahar
Author: Matan Bahar
Commands:
- Category: Execute
  Command: reset.exe session
  Description: Once executed, `reset.exe` will execute `rwinsta.exe` in the same folder. Thus, if `reset.exe` is copied to
    a folder and an arbitrary executable is renamed to `rwinsta.exe`, `reset.exe` will spawn it.
  MitreID: T1218
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  - Requires: Rename
  Usecase: Execute an arbitrary executable via trusted system executable.
Created: 2025-07-31
Description: Remote Desktop Services Reset Utility
Detection:
- IOC: reset.exe being executed and executes rwinsta.exe outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\
Full_Path:
- Path: c:\windows\system32\reset.exe
- Path: c:\windows\syswow64\reset.exe
Name: Reset.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Reset.yml
```

## Detection / Analysis Notes

```text
IOC: reset.exe being executed and executes rwinsta.exe outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\
```

```text
- IOC: reset.exe being executed and executes rwinsta.exe outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\
```
