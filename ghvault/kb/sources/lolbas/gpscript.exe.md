---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Gpscript.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `gpscript.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Gpscript.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Gpscript.exe](../../tools/windows/gpscript.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | gpscript.exe |
| name | Gpscript.exe |
| type | tool |
| source | lolbas |
| url | https://oddvar.moe/2018/04/27/gpscript-exe-another-lolbin-to-the-list/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@oddvarmoe'
  Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: Gpscript /logon
  Description: Executes logon scripts configured in Group Policy.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: CMD
  Usecase: Add local group policy logon script to execute file and hide from defensive counter measures
- Category: Execute
  Command: Gpscript /startup
  Description: Executes startup scripts configured in Group Policy
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: Administrator
  Tags:
  - Execute: CMD
  Usecase: Add local group policy logon script to execute file and hide from defensive counter measures
Created: 2018-05-25
Description: Used by group policy to process scripts
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_gpscript.yml
- IOC: Scripts added in local group policy
- IOC: Execution of Gpscript.exe after logon
Full_Path:
- Path: C:\Windows\System32\gpscript.exe
- Path: C:\Windows\SysWOW64\gpscript.exe
Name: Gpscript.exe
Resources:
- Link: https://oddvar.moe/2018/04/27/gpscript-exe-another-lolbin-to-the-list/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Gpscript.yml
```

## Detection / Analysis Notes

```text
IOC: Execution of Gpscript.exe after logon
```

```text
IOC: Scripts added in local group policy
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_gpscript.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_gpscript.yml
- IOC: Scripts added in local group policy
- IOC: Execution of Gpscript.exe after logon
```
