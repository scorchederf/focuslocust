---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Infdefaultinstall.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `infdefaultinstall.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Infdefaultinstall.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary used to perform installation based on content inside inf files

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/infdefaultinstall.md)
- Source verification: [source record](../../sources/lolbas/infdefaultinstall.exe.md)

## Aliases

- `Infdefaultinstall.exe`
- `infdefaultinstall.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: InfDefaultInstall.exe {PATH:.inf} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/infdefaultinstall.exe.md)

## Source Verification

[source record](../../sources/lolbas/infdefaultinstall.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@kylehanslovan'
Person: Kyle Hanslovan
Author: Oddvar Moe
Code_Sample:
- Code: https://gist.github.com/KyleHanslovan/5e0f00d331984c1fb5be32c40f3b265a
Commands:
- Category: Execute
```
