---
parsed_by: focuslocust
source: commands
type: generated
---
# Csc Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Csc.exe

Tool page: [Csc.exe](../../tools/windows/csc.exe.md)

### Compile attacker code on system. Bypass defensive counter measures.

```text
csc.exe -out:{PATH:.exe} {PATH:.cs}
```

Description:

Use csc.exe to compile C# code, targeting the .NET Framework, stored in the specified .cs file and output the compiled version to the specified .exe path.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Csc.yml` |
| Evidence | Command preserved from source parser. |

### Compile attacker code on system. Bypass defensive counter measures.

```text
csc -target:library {PATH:.cs}
```

Description:

Use csc.exe to compile C# code, targeting the .NET Framework, stored in the specified .cs file and output the compiled version to a DLL file with the same name.

Related ATT&CK:

- [T1127](../../attack/techniques/T1127-trusted-developer-utilities-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Csc.yml` |
| Evidence | Command preserved from source parser. |
