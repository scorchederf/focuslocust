---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Replace.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `replace.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Replace.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used to replace file with another file

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/replace.md)
- Source verification: [source record](../../sources/lolbas/replace.exe.md)

## Aliases

- `Replace.exe`
- `replace.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: replace.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:folder} /A |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/replace.exe.md)

## Source Verification

[source record](../../sources/lolbas/replace.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@elceef'
Person: elceef
Author: Oddvar Moe
Commands:
- Category: Copy
Command: replace.exe {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE:folder} /A
Description: Copy .cab file to destination
```
