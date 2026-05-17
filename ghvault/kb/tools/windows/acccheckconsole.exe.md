---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AccCheckConsole.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `acccheckconsole.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/AccCheckConsole.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Verifies UI accessibility requirements

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/acccheckconsole.md)
- Source verification: [source record](../../sources/lolbas/acccheckconsole.exe.md)

## Aliases

- `AccCheckConsole.exe`
- `acccheckconsole.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: AccCheckConsole.exe -window "Untitled - Notepad" {PATH_ABSOLUTE:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/acccheckconsole.exe.md)

## Source Verification

[source record](../../sources/lolbas/acccheckconsole.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: Jimmy
Author: bohops
Code_Sample:
- Code: https://docs.microsoft.com/en-us/windows/win32/winauto/custom-verification-routines
Commands:
- Category: Execute
```
