---
parsed_by: focuslocust
source: commands
type: generated
---
# Wlrmdr Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Wlrmdr.exe

Tool page: [Wlrmdr.exe](../../tools/windows/wlrmdr.exe.md)

### Use wlrmdr as a proxy binary to evade defensive countermeasures

```text
wlrmdr.exe -s 3600 -f 0 -t _ -m _ -a 11 -u {PATH:.exe}
```

Description:

Execute executable with wlrmdr.exe as parent process

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wlrmdr.yml` |
| Evidence | Command preserved from source parser. |
