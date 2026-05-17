---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Powershell.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `powershell.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/PowerShell.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Powershell.exe](../../tools/windows/powershell.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | powershell.exe |
| name | Powershell.exe |
| type | tool |
| source | lolbas |
| url | https://attack.mitre.org/techniques/T1059/001/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@alltheoffensivecyberers'
  Person: Everyone
Author: Everyone
Commands:
- Category: Execute
  Command: powershell.exe -ep bypass -file c:\path\to\a\script.ps1
  Description: Set the execution policy to bypass and execute a PowerShell script without warning
  MitreID: T1059.001
  OperatingSystem: Windows 7 and up
  Privileges: User
  Usecase: Execute PowerShell cmdlets, .NET code, and just about anything else your heart desires
- Category: Execute
  Command: powershell.exe -ep bypass -command "Invoke-AllTheThings..."
  Description: Set the execution policy to bypass and execute a PowerShell command
  MitreID: T1059.001
  OperatingSystem: Windows 7 and up
  Privileges: User
  Usecase: Execute PowerShell cmdlets, .NET code, and just about anything else your heart desires
- Category: Execute
  Command: powershell.exe -ep bypass -ec IgBXAGUAIAA8ADMAIABMAE8ATABCAEEAUwAiAA==
  Description: Set the execution policy to bypass and execute a very malicious PowerShell encoded command
  MitreID: T1059.001
  OperatingSystem: Windows 7 and up
  Privileges: User
  Usecase: Execute PowerShell cmdlets, .NET code, and just about anything else your heart desires
Created: 2024-04-03
Description: Powershell.exe is a a task-based command-line shell built on .NET.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/tree/71ae004b32bb3c7fb04714f8a051fc8e5edda68c/rules/windows/powershell
Full_Path:
- Path: C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe
- Path: C:\Windows\SysWOW64\WindowsPowerShell\v1.0\powershell.exe
Name: Powershell.exe
Resources:
- Link: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_powershell_exe?view=powershell-5.1
- Link: https://attack.mitre.org/techniques/T1059/001/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/PowerShell.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/tree/71ae004b32bb3c7fb04714f8a051fc8e5edda68c/rules/windows/powershell
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/tree/71ae004b32bb3c7fb04714f8a051fc8e5edda68c/rules/windows/powershell
```
