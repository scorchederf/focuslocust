---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Query.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `query.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Query.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Query.exe](../../tools/windows/query.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | query.exe |
| name | Query.exe |
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
  Command: query.exe user
  Description: Once executed, `query.exe` will execute `quser.exe` in the same folder. Thus, if `query.exe` is copied to a
    folder and an arbitrary executable is renamed to `quser.exe`, `query.exe` will spawn it. Instead of `user`, it is also
    possible to use `session`, `termsession` or `process` as command-line option.
  MitreID: T1218
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  - Requires: Rename
  Usecase: Execute an arbitrary executable via trusted system executable.
Created: 2025-07-31
Description: Remote Desktop Services MultiUser Query Utility
Detection:
- IOC: query.exe being executed and executes a child process outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\
Full_Path:
- Path: c:\windows\system32\query.exe
- Path: c:\windows\syswow64\query.exe
Name: Query.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Query.yml
```

## Detection / Analysis Notes

```text
IOC: query.exe being executed and executes a child process outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\
```

```text
- IOC: query.exe being executed and executes a child process outside of its normal path of c:\windows\system32\ or c:\windows\syswow64\
```
