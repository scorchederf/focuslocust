---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Shell32.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `shell32.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Shell32.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Shell Common Dll

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/shell32.dll.md)
- Source verification: [source record](../../sources/lolbas/shell32.dll.md)

## Aliases

- `Shell32.dll`
- `shell32.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | Command metadata lists T1218.011: rundll32.exe shell32.dll,#44 {PATH:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/shell32.dll.md)

## Source Verification

[source record](../../sources/lolbas/shell32.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@hexacorn'
Person: Adam (Control_RunDLL, Control_RunDLLNoFallback)
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken (ShellExec_RunDLL)
- Handle: '@mattifestation'
Person: Matt Graeber (ShellExec_RunDLL)
- Handle: '@KyleHanslovan'
```
