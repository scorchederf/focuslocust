---
parsed_by: focuslocust
source: lolbas
type: generated
---
# dtutil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dtutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dtutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft command line utility used to manage SQL Server Integration Services packages.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/dtutil.md)
- Source verification: [source record](../../sources/lolbas/dtutil.exe.md)

## Aliases

- `dtutil.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: dtutil.exe /FILE {PATH_ABSOLUTE:.source.ext} /COPY FILE;{PATH_ABSOLUTE:.dest.ext} |

## Source Verification

[source record](../../sources/lolbas/dtutil.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Copy
Command: dtutil.exe /FILE {PATH_ABSOLUTE:.source.ext} /COPY FILE;{PATH_ABSOLUTE:.dest.ext}
Description: Copy file from source to destination
```
