---
parsed_by: focuslocust
source: lolbas
type: generated
---
# VSIISExeLauncher.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vsiisexelauncher.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VSIISExeLauncher.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [VSIISExeLauncher.exe](../../tools/windows/vsiisexelauncher.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | vsiisexelauncher.exe |
| name | VSIISExeLauncher.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/timwhitez |

## Preserved Source Material

```yaml
Acknowledgement:
- Person: timwhite
Author: timwhite
Commands:
- Category: Execute
  Command: VSIISExeLauncher.exe -p {PATH:.exe} -a "{CMD:args}"
  Description: The above binary will execute other binary.
  MitreID: T1218
  OperatingSystem: Windows 10 and up with VS/VScode installed
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Execute any binary with given arguments.
Created: 2021-09-24
Description: Binary will execute specified binary. Part of VS/VScode installation.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_vsiisexelauncher.yml
- IOC: VSIISExeLauncher.exe spawned an unknown process
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\Extensions\Microsoft\Web Tools\ProjectSystem\VSIISExeLauncher.exe
Name: VSIISExeLauncher.exe
Resources:
- Link: https://github.com/timwhitez
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VSIISExeLauncher.yml
```

## Detection / Analysis Notes

```text
IOC: VSIISExeLauncher.exe spawned an unknown process
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_vsiisexelauncher.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_vsiisexelauncher.yml
- IOC: VSIISExeLauncher.exe spawned an unknown process
```
