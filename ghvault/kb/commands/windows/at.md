---
parsed_by: focuslocust
source: commands
type: generated
---
# At Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## At.exe

Tool page: [At.exe](../../tools/windows/at.exe.md)

### Create a recurring task, to eg. to keep reverse shell session(s) alive

```text
C:\Windows\System32\at.exe 09:00 /interactive /every:m,t,w,th,f,s,su {CMD}
```

Description:

Create a recurring task to execute every day at a specific time.

Related ATT&CK:

- [T1053.002](../../attack/techniques/T1053.002-at.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/At.yml` |
| Evidence | Command preserved from source parser. |
