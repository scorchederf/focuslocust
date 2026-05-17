---
parsed_by: focuslocust
source: commands
type: generated
---
# Setres Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Setres.exe

Tool page: [Setres.exe](../../tools/windows/setres.exe.md)

### Executes arbitrary code

```text
setres.exe -w 800 -h 600
```

Description:

Sets the resolution and then launches 'choice' command from the working directory.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Setres.yml` |
| Evidence | Command preserved from source parser. |
