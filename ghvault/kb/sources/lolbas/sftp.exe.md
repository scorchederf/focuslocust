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

## Generated Concept Page

- [Sftp.exe](../../tools/windows/sftp.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | sftp.exe |
| name | Sftp.exe |
| type | tool |
| source | lolbas |
| url | https://news.sophos.com/en-us/2025/05/09/lumma-stealer-coming-and-going/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@_swachchhanda_'
  Person: Swachchhanda Shrawan Poudel
Author: Swachchhanda Shrawan Poudel
Commands:
- Category: Execute
  Command: sftp -o ProxyCommand="{CMD}" .
  Description: Spawns ssh.exe which in turn spawns the specified command line. See also this project's entry for ssh.exe.
  MitreID: T1202
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Proxy execution of specified command, can be used as a defensive evasion.
Created: 2025-05-13
Description: sftp.exe is a Windows command-line utility that uses the Secure File Transfer Protocol (SFTP) to securely transfer
  files between a local machine and a remote server.
Detection:
- IOC: sftp.exe executions with ProxyCommand on the command line
- IOC: sftp.exe spawning ssh.exe with ProxyCommand on the command line
- Sigma: https://github.com/SigmaHQ/sigma/pull/5414/files
Full_Path:
- Path: C:\Windows\System32\OpenSSH\sftp.exe
Name: Sftp.exe
Resources:
- Link: https://news.sophos.com/en-us/2025/05/09/lumma-stealer-coming-and-going/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Sftp.yml
```

## Detection / Analysis Notes

```text
IOC: sftp.exe executions with ProxyCommand on the command line
```

```text
IOC: sftp.exe spawning ssh.exe with ProxyCommand on the command line
```

```text
Sigma: https://github.com/SigmaHQ/sigma/pull/5414/files
```

```text
- IOC: sftp.exe executions with ProxyCommand on the command line
- IOC: sftp.exe spawning ssh.exe with ProxyCommand on the command line
- Sigma: https://github.com/SigmaHQ/sigma/pull/5414/files
```
