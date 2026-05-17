---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Tttracer.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `tttracer.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Tttracer.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used by Windows 1809 and newer to Debug Time Travel

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/tttracer.md)
- Source verification: [source record](../../sources/lolbas/tttracer.exe.md)

## Aliases

- `Tttracer.exe`
- `tttracer.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1003 - OS Credential Dumping](../../attack/techniques/T1003-os-credential-dumping.md) | explicit | source | Command metadata lists T1003: TTTracer.exe -dumpFull -attach {PID} |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: tttracer.exe {PATH_ABSOLUTE:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/tttracer.exe.md)

## Source Verification

[source record](../../sources/lolbas/tttracer.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@oulusoyum'
Person: Onur Ulusoy
- Handle: '@mattifestation'
Person: Matt Graeber
Author: Oddvar Moe
Commands:
- Category: Execute
```
