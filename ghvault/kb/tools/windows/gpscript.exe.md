---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Gpscript.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `gpscript.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Gpscript.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by group policy to process scripts

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/gpscript.md)
- Source verification: [source record](../../sources/lolbas/gpscript.exe.md)

## Aliases

- `Gpscript.exe`
- `gpscript.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: Gpscript /startup |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/gpscript.exe.md)

## Source Verification

[source record](../../sources/lolbas/gpscript.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: Execute
Command: Gpscript /logon
Description: Executes logon scripts configured in Group Policy.
```
