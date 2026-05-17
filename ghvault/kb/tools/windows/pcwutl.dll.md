---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pcwutl.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pcwutl.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Pcwutl.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft HTML Viewer

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/pcwutl.dll.md)
- Source verification: [source record](../../sources/lolbas/pcwutl.dll.md)

## Aliases

- `Pcwutl.dll`
- `pcwutl.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | Command metadata lists T1218.011: rundll32.exe pcwutl.dll,LaunchApplication {PATH:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/pcwutl.dll.md)

## Source Verification

[source record](../../sources/lolbas/pcwutl.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@harr0ey'
Person: Matt harr0ey
Author: LOLBAS Team
Commands:
- Category: Execute
Command: rundll32.exe pcwutl.dll,LaunchApplication {PATH:.exe}
Description: Launch executable by calling the LaunchApplication function.
```
