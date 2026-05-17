---
parsed_by: focuslocust
source: commands
type: generated
---
# iscsicpl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## iscsicpl.exe

Tool page: [iscsicpl.exe](../../tools/windows/iscsicpl.exe.md)

### Execute a custom DLL via a trusted high-integrity process without a UAC prompt.

```text
c:\windows\syswow64\iscsicpl.exe
```

Description:

c:\windows\syswow64\iscsicpl.exe has a DLL injection through `C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\ISCSIEXE.dll`, resulting in UAC bypass.

Related ATT&CK:

- [T1548.002](../../attack/techniques/T1548.002-bypass-user-account-control.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Iscsicpl.yml` |
| Evidence | Command preserved from source parser. |

### Execute a binary or script as a high-integrity process without a UAC prompt.

```text
iscsicpl.exe
```

Description:

Both `c:\windows\system32\iscsicpl.exe` and `c:\windows\system64\iscsicpl.exe` have UAC bypass through launching iscicpl.exe, then navigating into the Configuration tab, clicking Report, then launching your custom command.

Related ATT&CK:

- [T1548.002](../../attack/techniques/T1548.002-bypass-user-account-control.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Iscsicpl.yml` |
| Evidence | Command preserved from source parser. |
