---
parsed_by: focuslocust
source: lolbas
type: generated
---
# adplus.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `adplus.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Adplus.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Debugging tool included with Windows Debugging Tools

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/adplus.md)
- Source verification: [source record](../../sources/lolbas/adplus.exe.md)

## Aliases

- `adplus.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.001 - LSASS Memory](../../attack/techniques/T1003.001-lsass-memory.md) | explicit | source | Command metadata lists T1003.001: adplus.exe -c {PATH:.xml} |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: adplus.exe -crash -o "{PATH_ABSOLUTE:folder}" -sc {PATH:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/adplus.exe.md)

## Source Verification

[source record](../../sources/lolbas/adplus.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mrd0x'
Person: mr.d0x
- Handle: '@nas_bench'
Person: Nasreddine Bencherchali
Author: mr.d0x
Code_Sample:
- Code: https://gist.github.com/nasbench/e34ca2cd90e3a845a558a102a4f607da
```
