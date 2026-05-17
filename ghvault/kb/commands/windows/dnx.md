---
parsed_by: focuslocust
source: commands
type: generated
---
# dnx Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## dnx.exe

Tool page: [dnx.exe](../../tools/windows/dnx.exe.md)

### Local execution of C# project stored in consoleapp folder.

```text
dnx.exe {PATH_ABSOLUTE:folder}
```

Description:

Execute C# code located in the specified folder via 'Program.cs' and 'Project.json' (Note - Requires dependencies)

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dnx.yml` |
| Evidence | Command preserved from source parser. |
