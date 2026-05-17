---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Atbroker.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `atbroker.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Atbroker.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Helper binary for Assistive Technology (AT)

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/atbroker.md)
- Source verification: [source record](../../sources/lolbas/atbroker.exe.md)

## Aliases

- `Atbroker.exe`
- `atbroker.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: ATBroker.exe /start malware |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/atbroker.exe.md)

## Source Verification

[source record](../../sources/lolbas/atbroker.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@hexacorn'
Person: Adam
Author: Oddvar Moe
Commands:
- Category: Execute
Command: ATBroker.exe /start malware
Description: Start a registered Assistive Technology (AT).
```
