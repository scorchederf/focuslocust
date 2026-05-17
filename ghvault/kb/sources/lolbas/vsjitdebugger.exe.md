---
parsed_by: focuslocust
source: lolbas
type: generated
---
# vsjitdebugger.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vsjitdebugger.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Vsjitdebugger.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [vsjitdebugger.exe](../../tools/windows/vsjitdebugger.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | vsjitdebugger.exe |
| name | vsjitdebugger.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/pabraeken/status/990758590020452353 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@pabraeken'
  Person: Pierre-Alexandre Braeken
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: Vsjitdebugger.exe {PATH:.exe}
  Description: Executes specified executable as a subprocess of Vsjitdebugger.exe.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Execution of local PE file as a subprocess of Vsjitdebugger.exe.
Created: 2018-05-25
Description: Just-In-Time (JIT) debugger included with Visual Studio
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_use_of_vsjitdebugger_bin.yml
Full_Path:
- Path: c:\windows\system32\vsjitdebugger.exe
Name: vsjitdebugger.exe
Resources:
- Link: https://twitter.com/pabraeken/status/990758590020452353
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Vsjitdebugger.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_use_of_vsjitdebugger_bin.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_use_of_vsjitdebugger_bin.yml
```
