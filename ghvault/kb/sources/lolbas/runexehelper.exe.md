---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Runexehelper.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `runexehelper.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Runexehelper.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Runexehelper.exe](../../tools/windows/runexehelper.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | runexehelper.exe |
| name | Runexehelper.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/0gtweet/status/1206692239839289344 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@0gtweet'
  Person: Grzegorz Tworek
Author: Grzegorz Tworek
Commands:
- Category: Execute
  Command: runexehelper.exe {PATH_ABSOLUTE:.exe}
  Description: 'Launches the specified exe. Prerequisites: (1) diagtrack_action_output environment variable must be set to
    an existing, writable folder; (2) runexewithargs_output.txt file cannot exist in the folder indicated by the variable.'
  MitreID: T1218
  OperatingSystem: Windows 10, Windows 11, Windows Server 2012, Windows Server 2016, Windows Server 2019, Windows Server 2022
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Executes arbitrary code
Created: 2022-12-13
Description: Launcher process
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_runexehelper.yml
- IOC: c:\windows\system32\runexehelper.exe is run
- IOC: Existence of runexewithargs_output.txt file
Full_Path:
- Path: c:\windows\system32\runexehelper.exe
Name: Runexehelper.exe
Resources:
- Link: https://twitter.com/0gtweet/status/1206692239839289344
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Runexehelper.yml
```

## Detection / Analysis Notes

```text
IOC: Existence of runexewithargs_output.txt file
```

```text
IOC: c:\windows\system32\runexehelper.exe is run
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_runexehelper.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_runexehelper.yml
- IOC: c:\windows\system32\runexehelper.exe is run
- IOC: Existence of runexewithargs_output.txt file
```
