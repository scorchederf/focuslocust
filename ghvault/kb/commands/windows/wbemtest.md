---
parsed_by: focuslocust
source: commands
type: generated
---
# wbemtest Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## wbemtest.exe

Tool page: [wbemtest.exe](../../tools/windows/wbemtest.exe.md)

### Execute arbitrary commands through WMI classes

```text
wbemtest.exe
```

Description:

Execute arbitary commands through WMI through a GUI managment interface for Web Based Enterprise Management testing (WBEM). Uses WMI to Create and instance of a Win32_Process WMI class with a commandline argument of the target command to spawn. Spawns a GUI so it requires interactive access. For a demo, see link to blog in resources.

Related ATT&CK:

- [T1047](../../attack/techniques/T1047-windows-management-instrumentation.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wbemtest.yml` |
| Evidence | Command preserved from source parser. |
