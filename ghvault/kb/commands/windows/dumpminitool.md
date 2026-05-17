---
parsed_by: focuslocust
source: commands
type: generated
---
# DumpMinitool Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## DumpMinitool.exe

Tool page: [DumpMinitool.exe](../../tools/windows/dumpminitool.exe.md)

### Create memory dump and parse it offline

```text
DumpMinitool.exe --file {PATH_ABSOLUTE} --processId 1132 --dumpType Full
```

Description:

Creates a memory dump of the lsass process

Related ATT&CK:

- [T1003.001](../../attack/techniques/T1003.001-lsass-memory.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/DumpMinitool.yml` |
| Evidence | Command preserved from source parser. |
