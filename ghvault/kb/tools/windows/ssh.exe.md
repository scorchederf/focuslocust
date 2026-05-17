---
parsed_by: focuslocust
source: lolbas
type: generated
---
# ssh.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ssh.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ssh.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

Ssh.exe is the OpenSSH compatible client can be used to connect to Windows 10 (build 1809 and later) and Windows Server 2019 devices.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/ssh.md)
- Source verification: [source record](../../sources/lolbas/ssh.exe.md)

## Aliases

- `ssh.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: ssh -o ProxyCommand="{CMD}" . |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/ssh.exe.md)

## Source Verification

[source record](../../sources/lolbas/ssh.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Person: Akshat Pradhan
- Person: Felix Boulet
Author: Akshat Pradhan
Commands:
- Category: Execute
Command: ssh localhost "{CMD}"
Description: Executes specified command on host machine. The prompt for password can be eliminated by adding the host's
```
