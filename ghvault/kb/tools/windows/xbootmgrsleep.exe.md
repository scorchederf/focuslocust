---
parsed_by: focuslocust
source: lolbas
type: generated
---
# XBootMgrSleep.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `xbootmgrsleep.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/XBootMgrSleep.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Performance Toolkit binary used for tracing and analyzing system performance during sleep and resume transitions.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/xbootmgrsleep.md)
- Source verification: [source record](../../sources/lolbas/xbootmgrsleep.exe.md)

## Aliases

- `XBootMgrSleep.exe`
- `xbootmgrsleep.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: xbootmgrsleep.exe 1000 {PATH:.exe} |

## Source Verification

[source record](../../sources/lolbas/xbootmgrsleep.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
- Handle: '@yuvalsaban3'
Person: Yuval Saban
Author: Avihay Eldad
Commands:
- Category: Execute
```
