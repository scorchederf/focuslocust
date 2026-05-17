---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Provlaunch.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `provlaunch.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Provlaunch.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Provlaunch.exe](../../tools/windows/provlaunch.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | provlaunch.exe |
| name | Provlaunch.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/0gtweet/status/1674399582162153472 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@0gtweet'
  Person: Grzegorz Tworek
Author: Grzegorz Tworek
Commands:
- Category: Execute
  Command: provlaunch.exe LOLBin
  Description: Executes command defined in the Registry. Requires 3 levels of the key structure containing some keywords.
    Such keys may be created with two reg.exe commands, e.g. `reg.exe add HKLM\SOFTWARE\Microsoft\Provisioning\Commands\LOLBin\dummy1
    /v altitude /t REG_DWORD /d 0` and `reg add HKLM\SOFTWARE\Microsoft\Provisioning\Commands\LOLBin\dummy1\dummy2 /v Commandline
    /d calc.exe`. Registry keys are deleted after successful execution.
  MitreID: T1218
  OperatingSystem: Windows 10, Windows 11, Windows Server 2012, Windows Server 2016, Windows Server 2019, Windows Server 2022
  Privileges: Administrator
  Tags:
  - Execute: CMD
  Usecase: Executes arbitrary command
Created: 2023-06-30
Description: Launcher process
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_provlaunch_potential_abuse.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_provlaunch_susp_child_process.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_registry_provlaunch_provisioning_command.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/registry/registry_set/registry_set_provisioning_command_abuse.yml
- IOC: c:\windows\system32\provlaunch.exe executions
- IOC: Creation/existence of HKLM\SOFTWARE\Microsoft\Provisioning\Commands subkeys
Full_Path:
- Path: c:\windows\system32\provlaunch.exe
Name: Provlaunch.exe
Resources:
- Link: https://twitter.com/0gtweet/status/1674399582162153472
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Provlaunch.yml
```

## Detection / Analysis Notes

```text
IOC: Creation/existence of HKLM\SOFTWARE\Microsoft\Provisioning\Commands subkeys
```

```text
IOC: c:\windows\system32\provlaunch.exe executions
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_provlaunch_potential_abuse.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_provlaunch_susp_child_process.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_registry_provlaunch_provisioning_command.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/registry/registry_set/registry_set_provisioning_command_abuse.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_provlaunch_potential_abuse.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_provlaunch_susp_child_process.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/process_creation/proc_creation_win_registry_provlaunch_provisioning_command.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/9cb124f841c4358ca859e8474d6e7bb5268284a2/rules/windows/registry/registry_set/registry_set_provisioning_command_abuse.yml
- IOC: c:\windows\system32\provlaunch.exe executions
- IOC: Creation/existence of HKLM\SOFTWARE\Microsoft\Provisioning\Commands subkeys
```
