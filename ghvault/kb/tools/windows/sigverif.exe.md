---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Sigverif.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `sigverif.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Sigverif.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

File Signature Verification utility to verify digital signatures of files

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/sigverif.md)
- Source verification: [source record](../../sources/lolbas/sigverif.exe.md)

## Aliases

- `Sigverif.exe`
- `sigverif.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: sigverif.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/sigverif.exe.md)

## Source Verification

[source record](../../sources/lolbas/sigverif.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@0gtweet'
Person: Grzegorz Tworek
- Handle: '@Hexacorn'
Person: Adam
Author: Moshe Kaplan
Commands:
- Category: Execute
```
