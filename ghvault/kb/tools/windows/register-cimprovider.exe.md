---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Register-cimprovider.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `register-cimprovider.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Register-cimprovider.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used to register new wmi providers

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/register-cimprovider.md)
- Source verification: [source record](../../sources/lolbas/register-cimprovider.exe.md)

## Aliases

- `Register-cimprovider.exe`
- `register-cimprovider.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: Register-cimprovider -path {PATH_ABSOLUTE:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/register-cimprovider.exe.md)

## Source Verification

[source record](../../sources/lolbas/register-cimprovider.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@PhilipTsukerman'
Person: Philip Tsukerman
Author: Oddvar Moe
Commands:
- Category: Execute
Command: Register-cimprovider -path {PATH_ABSOLUTE:.dll}
Description: Load the target .DLL.
```
