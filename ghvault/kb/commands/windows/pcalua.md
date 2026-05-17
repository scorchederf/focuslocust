---
parsed_by: focuslocust
source: commands
type: generated
---
# Pcalua Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Pcalua.exe

Tool page: [Pcalua.exe](../../tools/windows/pcalua.exe.md)

### Proxy execution of binary

```text
pcalua.exe -a {PATH:.exe}
```

Description:

Open the target .EXE using the Program Compatibility Assistant.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pcalua.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution of remote dll file

```text
pcalua.exe -a {PATH_SMB:.dll}
```

Description:

Open the target .DLL file with the Program Compatibilty Assistant.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pcalua.yml` |
| Evidence | Command preserved from source parser. |

### Execution of CPL files

```text
pcalua.exe -a {PATH_ABSOLUTE:.cpl} -c Java
```

Description:

Open the target .CPL file with the Program Compatibility Assistant.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pcalua.yml` |
| Evidence | Command preserved from source parser. |
