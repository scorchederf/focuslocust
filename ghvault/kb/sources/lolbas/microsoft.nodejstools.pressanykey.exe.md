---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Microsoft.NodejsTools.PressAnyKey.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `microsoft.nodejstools.pressanykey.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Microsoft.NodejsTools.PressAnyKey.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Microsoft.NodejsTools.PressAnyKey.exe](../../tools/windows/microsoft.nodejstools.pressanykey.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | microsoft.nodejstools.pressanykey.exe |
| name | Microsoft.NodejsTools.PressAnyKey.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/mrd0x/status/1463526834918854661 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mrd0x'
  Person: mr.d0x
Author: mr.d0x
Commands:
- Category: Execute
  Command: Microsoft.NodejsTools.PressAnyKey.exe normal 1 {PATH:.exe}
  Description: Launch specified executable as a subprocess of Microsoft.NodejsTools.PressAnyKey.exe.
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: Spawn a new process via Microsoft.NodejsTools.PressAnyKey.exe.
Created: 2022-01-20
Description: Part of the NodeJS Visual Studio tools.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_renamed_pressanykey.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_pressanykey_lolbin_execution.yml
Full_Path:
- Path: C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\IDE\Extensions\Microsoft\NodeJsTools\NodeJsTools\Microsoft.NodejsTools.PressAnyKey.exe
- Path: C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\IDE\Extensions\Microsoft\NodeJsTools\NodeJsTools\Microsoft.NodejsTools.PressAnyKey.exe
Name: Microsoft.NodejsTools.PressAnyKey.exe
Resources:
- Link: https://twitter.com/mrd0x/status/1463526834918854661
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Microsoft.NodejsTools.PressAnyKey.yml
```

## Detection / Analysis Notes

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_pressanykey_lolbin_execution.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_renamed_pressanykey.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_renamed_pressanykey.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_pressanykey_lolbin_execution.yml
```
