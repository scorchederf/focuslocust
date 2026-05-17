---
parsed_by: focuslocust
source: lolbas
type: generated
---
# CL_Invocation.ps1

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cl-invocation.ps1` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Cl_invocation.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Aero diagnostics script

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/cl-invocation.ps1.md)
- Source verification: [source record](../../sources/lolbas/cl-invocation.ps1.md)

## Aliases

- `CL_Invocation.ps1`
- `cl-invocation.ps1`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1216 - System Script Proxy Execution](../../attack/techniques/T1216-system-script-proxy-execution.md) | explicit | source | Command metadata lists T1216: . C:\Windows\diagnostics\system\AERO\CL_Invocation.ps1 \nSyncInvoke {CMD} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/cl-invocation.ps1.md)

## Source Verification

[source record](../../sources/lolbas/cl-invocation.ps1.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: Jimmy
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken
Author: Oddvar Moe
Commands:
- Category: Execute
```
