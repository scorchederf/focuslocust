---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Logger.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `logger.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Logger.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

A logging configuration tool from the Windows Kits used to start and manage process logging.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/logger.md)
- Source verification: [source record](../../sources/lolbas/logger.exe.md)

## Aliases

- `Logger.exe`
- `logger.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: logger.exe "{CMD}" |

## Source Verification

[source record](../../sources/lolbas/logger.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
Command: logger.exe RUN "{CMD}"
Description: Executes the command specified after the `RUN` parameter as a child of `logger.exe`.
```
