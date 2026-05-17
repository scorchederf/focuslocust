---
parsed_by: focuslocust
source: commands
type: generated
---
# AddinUtil Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## AddinUtil.exe

Tool page: [AddinUtil.exe](../../tools/windows/addinutil.exe.md)

### Proxy execution of malicious serialized payload

```text
C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe -AddinRoot:.
```

Description:

AddinUtil is executed from the directory where the 'Addins.Store' payload exists, AddinUtil will execute the 'Addins.Store' payload.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Addinutil.yml` |
| Evidence | Command preserved from source parser. |
