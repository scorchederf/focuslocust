---
parsed_by: focuslocust
source: commands
type: generated
---
# Sftp Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Sftp.exe

Tool page: [Sftp.exe](../../tools/windows/sftp.exe.md)

### Proxy execution of specified command, can be used as a defensive evasion.

```text
sftp -o ProxyCommand="{CMD}" .
```

Description:

Spawns ssh.exe which in turn spawns the specified command line. See also this project's entry for ssh.exe.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Sftp.yml` |
| Evidence | Command preserved from source parser. |
