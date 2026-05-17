---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Fsutil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `fsutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Fsutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

File System Utility

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/fsutil.md)
- Source verification: [source record](../../sources/lolbas/fsutil.exe.md)

## Aliases

- `Fsutil.exe`
- `fsutil.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: fsutil.exe trace decode |
| [T1485 - Data Destruction](../../attack/techniques/T1485-data-destruction.md) | explicit | source | Command metadata lists T1485: fsutil.exe usn deletejournal /d c: |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/fsutil.exe.md)

## Source Verification

[source record](../../sources/lolbas/fsutil.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@elliotkillick'
Person: Elliot Killick
- Handle: '@bohops'
Person: Jimmy
- Handle: '@0gtweet'
Person: Grzegorz Tworek
Author: Elliot Killick
```
