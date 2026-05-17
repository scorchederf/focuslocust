---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Sftp.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `sftp.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Sftp.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Summary

sftp.exe is a Windows command-line utility that uses the Secure File Transfer Protocol (SFTP) to securely transfer files between a local machine and a remote server.

## Fast Retrieval

- Platform: `windows`
- Command page: [commands](../../commands/windows/sftp.md)
- Source verification: [source record](../../sources/lolbas/sftp.exe.md)

## Aliases

- `Sftp.exe`
- `sftp.exe`

## Related ATT&CK Techniques

| Item | Relationship | Confidence | Evidence |
| --- | --- | --- | --- |
| [T1202 - Indirect Command Execution](../../attack/techniques/T1202-indirect-command-execution.md) | explicit | source | Command metadata lists T1202: sftp -o ProxyCommand="{CMD}" . |

## Detection / Analysis Notes

This source record contains detection or analysis material. It is preserved on the source-record page rather than promoted into a full detection engineering page.

[source record](../../sources/lolbas/sftp.exe.md)

## Source Verification

[source record](../../sources/lolbas/sftp.exe.md)

## Evidence Excerpt

```text
Acknowledgement:
- Handle: '@_swachchhanda_'
Person: Swachchhanda Shrawan Poudel
Author: Swachchhanda Shrawan Poudel
Commands:
- Category: Execute
Command: sftp -o ProxyCommand="{CMD}" .
Description: Spawns ssh.exe which in turn spawns the specified command line. See also this project's entry for ssh.exe.
```
