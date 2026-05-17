---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Reg.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `reg.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Reg.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used to manipulate the registry

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/reg.md)
- Source verification: [source record](../../sources/lolbas/reg.exe.md)

## Aliases

- `Reg.exe`
- `reg.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.002 - Security Account Manager](../../attack/techniques/T1003.002-security-account-manager.md) | explicit | source | Command metadata lists T1003.002: reg save HKLM\SECURITY {PATH_ABSOLUTE:.1.bak} && reg save HKLM\SYSTEM {PATH_ABSOLUTE:.2.bak} && reg save HKLM\SAM {PATH_ABSOLUTE:.3.bak} |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: reg export HKLM\SOFTWARE\Microsoft\Evilreg {PATH_ABSOLUTE}:evilreg.reg |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/reg.exe.md)

## Source Verification

[source record](../../sources/lolbas/reg.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: ADS
Command: reg export HKLM\SOFTWARE\Microsoft\Evilreg {PATH_ABSOLUTE}:evilreg.reg
Description: Export the target Registry key and save it to the specified .REG file within an Alternate data stream.
```
