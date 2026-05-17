---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Msconfig.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msconfig.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msconfig.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

MSConfig is a troubleshooting tool which is used to temporarily disable or re-enable software, device drivers or Windows services that run during startup process to help the user determine the cause of a problem with Windows

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/msconfig.md)
- Source verification: [source record](../../sources/lolbas/msconfig.exe.md)

## Aliases

- `Msconfig.exe`
- `msconfig.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: Msconfig.exe -5 |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/msconfig.exe.md)

## Source Verification

[source record](../../sources/lolbas/msconfig.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken
Author: Oddvar Moe
Code_Sample:
- Code: https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS/master/OSBinaries/Payload/mscfgtlc.xml
Commands:
- Category: Execute
```
