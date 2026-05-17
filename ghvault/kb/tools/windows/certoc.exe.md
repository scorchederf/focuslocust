---
parsed_by: focuslocust
source: lolbas
type: generated
---
# CertOC.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `certoc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certoc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used for installing certificates

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/certoc.md)
- Source verification: [source record](../../sources/lolbas/certoc.exe.md)

## Aliases

- `CertOC.exe`
- `certoc.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: certoc.exe -GetCACAPS {REMOTEURL:.ps1} |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: certoc.exe -LoadDLL {PATH_ABSOLUTE:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/certoc.exe.md)

## Source Verification

[source record](../../sources/lolbas/certoc.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@sblmsrsn'
Person: Ensar Samil
Author: Ensar Samil
Commands:
- Category: Execute
Command: certoc.exe -LoadDLL {PATH_ABSOLUTE:.dll}
Description: Loads the target DLL file
```
