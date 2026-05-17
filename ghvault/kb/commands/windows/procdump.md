---
parsed_by: focuslocust
source: commands
type: generated
---
# Procdump Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Procdump.exe

Tool page: [Procdump.exe](../../tools/windows/procdump.exe.md)

### Performs execution of unsigned DLL.

```text
procdump.exe -md {PATH:.dll} explorer.exe
```

Description:

Loads the specified DLL where DLL is configured with a 'MiniDumpCallbackRoutine' exported function. Valid process must be provided as dump still created.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Procdump.yml` |
| Evidence | Command preserved from source parser. |

### Performs execution of unsigned DLL.

```text
procdump.exe -md {PATH:.dll} foobar
```

Description:

Loads the specified DLL where configured with DLL_PROCESS_ATTACH execution, process argument can be arbitrary.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Procdump.yml` |
| Evidence | Command preserved from source parser. |
