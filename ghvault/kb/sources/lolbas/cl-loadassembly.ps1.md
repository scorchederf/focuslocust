---
parsed_by: focuslocust
source: lolbas
type: generated
---
# CL_LoadAssembly.ps1

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cl-loadassembly.ps1` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/CL_LoadAssembly.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [CL_LoadAssembly.ps1](../../tools/windows/cl-loadassembly.ps1.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cl-loadassembly.ps1 |
| name | CL_LoadAssembly.ps1 |
| type | tool |
| source | lolbas |
| url | https://bohops.com/2018/01/07/executing-commands-and-bypassing-applocker-with-powershell-diagnostic-scripts/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@bohops'
  Person: Jimmy
Author: Jimmy (@bohops)
Commands:
- Category: Execute
  Command: powershell.exe -ep bypass -command "set-location -path C:\Windows\diagnostics\system\Audio; import-module .\CL_LoadAssembly.ps1;
    LoadAssemblyFromPath ..\..\..\..\testing\fun.dll;[Program]::Fun()"
  Description: Proxy execute Managed DLL with PowerShell
  MitreID: T1216
  OperatingSystem: Windows 10 21H1 (likely other versions as well), Windows 11
  Privileges: User
  Tags:
  - Execute: DLL (.NET)
  Usecase: Execute proxied payload with Microsoft signed binary
Created: 2021-09-26
Description: PowerShell Diagnostic Script
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff6c54ded6b52f379cec11fe17c1ccb956faa660/rules/windows/process_creation/proc_creation_win_lolbas_cl_loadassembly.yml
Full_Path:
- Path: C:\Windows\diagnostics\system\Audio\CL_LoadAssembly.ps1
Name: CL_LoadAssembly.ps1
Resources:
- Link: https://bohops.com/2018/01/07/executing-commands-and-bypassing-applocker-with-powershell-diagnostic-scripts/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/CL_LoadAssembly.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/ff6c54ded6b52f379cec11fe17c1ccb956faa660/rules/windows/process_creation/proc_creation_win_lolbas_cl_loadassembly.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/ff6c54ded6b52f379cec11fe17c1ccb956faa660/rules/windows/process_creation/proc_creation_win_lolbas_cl_loadassembly.yml
```
