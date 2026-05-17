---
parsed_by: focuslocust
source: commands
type: generated
---
# Netsh Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Netsh.exe

Tool page: [Netsh.exe](../../tools/windows/netsh.exe.md)

### Proxy execution of .dll

```text
netsh.exe add helper {PATH_ABSOLUTE:.dll}
```

Description:

Use Netsh in order to execute a .dll file and also gain persistence, every time the netsh command is called

Related ATT&CK:

- [T1546.007](../../attack/techniques/T1546.007-netsh-helper-dll.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Netsh.yml` |
| Evidence | Command preserved from source parser. |
