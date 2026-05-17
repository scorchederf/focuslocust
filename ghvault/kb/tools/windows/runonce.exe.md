---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Runonce.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `runonce.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Runonce.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Executes a Run Once Task that has been configured in the registry

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/runonce.md)
- Source verification: [source record](../../sources/lolbas/runonce.exe.md)

## Aliases

- `Runonce.exe`
- `runonce.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: Runonce.exe /AlternateShellStartup |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/runonce.exe.md)

## Source Verification

[source record](../../sources/lolbas/runonce.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken
Author: Oddvar Moe
Commands:
- Category: Execute
Command: Runonce.exe /AlternateShellStartup
Description: Executes a Run Once Task that has been configured in the registry.
```
