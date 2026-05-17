---
parsed_by: focuslocust
source: commands
type: generated
---
# vbc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## vbc.exe

Tool page: [vbc.exe](../../tools/windows/vbc.exe.md)

### Compile attacker code on system. Bypass defensive counter measures.

```text
vbc.exe /target:exe {PATH_ABSOLUTE:.vb}
```

Description:

Binary file used by .NET to compile Visual Basic code to an executable.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Vbc.yml` |
| Evidence | Command preserved from source parser. |

### Compile attacker code on system. Bypass defensive counter measures.

```text
vbc -reference:Microsoft.VisualBasic.dll {PATH_ABSOLUTE:.vb}
```

Description:

Binary file used by .NET to compile Visual Basic code to an executable.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Vbc.yml` |
| Evidence | Command preserved from source parser. |
