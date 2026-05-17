---
parsed_by: focuslocust
source: commands
type: generated
---
# Cmdkey Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Cmdkey.exe

Tool page: [Cmdkey.exe](../../tools/windows/cmdkey.exe.md)

### Get credential information from host

```text
cmdkey /list
```

Description:

List cached credentials

Related ATT&CK:

- [T1078](../../attack/techniques/T1078-valid-accounts.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmdkey.yml` |
| Evidence | Command preserved from source parser. |
