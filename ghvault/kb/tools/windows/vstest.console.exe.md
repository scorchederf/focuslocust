---
parsed_by: focuslocust
source: lolbas
type: generated
---
# vstest.console.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vstest.console.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/vstest.console.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

VSTest.Console.exe is the command-line tool to run tests

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/vstest.console.md)
- Source verification: [source record](../../sources/lolbas/vstest.console.exe.md)

## Aliases

- `vstest.console.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: vstest.console.exe {PATH:.dll} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/vstest.console.exe.md)

## Source Verification

[source record](../../sources/lolbas/vstest.console.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: Onat Uzunyayla
- Person: Ayberk Halac
Author: Onat Uzunyayla
Code_Sample:
- Code: https://github.com/onatuzunyayla/vstest-lolbin-example/
Commands:
- Category: AWL Bypass
```
