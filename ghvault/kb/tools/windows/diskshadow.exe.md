---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Diskshadow.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `diskshadow.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Diskshadow.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Diskshadow.exe is a tool that exposes the functionality offered by the volume shadow copy Service (VSS).

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/diskshadow.md)
- Source verification: [source record](../../sources/lolbas/diskshadow.exe.md)

## Aliases

- `Diskshadow.exe`
- `diskshadow.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003.003 - NTDS](../../attack/techniques/T1003.003-ntds.md) | explicit | source | Command metadata lists T1003.003: diskshadow.exe /s {PATH:.txt} |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: diskshadow> exec {PATH:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/diskshadow.exe.md)

## Source Verification

[source record](../../sources/lolbas/diskshadow.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: Jimmy
Author: Oddvar Moe
Commands:
- Category: Dump
Command: diskshadow.exe /s {PATH:.txt}
Description: Execute commands using diskshadow.exe from a prepared diskshadow script.
```
