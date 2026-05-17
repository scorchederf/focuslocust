---
parsed_by: focuslocust
source: commands
type: generated
---
# WFMFormat Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## WFMFormat.exe

Tool page: [WFMFormat.exe](../../tools/windows/wfmformat.exe.md)

### Proxy execution of binary

```text
WFMFormat.exe
```

Description:

Executes the file `tracerpt.exe` in the same folder as `WFMFormat.exe`. If the file `dumpfile.txt` (any content) exists in the current working directory, no arguments are required. Note that `WFMFormat.exe` requires .NET Framework 3.5.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/WFMFormat.yml` |
| Evidence | Command preserved from source parser. |
