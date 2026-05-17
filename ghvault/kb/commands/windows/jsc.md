---
parsed_by: focuslocust
source: commands
type: generated
---
# Jsc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Jsc.exe

Tool page: [Jsc.exe](../../tools/windows/jsc.exe.md)

### Compile attacker code on system. Bypass defensive counter measures.

```text
jsc.exe {PATH:.js}
```

Description:

Use jsc.exe to compile JavaScript code stored in the provided .JS file and generate a .EXE file with the same name.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Jsc.yml` |
| Evidence | Command preserved from source parser. |

### Compile attacker code on system. Bypass defensive counter measures.

```text
jsc.exe /t:library {PATH:.js}
```

Description:

Use jsc.exe to compile JavaScript code stored in the .JS file and generate a DLL file with the same name.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Jsc.yml` |
| Evidence | Command preserved from source parser. |
