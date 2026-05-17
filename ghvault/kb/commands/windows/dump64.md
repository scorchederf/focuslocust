---
parsed_by: focuslocust
source: commands
type: generated
---
# Dump64 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Dump64.exe

Tool page: [Dump64.exe](../../tools/windows/dump64.exe.md)

### Create memory dump and parse it offline to retrieve credentials.

```text
dump64.exe {PID} out.dmp
```

Description:

Creates a memory dump of the LSASS process.

Related ATT&CK:

- [T1003.001](../../attack/techniques/T1003.001-lsass-memory.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dump64.yml` |
| Evidence | Command preserved from source parser. |
