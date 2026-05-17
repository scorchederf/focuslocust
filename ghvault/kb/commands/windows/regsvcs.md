---
parsed_by: focuslocust
source: commands
type: generated
---
# Regsvcs Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Regsvcs.exe

Tool page: [Regsvcs.exe](../../tools/windows/regsvcs.exe.md)

### Execute dll file and bypass Application whitelisting

```text
regsvcs.exe {PATH:.dll}
```

Description:

Loads the target .NET DLL file and executes the RegisterClass function.

Related ATT&CK:

- [T1218.009](../../attack/techniques/T1218.009-regsvcs-regasm.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvcs.yml` |
| Evidence | Command preserved from source parser. |

### Execute dll file and bypass Application whitelisting

```text
regsvcs.exe {PATH:.dll}
```

Description:

Loads the target .NET DLL file and executes the RegisterClass function.

Related ATT&CK:

- [T1218.009](../../attack/techniques/T1218.009-regsvcs-regasm.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regsvcs.yml` |
| Evidence | Command preserved from source parser. |
