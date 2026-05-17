---
parsed_by: focuslocust
source: lolbas
type: generated
---
# CL_Mutexverifiers.ps1

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cl-mutexverifiers.ps1` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/CL_mutexverifiers.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CL_Mutexverifiers.ps1](../../tools/windows/cl-mutexverifiers.ps1.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cl-mutexverifiers.ps1 |
| name | CL_Mutexverifiers.ps1 |
| type | tool |
| source | lolbas |
| url | https://twitter.com/pabraeken/status/995111125447577600 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@pabraeken'
  Person: Pierre-Alexandre Braeken
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: . C:\Windows\diagnostics\system\AERO\CL_Mutexverifiers.ps1   \nrunAfterCancelProcess {PATH:.ps1}
  Description: Import the PowerShell Diagnostic CL_Mutexverifiers script and call runAfterCancelProcess to launch an executable.
  MitreID: T1216
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: PowerShell
  Usecase: Proxy execution
Created: 2018-05-25
Description: Proxy execution with CL_Mutexverifiers.ps1
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_cl_mutexverifiers.yml
Full_Path:
- Path: C:\Windows\diagnostics\system\WindowsUpdate\CL_Mutexverifiers.ps1
- Path: C:\Windows\diagnostics\system\Audio\CL_Mutexverifiers.ps1
- Path: C:\Windows\diagnostics\system\WindowsUpdate\CL_Mutexverifiers.ps1
- Path: C:\Windows\diagnostics\system\Video\CL_Mutexverifiers.ps1
- Path: C:\Windows\diagnostics\system\Speech\CL_Mutexverifiers.ps1
Name: CL_Mutexverifiers.ps1
Resources:
- Link: https://twitter.com/pabraeken/status/995111125447577600
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/CL_mutexverifiers.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_cl_mutexverifiers.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_cl_mutexverifiers.yml
```
