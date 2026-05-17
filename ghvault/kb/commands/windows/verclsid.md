---
parsed_by: focuslocust
source: commands
type: generated
---
# Verclsid Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Verclsid.exe

Tool page: [Verclsid.exe](../../tools/windows/verclsid.exe.md)

### Run a COM object created in registry to evade defensive counter measures

```text
verclsid.exe /S /C {CLSID}
```

Description:

Used to verify a COM object before it is instantiated by Windows Explorer

Related ATT&CK:

- [T1218.012](../../attack/techniques/T1218.012-verclsid.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Verclsid.yml` |
| Evidence | Command preserved from source parser. |
