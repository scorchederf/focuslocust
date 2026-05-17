---
parsed_by: focuslocust
source: commands
type: generated
---
# Psr Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Psr.exe

Tool page: [Psr.exe](../../tools/windows/psr.exe.md)

### Can be used to take screenshots of the user environment

```text
psr.exe /start /output {PATH_ABSOLUTE:.zip} /sc 1 /gui 0
```

Description:

Record a user screen without creating a GUI. You should use "psr.exe /stop" to stop recording and create output file.

Related ATT&CK:

- [T1113](../../attack/techniques/T1113-screen-capture.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Psr.yml` |
| Evidence | Command preserved from source parser. |
