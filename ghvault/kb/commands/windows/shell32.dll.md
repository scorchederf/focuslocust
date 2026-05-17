---
parsed_by: focuslocust
source: commands
type: generated
---
# Shell32.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Shell32.dll

Tool page: [Shell32.dll](../../tools/windows/shell32.dll.md)

### Load a DLL payload.

```text
rundll32.exe shell32.dll,Control_RunDLL {PATH_ABSOLUTE:.dll}
```

Description:

Launch a DLL payload by calling the Control_RunDLL function.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Shell32.yml` |
| Evidence | Command preserved from source parser. |

### Run an executable payload.

```text
rundll32.exe shell32.dll,ShellExec_RunDLL {PATH:.exe}
```

Description:

Launch an executable by calling the ShellExec_RunDLL function.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Shell32.yml` |
| Evidence | Command preserved from source parser. |

### Run an executable payload.

```text
rundll32 SHELL32.DLL,ShellExec_RunDLL {PATH:.exe} {CMD:args}
```

Description:

Launch command line by calling the ShellExec_RunDLL function.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Shell32.yml` |
| Evidence | Command preserved from source parser. |

### Load a DLL/CPL payload.

```text
rundll32.exe shell32.dll,#44 {PATH:.dll}
```

Description:

Load a DLL/CPL by calling undocumented Control_RunDLLNoFallback function.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Shell32.yml` |
| Evidence | Command preserved from source parser. |
