---
parsed_by: focuslocust
source: commands
type: generated
---
# Mshtml.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Mshtml.dll

Tool page: [Mshtml.dll](../../tools/windows/mshtml.dll.md)

### Launch an HTA application.

```text
rundll32.exe Mshtml.dll,PrintHTML {PATH_ABSOLUTE:.hta}
```

Description:

Invoke an HTML Application via mshta.exe (note: pops a security warning and a print dialogue box).

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Mshtml.yml` |
| Evidence | Command preserved from source parser. |
