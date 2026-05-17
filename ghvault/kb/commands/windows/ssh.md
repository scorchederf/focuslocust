---
parsed_by: focuslocust
source: commands
type: generated
---
# ssh Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## ssh.exe

Tool page: [ssh.exe](../../tools/windows/ssh.exe.md)

### Execute specified command, can be used for defense evasion.

```text
ssh localhost "{CMD}"
```

Description:

Executes specified command on host machine. The prompt for password can be eliminated by adding the host's public key in the user's authorized_keys file. Adversaries can do the same for execution on remote machines.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ssh.yml` |
| Evidence | Command preserved from source parser. |

### Performs execution of specified file, can be used as a defensive evasion.

```text
ssh -o ProxyCommand="{CMD}" .
```

Description:

Executes specified command from ssh.exe

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ssh.yml` |
| Evidence | Command preserved from source parser. |
