---
parsed_by: focuslocust
source: commands
type: generated
---
# Runonce Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Runonce.exe

Tool page: [Runonce.exe](../../tools/windows/runonce.exe.md)

### Persistence, bypassing defensive counter measures

```text
Runonce.exe /AlternateShellStartup
```

Description:

Executes a Run Once Task that has been configured in the registry.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Runonce.yml` |
| Evidence | Command preserved from source parser. |
