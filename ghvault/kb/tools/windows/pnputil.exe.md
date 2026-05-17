---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pnputil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pnputil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pnputil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Used for installing drivers

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/pnputil.md)
- Source verification: [source record](../../sources/lolbas/pnputil.exe.md)

## Aliases

- `Pnputil.exe`
- `pnputil.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1547 - Boot or Logon Autostart Execution](../../attack/techniques/T1547-boot-or-logon-autostart-execution.md) | explicit | source | Command metadata lists T1547: pnputil.exe -i -a {PATH_ABSOLUTE:.inf} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/pnputil.exe.md)

## Source Verification

[source record](../../sources/lolbas/pnputil.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@LuxNoBulIshit'
Person: Hai Vaknin(Lux)
- Handle: '@aloneliassaf'
Person: Avihay eldad
Author: Hai vaknin (lux)
Code_Sample:
- Code: https://github.com/LuxNoBulIshit/test.inf/blob/main/inf
```
