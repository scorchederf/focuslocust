---
parsed_by: focuslocust
source: commands
type: generated
---
# odbcad32 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## odbcad32.exe

Tool page: [odbcad32.exe](../../tools/windows/odbcad32.exe.md)

### Execute a binary as a high-integrity process without a UAC prompt.

```text
odbcad32.exe
```

Description:

Launch odbcad32.exe GUI, click 'Tracing' tab, click 'Browsing' button, enter abitrary command in the File Dialog's path, press enter.

Related ATT&CK:

- [T1548.002](../../attack/techniques/T1548.002-bypass-user-account-control.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/odbcad32.yml` |
| Evidence | Command preserved from source parser. |
