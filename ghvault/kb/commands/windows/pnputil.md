---
parsed_by: focuslocust
source: commands
type: generated
---
# Pnputil Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Pnputil.exe

Tool page: [Pnputil.exe](../../tools/windows/pnputil.exe.md)

### Add malicious driver

```text
pnputil.exe -i -a {PATH_ABSOLUTE:.inf}
```

Description:

Used for installing drivers

Related ATT&CK:

- [T1547](../../attack/techniques/T1547-boot-or-logon-autostart-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pnputil.yml` |
| Evidence | Command preserved from source parser. |
