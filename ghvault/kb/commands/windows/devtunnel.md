---
parsed_by: focuslocust
source: commands
type: generated
---
# devtunnel Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## devtunnel.exe

Tool page: [devtunnel.exe](../../tools/windows/devtunnel.exe.md)

### Download Files, Upload Files, Data Exfiltration

```text
devtunnel.exe host -p 8080
```

Description:

Enabling a forwarded port for locally hosted service at port 8080 to be exposed on the internet.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/devtunnels.yml` |
| Evidence | Command preserved from source parser. |
