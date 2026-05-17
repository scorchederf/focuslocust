---
parsed_by: focuslocust
source: lolbas
type: generated
---
# wbadmin.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wbadmin.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wbadmin.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Backup Administration utility

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/wbadmin.md)
- Source verification: [source record](../../sources/lolbas/wbadmin.exe.md)

## Aliases

- `wbadmin.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.003 - NTDS](../../attack/techniques/T1003.003-ntds.md) | explicit | source | Command metadata lists T1003.003: wbadmin start recovery -version:<VERSIONIDENTIFIER> -recoverytarget:{PATH_ABSOLUTE:folder} -itemtype:file -items:C:\Windows\NTDS\NTDS.dit,C:\Windows\System32\config\SYSTEM -notR... |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/wbadmin.exe.md)

## Source Verification

[source record](../../sources/lolbas/wbadmin.exe.md)

## Evidence Excerpt

```text
Author: Chris Eastwood
Commands:
- Category: Dump
Command: wbadmin start backup -backupTarget:{PATH_ABSOLUTE:folder} -include:C:\Windows\NTDS\NTDS.dit,C:\Windows\System32\config\SYSTEM
-quiet
Description: Extract NTDS.dit and SYSTEM hive into backup virtual hard drive file (.vhdx)
MitreID: T1003.003
OperatingSystem: Windows Server
```
