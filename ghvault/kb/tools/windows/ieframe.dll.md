---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ieframe.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ieframe.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Ieframe.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Internet Browser DLL for translating HTML code.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ieframe.dll.md)
- Source verification: [source record](../../sources/lolbas/ieframe.dll.md)

## Aliases

- `Ieframe.dll`
- `ieframe.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | Command metadata lists T1218.011: rundll32.exe ieframe.dll,OpenURL {PATH_ABSOLUTE:.url} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/ieframe.dll.md)

## Source Verification

[source record](../../sources/lolbas/ieframe.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: Jimmy
- Handle: '@hexacorn'
Person: Adam
Author: LOLBAS Team
Code_Sample:
- Code: https://gist.githubusercontent.com/bohops/89d7b11fa32062cfe31be9fdb18f050e/raw/1206a613a6621da21e7fd164b80a7ff01c5b64ab/calc.url
```
