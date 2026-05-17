---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Netsh.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `netsh.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Netsh.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Netsh is a Windows tool used to manipulate network interface settings.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/netsh.md)
- Source verification: [source record](../../sources/lolbas/netsh.exe.md)

## Aliases

- `Netsh.exe`
- `netsh.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1546.007 - Netsh Helper DLL](../../attack/techniques/T1546.007-netsh-helper-dll.md) | explicit | source | Command metadata lists T1546.007: netsh.exe add helper {PATH_ABSOLUTE:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/netsh.exe.md)

## Source Verification

[source record](../../sources/lolbas/netsh.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: null
Person: Freddie Barr-Smith
- Handle: null
Person: Riccardo Spolaor
- Handle: null
Person: Mariano Graziano
- Handle: null
```
