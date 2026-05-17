---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Netsh.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `netsh.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Netsh.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Netsh.exe](../../tools/windows/netsh.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | netsh.exe |
| name | Netsh.exe |
| type | tool |
| source | lolbas |
| url | https://freddiebarrsmith.com/trix/trix.html |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: null
  Person: Freddie Barr-Smith
- Handle: null
  Person: Riccardo Spolaor
- Handle: null
  Person: Mariano Graziano
- Handle: null
  Person: Xabier Ugarte-Pedrero
Author: Freddie Barr-Smith
Commands:
- Category: Execute
  Command: netsh.exe add helper {PATH_ABSOLUTE:.dll}
  Description: Use Netsh in order to execute a .dll file and also gain persistence, every time the netsh command is called
  MitreID: T1546.007
  OperatingSystem: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: Admin
  Tags:
  - Execute: DLL
  Usecase: Proxy execution of .dll
Created: 2019-12-24
Description: Netsh is a Windows tool used to manipulate network interface settings.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_netsh_helper_dll_persistence.yml
- Splunk: https://github.com/splunk/security_content/blob/2b87b26bdc2a84b65b1355ffbd5174bdbdb1879c/detections/endpoint/processes_launching_netsh.yml
- Splunk: https://github.com/splunk/security_content/blob/08ed88bd88259c03c771c30170d2934ed0a8f878/detections/deprecated/processes_created_by_netsh.yml
- IOC: Netsh initiating a network connection
Full_Path:
- Path: C:\WINDOWS\System32\Netsh.exe
- Path: C:\WINDOWS\SysWOW64\Netsh.exe
Name: Netsh.exe
Resources:
- Link: https://freddiebarrsmith.com/trix/trix.html
- Link: https://htmlpreview.github.io/?https://github.com/MatthewDemaske/blogbackup/blob/master/netshell.html
- Link: https://liberty-shell.com/sec/2018/07/28/netshlep/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Netsh.yml
```

## Detection / Analysis Notes

```text
IOC: Netsh initiating a network connection
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_netsh_helper_dll_persistence.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/08ed88bd88259c03c771c30170d2934ed0a8f878/detections/deprecated/processes_created_by_netsh.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/2b87b26bdc2a84b65b1355ffbd5174bdbdb1879c/detections/endpoint/processes_launching_netsh.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_netsh_helper_dll_persistence.yml
- Splunk: https://github.com/splunk/security_content/blob/2b87b26bdc2a84b65b1355ffbd5174bdbdb1879c/detections/endpoint/processes_launching_netsh.yml
- Splunk: https://github.com/splunk/security_content/blob/08ed88bd88259c03c771c30170d2934ed0a8f878/detections/deprecated/processes_created_by_netsh.yml
- IOC: Netsh initiating a network connection
```
