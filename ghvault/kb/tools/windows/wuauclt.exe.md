---
parsed_by: focuslocust
source: lolbas
type: generated
---
# wuauclt.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wuauclt.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wuauclt.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Update Client

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/wuauclt.md)
- Source verification: [source record](../../sources/lolbas/wuauclt.exe.md)

## Aliases

- `wuauclt.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: wuauclt.exe /UpdateDeploymentProvider {PATH_ABSOLUTE:.dll} /RunHandlerComServer |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/wuauclt.exe.md)

## Source Verification

[source record](../../sources/lolbas/wuauclt.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@dtmsecurity'
Person: David Middlehurst
Author: David Middlehurst
Commands:
- Category: Execute
Command: wuauclt.exe /UpdateDeploymentProvider {PATH_ABSOLUTE:.dll} /RunHandlerComServer
Description: Loads and executes DLL code on attach.
```
