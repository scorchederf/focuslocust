---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Setres.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `setres.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Setres.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Setres.exe](../../tools/windows/setres.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | setres.exe |
| name | Setres.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/0gtweet/status/1583356502340870144 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@0gtweet'
  Person: Grzegorz Tworek
Author: Grzegorz Tworek
Commands:
- Category: Execute
  Command: setres.exe -w 800 -h 600
  Description: Sets the resolution and then launches 'choice' command from the working directory.
  MitreID: T1218
  OperatingSystem: Windows Server 2012, Windows Server 2016, Windows Server 2019, Windows Server 2022
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Executes arbitrary code
Created: 2022-10-21
Description: Configures display settings
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_setres.yml
- IOC: Unusual location for choice.exe file
- IOC: Process created from choice.com binary
- IOC: Existence of choice.cmd file
Full_Path:
- Path: c:\windows\system32\setres.exe
Name: Setres.exe
Resources:
- Link: https://twitter.com/0gtweet/status/1583356502340870144
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Setres.yml
```

## Detection / Analysis Notes

```text
IOC: Existence of choice.cmd file
```

```text
IOC: Process created from choice.com binary
```

```text
IOC: Unusual location for choice.exe file
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_setres.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/19396788dbedc57249a46efed2bb1927abc376d4/rules/windows/process_creation/proc_creation_win_lolbin_setres.yml
- IOC: Unusual location for choice.exe file
- IOC: Process created from choice.com binary
- IOC: Existence of choice.cmd file
```
