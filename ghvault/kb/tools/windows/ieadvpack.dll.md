---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ieadvpack.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ieadvpack.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Ieadvpack.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

INF installer for Internet Explorer. Has much of the same functionality as advpack.dll.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ieadvpack.dll.md)
- Source verification: [source record](../../sources/lolbas/ieadvpack.dll.md)

## Aliases

- `Ieadvpack.dll`
- `ieadvpack.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | Command metadata lists T1218.011: rundll32 ieadvpack.dll, RegisterOCX {CMD} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/ieadvpack.dll.md)

## Source Verification

[source record](../../sources/lolbas/ieadvpack.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: Jimmy (LaunchINFSection)
- Handle: '@0rbz_'
Person: Fabrizio (RegisterOCX - DLL)
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken (RegisterOCX - CMD)
Author: LOLBAS Team
```
