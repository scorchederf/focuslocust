---
parsed_by: focuslocust
source: commands
type: generated
---
# Sigverif Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Sigverif.exe

Tool page: [Sigverif.exe](../../tools/windows/sigverif.exe.md)

### Execute arbitrary programs through a trusted Microsoft-signed binary to bypass application whitelisting.

```text
sigverif.exe
```

Description:

Launch sigverif.exe GUI, click 'Advanced', specify arbitrary executable path as 'log file name', then click 'View Log' to execute the binary.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Sigverif.yml` |
| Evidence | Command preserved from source parser. |
