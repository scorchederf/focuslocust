---
parsed_by: focuslocust
source: commands
type: generated
---
# Mpiexec Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Mpiexec.exe

Tool page: [Mpiexec.exe](../../tools/windows/mpiexec.exe.md)

### Executes commands under a trusted, Microsoft signed binary.

```text
mpiexec.exe {CMD}
```

Description:

Executes a command via MPI command-line tool.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Mpiexec.yml` |
| Evidence | Command preserved from source parser. |
