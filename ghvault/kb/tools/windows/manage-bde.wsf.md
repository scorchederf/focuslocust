---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Manage-bde.wsf

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `manage-bde.wsf` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSScripts/Manage-bde.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Script for managing BitLocker

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/manage-bde.wsf.md)
- Source verification: [source record](../../sources/lolbas/manage-bde.wsf.md)

## Aliases

- `Manage-bde.wsf`
- `manage-bde.wsf`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1216 - System Script Proxy Execution](../../attack/techniques/T1216-system-script-proxy-execution.md) | explicit | source | Command metadata lists T1216: copy c:\users\person\evil.exe c:\users\public\manage-bde.exe & cd c:\users\public\ & cscript.exe c:\windows\system32\manage-bde.wsf |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/manage-bde.wsf.md)

## Source Verification

[source record](../../sources/lolbas/manage-bde.wsf.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@bohops'
Person: Jimmy
- Handle: '@danielbohannon'
Person: Daniel Bohannon
- Handle: '@JohnLaTwC'
Person: John Lambert
Author: Oddvar Moe
```
