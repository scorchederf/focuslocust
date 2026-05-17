---
parsed_by: focuslocust
source: commands
type: generated
---
# Diskshadow Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Diskshadow.exe

Tool page: [Diskshadow.exe](../../tools/windows/diskshadow.exe.md)

### Use diskshadow to exfiltrate data from VSS such as NTDS.dit

```text
diskshadow.exe /s {PATH:.txt}
```

Description:

Execute commands using diskshadow.exe from a prepared diskshadow script.

Related ATT&CK:

- [T1003.003](../../attack/techniques/T1003.003-ntds.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Diskshadow.yml` |
| Evidence | Command preserved from source parser. |

### Use diskshadow to bypass defensive counter measures

```text
diskshadow> exec {PATH:.exe}
```

Description:

Execute commands using diskshadow.exe to spawn child process

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Diskshadow.yml` |
| Evidence | Command preserved from source parser. |
