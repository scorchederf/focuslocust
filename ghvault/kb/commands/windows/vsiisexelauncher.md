---
parsed_by: focuslocust
source: commands
type: generated
---
# VSIISExeLauncher Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## VSIISExeLauncher.exe

Tool page: [VSIISExeLauncher.exe](../../tools/windows/vsiisexelauncher.exe.md)

### Execute any binary with given arguments.

```text
VSIISExeLauncher.exe -p {PATH:.exe} -a "{CMD:args}"
```

Description:

The above binary will execute other binary.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VSIISExeLauncher.yml` |
| Evidence | Command preserved from source parser. |
