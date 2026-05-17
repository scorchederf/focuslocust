---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Explorer.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `explorer.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Explorer.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Explorer.exe](../../tools/windows/explorer.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | explorer.exe |
| name | Explorer.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/CyberRaiju/status/1273597319322058752?s=20 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@CyberRaiju'
  Person: Jai Minton
- Handle: '@bohops'
  Person: Jimmy
Author: Jai Minton
Commands:
- Category: Execute
  Command: explorer.exe /root,"{PATH_ABSOLUTE:.exe}"
  Description: Execute specified .exe with the parent process spawning from a new instance of explorer.exe
  MitreID: T1202
  OperatingSystem: Windows XP, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Performs execution of specified file with explorer parent process breaking the process tree, can be used for defense
    evasion.
- Category: Execute
  Command: explorer.exe {PATH_ABSOLUTE:.exe}
  Description: Execute notepad.exe with the parent process spawning from a new instance of explorer.exe
  MitreID: T1202
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Performs execution of specified file with explorer parent process breaking the process tree, can be used for defense
    evasion.
Created: 2020-06-24
Description: Binary used for managing files and system components within Windows
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_explorer_break_process_tree.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_explorer_lolbin_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f2bc0c685d83db7db395fc3dc4b9729759cd4329/rules/windows/initial_access_via_explorer_suspicious_child_parent_args.toml
- IOC: Multiple instances of explorer.exe or explorer.exe using the /root command line is suspicious.
Full_Path:
- Path: C:\Windows\explorer.exe
- Path: C:\Windows\SysWOW64\explorer.exe
Name: Explorer.exe
Resources:
- Link: https://twitter.com/CyberRaiju/status/1273597319322058752?s=20
- Link: https://twitter.com/bohops/status/1276356245541335048
- Link: https://twitter.com/bohops/status/986984122563391488
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Explorer.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/f2bc0c685d83db7db395fc3dc4b9729759cd4329/rules/windows/initial_access_via_explorer_suspicious_child_parent_args.toml
```

```text
IOC: Multiple instances of explorer.exe or explorer.exe using the /root command line is suspicious.
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_explorer_break_process_tree.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_explorer_lolbin_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_explorer_break_process_tree.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_explorer_lolbin_execution.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f2bc0c685d83db7db395fc3dc4b9729759cd4329/rules/windows/initial_access_via_explorer_suspicious_child_parent_args.toml
- IOC: Multiple instances of explorer.exe or explorer.exe using the /root command line is suspicious.
```
