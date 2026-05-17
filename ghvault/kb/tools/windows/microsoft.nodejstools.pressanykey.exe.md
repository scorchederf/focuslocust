---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Microsoft.NodejsTools.PressAnyKey.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `microsoft.nodejstools.pressanykey.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Microsoft.NodejsTools.PressAnyKey.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Part of the NodeJS Visual Studio tools.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/microsoft.nodejstools.pressanykey.md)
- Source verification: [source record](../../sources/lolbas/microsoft.nodejstools.pressanykey.exe.md)

## Aliases

- `Microsoft.NodejsTools.PressAnyKey.exe`
- `microsoft.nodejstools.pressanykey.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: Microsoft.NodejsTools.PressAnyKey.exe normal 1 {PATH:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/microsoft.nodejstools.pressanykey.exe.md)

## Source Verification

[source record](../../sources/lolbas/microsoft.nodejstools.pressanykey.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mrd0x'
Person: mr.d0x
Author: mr.d0x
Commands:
- Category: Execute
Command: Microsoft.NodejsTools.PressAnyKey.exe normal 1 {PATH:.exe}
Description: Launch specified executable as a subprocess of Microsoft.NodejsTools.PressAnyKey.exe.
```
