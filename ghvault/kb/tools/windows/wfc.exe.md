---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Wfc.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wfc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Wfc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The Workflow Command-line Compiler tool is included with the Windows Software Development Kit (SDK).

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/wfc.md)
- Source verification: [source record](../../sources/lolbas/wfc.exe.md)

## Aliases

- `Wfc.exe`
- `wfc.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: wfc.exe {PATH_ABSOLUTE:.xoml} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/wfc.exe.md)

## Source Verification

[source record](../../sources/lolbas/wfc.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mattifestation'
Person: Matt Graeber
- Handle: '@bohops'
Person: Jimmy
Author: Jimmy (@bohops)
Code_Sample:
- Code: https://bohops.com/2020/11/02/exploring-the-wdac-microsoft-recommended-block-rules-part-ii-wfc-fsi/
```
