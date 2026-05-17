---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Remote.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `remote.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Remote.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Debugging tool included with Windows Debugging Tools

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/remote.md)
- Source verification: [source record](../../sources/lolbas/remote.exe.md)

## Aliases

- `Remote.exe`
- `remote.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: Remote.exe /s {PATH_SMB:.exe} anythinghere |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/remote.exe.md)

## Source Verification

[source record](../../sources/lolbas/remote.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@mrd0x'
Person: mr.d0x
Author: mr.d0x
Commands:
- Category: AWL Bypass
Command: Remote.exe /s {PATH:.exe} anythinghere
Description: Spawns specified executable as a child process of remote.exe
```
