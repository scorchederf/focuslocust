---
parsed_by: focuslocust
source: lolbas
type: generated
---
# vbc.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vbc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Vbc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary file used for compile vbs code

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/vbc.md)
- Source verification: [source record](../../sources/lolbas/vbc.exe.md)

## Aliases

- `vbc.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: vbc -reference:Microsoft.VisualBasic.dll {PATH_ABSOLUTE:.vb} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/vbc.exe.md)

## Source Verification

[source record](../../sources/lolbas/vbc.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: Lior Adar
- Person: Hai Vaknin(Lux)
Author: Lior Adar
Commands:
- Category: Compile
Command: vbc.exe /target:exe {PATH_ABSOLUTE:.vb}
Description: Binary file used by .NET to compile Visual Basic code to an executable.
```
