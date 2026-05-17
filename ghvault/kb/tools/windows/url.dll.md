---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Url.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `url.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Url.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Internet Shortcut Shell Extension DLL.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/url.dll.md)
- Source verification: [source record](../../sources/lolbas/url.dll.md)

## Aliases

- `Url.dll`
- `url.dll`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.011 - Rundll32](../../attack/techniques/T1218.011-rundll32.md) | explicit | source | Command metadata lists T1218.011: rundll32.exe url.dll,FileProtocolHandler file:///C:/test/test.hta |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/url.dll.md)

## Source Verification

[source record](../../sources/lolbas/url.dll.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@hexacorn'
Person: Adam (OpenURL)
- Handle: '@bohops'
Person: Jimmy (OpenURL)
- Handle: '@DissectMalware'
Person: Malwrologist (FileProtocolHandler - HTA)
- Handle: '@r0lan'
```
