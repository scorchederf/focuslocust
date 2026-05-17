---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ilasm.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ilasm.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ilasm.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

used for compile c# code into dll or exe.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ilasm.md)
- Source verification: [source record](../../sources/lolbas/ilasm.exe.md)

## Aliases

- `Ilasm.exe`
- `ilasm.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: ilasm.exe {PATH_ABSOLUTE:.txt} /dll |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/ilasm.exe.md)

## Source Verification

[source record](../../sources/lolbas/ilasm.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@VakninHai'
Person: Hai Vaknin(Lux)
- Person: Lior Adar
Author: Hai vaknin (lux)
Commands:
- Category: Compile
Command: ilasm.exe {PATH_ABSOLUTE:.txt} /exe
```
