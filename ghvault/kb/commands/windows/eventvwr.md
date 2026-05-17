---
parsed_by: focuslocust
source: commands
type: generated
---
# Eventvwr Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Eventvwr.exe

Tool page: [Eventvwr.exe](../../tools/windows/eventvwr.exe.md)

### Execute a binary or script as a high-integrity process without a UAC prompt.

```text
eventvwr.exe
```

Description:

During startup, eventvwr.exe checks the registry value `HKCU\Software\Classes\mscfile\shell\open\command` for the location of mmc.exe, which is used to open the eventvwr.msc saved console file. If the location of another binary or script is added to this registry value, it will be executed as a high-integrity process without a UAC prompt being displayed to the user.

Related ATT&CK:

- [T1548.002](../../attack/techniques/T1548.002-bypass-user-account-control.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Eventvwr.yml` |
| Evidence | Command preserved from source parser. |

### Execute a command to bypass security restrictions that limit the use of command-line interpreters.

```text
ysoserial.exe -o raw -f BinaryFormatter - g DataSet -c "{CMD}" > RecentViews & copy RecentViews %LOCALAPPDATA%\Microsoft\EventV~1\RecentViews & eventvwr.exe
```

Description:

During startup, eventvwr.exe uses .NET deserialization with `%LOCALAPPDATA%\Microsoft\EventV~1\RecentViews` file. This file can be created using https://github.com/pwntester/ysoserial.net

Related ATT&CK:

- [T1548.002](../../attack/techniques/T1548.002-bypass-user-account-control.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Eventvwr.yml` |
| Evidence | Command preserved from source parser. |
