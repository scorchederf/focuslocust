---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Setres.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `setres.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Setres.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Configures display settings

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/setres.md)
- Source verification: [source record](../../sources/lolbas/setres.exe.md)

## Aliases

- `Setres.exe`
- `setres.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: setres.exe -w 800 -h 600 |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/setres.exe.md)

## Source Verification

[source record](../../sources/lolbas/setres.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@0gtweet'
Person: Grzegorz Tworek
Author: Grzegorz Tworek
Commands:
- Category: Execute
Command: setres.exe -w 800 -h 600
Description: Sets the resolution and then launches 'choice' command from the working directory.
```
