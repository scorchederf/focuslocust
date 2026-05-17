---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Provlaunch.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `provlaunch.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Provlaunch.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Launcher process

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/provlaunch.md)
- Source verification: [source record](../../sources/lolbas/provlaunch.exe.md)

## Aliases

- `Provlaunch.exe`
- `provlaunch.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: provlaunch.exe LOLBin |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/provlaunch.exe.md)

## Source Verification

[source record](../../sources/lolbas/provlaunch.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@0gtweet'
Person: Grzegorz Tworek
Author: Grzegorz Tworek
Commands:
- Category: Execute
Command: provlaunch.exe LOLBin
Description: Executes command defined in the Registry. Requires 3 levels of the key structure containing some keywords.
```
