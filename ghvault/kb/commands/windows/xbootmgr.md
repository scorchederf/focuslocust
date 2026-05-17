---
parsed_by: focuslocust
source: commands
type: generated
---
# XBootMgr Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## XBootMgr.exe

Tool page: [XBootMgr.exe](../../tools/windows/xbootmgr.exe.md)

### Executes code as part of post-trace automation flow.

```text
xbootmgr.exe -trace "{boot|hibernate|standby|shutdown|rebootCycle}" -callBack {PATH:.exe}
```

Description:

Executes an executable after the trace is complete using the callBack parameter.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/XBootMgr.yml` |
| Evidence | Command preserved from source parser. |

### Executes code as part of pre-trace automation or staging.

```text
xbootmgr.exe -trace "{boot|hibernate|standby|shutdown|rebootCycle}" -preTraceCmd {PATH:.exe}
```

Description:

Executes an executable before each trace run using the preTraceCmd parameter.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/XBootMgr.yml` |
| Evidence | Command preserved from source parser. |
