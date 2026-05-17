---
parsed_by: focuslocust
source: lolbas
type: generated
---
# AppLauncher.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `applauncher.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/AppLauncher.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

User Experience Virtualization tool that launches applications under monitoring to capture and synchronize user settings.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/applauncher.md)
- Source verification: [source record](../../sources/lolbas/applauncher.exe.md)

## Aliases

- `AppLauncher.exe`
- `applauncher.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: AppLauncher.exe {PATH_ABSOLUTE:.exe} |

## Source Verification

[source record](../../sources/lolbas/applauncher.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Execute
Command: AppLauncher.exe {PATH_ABSOLUTE:.exe}
Description: Launches an executable via User Experience Virtualization tool.
```
