---
parsed_by: focuslocust
source: commands
type: generated
---
# CL_Mutexverifiers.ps1 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## CL_Mutexverifiers.ps1

Tool page: [CL_Mutexverifiers.ps1](../../tools/windows/cl-mutexverifiers.ps1.md)

### Proxy execution

```text
. C:\Windows\diagnostics\system\AERO\CL_Mutexverifiers.ps1   \nrunAfterCancelProcess {PATH:.ps1}
```

Description:

Import the PowerShell Diagnostic CL_Mutexverifiers script and call runAfterCancelProcess to launch an executable.

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/CL_mutexverifiers.yml` |
| Evidence | Command preserved from source parser. |
