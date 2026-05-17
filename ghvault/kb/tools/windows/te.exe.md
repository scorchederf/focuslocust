---
parsed_by: focuslocust
source: lolbas
type: generated
---
# te.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `te.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Te.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Testing tool included with Microsoft Test Authoring and Execution Framework (TAEF).

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/te.md)
- Source verification: [source record](../../sources/lolbas/te.exe.md)

## Aliases

- `te.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: te.exe {PATH:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/te.exe.md)

## Source Verification

[source record](../../sources/lolbas/te.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@gN3mes1s'
Person: Giuseppe N3mes1s
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Oddvar Moe
Commands:
- Category: Execute
```
