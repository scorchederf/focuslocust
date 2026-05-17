---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Zipfldr.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `zipfldr.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Zipfldr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Compressed Folder library

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/zipfldr.dll.md)
- Source verification: [source record](../../sources/lolbas/zipfldr.dll.md)

## Aliases

- `Zipfldr.dll`
- `zipfldr.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | Command metadata lists T1218.011: rundll32.exe zipfldr.dll,RouteTheCall file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/zipfldr.dll.md)

## Source Verification

[source record](../../sources/lolbas/zipfldr.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@moriarty_meng'
Person: Moriarty (Execution)
- Handle: '@r0lan'
Person: r0lan (Obfuscation)
Author: LOLBAS Team
Commands:
- Category: Execute
```
