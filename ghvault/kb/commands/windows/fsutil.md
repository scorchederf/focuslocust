---
parsed_by: focuslocust
source: commands
type: generated
---
# Fsutil Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Fsutil.exe

Tool page: [Fsutil.exe](../../tools/windows/fsutil.exe.md)

### Can be used to forensically erase a file

```text
fsutil.exe file setZeroData offset=0 length=9999999999 {PATH_ABSOLUTE}
```

Description:

Zero out a file

Related ATT&CK:

- [T1485](../../attack/techniques/T1485-data-destruction.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Fsutil.yml` |
| Evidence | Command preserved from source parser. |

### Can be used to hide file creation activity

```text
fsutil.exe usn deletejournal /d c:
```

Description:

Delete the USN journal volume to hide file creation activity

Related ATT&CK:

- [T1485](../../attack/techniques/T1485-data-destruction.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Fsutil.yml` |
| Evidence | Command preserved from source parser. |

### Spawn a pre-planted executable from fsutil.exe.

```text
fsutil.exe trace decode
```

Description:

Executes a pre-planted binary named netsh.exe from the current directory.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Fsutil.yml` |
| Evidence | Command preserved from source parser. |
