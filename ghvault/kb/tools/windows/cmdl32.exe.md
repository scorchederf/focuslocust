---
parsed_by: focuslocust
source: lolbas
type: generated
---
# cmdl32.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cmdl32.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmdl32.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Connection Manager Auto-Download

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/cmdl32.md)
- Source verification: [source record](../../sources/lolbas/cmdl32.exe.md)

## Aliases

- `cmdl32.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: cmdl32 /vpn /lan %cd%\config |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/cmdl32.exe.md)

## Source Verification

[source record](../../sources/lolbas/cmdl32.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@elliotkillick'
Person: Elliot Killick
Author: Elliot Killick
Commands:
- Category: Download
Command: cmdl32 /vpn /lan %cd%\config
Description: Download a file from the web address specified in the configuration file. The downloaded file will be in %TMP%
```
