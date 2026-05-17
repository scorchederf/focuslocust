---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Control.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `control.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Control.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary used to launch controlpanel items in Windows

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/control.md)
- Source verification: [source record](../../sources/lolbas/control.exe.md)

## Aliases

- `Control.exe`
- `control.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.002 - Control Panel](../../attack/techniques/T1218.002-control-panel.md) | explicit | source | Command metadata lists T1218.002: control.exe {PATH_ABSOLUTE:.cpl} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/control.exe.md)

## Source Verification

[source record](../../sources/lolbas/control.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: Jimmy
Author: Oddvar Moe
Commands:
- Category: ADS
Command: control.exe {PATH_ABSOLUTE}:evil.dll
Description: Execute evil.dll which is stored in an Alternate Data Stream (ADS).
```
