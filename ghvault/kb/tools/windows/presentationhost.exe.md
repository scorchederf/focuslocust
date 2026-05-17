---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Presentationhost.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `presentationhost.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Presentationhost.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

File is used for executing Browser applications

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/presentationhost.md)
- Source verification: [source record](../../sources/lolbas/presentationhost.exe.md)

## Aliases

- `Presentationhost.exe`
- `presentationhost.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: Presentationhost.exe {REMOTEURL} |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: Presentationhost.exe {PATH_ABSOLUTE:.xbap} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/presentationhost.exe.md)

## Source Verification

[source record](../../sources/lolbas/presentationhost.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
- Handle: '@C_h4ck_0'
Person: Nir Chako (Pentera)
Author: Oddvar Moe
Commands:
- Category: Execute
```
