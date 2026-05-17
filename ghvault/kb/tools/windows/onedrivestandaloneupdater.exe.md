---
parsed_by: focuslocust
source: lolbas
type: generated
---
# OneDriveStandaloneUpdater.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `onedrivestandaloneupdater.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/OneDriveStandaloneUpdater.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

OneDrive Standalone Updater

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/onedrivestandaloneupdater.md)
- Source verification: [source record](../../sources/lolbas/onedrivestandaloneupdater.exe.md)

## Aliases

- `OneDriveStandaloneUpdater.exe`
- `onedrivestandaloneupdater.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: OneDriveStandaloneUpdater |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/onedrivestandaloneupdater.exe.md)

## Source Verification

[source record](../../sources/lolbas/onedrivestandaloneupdater.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@elliotkillick'
Person: Elliot Killick
Author: Elliot Killick
Commands:
- Category: Download
Command: OneDriveStandaloneUpdater
Description: Download a file from the web address specified in `HKCU\Software\Microsoft\OneDrive\UpdateOfficeConfig\UpdateRingSettingURLFromOC`.
```
