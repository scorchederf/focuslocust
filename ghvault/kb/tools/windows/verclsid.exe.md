---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Verclsid.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `verclsid.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Verclsid.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used to verify a COM object before it is instantiated by Windows Explorer

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/verclsid.md)
- Source verification: [source record](../../sources/lolbas/verclsid.exe.md)

## Aliases

- `Verclsid.exe`
- `verclsid.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.012 - Verclsid](../../attack/techniques/T1218.012-verclsid.md) | explicit | source | Command metadata lists T1218.012: verclsid.exe /S /C {CLSID} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/verclsid.exe.md)

## Source Verification

[source record](../../sources/lolbas/verclsid.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@NickTyrer'
Person: Nick Tyrer
Author: '@bohops'
Commands:
- Category: Execute
Command: verclsid.exe /S /C {CLSID}
Description: Used to verify a COM object before it is instantiated by Windows Explorer
```
