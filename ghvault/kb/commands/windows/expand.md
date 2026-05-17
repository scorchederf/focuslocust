---
parsed_by: focuslocust
source: commands
type: generated
---
# Expand Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Expand.exe

Tool page: [Expand.exe](../../tools/windows/expand.exe.md)

### Use to copies the source file to the destination file

```text
expand {PATH_SMB:.bat} {PATH_ABSOLUTE:.bat}
```

Description:

Copies source file to destination.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Expand.yml` |
| Evidence | Command preserved from source parser. |

### Copies files from A to B

```text
expand {PATH_ABSOLUTE:.source.ext} {PATH_ABSOLUTE:.dest.ext}
```

Description:

Copies source file to destination.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Expand.yml` |
| Evidence | Command preserved from source parser. |

### Copies files from A to B

```text
expand {PATH_SMB:.bat} {PATH_ABSOLUTE}:file.bat
```

Description:

Copies source file to destination Alternate Data Stream (ADS)

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Expand.yml` |
| Evidence | Command preserved from source parser. |
