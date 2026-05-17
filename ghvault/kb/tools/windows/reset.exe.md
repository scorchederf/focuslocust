---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Reset.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `reset.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Reset.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Remote Desktop Services Reset Utility

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/reset.md)
- Source verification: [source record](../../sources/lolbas/reset.exe.md)

## Aliases

- `Reset.exe`
- `reset.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: reset.exe session |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/reset.exe.md)

## Source Verification

[source record](../../sources/lolbas/reset.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@Bl4ckShad3'
Person: Matan Bahar
Author: Matan Bahar
Commands:
- Category: Execute
Command: reset.exe session
Description: Once executed, `reset.exe` will execute `rwinsta.exe` in the same folder. Thus, if `reset.exe` is copied to
```
