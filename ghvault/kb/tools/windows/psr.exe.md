---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Psr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `psr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Psr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Problem Steps Recorder, used to record screen and clicks.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/psr.md)
- Source verification: [source record](../../sources/lolbas/psr.exe.md)

## Aliases

- `Psr.exe`
- `psr.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1113 - Screen Capture](../../attack/techniques/T1113-screen-capture.md) | explicit | source | Command metadata lists T1113: psr.exe /start /output {PATH_ABSOLUTE:.zip} /sc 1 /gui 0 |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/psr.exe.md)

## Source Verification

[source record](../../sources/lolbas/psr.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@L3m0nada'
Person: Leon Rodenko
Author: Leon Rodenko
Commands:
- Category: Reconnaissance
Command: psr.exe /start /output {PATH_ABSOLUTE:.zip} /sc 1 /gui 0
Description: Record a user screen without creating a GUI. You should use "psr.exe /stop" to stop recording and create output
```
