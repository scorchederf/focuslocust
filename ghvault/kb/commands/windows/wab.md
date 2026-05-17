---
parsed_by: focuslocust
source: commands
type: generated
---
# Wab Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Wab.exe

Tool page: [Wab.exe](../../tools/windows/wab.exe.md)

### Execute dll file. Bypass defensive counter measures

```text
wab.exe
```

Description:

Change HKLM\Software\Microsoft\WAB\DLLPath and execute DLL of choice

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wab.yml` |
| Evidence | Command preserved from source parser. |
