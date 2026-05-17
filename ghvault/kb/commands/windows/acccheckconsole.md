---
parsed_by: focuslocust
source: commands
type: generated
---
# AccCheckConsole Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## AccCheckConsole.exe

Tool page: [AccCheckConsole.exe](../../tools/windows/acccheckconsole.exe.md)

### Local execution of managed code from assembly DLL.

```text
AccCheckConsole.exe -window "Untitled - Notepad" {PATH_ABSOLUTE:.dll}
```

Description:

Load a managed DLL in the context of AccCheckConsole.exe. The -window switch value can be set to an arbitrary active window name.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/AccCheckConsole.yml` |
| Evidence | Command preserved from source parser. |

### Local execution of managed code to bypass AppLocker.

```text
AccCheckConsole.exe -window "Untitled - Notepad" {PATH_ABSOLUTE:.dll}
```

Description:

Load a managed DLL in the context of AccCheckConsole.exe. The -window switch value can be set to an arbitrary active window name.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/AccCheckConsole.yml` |
| Evidence | Command preserved from source parser. |
