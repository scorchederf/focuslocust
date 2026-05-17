---
parsed_by: focuslocust
source: lolbas
type: generated
---
# DefaultPack.EXE

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `defaultpack.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/DefaultPack.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

This binary can be downloaded along side multiple software downloads on the Microsoft website. It gets downloaded when the user forgets to uncheck the option to set Bing as the default search provider.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/defaultpack.md)
- Source verification: [source record](../../sources/lolbas/defaultpack.exe.md)

## Aliases

- `DefaultPack.EXE`
- `defaultpack.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: DefaultPack.EXE /C:"{CMD}" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/defaultpack.exe.md)

## Source Verification

[source record](../../sources/lolbas/defaultpack.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@checkymander'
Person: checkymander
Author: '@checkymander'
Commands:
- Category: Execute
Command: DefaultPack.EXE /C:"{CMD}"
Description: Use DefaultPack.EXE to execute arbitrary binaries, with added argument support.
```
