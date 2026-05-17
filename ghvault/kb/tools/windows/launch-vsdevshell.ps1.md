---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Launch-VsDevShell.ps1

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `launch-vsdevshell.ps1` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Launch-VsDevShell.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Locates and imports a Developer PowerShell module and calls the Enter-VsDevShell cmdlet

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/launch-vsdevshell.ps1.md)
- Source verification: [source record](../../sources/lolbas/launch-vsdevshell.ps1.md)

## Aliases

- `Launch-VsDevShell.ps1`
- `launch-vsdevshell.ps1`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1216 - System Script Proxy Execution](../../attack/techniques/T1216-system-script-proxy-execution.md) | explicit | source | Command metadata lists T1216: powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsInstallationPath "/../../../../../; {PATH:.exe} ;" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/launch-vsdevshell.ps1.md)

## Source Verification

[source record](../../sources/lolbas/launch-vsdevshell.ps1.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@nas_bench'
Person: Nasreddine Bencherchali
Author: Nasreddine Bencherchali
Commands:
- Category: Execute
Command: powershell -ep RemoteSigned -f .\Launch-VsDevShell.ps1 -VsWherePath {PATH_ABSOLUTE:.exe}
Description: Execute binaries from the context of the signed script using the "VsWherePath" flag.
```
