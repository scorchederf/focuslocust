---
parsed_by: focuslocust
source: commands
type: generated
---
# Colorcpl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Colorcpl.exe

Tool page: [Colorcpl.exe](../../tools/windows/colorcpl.exe.md)

### Copies file(s) to a subfolder of a generally trusted folder (c:\Windows\System32), which can be used to hide files or make them blend into the environment.

```text
colorcpl {PATH}
```

Description:

Copies the referenced file to C:\Windows\System32\spool\drivers\color\.

Related ATT&CK:

- [T1036.005](../../attack/techniques/T1036.005-match-legitimate-resource-name-or-location.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Colorcpl.yml` |
| Evidence | Command preserved from source parser. |
