---
parsed_by: focuslocust
source: commands
type: generated
---
# Tttracer Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Tttracer.exe

Tool page: [Tttracer.exe](../../tools/windows/tttracer.exe.md)

### Spawn process using other binary

```text
tttracer.exe {PATH_ABSOLUTE:.exe}
```

Description:

Execute specified executable from tttracer.exe. Requires administrator privileges.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Tttracer.yml` |
| Evidence | Command preserved from source parser. |

### Dump process by PID

```text
TTTracer.exe -dumpFull -attach {PID}
```

Description:

Dumps process using tttracer.exe. Requires administrator privileges

Related ATT&CK:

- [T1003](../../attack/techniques/T1003-os-credential-dumping.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Tttracer.yml` |
| Evidence | Command preserved from source parser. |
