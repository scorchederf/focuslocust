---
parsed_by: focuslocust
source: lolbas
type: generated
---
# msedgewebview2.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msedgewebview2.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/msedgewebview2.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

msedgewebview2.exe is the executable file for Microsoft Edge WebView2, which is a web browser control used by applications to display web content.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/msedgewebview2.md)
- Source verification: [source record](../../sources/lolbas/msedgewebview2.exe.md)

## Aliases

- `msedgewebview2.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218.015 - Electron Applications](../../attack/techniques/T1218.015-electron-applications.md) | explicit | source | Command metadata lists T1218.015: msedgewebview2.exe --no-sandbox --renderer-cmd-prefix="{CMD}" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/msedgewebview2.exe.md)

## Source Verification

[source record](../../sources/lolbas/msedgewebview2.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@MalFuzzer'
Person: Uriel Kosayev
- Handle: '@VakninHai'
Person: Hai Vaknin
- Handle: '@Tamirye94'
Person: Tamir Yehuda
- Handle: '@Bl4ckShad3'
```
