---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ldifde.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ldifde.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ldifde.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Creates, modifies, and deletes LDAP directory objects.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ldifde.md)
- Source verification: [source record](../../sources/lolbas/ldifde.exe.md)

## Aliases

- `Ldifde.exe`
- `ldifde.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: Ldifde -i -f {PATH:.ldf} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/ldifde.exe.md)

## Source Verification

[source record](../../sources/lolbas/ldifde.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@0gtweet'
Person: Grzegorz Tworek
Author: Grzegorz Tworek
Commands:
- Category: Download
Command: Ldifde -i -f {PATH:.ldf}
Description: Import specified .ldf file into LDAP. If the file contains http-based attrval-spec such as `thumbnailPhoto:<
```
