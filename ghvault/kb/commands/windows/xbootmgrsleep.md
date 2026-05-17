---
parsed_by: focuslocust
source: commands
type: generated
---
# XBootMgrSleep Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## XBootMgrSleep.exe

Tool page: [XBootMgrSleep.exe](../../tools/windows/xbootmgrsleep.exe.md)

### Performs execution of specified executable, can be used as a defense evasion

```text
xbootmgrsleep.exe 1000 {PATH:.exe}
```

Description:

Execute executable via XBootMgrSleep, with a 1 second (=1000 milliseconds) delay. Alternatively, it is also possible to replace the delay with any string for immediate execution.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/XBootMgrSleep.yml` |
| Evidence | Command preserved from source parser. |
