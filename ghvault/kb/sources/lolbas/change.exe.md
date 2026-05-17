---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Change.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `change.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Change.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Change.exe](../../tools/windows/change.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | change.exe |
| name | Change.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@IdanLerman'
  Person: Idan Lerman
Author: Idan Lerman
Commands:
- Category: Execute
  Command: change.exe user
  Description: Once executed, `change.exe` will execute `chgusr.exe` in the same folder. Thus, if `change.exe` is copied to
    a folder and an arbitrary executable is renamed to `chgusr.exe`, `change.exe` will spawn it. Instead of `user`, it is
    also possible to use `port` or `logon` as command-line option.
  MitreID: T1218
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  - Requires: Rename
  Usecase: Execute an arbitrary executable via trusted system executable.
Created: 2025-07-31
Description: Remote Desktop Services MultiUser Change Utility
Detection:
- IOC: change.exe being executed and executes a child process outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\
Full_Path:
- Path: c:\windows\system32\change.exe
- Path: c:\windows\syswow64\change.exe
Name: Change.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Change.yml
```

## Detection / Analysis Notes

```text
IOC: change.exe being executed and executes a child process outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\
```

```text
- IOC: change.exe being executed and executes a child process outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\
```
