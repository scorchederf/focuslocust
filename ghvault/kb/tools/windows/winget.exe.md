---
parsed_by: focuslocust
source: lolbas
type: generated
---
# winget.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `winget.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Winget.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Package Manager tool

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/winget.md)
- Source verification: [source record](../../sources/lolbas/winget.exe.md)

## Aliases

- `winget.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: winget.exe install --accept-package-agreements -s msstore {name or ID} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/winget.exe.md)

## Source Verification

[source record](../../sources/lolbas/winget.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@saulpanders'
Person: Paul
- Person: Konrad 'unrooted' Klawikowski
- Person: Fredrik H. Brathen
Author: Paul Sanders
Code_Sample:
- Code: https://gist.github.com/saulpanders/00e1177602a8c01a3a8bfa932b3886b0
```
