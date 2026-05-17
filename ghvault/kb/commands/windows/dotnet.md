---
parsed_by: focuslocust
source: commands
type: generated
---
# Dotnet Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Dotnet.exe

Tool page: [Dotnet.exe](../../tools/windows/dotnet.exe.md)

### Execute code bypassing AWL

```text
dotnet.exe {PATH:.dll}
```

Description:

dotnet.exe will execute any DLL even if applocker is enabled.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dotnet.yml` |
| Evidence | Command preserved from source parser. |

### Execute DLL

```text
dotnet.exe {PATH:.dll}
```

Description:

dotnet.exe will execute any DLL.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dotnet.yml` |
| Evidence | Command preserved from source parser. |

### Execute arbitrary F# code

```text
dotnet.exe fsi
```

Description:

dotnet.exe will open a console which allows for the execution of arbitrary F# commands

Related ATT&CK:

- [T1059](../../attack/techniques/T1059-command-and-scripting-interpreter.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dotnet.yml` |
| Evidence | Command preserved from source parser. |

### Execute code bypassing AWL

```text
dotnet.exe msbuild {PATH:.csproj}
```

Description:

dotnet.exe with msbuild (SDK Version) will execute unsigned code

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Dotnet.yml` |
| Evidence | Command preserved from source parser. |
