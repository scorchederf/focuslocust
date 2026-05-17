---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Wmic.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wmic.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wmic.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The WMI command-line (WMIC) utility provides a command-line interface for WMI

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/wmic.md)
- Source verification: [source record](../../sources/lolbas/wmic.exe.md)

## Aliases

- `Wmic.exe`
- `wmic.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: wmic.exe datafile where "Name='C:\\windows\\system32\\calc.exe'" call Copy "C:\\users\\public\\calc.exe" |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: wmic.exe process get brief /format:"{PATH_SMB:.xsl}" |
| [T1564.004 - NTFS File Attributes](../../attack/techniques/T1564.004-ntfs-file-attributes.md) | explicit | source | Command metadata lists T1564.004: wmic.exe process call create "{PATH_ABSOLUTE}:program.exe" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/wmic.exe.md)

## Source Verification

[source record](../../sources/lolbas/wmic.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Oddvar Moe
Commands:
- Category: ADS
```
