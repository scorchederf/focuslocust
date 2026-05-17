---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Msdeploy.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msdeploy.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msdeploy.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft tool used to deploy Web Applications.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/msdeploy.md)
- Source verification: [source record](../../sources/lolbas/msdeploy.exe.md)

## Aliases

- `Msdeploy.exe`
- `msdeploy.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: msdeploy.exe -verb:sync -source:filePath={PATH_ABSOLUTE:.source.ext} -dest:filePath={PATH_ABSOLUTE:.dest.ext} |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: msdeploy.exe -verb:sync -source:RunCommand -dest:runCommand="{PATH_ABSOLUTE:.bat}" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/msdeploy.exe.md)

## Source Verification

[source record](../../sources/lolbas/msdeploy.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@pabraeken'
Person: Pierre-Alexandre Braeken
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Oddvar Moe
Commands:
- Category: Execute
```
