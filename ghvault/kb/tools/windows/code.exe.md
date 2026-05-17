---
parsed_by: focuslocust
source: lolbas
type: generated
---
# code.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `code.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/HonorableMentions/Code.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

VSCode binary, also portable (CLI) version

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/code.md)
- Source verification: [source record](../../sources/lolbas/code.exe.md)

## Aliases

- `code.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1219.001 - IDE Tunneling](../../attack/techniques/T1219.001-ide-tunneling.md) | explicit | source | Command metadata lists T1219.001: code.exe tunnel --accept-server-license-terms --name "tunnel-name" |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/code.exe.md)

## Source Verification

[source record](../../sources/lolbas/code.exe.md)

## Evidence Excerpt

```text
Author: PfiatDe
Commands:
- Category: Execute
Command: code.exe tunnel --accept-server-license-terms --name "tunnel-name"
Description: Starts a reverse PowerShell connection over global.rel.tunnels.api.visualstudio.com via websockets; command
MitreID: T1219.001
OperatingSystem: Windows 10, Windows 11
Privileges: User
```
