---
parsed_by: focuslocust
source: commands
type: generated
---
# Powershell Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Powershell.exe

Tool page: [Powershell.exe](../../tools/windows/powershell.exe.md)

### Execute PowerShell cmdlets, .NET code, and just about anything else your heart desires

```text
powershell.exe -ep bypass -file c:\path\to\a\script.ps1
```

Description:

Set the execution policy to bypass and execute a PowerShell script without warning

Related ATT&CK:

- [T1059.001](../../attack/techniques/T1059.001-powershell.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/PowerShell.yml` |
| Evidence | Command preserved from source parser. |

### Execute PowerShell cmdlets, .NET code, and just about anything else your heart desires

```text
powershell.exe -ep bypass -command "Invoke-AllTheThings..."
```

Description:

Set the execution policy to bypass and execute a PowerShell command

Related ATT&CK:

- [T1059.001](../../attack/techniques/T1059.001-powershell.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/PowerShell.yml` |
| Evidence | Command preserved from source parser. |

### Execute PowerShell cmdlets, .NET code, and just about anything else your heart desires

```text
powershell.exe -ep bypass -ec IgBXAGUAIAA8ADMAIABMAE8ATABCAEEAUwAiAA==
```

Description:

Set the execution policy to bypass and execute a very malicious PowerShell encoded command

Related ATT&CK:

- [T1059.001](../../attack/techniques/T1059.001-powershell.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/PowerShell.yml` |
| Evidence | Command preserved from source parser. |
