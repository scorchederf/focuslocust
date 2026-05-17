---
parsed_by: focuslocust
source: commands
type: generated
---
# Ttdinject Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Ttdinject.exe

Tool page: [Ttdinject.exe](../../tools/windows/ttdinject.exe.md)

### Spawn process using other binary

```text
TTDInject.exe /ClientParams "7 tmp.run 0 0 0 0 0 0 0 0 0 0" /Launch "{PATH:.exe}"
```

Description:

Execute a program using ttdinject.exe. Requires administrator privileges. A log file will be created in tmp.run. The log file can be changed, but the length (7) has to be updated.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ttdinject.yml` |
| Evidence | Command preserved from source parser. |

### Spawn process using other binary

```text
ttdinject.exe /ClientScenario TTDRecorder /ddload 0 /ClientParams "7 tmp.run 0 0 0 0 0 0 0 0 0 0" /launch "{PATH:.exe}"
```

Description:

Execute a program using ttdinject.exe. Requires administrator privileges. A log file will be created in tmp.run. The log file can be changed, but the length (7) has to be updated.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ttdinject.yml` |
| Evidence | Command preserved from source parser. |
