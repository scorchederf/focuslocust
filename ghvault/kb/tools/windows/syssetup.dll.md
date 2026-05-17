---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Syssetup.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `syssetup.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Syssetup.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows NT System Setup

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/syssetup.dll.md)
- Source verification: [source record](../../sources/lolbas/syssetup.dll.md)

## Aliases

- `Syssetup.dll`
- `syssetup.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | Command metadata lists T1218.011: rundll32 syssetup.dll,SetupInfObjectInstallAction DefaultInstall 128 {PATH_ABSOLUTE:.inf} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/syssetup.dll.md)

## Source Verification

[source record](../../sources/lolbas/syssetup.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken (Execute)
- Handle: '@harr0ey'
Person: Matt harr0ey (Execute)
- Handle: '@bohops'
Person: Jimmy (Scriptlet)
Author: LOLBAS Team
```
