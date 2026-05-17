---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Change.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `change.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Change.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Remote Desktop Services MultiUser Change Utility

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/change.md)
- Source verification: [source record](../../sources/lolbas/change.exe.md)

## Aliases

- `Change.exe`
- `change.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: change.exe user |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/change.exe.md)

## Source Verification

[source record](../../sources/lolbas/change.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@IdanLerman'
Person: Idan Lerman
Author: Idan Lerman
Commands:
- Category: Execute
Command: change.exe user
Description: Once executed, `change.exe` will execute `chgusr.exe` in the same folder. Thus, if `change.exe` is copied to
```
