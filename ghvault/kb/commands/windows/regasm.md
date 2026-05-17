---
parsed_by: focuslocust
source: commands
type: generated
---
# Regasm Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Regasm.exe

Tool page: [Regasm.exe](../../tools/windows/regasm.exe.md)

### Execute code and bypass Application whitelisting

```text
regasm.exe {PATH:.dll}
```

Description:

Loads the target .NET DLL file and executes the RegisterClass function.

Related ATT&CK:

- [T1218.009](../../attack/techniques/T1218.009-regsvcs-regasm.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regasm.yml` |
| Evidence | Command preserved from source parser. |

### Execute code and bypass Application whitelisting

```text
regasm.exe /U {PATH:.dll}
```

Description:

Loads the target .DLL file and executes the UnRegisterClass function.

Related ATT&CK:

- [T1218.009](../../attack/techniques/T1218.009-regsvcs-regasm.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regasm.yml` |
| Evidence | Command preserved from source parser. |
