---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Runexehelper.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `runexehelper.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Runexehelper.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Launcher process

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/runexehelper.md)
- Source verification: [source record](../../sources/lolbas/runexehelper.exe.md)

## Aliases

- `Runexehelper.exe`
- `runexehelper.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: runexehelper.exe {PATH_ABSOLUTE:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/runexehelper.exe.md)

## Source Verification

[source record](../../sources/lolbas/runexehelper.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@0gtweet'
Person: Grzegorz Tworek
Author: Grzegorz Tworek
Commands:
- Category: Execute
Command: runexehelper.exe {PATH_ABSOLUTE:.exe}
Description: 'Launches the specified exe. Prerequisites: (1) diagtrack_action_output environment variable must be set to
```
