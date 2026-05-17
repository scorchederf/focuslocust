---
parsed_by: focuslocust
source: commands
type: generated
---
# vsjitdebugger Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## vsjitdebugger.exe

Tool page: [vsjitdebugger.exe](../../tools/windows/vsjitdebugger.exe.md)

### Execution of local PE file as a subprocess of Vsjitdebugger.exe.

```text
Vsjitdebugger.exe {PATH:.exe}
```

Description:

Executes specified executable as a subprocess of Vsjitdebugger.exe.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Vsjitdebugger.yml` |
| Evidence | Command preserved from source parser. |
