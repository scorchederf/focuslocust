---
parsed_by: focuslocust
source: commands
type: generated
---
# Regini Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Regini.exe

Tool page: [Regini.exe](../../tools/windows/regini.exe.md)

### Write to registry

```text
regini.exe {PATH}:hidden.ini
```

Description:

Write registry keys from data inside the Alternate data stream.

Related ATT&CK:

- [T1564.004](../../attack/techniques/T1564.004-ntfs-file-attributes.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Regini.yml` |
| Evidence | Command preserved from source parser. |
