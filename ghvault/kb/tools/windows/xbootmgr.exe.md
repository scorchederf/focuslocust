---
parsed_by: focuslocust
source: lolbas
type: generated
---
# XBootMgr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `xbootmgr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/XBootMgr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Windows Performance Toolkit binary used to start performance traces.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/xbootmgr.md)
- Source verification: [source record](../../sources/lolbas/xbootmgr.exe.md)

## Aliases

- `XBootMgr.exe`
- `xbootmgr.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: xbootmgr.exe -trace "{boot\|hibernate\|standby\|shutdown\|rebootCycle}" -preTraceCmd {PATH:.exe} |

## Source Verification

[source record](../../sources/lolbas/xbootmgr.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
- Person: Tommy Warren
Author: Avihay Eldad
Commands:
- Category: Execute
Command: xbootmgr.exe -trace "{boot|hibernate|standby|shutdown|rebootCycle}" -callBack {PATH:.exe}
```
