---
parsed_by: focuslocust
source: commands
type: generated
---
# Createdump Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Createdump.exe

Tool page: [Createdump.exe](../../tools/windows/createdump.exe.md)

### Dump process memory contents using PID.

```text
createdump.exe -n -f {PATH:.dmp} {PID}
```

Description:

Dump process by PID and create a minidump file. If "-f dump.dmp" is not specified, the file is created as '%TEMP%\dump.%p.dmp' where %p is the PID of the target process.

Related ATT&CK:

- [T1003](../../attack/techniques/T1003-os-credential-dumping.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Createdump.yml` |
| Evidence | Command preserved from source parser. |
