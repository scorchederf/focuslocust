---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Advpack.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `advpack.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Advpack.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Utility for installing software and drivers with rundll32.exe

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/advpack.dll.md)
- Source verification: [source record](../../sources/lolbas/advpack.dll.md)

## Aliases

- `Advpack.dll`
- `advpack.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | Command metadata lists T1218.011: rundll32 advpack.dll, RegisterOCX {CMD} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/advpack.dll.md)

## Source Verification

[source record](../../sources/lolbas/advpack.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: Jimmy (LaunchINFSection)
- Handle: '@0rbz_'
Person: Fabrizio (RegisterOCX - DLL)
- Handle: '@moriarty_meng'
Person: Moriarty (RegisterOCX - CMD)
- Handle: '@ItsReallyNick'
```
