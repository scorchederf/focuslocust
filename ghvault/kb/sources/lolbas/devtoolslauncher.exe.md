---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Devtoolslauncher.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `devtoolslauncher.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Devtoolslauncher.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Devtoolslauncher.exe](../../tools/windows/devtoolslauncher.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | devtoolslauncher.exe |
| name | Devtoolslauncher.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/_felamos/status/1179811992841797632 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@_felamos'
  Person: felamos
Author: felamos
Commands:
- Category: Execute
  Command: devtoolslauncher.exe LaunchForDeploy {PATH_ABSOLUTE:.exe} "{CMD:args}" test
  Description: The above binary will execute other binary.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Execute any binary with given arguments and it will call `developertoolssvc.exe`. `developertoolssvc` is actually
    executing the binary.
- Category: Execute
  Command: devtoolslauncher.exe LaunchForDebug {PATH_ABSOLUTE:.exe} "{CMD:args}" test
  Description: The above binary will execute other binary.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Execute any binary with given arguments.
Created: 2019-10-04
Description: Binary will execute specified binary. Part of VS/VScode installation.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_devtoolslauncher.yml
- IOC: DeveloperToolsSvc.exe spawned an unknown process
Full_Path:
- Path: c:\windows\system32\devtoolslauncher.exe
Name: Devtoolslauncher.exe
Resources:
- Link: https://twitter.com/_felamos/status/1179811992841797632
- Link: https://www.virustotal.com/gui/file/84877a507af8b70c145777a87eaf28a8327c50a1563fe650f34572bef8a42ff6/details
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Devtoolslauncher.yml
```

## Detection / Analysis Notes

```text
IOC: DeveloperToolsSvc.exe spawned an unknown process
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_devtoolslauncher.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_devtoolslauncher.yml
- IOC: DeveloperToolsSvc.exe spawned an unknown process
```
