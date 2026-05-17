---
parsed_by: focuslocust
source: commands
type: generated
---
# ComputerDefaults Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ComputerDefaults.exe

Tool page: [ComputerDefaults.exe](../../tools/windows/computerdefaults.exe.md)

### Execute a binary or script as a high-integrity process without a UAC prompt.

```text
ComputerDefaults.exe
```

Description:

Upon execution, ComputerDefaults.exe checks two registry values at HKEY_CURRENT_USER\Software\Classes\ms-settings\Shell\open\command; if these are set by an attacker, the set command will be executed as a high-integrity process without a UAC prompt being displayed to the user. See 'resources' for which registry keys/values to set.

Related ATT&CK:

- [T1548.002](../../attack/techniques/T1548.002-bypass-user-account-control.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/ComputerDefaults.yml` |
| Evidence | Command preserved from source parser. |
