---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ie4uinit.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ie4uinit.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ie4uinit.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Executes commands from a specially prepared ie4uinit.inf file.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ie4uinit.md)
- Source verification: [source record](../../sources/lolbas/ie4uinit.exe.md)

## Aliases

- `Ie4uinit.exe`
- `ie4uinit.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: ie4uinit.exe -BaseSettings |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/ie4uinit.exe.md)

## Source Verification

[source record](../../sources/lolbas/ie4uinit.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: Jimmy
Author: Oddvar Moe
Commands:
- Category: Execute
Command: ie4uinit.exe -BaseSettings
Description: Executes commands from a specially prepared ie4uinit.inf file.
```
