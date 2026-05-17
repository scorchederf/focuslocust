---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Cdb.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cdb.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Cdb.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Debugging tool included with Windows Debugging Tools.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/cdb.md)
- Source verification: [source record](../../sources/lolbas/cdb.exe.md)

## Aliases

- `Cdb.exe`
- `cdb.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: cdb.exe -c {PATH:.txt} "{CMD}" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/cdb.exe.md)

## Source Verification

[source record](../../sources/lolbas/cdb.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mattifestation'
Person: Matt Graeber
- Handle: '@mrd0x'
Person: mr.d0x
- Handle: '@sec_spooky'
Person: Spooky Sec
- Handle: '@nas_bench'
```
