---
parsed_by: focuslocust
source: commands
type: generated
---
# Mftrace Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Mftrace.exe

Tool page: [Mftrace.exe](../../tools/windows/mftrace.exe.md)

### Local execution of cmd.exe as a subprocess of Mftrace.exe.

```text
Mftrace.exe {PATH:.exe}
```

Description:

Launch specified executable as a subprocess of Mftrace.exe.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Mftrace.yml` |
| Evidence | Command preserved from source parser. |
