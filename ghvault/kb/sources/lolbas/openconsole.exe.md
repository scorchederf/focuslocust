---
parsed_by: focuslocust
source: lolbas
type: generated
---
# OpenConsole.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `openconsole.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/OpenConsole.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [OpenConsole.exe](../../tools/windows/openconsole.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | openconsole.exe |
| name | OpenConsole.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/nas_bench/status/1537563834478645252 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@nas_bench'
  Person: Nasreddine Bencherchali
Author: Nasreddine Bencherchali
Commands:
- Category: Execute
  Command: OpenConsole.exe {PATH:.exe}
  Description: Execute specified process with OpenConsole.exe as parent process
  MitreID: T1202
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Use OpenConsole.exe as a proxy binary to evade defensive counter-measures
Created: 2022-06-17
Description: Console Window host for Windows Terminal
Detection:
- IOC: OpenConsole.exe spawning unexpected processes
- Sigma: https://github.com/SigmaHQ/sigma/blob/9e0ef7251b075f15e7abafbbec16d3230c5fa477/rules/windows/process_creation/proc_creation_win_lolbin_openconsole.yml
Full_Path:
- Path: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os64\OpenConsole.exe
- Path: C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os86\OpenConsole.exe
- Path: C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\Terminal\ServiceHub\os64\OpenConsole.exe
- Path: C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_1.18.10301.0_x64__8wekyb3d8bbwe\OpenConsole.exe
Name: OpenConsole.exe
Resources:
- Link: https://twitter.com/nas_bench/status/1537563834478645252
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/OpenConsole.yml
```

## Detection / Analysis Notes

```text
IOC: OpenConsole.exe spawning unexpected processes
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/9e0ef7251b075f15e7abafbbec16d3230c5fa477/rules/windows/process_creation/proc_creation_win_lolbin_openconsole.yml
```

```text
- IOC: OpenConsole.exe spawning unexpected processes
- Sigma: https://github.com/SigmaHQ/sigma/blob/9e0ef7251b075f15e7abafbbec16d3230c5fa477/rules/windows/process_creation/proc_creation_win_lolbin_openconsole.yml
```
