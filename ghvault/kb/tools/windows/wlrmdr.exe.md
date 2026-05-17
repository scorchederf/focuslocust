---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Wlrmdr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wlrmdr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wlrmdr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Logon Reminder executable

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/wlrmdr.md)
- Source verification: [source record](../../sources/lolbas/wlrmdr.exe.md)

## Aliases

- `Wlrmdr.exe`
- `wlrmdr.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: wlrmdr.exe -s 3600 -f 0 -t _ -m _ -a 11 -u {PATH:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/wlrmdr.exe.md)

## Source Verification

[source record](../../sources/lolbas/wlrmdr.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@0gtweet'
Person: Grzegorz Tworek
- Handle: '@Oddvarmoe'
Person: Oddvar Moe
- Handle: '@falsneg'
Person: Freddy
Author: Moshe Kaplan
```
