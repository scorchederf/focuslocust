---
parsed_by: focuslocust
source: commands
type: generated
---
# Vshadow Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Vshadow.exe

Tool page: [Vshadow.exe](../../tools/windows/vshadow.exe.md)

### Performs execution of specified executable file.

```text
vshadow.exe -nw -exec={PATH_ABSOLUTE:.exe} C:
```

Description:

Executes specified executable from vshadow.exe.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Vshadow.yml` |
| Evidence | Command preserved from source parser. |
