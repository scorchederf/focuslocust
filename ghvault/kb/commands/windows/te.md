---
parsed_by: focuslocust
source: commands
type: generated
---
# te Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## te.exe

Tool page: [te.exe](../../tools/windows/te.exe.md)

### Execute Visual Basic script stored in local Windows Script Component file.

```text
te.exe {PATH:.wsc}
```

Description:

Run COM Scriptlets (e.g. VBScript) by calling a Windows Script Component (WSC) file.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Te.yml` |
| Evidence | Command preserved from source parser. |

### Execute DLL file.

```text
te.exe {PATH:.dll}
```

Description:

Execute commands from a DLL file with Test Authoring and Execution Framework (TAEF) tests. See resources section for required structures.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Te.yml` |
| Evidence | Command preserved from source parser. |
