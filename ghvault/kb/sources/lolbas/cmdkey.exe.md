---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Cmdkey.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `cmdkey.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmdkey.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Cmdkey.exe](../../tools/windows/cmdkey.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | cmdkey.exe |
| name | Cmdkey.exe |
| type | tool |
| source | lolbas |
| url | https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey |

## Preserved Source Material

```yaml
Author: Oddvar Moe
Commands:
- Category: Credentials
  Command: cmdkey /list
  Description: List cached credentials
  MitreID: T1078
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Get credential information from host
Created: 2018-05-25
Description: creates, lists, and deletes stored user names and passwords or credentials.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_cmdkey_recon.yml
Full_Path:
- Path: C:\Windows\System32\cmdkey.exe
- Path: C:\Windows\SysWOW64\cmdkey.exe
Name: Cmdkey.exe
Resources:
- Link: https://web.archive.org/web/20230202122017/https://www.peew.pw/blog/2017/11/26/exploring-cmdkey-an-edge-case-for-privilege-escalation
- Link: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Cmdkey.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_cmdkey_recon.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_cmdkey_recon.yml
```
