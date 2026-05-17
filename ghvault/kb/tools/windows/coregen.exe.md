---
parsed_by: focuslocust
source: lolbas
type: generated
---
# coregen.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `coregen.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Coregen.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary coregen.exe (Microsoft CoreCLR Native Image Generator) loads exported function GetCLRRuntimeHost from coreclr.dll or from .DLL in arbitrary path. Coregen is located within "C:\Program Files (x86)\Microsoft Silverlight\5.1.50918.0\" or another version of Silverlight. Coregen is signed by Microsoft and bundled with Microsoft Silverlight.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/coregen.md)
- Source verification: [source record](../../sources/lolbas/coregen.exe.md)

## Aliases

- `coregen.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1055 - Process Injection](../../attack/techniques/T1055-process-injection.md) | explicit | source | Command metadata lists T1055: coregen.exe dummy_assembly_name |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: coregen.exe /L {PATH_ABSOLUTE:.dll} dummy_assembly_name |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/coregen.exe.md)

## Source Verification

[source record](../../sources/lolbas/coregen.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: Nicky Tyrer
- Person: Evan Pena
- Person: Casey Erikson
Author: Martin Sohn Christensen
Commands:
- Category: Execute
Command: coregen.exe /L {PATH_ABSOLUTE:.dll} dummy_assembly_name
```
