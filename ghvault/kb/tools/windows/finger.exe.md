---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Finger.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `finger.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Finger.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Displays information about a user or users on a specified remote computer that is running the Finger service or daemon

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/finger.md)
- Source verification: [source record](../../sources/lolbas/finger.exe.md)

## Aliases

- `Finger.exe`
- `finger.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: finger user@example.host.com \| more +2 \| cmd |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/finger.exe.md)

## Source Verification

[source record](../../sources/lolbas/finger.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@rubn_RB'
Person: Ruben Revuelta (MAPFRE CERT)
- Handle: '@Ocelotty6669'
Person: Jose A. Jimenez (MAPFRE CERT)
- Handle: '@DissectMalware'
Person: Malwrologist
Author: Ruben Revuelta
```
