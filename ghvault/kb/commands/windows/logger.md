---
parsed_by: focuslocust
source: commands
type: generated
---
# Logger Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Logger.exe

Tool page: [Logger.exe](../../tools/windows/logger.exe.md)

### Executes an abitrary command via a signed binary to evade detection.

```text
logger.exe RUN "{CMD}"
```

Description:

Executes the command specified after the `RUN` parameter as a child of `logger.exe`.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Logger.yml` |
| Evidence | Command preserved from source parser. |

### Executes an abitrary command via a signed binary to evade detection.

```text
logger.exe RUNW "{CMD}"
```

Description:

Executes the command specified after the `RUNW` parameter as a child of `logger.exe`.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Logger.yml` |
| Evidence | Command preserved from source parser. |

### Executes an abitrary command via a signed binary to evade detection.

```text
logger.exe "{CMD}"
```

Description:

Executes the command specified as a child of `logger.exe`.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Logger.yml` |
| Evidence | Command preserved from source parser. |
