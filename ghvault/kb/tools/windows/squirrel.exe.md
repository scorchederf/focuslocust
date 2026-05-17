---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Squirrel.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `squirrel.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Squirrel.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary to update the existing installed Nuget/squirrel package. Part of Microsoft Teams installation.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/squirrel.md)
- Source verification: [source record](../../sources/lolbas/squirrel.exe.md)

## Aliases

- `Squirrel.exe`
- `squirrel.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: squirrel.exe --updateRollback={REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/squirrel.exe.md)

## Source Verification

[source record](../../sources/lolbas/squirrel.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@reegun21'
Person: Reegun J (OCBC Bank)
- Handle: '@Hexacorn'
Person: Adam
Author: Reegun J (OCBC Bank) - @reegun21
Code_Sample:
- Code: https://github.com/jreegun/POC-s/tree/master/nuget-squirrel
```
