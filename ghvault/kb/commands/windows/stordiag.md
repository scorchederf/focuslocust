---
parsed_by: focuslocust
source: commands
type: generated
---
# Stordiag Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Stordiag.exe

Tool page: [Stordiag.exe](../../tools/windows/stordiag.exe.md)

### Possible defence evasion purposes.

```text
stordiag.exe
```

Description:

Once executed, Stordiag.exe will execute schtasks.exe systeminfo.exe and fltmc.exe - if stordiag.exe is copied to a folder and an arbitrary executable is renamed to one of these names, stordiag.exe will execute it.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Stordiag.yml` |
| Evidence | Command preserved from source parser. |

### Possible defence evasion purposes.

```text
stordiag.exe
```

Description:

Once executed, Stordiag.exe will execute schtasks.exe and powershell.exe - if stordiag.exe is copied to a folder and an arbitrary executable is renamed to one of these names, stordiag.exe will execute it.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Stordiag.yml` |
| Evidence | Command preserved from source parser. |
