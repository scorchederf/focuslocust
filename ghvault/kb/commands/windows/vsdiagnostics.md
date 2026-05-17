---
parsed_by: focuslocust
source: commands
type: generated
---
# VSDiagnostics Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## VSDiagnostics.exe

Tool page: [VSDiagnostics.exe](../../tools/windows/vsdiagnostics.exe.md)

### Proxy execution of binary

```text
VSDiagnostics.exe start 1 /launch:{PATH:.exe}
```

Description:

Starts a collection session with sessionID 1 and calls kernelbase.CreateProcessW to launch specified executable.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VSDiagnostics.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution of binary with arguments

```text
VSDiagnostics.exe start 2 /launch:{PATH:.exe} /launchArgs:"{CMD:args}"
```

Description:

Starts a collection session with sessionID 2 and calls kernelbase.CreateProcessW to launch specified executable. Arguments specified in launchArgs are passed to CreateProcessW.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VSDiagnostics.yml` |
| Evidence | Command preserved from source parser. |
