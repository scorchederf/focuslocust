---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AddinUtil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `addinutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Addinutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

.NET Tool used for updating cache files for Microsoft Office Add-Ins.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/addinutil.md)
- Source verification: [source record](../../sources/lolbas/addinutil.exe.md)

## Aliases

- `AddinUtil.exe`
- `addinutil.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: C:\Windows\Microsoft.NET\Framework\v4.0.30319\AddinUtil.exe -AddinRoot:. |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/addinutil.exe.md)

## Source Verification

[source record](../../sources/lolbas/addinutil.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@MckinleyMike'
Person: Michael McKinley
- Handle: '@TheLatteri'
Person: Tony Latteri
Author: Michael McKinley @MckinleyMike
Code_Sample:
- Code: https://gist.github.com/SILJAEUROPA/a850d476179d73df230a876944e9f3b1#file-addins-store
```
