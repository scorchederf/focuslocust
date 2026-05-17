---
parsed_by: focuslocust
source: lolbas
type: generated
---
# DefaultPack.EXE

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `defaultpack.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/DefaultPack.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [DefaultPack.EXE](../../tools/windows/defaultpack.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | defaultpack.exe |
| name | DefaultPack.EXE |
| type | tool |
| source | lolbas |
| url | https://twitter.com/checkymander/status/1311509470275604480. |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@checkymander'
  Person: checkymander
Author: '@checkymander'
Commands:
- Category: Execute
  Command: DefaultPack.EXE /C:"{CMD}"
  Description: Use DefaultPack.EXE to execute arbitrary binaries, with added argument support.
  MitreID: T1218
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: CMD
  Usecase: Can be used to execute stagers, binaries, and other malicious commands.
Created: 2020-10-01
Description: This binary can be downloaded along side multiple software downloads on the Microsoft website. It gets downloaded
  when the user forgets to uncheck the option to set Bing as the default search provider.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_lolbin_defaultpack.yml
- IOC: DefaultPack.EXE spawned an unknown process
Full_Path:
- Path: C:\Program Files (x86)\Microsoft\DefaultPack\DefaultPack.exe
Name: DefaultPack.EXE
Resources:
- Link: https://twitter.com/checkymander/status/1311509470275604480.
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/DefaultPack.yml
```

## Detection / Analysis Notes

```text
IOC: DefaultPack.EXE spawned an unknown process
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_lolbin_defaultpack.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_lolbin_defaultpack.yml
- IOC: DefaultPack.EXE spawned an unknown process
```
