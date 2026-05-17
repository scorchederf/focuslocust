---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Query.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `query.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Query.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Remote Desktop Services MultiUser Query Utility

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/query.md)
- Source verification: [source record](../../sources/lolbas/query.exe.md)

## Aliases

- `Query.exe`
- `query.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: query.exe user |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/query.exe.md)

## Source Verification

[source record](../../sources/lolbas/query.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@IdanLerman'
Person: Idan Lerman
Author: Idan Lerman
Commands:
- Category: Execute
Command: query.exe user
Description: Once executed, `query.exe` will execute `quser.exe` in the same folder. Thus, if `query.exe` is copied to a
```
