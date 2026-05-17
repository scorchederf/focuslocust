---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Sqlps.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `sqlps.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Sqlps.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Tool included with Microsoft SQL Server that loads SQL Server cmdlets. Microsoft SQL Server\100 and 110 are Powershell v2. Microsoft SQL Server\120 and 130 are Powershell version 4. Replaced by SQLToolsPS.exe in SQL Server 2016, but will be included with installation for compatability reasons.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/sqlps.md)
- Source verification: [source record](../../sources/lolbas/sqlps.exe.md)

## Aliases

- `Sqlps.exe`
- `sqlps.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: Sqlps.exe -noprofile |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/sqlps.exe.md)

## Source Verification

[source record](../../sources/lolbas/sqlps.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bryon_'
Person: Bryon
- Handle: '@ManuelBerrueta'
Person: Manny
Author: Oddvar Moe
Commands:
- Category: Execute
```
