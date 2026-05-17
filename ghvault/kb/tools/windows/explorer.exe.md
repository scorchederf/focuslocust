---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Explorer.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `explorer.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Explorer.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Binary used for managing files and system components within Windows

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/explorer.md)
- Source verification: [source record](../../sources/lolbas/explorer.exe.md)

## Aliases

- `Explorer.exe`
- `explorer.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: explorer.exe {PATH_ABSOLUTE:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/explorer.exe.md)

## Source Verification

[source record](../../sources/lolbas/explorer.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@CyberRaiju'
Person: Jai Minton
- Handle: '@bohops'
Person: Jimmy
Author: Jai Minton
Commands:
- Category: Execute
```
