---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ttdinject.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ttdinject.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ttdinject.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by Windows 1809 and newer to Debug Time Travel (Underlying call of tttracer.exe)

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ttdinject.md)
- Source verification: [source record](../../sources/lolbas/ttdinject.exe.md)

## Aliases

- `Ttdinject.exe`
- `ttdinject.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: ttdinject.exe /ClientScenario TTDRecorder /ddload 0 /ClientParams "7 tmp.run 0 0 0 0 0 0 0 0 0 0" /launch "{PATH:.exe}" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/ttdinject.exe.md)

## Source Verification

[source record](../../sources/lolbas/ttdinject.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oddvarmoe'
Person: Oddvar Moe
- Handle: '@m_nad0'
Person: Maxime Nadeau
Author: Maxime Nadeau
Commands:
- Category: Execute
```
