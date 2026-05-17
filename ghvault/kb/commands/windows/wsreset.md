---
parsed_by: focuslocust
source: commands
type: generated
---
# Wsreset Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Wsreset.exe

Tool page: [Wsreset.exe](../../tools/windows/wsreset.exe.md)

### Execute a binary or script as a high-integrity process without a UAC prompt.

```text
wsreset.exe
```

Description:

During startup, wsreset.exe checks the registry value HKCU\Software\Classes\AppX82a6gwre4fdg3bt635tn5ctqjf8msdd2\Shell\open\command for the command to run. Binary will be executed as a high-integrity process without a UAC prompt being displayed to the user.

Related ATT&CK:

- [T1548.002](../../attack/techniques/T1548.002-bypass-user-account-control.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Wsreset.yml` |
| Evidence | Command preserved from source parser. |
