---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Pcwrun.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `pcwrun.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pcwrun.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Pcwrun.exe](../../tools/windows/pcwrun.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | pcwrun.exe |
| name | Pcwrun.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/nas_bench/status/1535663791362519040 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@pabraeken'
  Person: Pierre-Alexandre Braeken
- Handle: '@nas_bench'
  Person: Nasreddine Bencherchali
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: Pcwrun.exe {PATH_ABSOLUTE:.exe}
  Description: Open the target .EXE file with the Program Compatibility Wizard.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Proxy execution of binary
- Category: Execute
  Command: Pcwrun.exe /../../$(calc).exe
  Description: Leverage the MSDT follina vulnerability through Pcwrun to execute arbitrary commands and binaries. Note that
    this specific technique will not work on a patched system with the June 2022 Windows Security update.
  MitreID: T1202
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Proxy execution of binary
Created: 2018-05-25
Description: Program Compatibility Wizard
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_pcwrun_follina.yml
Full_Path:
- Path: C:\Windows\System32\pcwrun.exe
Name: Pcwrun.exe
Resources:
- Link: https://twitter.com/pabraeken/status/991335019833708544
- Link: https://twitter.com/nas_bench/status/1535663791362519040
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Pcwrun.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_pcwrun_follina.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/6199a703221a98ae6ad343c79c558da375203e4e/rules/windows/process_creation/proc_creation_win_lolbin_pcwrun_follina.yml
```
