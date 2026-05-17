---
parsed_by: focuslocust
source: lolbas
type: generated
---
# csi.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `csi.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Csi.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Command line interface included with Visual Studio.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/csi.md)
- Source verification: [source record](../../sources/lolbas/csi.exe.md)

## Aliases

- `csi.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: csi.exe {PATH:.cs} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/csi.exe.md)

## Source Verification

[source record](../../sources/lolbas/csi.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: Execute
Command: csi.exe {PATH:.cs}
Description: Use csi.exe to run unsigned C# code.
```
