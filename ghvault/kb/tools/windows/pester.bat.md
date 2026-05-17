---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pester.bat

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pester.bat` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/pester.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used as part of the Powershell pester

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/pester.bat.md)
- Source verification: [source record](../../sources/lolbas/pester.bat.md)

## Aliases

- `Pester.bat`
- `pester.bat`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1216 - System Script Proxy Execution](../../attack/techniques/T1216-system-script-proxy-execution.md) | explicit | source | Command metadata lists T1216: Pester.bat ;{PATH:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/pester.bat.md)

## Source Verification

[source record](../../sources/lolbas/pester.bat.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@p0w3rsh3ll'
Person: Emin Atac
- Handle: '@_st0pp3r_'
Person: Stamatis Chatzimangou
Author: Oddvar Moe
Commands:
- Category: Execute
```
