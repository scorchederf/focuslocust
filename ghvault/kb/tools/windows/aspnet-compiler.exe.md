---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Aspnet_Compiler.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `aspnet-compiler.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Aspnet_Compiler.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

ASP.NET Compilation Tool

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/aspnet-compiler.md)
- Source verification: [source record](../../sources/lolbas/aspnet-compiler.exe.md)

## Aliases

- `Aspnet_Compiler.exe`
- `aspnet-compiler.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_compiler.exe -v none -p C:\users\cpl.internal\desktop\asptest\ -f C:\users\cpl.internal\desktop\asptest\none -u |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/aspnet-compiler.exe.md)

## Source Verification

[source record](../../sources/lolbas/aspnet-compiler.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@cpl3h'
Person: cpl
Author: Jimmy (@bohops)
Code_Sample:
- Code: https://github.com/ThunderGunExpress/BringYourOwnBuilder
Commands:
- Category: AWL Bypass
```
