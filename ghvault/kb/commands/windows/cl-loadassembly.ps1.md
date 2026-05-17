---
parsed_by: focuslocust
source: commands
type: generated
---
# CL_LoadAssembly.ps1 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## CL_LoadAssembly.ps1

Tool page: [CL_LoadAssembly.ps1](../../tools/windows/cl-loadassembly.ps1.md)

### Execute proxied payload with Microsoft signed binary

```text
powershell.exe -ep bypass -command "set-location -path C:\Windows\diagnostics\system\Audio; import-module .\CL_LoadAssembly.ps1; LoadAssemblyFromPath ..\..\..\..\testing\fun.dll;[Program]::Fun()"
```

Description:

Proxy execute Managed DLL with PowerShell

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/CL_LoadAssembly.yml` |
| Evidence | Command preserved from source parser. |
