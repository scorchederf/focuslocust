---
parsed_by: focuslocust
source: commands
type: generated
---
# Extexport Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Extexport.exe

Tool page: [Extexport.exe](../../tools/windows/extexport.exe.md)

### Execute dll file

```text
Extexport.exe {PATH_ABSOLUTE:folder} foo bar
```

Description:

Load a DLL located in the specified folder with one of the following names mozcrt19.dll, mozsqlite3.dll, or sqlite.dll.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Extexport.yml` |
| Evidence | Command preserved from source parser. |
