---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pktmon.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pktmon.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pktmon.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Capture Network Packets on the windows 10 with October 2018 Update or later.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/pktmon.md)
- Source verification: [source record](../../sources/lolbas/pktmon.exe.md)

## Aliases

- `Pktmon.exe`
- `pktmon.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1040 - Network Sniffing](../../attack/techniques/T1040-network-sniffing.md) | explicit | source | Command metadata lists T1040: pktmon.exe filter add -p 445 |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/pktmon.exe.md)

## Source Verification

[source record](../../sources/lolbas/pktmon.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: Derek Johnson
Author: Derek Johnson
Commands:
- Category: Reconnaissance
Command: pktmon.exe start --etw
Description: Will start a packet capture and store log file as PktMon.etl. Use pktmon.exe stop
MitreID: T1040
```
