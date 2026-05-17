---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Colorcpl.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `colorcpl.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Colorcpl.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary that handles color management

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/colorcpl.md)
- Source verification: [source record](../../sources/lolbas/colorcpl.exe.md)

## Aliases

- `Colorcpl.exe`
- `colorcpl.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1036.005 - Match Legitimate Resource Name or Location](../../attack/techniques/T1036.005-match-legitimate-resource-name-or-location.md) | explicit | source | Command metadata lists T1036.005: colorcpl {PATH} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/colorcpl.exe.md)

## Source Verification

[source record](../../sources/lolbas/colorcpl.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@eral4m'
Person: eral4m
Author: Arjan Onwezen
Commands:
- Category: Copy
Command: colorcpl {PATH}
Description: Copies the referenced file to C:\Windows\System32\spool\drivers\color\.
```
