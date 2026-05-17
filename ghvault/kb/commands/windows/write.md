---
parsed_by: focuslocust
source: commands
type: generated
---
# write Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## write.exe

Tool page: [write.exe](../../tools/windows/write.exe.md)

### Execute binary through legitimate proxy. This might be utilized to confuse detection solutions that rely on parent-child relationships.

```text
write.exe
```

Description:

Executes a binary provided in default value of `HKCU\Software\Microsoft\Windows\CurrentVersion\App Paths\wordpad.exe`.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/write.yml` |
| Evidence | Command preserved from source parser. |
