---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Nmcap.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `nmcap.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Nmcap.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Command-line packet capture utility from Microsoft Network Monitor 3.x.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/nmcap.md)
- Source verification: [source record](../../sources/lolbas/nmcap.exe.md)

## Aliases

- `Nmcap.exe`
- `nmcap.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1040 - Network Sniffing](../../attack/techniques/T1040-network-sniffing.md) | explicit | source | Command metadata lists T1040: nmcap.exe /network * /capture /file {PATH_ABSOLUTE:.cap} |

## Source Verification

[source record](../../sources/lolbas/nmcap.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Reconnaissance
Command: nmcap.exe /network * /capture /file {PATH_ABSOLUTE:.cap}
Description: 'Start capture on all network adapters and save to specified .cap (circular) file.
```
