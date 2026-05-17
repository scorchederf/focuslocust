---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Appvlp.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `appvlp.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Appvlp.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Application Virtualization Utility Included with Microsoft Office 2016

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/appvlp.md)
- Source verification: [source record](../../sources/lolbas/appvlp.exe.md)

## Aliases

- `Appvlp.exe`
- `appvlp.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: AppVLP.exe powershell.exe -c "$e=New-Object -ComObject shell.application;$e.ShellExecute('{PATH:.exe}','', '', 'open', 1)" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/appvlp.exe.md)

## Source Verification

[source record](../../sources/lolbas/appvlp.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@0rbz_'
Person: fab
- Handle: '@moo_hax'
Person: Will
- Handle: '@enigma0x3'
Person: Matt Wilson
Author: Oddvar Moe
```
