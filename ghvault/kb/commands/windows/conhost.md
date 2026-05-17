---
parsed_by: focuslocust
source: commands
type: generated
---
# Conhost Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Conhost.exe

Tool page: [Conhost.exe](../../tools/windows/conhost.exe.md)

### Use conhost.exe as a proxy binary to evade defensive counter-measures

```text
conhost.exe {CMD}
```

Description:

Execute a command line with conhost.exe as parent process

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Conhost.yml` |
| Evidence | Command preserved from source parser. |

### Specify --headless parameter to hide child process window (if applicable)

```text
conhost.exe --headless {CMD}
```

Description:

Execute a command line with conhost.exe as parent process

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Conhost.yml` |
| Evidence | Command preserved from source parser. |
