---
parsed_by: focuslocust
source: lolbas
type: generated
---
# wt.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wt.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/wt.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Terminal

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/wt.md)
- Source verification: [source record](../../sources/lolbas/wt.exe.md)

## Aliases

- `wt.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: wt.exe {CMD} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/wt.exe.md)

## Source Verification

[source record](../../sources/lolbas/wt.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@nas_bench'
Person: Nasreddine Bencherchali
Author: Nasreddine Bencherchali
Commands:
- Category: Execute
Command: wt.exe {CMD}
Description: Execute a command via Windows Terminal.
```
