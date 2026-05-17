---
parsed_by: focuslocust
source: commands
type: generated
---
# Aspnet_Compiler Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Aspnet_Compiler.exe

Tool page: [Aspnet_Compiler.exe](../../tools/windows/aspnet-compiler.exe.md)

### Execute proxied payload with Microsoft signed binary to bypass application control solutions

```text
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_compiler.exe -v none -p C:\users\cpl.internal\desktop\asptest\ -f C:\users\cpl.internal\desktop\asptest\none -u
```

Description:

Execute C# code with the Build Provider and proper folder structure in place.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Aspnet_Compiler.yml` |
| Evidence | Command preserved from source parser. |
