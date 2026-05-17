---
parsed_by: focuslocust
source: commands
type: generated
---
# Infdefaultinstall Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Infdefaultinstall.exe

Tool page: [Infdefaultinstall.exe](../../tools/windows/infdefaultinstall.exe.md)

### Code execution

```text
InfDefaultInstall.exe {PATH:.inf}
```

Description:

Executes SCT script using scrobj.dll from a command in entered into a specially prepared INF file.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Infdefaultinstall.yml` |
| Evidence | Command preserved from source parser. |
