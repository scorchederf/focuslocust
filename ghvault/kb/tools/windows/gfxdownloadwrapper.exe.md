---
parsed_by: focuslocust
source: lolbas
type: generated
---
# GfxDownloadWrapper.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `gfxdownloadwrapper.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/GfxDownloadWrapper.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Remote file download used by the Intel Graphics Control Panel, receives as first parameter a URL and a destination file path.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/gfxdownloadwrapper.md)
- Source verification: [source record](../../sources/lolbas/gfxdownloadwrapper.exe.md)

## Aliases

- `GfxDownloadWrapper.exe`
- `gfxdownloadwrapper.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: C:\Windows\System32\DriverStore\FileRepository\igdlh64.inf_amd64_[0-9]+\GfxDownloadWrapper.exe "URL" "DESTINATION FILE" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/gfxdownloadwrapper.exe.md)

## Source Verification

[source record](../../sources/lolbas/gfxdownloadwrapper.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: null
Person: Jesus Galvez
Author: Jesus Galvez
Commands:
- Category: Download
Command: C:\Windows\System32\DriverStore\FileRepository\igdlh64.inf_amd64_[0-9]+\GfxDownloadWrapper.exe "URL" "DESTINATION
FILE"
```
