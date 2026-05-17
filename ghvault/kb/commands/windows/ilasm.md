---
parsed_by: focuslocust
source: commands
type: generated
---
# Ilasm Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Ilasm.exe

Tool page: [Ilasm.exe](../../tools/windows/ilasm.exe.md)

### Compile attacker code on system. Bypass defensive counter measures.

```text
ilasm.exe {PATH_ABSOLUTE:.txt} /exe
```

Description:

Binary file used by .NET to compile C#/intermediate (IL) code to .exe

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ilasm.yml` |
| Evidence | Command preserved from source parser. |

### A description of the usecase

```text
ilasm.exe {PATH_ABSOLUTE:.txt} /dll
```

Description:

Binary file used by .NET to compile C#/intermediate (IL) code to dll

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ilasm.yml` |
| Evidence | Command preserved from source parser. |
