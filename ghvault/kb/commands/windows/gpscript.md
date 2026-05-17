---
parsed_by: focuslocust
source: commands
type: generated
---
# Gpscript Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Gpscript.exe

Tool page: [Gpscript.exe](../../tools/windows/gpscript.exe.md)

### Add local group policy logon script to execute file and hide from defensive counter measures

```text
Gpscript /logon
```

Description:

Executes logon scripts configured in Group Policy.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Gpscript.yml` |
| Evidence | Command preserved from source parser. |

### Add local group policy logon script to execute file and hide from defensive counter measures

```text
Gpscript /startup
```

Description:

Executes startup scripts configured in Group Policy

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Gpscript.yml` |
| Evidence | Command preserved from source parser. |
