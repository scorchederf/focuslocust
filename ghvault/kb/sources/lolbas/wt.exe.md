---
parsed_by: focuslocust
source: lolbas
type: generated
---
# wt.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `wt.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/wt.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [wt.exe](../../tools/windows/wt.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | wt.exe |
| name | wt.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/nas_bench/status/1552100271668469761 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@nas_bench'
  Person: Nasreddine Bencherchali
Author: Nasreddine Bencherchali
Commands:
- Category: Execute
  Command: wt.exe {CMD}
  Description: Execute a command via Windows Terminal.
  MitreID: T1202
  OperatingSystem: Windows 11
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Use wt.exe as a proxy binary to evade defensive counter-measures
Created: 2022-07-27
Description: Windows Terminal
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_windows_terminal_susp_children.yml
Full_Path:
- Path: C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_<version_packageid>\wt.exe
Name: wt.exe
Resources:
- Link: https://twitter.com/nas_bench/status/1552100271668469761
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/wt.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_windows_terminal_susp_children.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_windows_terminal_susp_children.yml
```
