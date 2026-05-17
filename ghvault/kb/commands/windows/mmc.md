---
parsed_by: focuslocust
source: commands
type: generated
---
# Mmc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Mmc.exe

Tool page: [Mmc.exe](../../tools/windows/mmc.exe.md)

### Configure a snap-in to load a COM custom class (CLSID) that has been added to the registry

```text
mmc.exe -Embedding {PATH_ABSOLUTE:.msc}
```

Description:

Launch a 'backgrounded' MMC process and invoke a COM payload

Related ATT&CK:

- [T1218.014](../../attack/techniques/T1218.014-mmc.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mmc.yml` |
| Evidence | Command preserved from source parser. |

### Modify HKCU\Environment key in Registry with COR profiler values then launch MMC to load the payload DLL.

```text
mmc.exe gpedit.msc
```

Description:

Load an arbitrary payload DLL by configuring COR Profiler registry settings and launching MMC to bypass UAC.

Related ATT&CK:

- [T1218.014](../../attack/techniques/T1218.014-mmc.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mmc.yml` |
| Evidence | Command preserved from source parser. |

### Download file from Internet

```text
mmc.exe -Embedding {PATH_ABSOLUTE:.msc}
```

Description:

Download and save an executable to disk

Related ATT&CK:

- [T1218.014](../../attack/techniques/T1218.014-mmc.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mmc.yml` |
| Evidence | Command preserved from source parser. |
