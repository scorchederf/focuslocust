---
parsed_by: focuslocust
source: commands
type: generated
---
# Syssetup.dll Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Syssetup.dll

Tool page: [Syssetup.dll](../../tools/windows/syssetup.dll.md)

### Run local or remote script(let) code through INF file specification (Note May pop an error window).

```text
rundll32 syssetup.dll,SetupInfObjectInstallAction DefaultInstall 128 {PATH_ABSOLUTE:.inf}
```

Description:

Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (section name specified).

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Syssetup.yml` |
| Evidence | Command preserved from source parser. |

### Load an executable payload.

```text
rundll32 syssetup.dll,SetupInfObjectInstallAction DefaultInstall 128 {PATH_ABSOLUTE:.inf}
```

Description:

Launch an executable file via the SetupInfObjectInstallAction function and .inf file section directive.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Syssetup.yml` |
| Evidence | Command preserved from source parser. |
