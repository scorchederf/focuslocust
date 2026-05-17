---
parsed_by: focuslocust
source: lolbas
type: generated
---
# dsdbutil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dsdbutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dsdbutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Dsdbutil is a command-line tool that is built into Windows Server. It is available if you have the AD LDS server role installed. Can be used as a command line utility to export Active Directory.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/dsdbutil.md)
- Source verification: [source record](../../sources/lolbas/dsdbutil.exe.md)

## Aliases

- `dsdbutil.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.003 - NTDS](../../attack/techniques/T1003.003-ntds.md) | explicit | source | Command metadata lists T1003.003: dsdbutil.exe "activate instance ntds" "snapshot" "list all" "delete 1" "quit" "quit" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/dsdbutil.exe.md)

## Source Verification

[source record](../../sources/lolbas/dsdbutil.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: bohop
- Handle: '@eki_erk'
Person: Ekitji
Aliases:
- Alias: dsDbUtil.exe
Author: Ekitji
```
