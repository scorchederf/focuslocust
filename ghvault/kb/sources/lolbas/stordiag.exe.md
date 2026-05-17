---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Stordiag.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `stordiag.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Stordiag.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Stordiag.exe](../../tools/windows/stordiag.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | stordiag.exe |
| name | Stordiag.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/eral4m/status/1451112385041911809 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@eral4m'
  Person: Eral4m
- Handle: '@eki_erk'
  Person: Ekitji
Author: Eral4m
Commands:
- Category: Execute
  Command: stordiag.exe
  Description: Once executed, Stordiag.exe will execute schtasks.exe systeminfo.exe and fltmc.exe - if stordiag.exe is copied
    to a folder and an arbitrary executable is renamed to one of these names, stordiag.exe will execute it.
  MitreID: T1218
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Possible defence evasion purposes.
- Category: Execute
  Command: stordiag.exe
  Description: Once executed, Stordiag.exe will execute schtasks.exe and powershell.exe - if stordiag.exe is copied to a folder
    and an arbitrary executable is renamed to one of these names, stordiag.exe will execute it.
  MitreID: T1218
  OperatingSystem: Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Possible defence evasion purposes.
Created: 2021-10-21
Description: Storage diagnostic tool
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_stordiag_susp_child_process.yml
- IOC: systeminfo.exe, fltmc.exe or schtasks.exe or powershell.exe being executed outside of their normal path of c:\windows\system32\
    or c:\windows\syswow64\
Full_Path:
- Path: c:\windows\system32\stordiag.exe
- Path: c:\windows\syswow64\stordiag.exe
Name: Stordiag.exe
Resources:
- Link: https://twitter.com/eral4m/status/1451112385041911809
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Stordiag.yml
```

## Detection / Analysis Notes

```text
IOC: systeminfo.exe, fltmc.exe or schtasks.exe or powershell.exe being executed outside of their normal path of c:\windows\system32\ or c:\windows\syswow64\
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_stordiag_susp_child_process.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_stordiag_susp_child_process.yml
- IOC: systeminfo.exe, fltmc.exe or schtasks.exe or powershell.exe being executed outside of their normal path of c:\windows\system32\
    or c:\windows\syswow64\
```
