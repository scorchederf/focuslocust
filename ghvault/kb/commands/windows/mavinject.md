---
parsed_by: focuslocust
source: commands
type: generated
---
# Mavinject Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Mavinject.exe

Tool page: [Mavinject.exe](../../tools/windows/mavinject.exe.md)

### Inject dll file into running process

```text
MavInject.exe 3110 /INJECTRUNNING {PATH_ABSOLUTE:.dll}
```

Description:

Inject evil.dll into a process with PID 3110.

Related ATT&CK:

- [T1218.013](../../attack/techniques/T1218.013-mavinject.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mavinject.yml` |
| Evidence | Command preserved from source parser. |

### Inject dll file into running process

```text
Mavinject.exe 4172 /INJECTRUNNING {PATH_ABSOLUTE}:file.dll
```

Description:

Inject file.dll stored as an Alternate Data Stream (ADS) into a process with PID 4172

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mavinject.yml` |
| Evidence | Command preserved from source parser. |
