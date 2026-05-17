---
parsed_by: focuslocust
source: lolbas
type: generated
---
# IntelliTrace.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `intellitrace.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/IntelliTrace.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Visual Studio command-line tool for collecting and managing diagnostic trace files.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/intellitrace.md)
- Source verification: [source record](../../sources/lolbas/intellitrace.exe.md)

## Aliases

- `IntelliTrace.exe`
- `intellitrace.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: IntelliTrace.exe launch /cp:"collectionplan.xml" /f:"c:\users\public\log" "C:\Windows\System32\calc.exe" |

## Source Verification

[source record](../../sources/lolbas/intellitrace.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
Command: IntelliTrace.exe launch /cp:"collectionplan.xml" /f:"c:\users\public\log" "C:\Windows\System32\calc.exe"
Description: Launches an executable via Visual Studio command line utility.
```
