---
parsed_by: focuslocust
source: lolbas
type: generated
---
# CustomShellHost.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `customshellhost.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/CustomShellHost.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

A host process that is used by custom shells when using Windows in Kiosk mode.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/customshellhost.md)
- Source verification: [source record](../../sources/lolbas/customshellhost.exe.md)

## Aliases

- `CustomShellHost.exe`
- `customshellhost.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: CustomShellHost.exe |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/customshellhost.exe.md)

## Source Verification

[source record](../../sources/lolbas/customshellhost.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@YoSignals'
Person: John Carroll
Author: Wietze Beukema
Commands:
- Category: Execute
Command: CustomShellHost.exe
Description: Executes explorer.exe (with command-line argument /NoShellRegistrationCheck) if present in the current working
```
