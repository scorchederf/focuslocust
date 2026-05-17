---
parsed_by: focuslocust
source: commands
type: generated
---
# Makecab Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Makecab.exe

Tool page: [Makecab.exe](../../tools/windows/makecab.exe.md)

### Hide data compressed into an alternate data stream

```text
makecab {PATH_ABSOLUTE:.exe} {PATH_ABSOLUTE}:autoruns.cab
```

Description:

Compresses the target file into a CAB file stored in the Alternate Data Stream (ADS) of the target file.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Makecab.yml` |
| Evidence | Command preserved from source parser. |

### Hide data compressed into an alternate data stream

```text
makecab {PATH_SMB:.exe} {PATH_ABSOLUTE}:file.cab
```

Description:

Compresses the target file into a CAB file stored in the Alternate Data Stream (ADS) of the target file.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Makecab.yml` |
| Evidence | Command preserved from source parser. |

### Download file and compress into a cab file

```text
makecab {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab}
```

Description:

Download and compresses the target file and stores it in the target file.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Makecab.yml` |
| Evidence | Command preserved from source parser. |

### Bypass command-line based detections

```text
makecab /F {PATH:.ddf}
```

Description:

Execute makecab commands as defined in the specified Diamond Definition File (.ddf); see resources for the format specification.

Related ATT&CK:

- [T1036](../../attack/techniques/T1036-masquerading.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Makecab.yml` |
| Evidence | Command preserved from source parser. |
