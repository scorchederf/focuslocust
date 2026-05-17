---
parsed_by: focuslocust
source: commands
type: generated
---
# Ntsd Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Ntsd.exe

Tool page: [Ntsd.exe](../../tools/windows/ntsd.exe.md)

### Executes an executable under a trusted microsoft signed binary.

```text
ntsd.exe -g {CMD}
```

Description:

Launches command through the debugging process; optionally add `-G` to exit the debugger automatically.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Ntsd.yml` |
| Evidence | Command preserved from source parser. |
