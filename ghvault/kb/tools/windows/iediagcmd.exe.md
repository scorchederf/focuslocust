---
parsed_by: focuslocust
source: lolbas
type: generated
---
# iediagcmd.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `iediagcmd.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Iediagcmd.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Diagnostics Utility for Internet Explorer

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/iediagcmd.md)
- Source verification: [source record](../../sources/lolbas/iediagcmd.exe.md)

## Aliases

- `iediagcmd.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: set windir=c:\test& cd "C:\Program Files\Internet Explorer\" & iediagcmd.exe /out:{PATH_ABSOLUTE:.cab} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/iediagcmd.exe.md)

## Source Verification

[source record](../../sources/lolbas/iediagcmd.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@hexacorn'
Person: Adam
Author: manasmbellani
Commands:
- Category: Execute
Command: set windir=c:\test& cd "C:\Program Files\Internet Explorer\" & iediagcmd.exe /out:{PATH_ABSOLUTE:.cab}
Description: Executes binary that is pre-planted at C:\test\system32\netsh.exe.
```
