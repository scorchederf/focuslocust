---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pixtool.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pixtool.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Pixtool.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Command line utility for taking and analyzing PIX GPU captures.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/pixtool.md)
- Source verification: [source record](../../sources/lolbas/pixtool.exe.md)

## Aliases

- `Pixtool.exe`
- `pixtool.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: pixtool.exe launch {PATH_ABSOLUTE:.exe} |

## Source Verification

[source record](../../sources/lolbas/pixtool.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
Command: pixtool.exe launch {PATH_ABSOLUTE:.exe}
Description: Launches an executable via PIX command-line utility.
```
