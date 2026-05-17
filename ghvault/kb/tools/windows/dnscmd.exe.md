---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Dnscmd.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dnscmd.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Dnscmd.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

A command-line interface for managing DNS servers

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/dnscmd.md)
- Source verification: [source record](../../sources/lolbas/dnscmd.exe.md)

## Aliases

- `Dnscmd.exe`
- `dnscmd.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1543.003 - Windows Service](../../attack/techniques/T1543.003-windows-service.md) | explicit | source | Command metadata lists T1543.003: dnscmd.exe dc1.lab.int /config /serverlevelplugindll {PATH_SMB:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/dnscmd.exe.md)

## Source Verification

[source record](../../sources/lolbas/dnscmd.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: Shay Ber
- Handle: '@dim0x69'
Person: Dimitrios Slamaris
- Handle: '@nikhil_mitt'
Person: Nikhil SamratAshok
Author: Oddvar Moe
Commands:
```
