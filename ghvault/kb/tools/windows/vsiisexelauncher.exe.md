---
parsed_by: focuslocust
source: lolbas
type: generated
---
# VSIISExeLauncher.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vsiisexelauncher.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VSIISExeLauncher.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary will execute specified binary. Part of VS/VScode installation.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/vsiisexelauncher.md)
- Source verification: [source record](../../sources/lolbas/vsiisexelauncher.exe.md)

## Aliases

- `VSIISExeLauncher.exe`
- `vsiisexelauncher.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: VSIISExeLauncher.exe -p {PATH:.exe} -a "{CMD:args}" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/vsiisexelauncher.exe.md)

## Source Verification

[source record](../../sources/lolbas/vsiisexelauncher.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: timwhite
Author: timwhite
Commands:
- Category: Execute
Command: VSIISExeLauncher.exe -p {PATH:.exe} -a "{CMD:args}"
Description: The above binary will execute other binary.
MitreID: T1218
```
