---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Wsreset.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wsreset.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wsreset.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used to reset Windows Store settings according to its manifest file

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/wsreset.md)
- Source verification: [source record](../../sources/lolbas/wsreset.exe.md)

## Aliases

- `Wsreset.exe`
- `wsreset.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | Command metadata lists T1548.002: wsreset.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/wsreset.exe.md)

## Source Verification

[source record](../../sources/lolbas/wsreset.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@ihack4falafel'
Person: Hashim Jawad
Author: Oddvar Moe
Commands:
- Category: UAC Bypass
Command: wsreset.exe
Description: During startup, wsreset.exe checks the registry value HKCU\Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command
```
