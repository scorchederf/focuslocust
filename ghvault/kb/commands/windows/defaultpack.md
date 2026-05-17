---
parsed_by: focuslocust
source: commands
type: generated
---
# DefaultPack Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## DefaultPack.EXE

Tool page: [DefaultPack.EXE](../../tools/windows/defaultpack.exe.md)

### Can be used to execute stagers, binaries, and other malicious commands.

```text
DefaultPack.EXE /C:"{CMD}"
```

Description:

Use DefaultPack.EXE to execute arbitrary binaries, with added argument support.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/DefaultPack.yml` |
| Evidence | Command preserved from source parser. |
