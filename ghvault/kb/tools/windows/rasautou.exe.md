---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Rasautou.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `rasautou.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Rasautou.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Remote Access Dialer

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/rasautou.md)
- Source verification: [source record](../../sources/lolbas/rasautou.exe.md)

## Aliases

- `Rasautou.exe`
- `rasautou.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: rasautou -d {PATH:.dll} -p export_name -a a -e e |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/rasautou.exe.md)

## Source Verification

[source record](../../sources/lolbas/rasautou.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@FireEye'
Person: FireEye
Author: Tony Lambert
Commands:
- Category: Execute
Command: rasautou -d {PATH:.dll} -p export_name -a a -e e
Description: Loads the target .DLL specified in -d and executes the export specified in -p. Options removed in Windows 10.
```
