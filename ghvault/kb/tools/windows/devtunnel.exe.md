---
parsed_by: focuslocust
source: lolbas
type: generated
---
# devtunnel.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `devtunnel.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/devtunnels.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary to enable forwarded ports on windows operating systems.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/devtunnel.md)
- Source verification: [source record](../../sources/lolbas/devtunnel.exe.md)

## Aliases

- `devtunnel.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: devtunnel.exe host -p 8080 |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/devtunnel.exe.md)

## Source Verification

[source record](../../sources/lolbas/devtunnel.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@deFr0ggy'
Person: Kamran Saifullah
Author: Kamran Saifullah
Commands:
- Category: Download
Command: devtunnel.exe host -p 8080
Description: Enabling a forwarded port for locally hosted service at port 8080 to be exposed on the internet.
```
