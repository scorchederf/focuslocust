---
parsed_by: focuslocust
source: commands
type: generated
---
# Fsi Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Fsi.exe

Tool page: [Fsi.exe](../../tools/windows/fsi.exe.md)

### Execute payload with Microsoft signed binary to bypass WDAC policies

```text
fsi.exe {PATH:.fsscript}
```

Description:

Execute F# code via script file

Related ATT&CK:

- [T1059](../../attack/techniques/T1059-command-and-scripting-interpreter.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Fsi.yml` |
| Evidence | Command preserved from source parser. |

### Execute payload with Microsoft signed binary to bypass WDAC policies

```text
fsi.exe
```

Description:

Execute F# code via interactive command line

Related ATT&CK:

- [T1059](../../attack/techniques/T1059-command-and-scripting-interpreter.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Fsi.yml` |
| Evidence | Command preserved from source parser. |
