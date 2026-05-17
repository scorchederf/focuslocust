---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Setupapi.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `setupapi.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Setupapi.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Setup Application Programming Interface

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/setupapi.dll.md)
- Source verification: [source record](../../sources/lolbas/setupapi.dll.md)

## Aliases

- `Setupapi.dll`
- `setupapi.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | Command metadata lists T1218.011: rundll32.exe setupapi.dll,InstallHinfSection DefaultInstall 128 {PATH_ABSOLUTE:.inf} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/setupapi.dll.md)

## Source Verification

[source record](../../sources/lolbas/setupapi.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@KyleHanslovan'
Person: Kyle Hanslovan (COM Scriptlet)
- Handle: '@HuntressLabs'
Person: Huntress Labs (COM Scriptlet)
- Handle: '@subTee'
Person: Casey Smith (COM Scriptlet)
- Handle: '@ItsReallyNick'
```
