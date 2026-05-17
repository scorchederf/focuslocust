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

## Generated Concept Page

- [ssh.exe](../../tools/windows/ssh.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ssh.exe |
| name | ssh.exe |
| type | tool |
| source | lolbas |
| url | https://gtfobins.github.io/gtfobins/ssh/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: Akshat Pradhan
- Person: Felix Boulet
Author: Akshat Pradhan
Commands:
- Category: Execute
  Command: ssh localhost "{CMD}"
  Description: Executes specified command on host machine. The prompt for password can be eliminated by adding the host's
    public key in the user's authorized_keys file. Adversaries can do the same for execution on remote machines.
  MitreID: T1202
  OperatingSystem: Windows 10 1809, Windows Server 2019
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Execute specified command, can be used for defense evasion.
- Category: Execute
  Command: ssh -o ProxyCommand="{CMD}" .
  Description: Executes specified command from ssh.exe
  MitreID: T1202
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Performs execution of specified file, can be used as a defensive evasion.
Created: 2021-11-08
Description: Ssh.exe is the OpenSSH compatible client can be used to connect to Windows 10 (build 1809 and later) and Windows
  Server 2019 devices.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_ssh.yml
- IOC: Event ID 4624 with process name C:\Windows\System32\OpenSSH\sshd.exe.
- IOC: command line arguments specifying execution.
Full_Path:
- Path: c:\windows\system32\OpenSSH\ssh.exe
Name: ssh.exe
Resources:
- Link: https://gtfobins.github.io/gtfobins/ssh/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ssh.yml
```

## Detection / Analysis Notes

```text
IOC: Event ID 4624 with process name C:\Windows\System32\OpenSSH\sshd.exe.
```

```text
IOC: command line arguments specifying execution.
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_ssh.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_ssh.yml
- IOC: Event ID 4624 with process name C:\Windows\System32\OpenSSH\sshd.exe.
- IOC: command line arguments specifying execution.
```
