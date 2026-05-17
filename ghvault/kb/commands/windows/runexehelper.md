---
parsed_by: focuslocust
source: commands
type: generated
---
# Runexehelper Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Runexehelper.exe

Tool page: [Runexehelper.exe](../../tools/windows/runexehelper.exe.md)

### Executes arbitrary code

```text
runexehelper.exe {PATH_ABSOLUTE:.exe}
```

Description:

Launches the specified exe. Prerequisites: (1) diagtrack_action_output environment variable must be set to an existing, writable folder; (2) runexewithargs_output.txt file cannot exist in the folder indicated by the variable.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Runexehelper.yml` |
| Evidence | Command preserved from source parser. |
