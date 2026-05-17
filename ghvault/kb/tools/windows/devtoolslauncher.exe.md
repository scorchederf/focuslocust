---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Devtoolslauncher.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `devtoolslauncher.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Devtoolslauncher.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary will execute specified binary. Part of VS/VScode installation.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/devtoolslauncher.md)
- Source verification: [source record](../../sources/lolbas/devtoolslauncher.exe.md)

## Aliases

- `Devtoolslauncher.exe`
- `devtoolslauncher.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: devtoolslauncher.exe LaunchForDebug {PATH_ABSOLUTE:.exe} "{CMD:args}" test |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/devtoolslauncher.exe.md)

## Source Verification

[source record](../../sources/lolbas/devtoolslauncher.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@_felamos'
Person: felamos
Author: felamos
Commands:
- Category: Execute
Command: devtoolslauncher.exe LaunchForDeploy {PATH_ABSOLUTE:.exe} "{CMD:args}" test
Description: The above binary will execute other binary.
```
