---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Mshta.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `mshta.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Mshta.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by Windows to execute html applications. (.hta)

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/mshta.md)
- Source verification: [source record](../../sources/lolbas/mshta.exe.md)

## Aliases

- `Mshta.exe`
- `mshta.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: mshta.exe {REMOTEURL} |
| [T1218.005 - Mshta](../../attack/techniques/T1218.005-mshta.md) | explicit | source | Command metadata lists T1218.005: mshta.exe "{PATH_ABSOLUTE}:file.hta" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/mshta.exe.md)

## Source Verification

[source record](../../sources/lolbas/mshta.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
- Handle: '@oddvarmoe'
Person: Oddvar Moe
- Handle: '@C_h4ck_0'
Person: Nir Chako (Pentera)
Author: Oddvar Moe
```
