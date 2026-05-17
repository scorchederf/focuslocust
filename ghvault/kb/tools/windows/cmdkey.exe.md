---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Cmdkey.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cmdkey.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmdkey.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

creates, lists, and deletes stored user names and passwords or credentials.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/cmdkey.md)
- Source verification: [source record](../../sources/lolbas/cmdkey.exe.md)

## Aliases

- `Cmdkey.exe`
- `cmdkey.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1078 - Valid Accounts](../../attack/techniques/T1078-valid-accounts.md) | explicit | source | Command metadata lists T1078: cmdkey /list |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/cmdkey.exe.md)

## Source Verification

[source record](../../sources/lolbas/cmdkey.exe.md)

## Evidence Excerpt

```text
Author: Oddvar Moe
Commands:
- Category: Credentials
Command: cmdkey /list
Description: List cached credentials
MitreID: T1078
OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
Privileges: User
```
