---
parsed_by: focuslocust
source: commands
type: generated
---
# Msbuild Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Msbuild.exe

Tool page: [Msbuild.exe](../../tools/windows/msbuild.exe.md)

### Compile and run code

```text
msbuild.exe {PATH:.xml}
```

Description:

Build and execute a C# project stored in the target XML file.

Related ATT&CK:

- [T1127.001](../../attack/techniques/T1127.001-msbuild.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msbuild.yml` |
| Evidence | Command preserved from source parser. |

### Compile and run code

```text
msbuild.exe {PATH:.csproj}
```

Description:

Build and execute a C# project stored in the target csproj file.

Related ATT&CK:

- [T1127.001](../../attack/techniques/T1127.001-msbuild.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msbuild.yml` |
| Evidence | Command preserved from source parser. |

### Execute DLL

```text
msbuild.exe /logger:TargetLogger,{PATH_ABSOLUTE:.dll};MyParameters,Foo
```

Description:

Executes generated Logger DLL file with TargetLogger export.

Related ATT&CK:

- [T1127.001](../../attack/techniques/T1127.001-msbuild.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msbuild.yml` |
| Evidence | Command preserved from source parser. |

### Execute project file that contains XslTransformation tag parameters

```text
msbuild.exe {PATH:.proj}
```

Description:

Execute JScript/VBScript code through XML/XSL Transformation. Requires Visual Studio MSBuild v14.0+.

Related ATT&CK:

- [T1127.001](../../attack/techniques/T1127.001-msbuild.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msbuild.yml` |
| Evidence | Command preserved from source parser. |

### Bypass command-line based detections

```text
msbuild.exe @{PATH:.rsp}
```

Description:

By putting any valid msbuild.exe command-line options in an RSP file and calling it as above will interpret the options as if they were passed on the command line.

Related ATT&CK:

- [T1036](../../attack/techniques/T1036-masquerading.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msbuild.yml` |
| Evidence | Command preserved from source parser. |
