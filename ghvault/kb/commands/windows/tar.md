---
parsed_by: focuslocust
source: commands
type: generated
---
# Tar Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Tar.exe

Tool page: [Tar.exe](../../tools/windows/tar.exe.md)

### Can be used to evade defensive countermeasures, or to hide as part of a persistence mechanism

```text
tar -cf {PATH}:ads {PATH_ABSOLUTE:folder}
```

Description:

Compress one or more files to an alternate data stream (ADS).

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Tar.yml` |
| Evidence | Command preserved from source parser. |

### Can be used to evade defensive countermeasures, or to hide as part of a persistence mechanism

```text
tar -xf {PATH}:ads
```

Description:

Decompress a compressed file from an alternate data stream (ADS).

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Tar.yml` |
| Evidence | Command preserved from source parser. |

### Copy files

```text
tar -xf {PATH_SMB:.tar}
```

Description:

Extracts archive.tar from the remote (internal) host to the current host.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Tar.yml` |
| Evidence | Command preserved from source parser. |
