---
parsed_by: focuslocust
source: commands
type: generated
---
# Schtasks Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Schtasks.exe

Tool page: [Schtasks.exe](../../tools/windows/schtasks.exe.md)

### Create a recurring task to keep reverse shell session(s) alive

```text
schtasks /create /sc minute /mo 1 /tn "Reverse shell" /tr "{CMD}"
```

Description:

Create a recurring task to execute every minute.

Related ATT&CK:

- [T1053.005](../../attack/techniques/T1053.005-scheduled-task.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Schtasks.yml` |
| Evidence | Command preserved from source parser. |

### Create a remote task to run daily relative to the the time of creation

```text
schtasks /create /s targetmachine /tn "MyTask" /tr "{CMD}" /sc daily
```

Description:

Create a scheduled task on a remote computer for persistence/lateral movement

Related ATT&CK:

- [T1053.005](../../attack/techniques/T1053.005-scheduled-task.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Schtasks.yml` |
| Evidence | Command preserved from source parser. |
