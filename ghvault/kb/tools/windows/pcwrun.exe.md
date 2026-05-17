---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pcwrun.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pcwrun.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pcwrun.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Program Compatibility Wizard

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/pcwrun.md)
- Source verification: [source record](../../sources/lolbas/pcwrun.exe.md)

## Aliases

- `Pcwrun.exe`
- `pcwrun.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: Pcwrun.exe /../../$(calc).exe |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: Pcwrun.exe {PATH_ABSOLUTE:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/pcwrun.exe.md)

## Source Verification

[source record](../../sources/lolbas/pcwrun.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken
- Handle: '@nas_bench'
Person: Nasreddine Bencherchali
Author: Oddvar Moe
Commands:
- Category: Execute
```
