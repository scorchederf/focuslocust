---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Bginfo.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `bginfo.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Bginfo.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Background Information Utility included with SysInternals Suite

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/bginfo.md)
- Source verification: [source record](../../sources/lolbas/bginfo.exe.md)

## Aliases

- `Bginfo.exe`
- `bginfo.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: \\live.sysinternals.com\Tools\bginfo.exe {PATH_SMB:.bgi} /popup /nolicprompt |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/bginfo.exe.md)

## Source Verification

[source record](../../sources/lolbas/bginfo.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
Author: Oddvar Moe
Commands:
- Category: Execute
Command: bginfo.exe {PATH:.bgi} /popup /nolicprompt
Description: Execute VBscript code that is referenced within the specified .bgi file.
```
