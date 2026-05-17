---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Extexport.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `extexport.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Extexport.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Load a DLL located in the c:\test folder with a specific name.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/extexport.md)
- Source verification: [source record](../../sources/lolbas/extexport.exe.md)

## Aliases

- `Extexport.exe`
- `extexport.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: Extexport.exe {PATH_ABSOLUTE:folder} foo bar |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/extexport.exe.md)

## Source Verification

[source record](../../sources/lolbas/extexport.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@hexacorn'
Person: Adam
Author: Oddvar Moe
Commands:
- Category: Execute
Command: Extexport.exe {PATH_ABSOLUTE:folder} foo bar
Description: Load a DLL located in the specified folder with one of the following names mozcrt19.dll, mozsqlite3.dll, or
```
