---
parsed_by: focuslocust
source: commands
type: generated
---
# CL_Invocation.ps1 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## CL_Invocation.ps1

Tool page: [CL_Invocation.ps1](../../tools/windows/cl-invocation.ps1.md)

### Proxy execution

```text
. C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1   \nSyncInvoke {CMD}
```

Description:

Import the PowerShell Diagnostic CL_Invocation script and call SyncInvoke to launch an executable.

Related ATT&CK:

- [T1216](../../attack/techniques/T1216-system-script-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Cl_invocation.yml` |
| Evidence | Command preserved from source parser. |
