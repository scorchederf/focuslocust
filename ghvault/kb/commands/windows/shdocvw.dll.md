---
parsed_by: focuslocust
source: commands
type: generated
---
# Shdocvw.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Shdocvw.dll

Tool page: [Shdocvw.dll](../../tools/windows/shdocvw.dll.md)

### Load an executable payload by calling a .url file with or without quotes. The .url file extension can be renamed.

```text
rundll32.exe shdocvw.dll,OpenURL {PATH_ABSOLUTE:.url}
```

Description:

Launch an executable payload via proxy through a URL (information) file by calling OpenURL.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Shdocvw.yml` |
| Evidence | Command preserved from source parser. |
