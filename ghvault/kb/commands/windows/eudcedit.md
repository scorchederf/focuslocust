---
parsed_by: focuslocust
source: commands
type: generated
---
# Eudcedit Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Eudcedit.exe

Tool page: [Eudcedit.exe](../../tools/windows/eudcedit.exe.md)

### Execute a binary or script as a high-integrity process without a UAC prompt.

```text
eudcedit
```

Description:

Once executed, the Private Charecter Editor will be opened - click OK, then click File -> Font Links. In the next window choose the option "Link with Selected Fonts" and click on Save As, then in the opened enter the command you want to execute.

Related ATT&CK:

- [T1548.002](../../attack/techniques/T1548.002-bypass-user-account-control.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Eudcedit.yml` |
| Evidence | Command preserved from source parser. |
