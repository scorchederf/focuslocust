---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mshtml.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mshtml.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Mshtml.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft HTML Viewer

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/mshtml.dll.md)
- Source verification: [source record](../../sources/lolbas/mshtml.dll.md)

## Aliases

- `Mshtml.dll`
- `mshtml.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | Command metadata lists T1218.011: rundll32.exe Mshtml.dll,PrintHTML {PATH_ABSOLUTE:.hta} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/mshtml.dll.md)

## Source Verification

[source record](../../sources/lolbas/mshtml.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken
Author: LOLBAS Team
Commands:
- Category: Execute
Command: rundll32.exe Mshtml.dll,PrintHTML {PATH_ABSOLUTE:.hta}
Description: 'Invoke an HTML Application via mshta.exe (note: pops a security warning and a print dialogue box).'
```
