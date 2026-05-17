---
parsed_by: focuslocust
source: commands
type: generated
---
# Wfc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Wfc.exe

Tool page: [Wfc.exe](../../tools/windows/wfc.exe.md)

### Execute proxied payload with Microsoft signed binary to bypass WDAC policies

```text
wfc.exe {PATH_ABSOLUTE:.xoml}
```

Description:

Execute arbitrary C# code embedded in a XOML file.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Wfc.yml` |
| Evidence | Command preserved from source parser. |
