---
parsed_by: focuslocust
source: commands
type: generated
---
# Explorer Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Explorer.exe

Tool page: [Explorer.exe](../../tools/windows/explorer.exe.md)

### Performs execution of specified file with explorer parent process breaking the process tree, can be used for defense evasion.

```text
explorer.exe /root,"{PATH_ABSOLUTE:.exe}"
```

Description:

Execute specified .exe with the parent process spawning from a new instance of explorer.exe

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Explorer.yml` |
| Evidence | Command preserved from source parser. |

### Performs execution of specified file with explorer parent process breaking the process tree, can be used for defense evasion.

```text
explorer.exe {PATH_ABSOLUTE:.exe}
```

Description:

Execute notepad.exe with the parent process spawning from a new instance of explorer.exe

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Explorer.yml` |
| Evidence | Command preserved from source parser. |
