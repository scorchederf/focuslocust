---
parsed_by: focuslocust
source: commands
type: generated
---
# Pcwutl.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Pcwutl.dll

Tool page: [Pcwutl.dll](../../tools/windows/pcwutl.dll.md)

### Launch an executable.

```text
rundll32.exe pcwutl.dll,LaunchApplication {PATH:.exe}
```

Description:

Launch executable by calling the LaunchApplication function.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Pcwutl.yml` |
| Evidence | Command preserved from source parser. |
