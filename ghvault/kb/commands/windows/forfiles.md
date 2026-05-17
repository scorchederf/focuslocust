---
parsed_by: focuslocust
source: commands
type: generated
---
# Forfiles Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Forfiles.exe

Tool page: [Forfiles.exe](../../tools/windows/forfiles.exe.md)

### Use forfiles to start a new process to evade defensive counter measures

```text
forfiles /p c:\windows\system32 /m notepad.exe /c "{CMD}"
```

Description:

Executes specified command since there is a match for notepad.exe in the c:\windows\System32 folder.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Forfiles.yml` |
| Evidence | Command preserved from source parser. |

### Use forfiles to start a new process from a binary hidden in an alternate data stream

```text
forfiles /p c:\windows\system32 /m notepad.exe /c "{PATH_ABSOLUTE}:evil.exe"
```

Description:

Executes the evil.exe Alternate Data Stream (AD) since there is a match for notepad.exe in the c:\windows\system32 folder.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Forfiles.yml` |
| Evidence | Command preserved from source parser. |
