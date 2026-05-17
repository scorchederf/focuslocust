---
parsed_by: focuslocust
source: commands
type: generated
---
# Provlaunch Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Provlaunch.exe

Tool page: [Provlaunch.exe](../../tools/windows/provlaunch.exe.md)

### Executes arbitrary command

```text
provlaunch.exe LOLBin
```

Description:

Executes command defined in the Registry. Requires 3 levels of the key structure containing some keywords. Such keys may be created with two reg.exe commands, e.g. `reg.exe add HKLM\SOFTWARE\Microsoft\Provisioning\Commands\LOLBin\dummy1 /v altitude /t REG_DWORD /d 0` and `reg add HKLM\SOFTWARE\Microsoft\Provisioning\Commands\LOLBin\dummy1\dummy2 /v Commandline /d calc.exe`. Registry keys are deleted after successful execution.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Provlaunch.yml` |
| Evidence | Command preserved from source parser. |
