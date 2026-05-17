---
parsed_by: focuslocust
source: lolbas
type: generated
---
# te.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `te.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Te.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [te.exe](../../tools/windows/te.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | te.exe |
| name | te.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/LOLBAS-Project/LOLBAS/pull/359 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@gN3mes1s'
  Person: Giuseppe N3mes1s
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: te.exe {PATH:.wsc}
  Description: Run COM Scriptlets (e.g. VBScript) by calling a Windows Script Component (WSC) file.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: WSH
  Usecase: Execute Visual Basic script stored in local Windows Script Component file.
- Category: Execute
  Command: te.exe {PATH:.dll}
  Description: Execute commands from a DLL file with Test Authoring and Execution Framework (TAEF) tests. See resources section
    for required structures.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: DLL
  - Input: Custom Format
  Usecase: Execute DLL file.
Created: 2018-05-25
Description: Testing tool included with Microsoft Test Authoring and Execution Framework (TAEF).
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_use_of_te_bin.yml
Full_Path:
- Path: no default
Name: te.exe
Resources:
- Link: https://twitter.com/gn3mes1s/status/927680266390384640
- Link: https://github.com/LOLBAS-Project/LOLBAS/pull/359
- Link: https://learn.microsoft.com/en-us/windows-hardware/drivers/taef/authoring-tests
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Te.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_use_of_te_bin.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_use_of_te_bin.yml
```
