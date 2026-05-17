---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Eventvwr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `eventvwr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Eventvwr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Displays Windows Event Logs in a GUI window.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/eventvwr.md)
- Source verification: [source record](../../sources/lolbas/eventvwr.exe.md)

## Aliases

- `Eventvwr.exe`
- `eventvwr.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1548.002 - Bypass User Account Control](../../attack/techniques/T1548.002-bypass-user-account-control.md) | explicit | source | Command metadata lists T1548.002: ysoserial.exe -o raw -f BinaryFormatter - g DataSet -c "{CMD}" > RecentViews & copy RecentViews %LOCALAPPDATA%\Microsoft\EventV~1\RecentViews & eventvwr.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/eventvwr.exe.md)

## Source Verification

[source record](../../sources/lolbas/eventvwr.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@enigma0x3'
Person: Matt Nelson
- Handle: '@mattifestation'
Person: Matt Graeber
- Handle: '@orange_8361'
Person: Orange Tsai
Author: Jacob Gajek
```
