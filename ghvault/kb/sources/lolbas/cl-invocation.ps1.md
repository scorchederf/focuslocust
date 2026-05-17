---
parsed_by: focuslocust
source: lolbas
type: generated
---
# CL_Invocation.ps1

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cl-invocation.ps1` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Cl_invocation.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CL_Invocation.ps1](../../tools/windows/cl-invocation.ps1.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cl-invocation.ps1 |
| name | CL_Invocation.ps1 |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@bohops'
  Person: Jimmy
- Handle: '@pabraeken'
  Person: Pierre-Alexandre Braeken
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: . C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1   \nSyncInvoke {CMD}
  Description: Import the PowerShell Diagnostic CL_Invocation script and call SyncInvoke to launch an executable.
  MitreID: T1216
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Proxy execution
Created: 2018-05-25
Description: Aero diagnostics script
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_cl_invocation.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_script/posh_ps_cl_invocation_lolscript.yml
Full_Path:
- Path: C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1
- Path: C:\Windows\diagnostics\system\Audio\CL_Invocation.ps1
- Path: C:\Windows\diagnostics\system\WindowsUpdate\CL_Invocation.ps1
Name: CL_Invocation.ps1
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Cl_invocation.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_script/posh_ps_cl_invocation_lolscript.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_cl_invocation.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_cl_invocation.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/powershell/powershell_script/posh_ps_cl_invocation_lolscript.yml
```
