---
parsed_by: focuslocust
source: commands
type: generated
---
# Msconfig Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Msconfig.exe

Tool page: [Msconfig.exe](../../tools/windows/msconfig.exe.md)

### Code execution using Msconfig.exe

```text
Msconfig.exe -5
```

Description:

Executes command embeded in crafted c:\windows\system32\mscfgtlc.xml.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msconfig.yml` |
| Evidence | Command preserved from source parser. |
